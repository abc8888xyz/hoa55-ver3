import json
import copy
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('C:/Users/ADMIN/hoa55_ ver3/original_blocks.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('C:/Users/ADMIN/hoa55_ ver3/translation_map.json', 'r', encoding='utf-8') as f:
    translations = json.load(f)

translated = copy.deepcopy(data)

# Apply translations
translated_count = 0
for block in translated['blocks']:
    for element in block.get('elements', []):
        if element.get('type') == 'text_run':
            content = element['content']
            if content in translations:
                element['content'] = translations[content]
                translated_count += 1

# Write output
with open('C:/Users/ADMIN/hoa55_ ver3/translated_blocks.json', 'w', encoding='utf-8') as f:
    json.dump(translated, f, ensure_ascii=False, indent=2)

print(f"Translations applied: {translated_count}")
print(f"Total blocks: {len(translated['blocks'])}")

# Check for remaining Chinese content
untranslated = []
for i, block in enumerate(translated['blocks']):
    for j, element in enumerate(block.get('elements', [])):
        if element.get('type') == 'text_run':
            content = element['content']
            if re.search(r'[\u4e00-\u9fff]', content):
                untranslated.append((i, block['block_id'], content[:100]))

print(f"\nRemaining untranslated Chinese strings: {len(untranslated)}")
for idx, bid, content in untranslated:
    print(f"  Block {idx} ({bid}): {content}")

# Verify JSON is valid
with open('C:/Users/ADMIN/hoa55_ ver3/translated_blocks.json', 'r', encoding='utf-8') as f:
    verify = json.load(f)
print(f"\nJSON valid: True")
print(f"Verified block count: {len(verify['blocks'])}")
