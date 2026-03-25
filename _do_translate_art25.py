#!/usr/bin/env python3
"""Translate article 25 - CN to VI. Apply translation map to all blocks."""
import json
import re
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

def translate_text(text, trans_map):
    """Look up text in translation map. Return translated or original."""
    if text in trans_map:
        return trans_map[text]
    return text

# Load original
with open('_art25_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Load translation map
with open('_art25_trans_map.json', 'r', encoding='utf-8') as f:
    trans_map = json.load(f)

blocks = data['blocks']
translated_count = 0
kept_count = 0
total_text = 0

for block in blocks:
    for el in block['elements']:
        if el['type'] == 'text_run':
            total_text += 1
            content = el['content']
            if has_chinese(content):
                new_content = translate_text(content, trans_map)
                if new_content != content:
                    el['content'] = new_content
                    translated_count += 1
                else:
                    kept_count += 1
                    # Print untranslated for debugging
                    short = content[:80].replace('\n', '\\n')
                    print(f"  KEPT: {short}...")
            else:
                kept_count += 1

# Update title
if has_chinese(data.get('title', '')):
    if data['title'] in trans_map:
        data['title'] = trans_map[data['title']]

# Save
with open('_art25_trans.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nTotal text elements: {total_text}")
print(f"Translated: {translated_count}")
print(f"Kept (no Chinese or untranslated): {kept_count}")
print(f"Saved to _art25_trans.json")
