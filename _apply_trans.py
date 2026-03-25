# -*- coding: utf-8 -*-
import json, copy, re

with open('_art4_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('_art4_trans_map.json', 'r', encoding='utf-8') as f:
    T = json.load(f)

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

translated = copy.deepcopy(data)
total_text = 0
translated_count = 0
kept_count = 0
missed = []

for block in translated['blocks']:
    for el in block.get('elements', []):
        if 'content' not in el:
            continue
        original = el['content']
        total_text += 1

        if original in T:
            el['content'] = T[original]
            if T[original] != original:
                translated_count += 1
            else:
                kept_count += 1
        elif not has_chinese(original):
            kept_count += 1
        else:
            missed.append(original)
            kept_count += 1

with open('_art4_trans.json', 'w', encoding='utf-8') as f:
    json.dump(translated, f, ensure_ascii=False, indent=2)

print(f"Total blocks: {len(translated['blocks'])}")
print(f"Total text segments: {total_text}")
print(f"Translated: {translated_count}")
print(f"Kept unchanged: {kept_count}")
print(f"Missed (still has Chinese): {len(missed)}")
for m in missed:
    print(f"  MISSED: {repr(m[:100])}")
