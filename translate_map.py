# -*- coding: utf-8 -*-
"""Apply translation mapping to a Lark document JSON file."""
import sys
import json
import re

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')


def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff\u3400-\u4dbf]', text))


def apply_translations(input_file, output_file, mapping):
    """
    mapping: dict of {original_chinese: vietnamese_translation}
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    translated_count = 0
    kept_count = 0
    error_count = 0

    for block in data.get("blocks", []):
        for elem in block.get("elements", []):
            content = elem.get("content", "")
            if not content.strip():
                continue
            if has_chinese(content):
                if content in mapping:
                    elem["content"] = mapping[content]
                    translated_count += 1
                else:
                    # Try partial match or keep original
                    error_count += 1
                    print(f"  UNMAPPED: {content[:80]}", file=sys.stderr)
            else:
                kept_count += 1

    # Translate title if in mapping
    title = data.get("title", "")
    if title in mapping:
        data["title"] = mapping[title]

    total_text = translated_count + kept_count + error_count
    total_blocks = data.get("translatable_blocks", len(data.get("blocks", [])))

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Done: {translated_count} translated, {kept_count} kept, {error_count} errors")
    print(f"STATS:total_blocks={total_blocks},translated={translated_count},kept={kept_count},errors={error_count},total_text={total_text}")
    return translated_count, kept_count, error_count, total_text, total_blocks


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python translate_map.py <input.json> <output.json> <mapping.json>")
        sys.exit(1)

    with open(sys.argv[3], 'r', encoding='utf-8') as f:
        mapping = json.load(f)

    apply_translations(sys.argv[1], sys.argv[2], mapping)
