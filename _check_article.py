"""Check if an article needs translation by reading it and counting Chinese text."""
import json, sys, re, subprocess
sys.stdout.reconfigure(encoding='utf-8')

url = sys.argv[1]
result = subprocess.run(['python', 'lark_api.py', 'read', url, '--output', 'original_blocks.json'], 
                       capture_output=True, text=True, encoding='utf-8')
print(result.stdout.strip())
if result.returncode != 0:
    print(f"ERROR: {result.stderr}")
    sys.exit(1)

with open('original_blocks.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

cn_count = 0
total_text = 0
cn_texts = []
for block in data['blocks']:
    for elem in block.get('elements', []):
        if elem['type'] == 'text_run':
            total_text += 1
            if has_chinese(elem['content']):
                cn_count += 1
                if elem['content'] not in cn_texts:
                    cn_texts.append(elem['content'])

print(f"STATS: total_blocks={data['total_blocks']}, translatable={data['translatable_blocks']}, total_text={total_text}, chinese={cn_count}, unique_chinese={len(cn_texts)}")

if cn_count == 0:
    print("STATUS: ALREADY_TRANSLATED")
else:
    print("STATUS: NEEDS_TRANSLATION")
    # Save unique Chinese texts
    with open('_cn_texts.json', 'w', encoding='utf-8') as f:
        json.dump(cn_texts, f, ensure_ascii=False, indent=2)
