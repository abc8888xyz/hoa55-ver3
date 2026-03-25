# -*- coding: utf-8 -*-
"""Translate article 23: Apply translation map to original JSON."""
import json, sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('_art23_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('_art23_trans_map.json', 'r', encoding='utf-8') as f:
    trans_map = json.load(f)

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

translated_count = 0
kept_count = 0
total_text_runs = 0
missing = []

for block in data['blocks']:
    for el in block['elements']:
        if el['type'] != 'text_run':
            continue
        total_text_runs += 1
        content = el['content']
        if content in trans_map:
            el['content'] = trans_map[content]
            translated_count += 1
        elif not has_chinese(content):
            kept_count += 1
        else:
            missing.append(content[:80])

if missing:
    print(f"MISSING translations: {len(missing)}")
    for m in missing[:10]:
        print(f"  - {m}")
else:
    print("All Chinese text translated!")

print(f"\nTranslated: {translated_count}")
print(f"Kept (no Chinese): {kept_count}")
print(f"Total text_runs: {total_text_runs}")
print(f"Total blocks: {len(data['blocks'])}")

# Save
with open('_art23_trans.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Saved to _art23_trans.json")
