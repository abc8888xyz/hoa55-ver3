#!/usr/bin/env python3
"""Batch translate Chinese to Vietnamese for Lark documents."""
import json
import re
import sys
import copy

sys.stdout.reconfigure(encoding='utf-8')

def has_chinese(text):
    """Check if text contains Chinese characters."""
    return bool(re.search(r'[\u4e00-\u9fff\u3400-\u4dbf]', text))

def translate_text(text):
    """Translate Chinese text to Vietnamese. Returns (translated_text, was_translated)."""
    if not text or not text.strip():
        return text, False
    if not has_chinese(text):
        return text, False
    # This will be replaced by the actual translations dict
    return None, True  # Signal that translation is needed

def main():
    with open('original_blocks.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extract all Chinese texts that need translation
    texts_to_translate = []
    for block in data['blocks']:
        for elem in block.get('elements', []):
            content = elem.get('content', '')
            if has_chinese(content):
                texts_to_translate.append(content)

    print(f"Total texts needing translation: {len(texts_to_translate)}")
    # Output texts for translation
    with open('texts_to_translate.json', 'w', encoding='utf-8') as f:
        json.dump(texts_to_translate, f, ensure_ascii=False, indent=2)
    print("Saved to texts_to_translate.json")

if __name__ == '__main__':
    main()
