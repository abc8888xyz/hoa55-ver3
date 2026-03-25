# -*- coding: utf-8 -*-
"""
Translate all Chinese text in a Lark document JSON file.
Reads original blocks, extracts all Chinese text segments,
sends them to Claude for translation, and saves the result.

Usage: python do_translate_chunk.py <input.json> <output.json>
"""
import sys
import json
import re
import os
import anthropic

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')


def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff\u3400-\u4dbf]', text))


def extract_chinese_segments(data):
    """Extract all Chinese text segments with their paths for replacement."""
    segments = []
    for bi, block in enumerate(data.get("blocks", [])):
        for ei, elem in enumerate(block.get("elements", [])):
            content = elem.get("content", "")
            if content.strip() and has_chinese(content):
                segments.append({
                    "block_idx": bi,
                    "elem_idx": ei,
                    "original": content,
                })
    return segments


def translate_batch(segments, batch_size=80):
    """Translate segments in batches using Claude API."""
    client = anthropic.Anthropic()
    all_translations = []

    for start in range(0, len(segments), batch_size):
        batch = segments[start:start + batch_size]
        # Build numbered list
        lines = []
        for i, seg in enumerate(batch):
            lines.append(f"[{i}] {seg['original']}")
        text_block = "\n".join(lines)

        prompt = f"""You are a professional Chinese-to-Vietnamese translator. Translate the following Chinese text segments to Vietnamese.

RULES:
- Translate Chinese text to natural, accurate Vietnamese
- Keep English words, brand names, technical terms (OpenClaw, Codex, Claude, GPT, API, etc.) unchanged
- Keep emojis, URLs, code snippets, numbers unchanged
- Keep punctuation style appropriate for Vietnamese
- Do NOT add or remove content
- Output ONLY the translations in the exact same numbered format

TEXT TO TRANSLATE:
{text_block}

OUTPUT FORMAT (one translation per line, same numbering):
[0] Vietnamese translation here
[1] Vietnamese translation here
...etc"""

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=8000,
            messages=[{"role": "user", "content": prompt}]
        )

        result_text = response.content[0].text.strip()
        translations = {}
        for line in result_text.split("\n"):
            line = line.strip()
            m = re.match(r'\[(\d+)\]\s*(.*)', line)
            if m:
                idx = int(m.group(1))
                trans = m.group(2).strip()
                translations[idx] = trans

        for i, seg in enumerate(batch):
            if i in translations and translations[i]:
                all_translations.append(translations[i])
            else:
                # Fallback: keep original
                all_translations.append(seg['original'])
                print(f"  WARNING: No translation for segment {start + i}, keeping original", file=sys.stderr)

    return all_translations


def main():
    if len(sys.argv) < 3:
        print("Usage: python do_translate_chunk.py <input.json> <output.json>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    segments = extract_chinese_segments(data)
    print(f"Found {len(segments)} Chinese text segments to translate")

    if not segments:
        # No Chinese text, just copy
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("No Chinese text found, copied as-is")
        return

    translations = translate_batch(segments)

    # Apply translations
    for seg, trans in zip(segments, translations):
        bi = seg["block_idx"]
        ei = seg["elem_idx"]
        data["blocks"][bi]["elements"][ei]["content"] = trans

    # Also translate the title if it has Chinese
    title = data.get("title", "")
    if has_chinese(title):
        client = anthropic.Anthropic()
        resp = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=500,
            messages=[{"role": "user", "content": f"Translate this Chinese title to Vietnamese. Output ONLY the translation, nothing else:\n{title}"}]
        )
        data["title"] = resp.content[0].text.strip()

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Count stats
    total_text = sum(1 for b in data["blocks"] for e in b.get("elements", []) if e.get("content", "").strip())
    print(f"Translation complete: {len(segments)} segments translated, saved to {output_file}")
    print(f"STATS:total_blocks={data.get('translatable_blocks', 0)},translated={len(segments)},kept={total_text - len(segments)},total_text={total_text}")


if __name__ == "__main__":
    main()
