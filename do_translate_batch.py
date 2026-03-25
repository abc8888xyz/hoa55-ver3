"""
Batch translate Chinese to Vietnamese for Lark document blocks.
Reads original_blocks.json, translates Chinese content, saves to translated_blocks.json.
Uses a dictionary-based approach for common terms + regex for Chinese detection.
"""
import json
import re
import sys
import copy

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

def has_chinese(text):
    """Check if text contains Chinese characters"""
    return bool(re.search(r'[\u4e00-\u9fff\u3400-\u4dbf]', text))

def is_url(text):
    """Check if text is primarily a URL"""
    text = text.strip()
    return text.startswith('http://') or text.startswith('https://') or text.startswith('www.')

def translate_text(text, translations):
    """Look up text in translation dict, return translated version or original"""
    if text in translations:
        return translations[text]
    return text

def main():
    with open('original_blocks.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Load translation mapping
    with open('translation_map_current.json', 'r', encoding='utf-8') as f:
        translations = json.load(f)

    translated = copy.deepcopy(data)

    total_segments = 0
    translated_count = 0
    kept_count = 0

    for block in translated['blocks']:
        for el in block.get('elements', []):
            content = el.get('content', '')
            if not content.strip():
                continue
            total_segments += 1

            if content in translations:
                el['content'] = translations[content]
                translated_count += 1
            elif not has_chinese(content):
                kept_count += 1
            else:
                # Chinese text not in translation map - keep original
                kept_count += 1
                print(f"WARNING: Untranslated Chinese text: {content[:80]}...")

    with open('translated_blocks.json', 'w', encoding='utf-8') as f:
        json.dump(translated, f, ensure_ascii=False, indent=2)

    print(f"Total segments: {total_segments}")
    print(f"Translated: {translated_count}")
    print(f"Kept as-is: {kept_count}")
    print(f"Saved to translated_blocks.json")

if __name__ == '__main__':
    main()
