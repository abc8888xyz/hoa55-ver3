#!/usr/bin/env python3
"""Translate article 1 from Chinese to Vietnamese."""
import json, sys, re, copy
sys.stdout.reconfigure(encoding='utf-8')

def has_cn(t):
    return bool(re.search(r'[\u4e00-\u9fff\u3400-\u4dbf]', t))

with open('_c1_art1_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('_c1_translations.json', 'r', encoding='utf-8') as f:
    T = json.load(f)

translated = copy.deepcopy(data)
total_blocks = len(translated['blocks'])
total_texts = 0
translated_count = 0
kept_count = 0
remaining_cn = 0

for block in translated['blocks']:
    for elem in block.get('elements', []):
        content = elem.get('content', '')
        if not content.strip():
            continue
        total_texts += 1
        if content in T:
            elem['content'] = T[content]
            translated_count += 1
        elif not has_cn(content):
            kept_count += 1
        else:
            kept_count += 1
            remaining_cn += 1

with open('_c1_translated.json', 'w', encoding='utf-8') as f:
    json.dump(translated, f, ensure_ascii=False, indent=2)

print(f"Total blocks: {total_blocks}")
print(f"Total texts: {total_texts}")
print(f"Translated: {translated_count}")
print(f"Kept as-is (no Chinese): {kept_count - remaining_cn}")
print(f"Remaining Chinese: {remaining_cn}")

# Show remaining Chinese texts
if remaining_cn > 0:
    print("\n--- Remaining Chinese texts ---")
    for block in translated['blocks']:
        for elem in block.get('elements', []):
            c = elem.get('content', '')
            if has_cn(c) and c not in T:
                print(f"  [{block.get('block_id','')}] {c[:100]}")
