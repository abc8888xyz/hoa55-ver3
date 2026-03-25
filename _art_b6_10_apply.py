# -*- coding: utf-8 -*-
"""Apply translation map to create _art_b6_10_trans.json"""
import json, sys, re

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

with open('_art_b6_10_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('_art_b6_10_map.json', 'r', encoding='utf-8') as f:
    trans = json.load(f)

translated_count = 0
kept_count = 0
total_text = 0

for i, block in enumerate(data['blocks']):
    for j, el in enumerate(block['elements']):
        if el['type'] == 'text_run':
            total_text += 1
            key = f"{i}|{j}"
            if key in trans:
                el['content'] = trans[key]
                translated_count += 1
            else:
                kept_count += 1

# Add spaces between adjacent Vietnamese text_runs where needed
for block in data['blocks']:
    elements = block['elements']
    for i in range(len(elements) - 1):
        el = elements[i]
        next_el = elements[i + 1]
        if el['type'] == 'text_run' and next_el['type'] == 'text_run':
            curr = el['content']
            nxt = next_el['content']
            if curr and nxt:
                if not curr[-1] in ' \n\t' and not nxt[0] in ' \n\t':
                    curr_is_code = el.get('style', {}).get('inline_code', False)
                    next_is_code = next_el.get('style', {}).get('inline_code', False)
                    if not curr_is_code and not next_is_code:
                        el['content'] = curr + ' '

# Update title
vi_title = trans.get("0|0", data['title'])
data['title'] = vi_title

with open('_art_b6_10_trans.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total text elements: {total_text}")
print(f"Translated: {translated_count}")
print(f"Kept as-is: {kept_count}")
print(f"Done! Saved to _art_b6_10_trans.json")
