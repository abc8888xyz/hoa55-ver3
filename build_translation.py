"""Build translation_map_current.json from original_blocks.json by mapping Chinese->Vietnamese"""
import json
import re
import sys
import copy

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff\u3400-\u4dbf]', text))

# Read the original blocks
with open('original_blocks.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Collect all Chinese texts
chinese_texts = []
for block in data['blocks']:
    for el in block.get('elements', []):
        c = el.get('content', '')
        if c.strip() and has_chinese(c):
            if c not in chinese_texts:
                chinese_texts.append(c)

print(f"Unique Chinese segments: {len(chinese_texts)}")

# Write them to a file for reference
with open('chinese_segments.txt', 'w', encoding='utf-8') as f:
    for i, t in enumerate(chinese_texts):
        f.write(f"[{i}] {t}\n")

print("Written to chinese_segments.txt")
print("Now provide translations via translation_pairs.py")
