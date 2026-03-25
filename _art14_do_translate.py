# -*- coding: utf-8 -*-
"""Apply translation map to art14"""
import json, sys, re

sys.stdout.reconfigure(encoding='utf-8')

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

with open('_art14_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('_art14_map.json', 'r', encoding='utf-8') as f:
    trans_map = json.load(f)

total_text = 0
translated_text = 0
kept_text = 0
missing = []

for block in data['blocks']:
    for el in block['elements']:
        if el['type'] == 'text_run':
            total_text += 1
            content = el['content']
            if has_chinese(content):
                if content in trans_map:
                    el['content'] = trans_map[content]
                    translated_text += 1
                else:
                    missing.append(content[:80])
                    kept_text += 1
            else:
                kept_text += 1

with open('_art14_trans.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total text elements: {total_text}")
print(f"Translated: {translated_text}")
print(f"Kept as-is: {kept_text}")
print(f"Missing translations: {len(missing)}")
if missing:
    for m in missing:
        print(f"  MISSING: {m}")
