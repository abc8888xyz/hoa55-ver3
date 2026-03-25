# -*- coding: utf-8 -*-
"""Apply translation map to art31"""
import json, sys, copy, re

sys.stdout.reconfigure(encoding='utf-8')

with open('_art31_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('_art31_map.json', 'r', encoding='utf-8') as f:
    trans = json.load(f)

out = copy.deepcopy(data)
translated_count = 0
kept_count = 0
total_text = 0
missing = []

for block in out['blocks']:
    for el in block['elements']:
        if el['type'] == 'text_run':
            total_text += 1
            content = el['content']
            if content in trans:
                el['content'] = trans[content]
                if trans[content] != content:
                    translated_count += 1
                else:
                    kept_count += 1
            elif content.strip() == '':
                kept_count += 1
            else:
                stripped = content.strip()
                # Keep URLs, code, technical terms
                if (stripped.startswith('http') or
                    stripped.startswith('~/') or
                    re.match(r'^[A-Za-z0-9_./:@#%=&?\-+\s]+$', stripped) or
                    stripped in ['• ']):
                    kept_count += 1
                else:
                    missing.append(content)
                    kept_count += 1

if missing:
    print(f'MISSING translations ({len(missing)}):')
    for m in missing[:50]:
        print(f'  [{m[:100]}]')

print(f'\nTotal text elements: {total_text}')
print(f'Translated: {translated_count}')
print(f'Kept as-is: {kept_count}')
print(f'Missing: {len(missing)}')

with open('_art31_trans.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print(f'Saved _art31_trans.json with {len(out["blocks"])} blocks')
