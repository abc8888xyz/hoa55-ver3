import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('original_blocks.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('_trans_map.json', 'r', encoding='utf-8') as f:
    t = json.load(f)

translated_count = 0
kept_count = 0
for block in data['blocks']:
    for elem in block.get('elements', []):
        if elem['type'] == 'text_run':
            if elem['content'] in t:
                elem['content'] = t[elem['content']]
                translated_count += 1
            else:
                kept_count += 1

with open('translated_blocks.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'Translated: {translated_count}, Kept: {kept_count}')
