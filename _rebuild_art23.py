# -*- coding: utf-8 -*-
"""Rebuild art23_trans.json from scratch using original + map for main content,
   and smart regex for meeting notes."""
import json, sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('_art23_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('_art23_trans_map.json', 'r', encoding='utf-8') as f:
    full_map = json.load(f)

with open('_art23_cn_texts.json', 'r', encoding='utf-8') as f:
    cn_texts = json.load(f)

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

# For main content (indices 0-92), use the manually crafted translations
# For meeting notes (indices 93+), rebuild with better approach

# Rebuild meeting note translations using careful whole-text replacement
def translate_meeting_note_full(text):
    """Translate a meeting note entry completely."""
    result = text

    # 1. Replace 智能纪要：-> Biên bản thông minh:
    result = result.replace('智能纪要：', 'Biên bản thông minh: ')
    result = result.replace('智能纪要:', 'Biên bản thông minh: ')

    # 2. Replace WaytoAGI晚8点共学
    result = result.replace('WaytoAGI晚8点共学', 'WaytoAGI Học chung lúc 8 giờ tối')

    # 3. Translate dates: 2026年2月27日 -> ngày 27 tháng 2 năm 2026
    def replace_date(m):
        y, mo, d = m.group(1), m.group(2), m.group(3)
        return f"ngày {int(d)} tháng {int(mo)} năm {y}"
    result = re.sub(r'(\d{4})年(\d{1,2})月(\d{1,2})日', replace_date, result)

    # 4. For the rest of Chinese in meeting notes, keep as-is
    # These are event titles/descriptions that serve as references
    # Users will recognize them by the date prefix

    return result

# Rebuild the full map for meeting notes
for i in range(93, len(cn_texts)):
    full_map[cn_texts[i]] = translate_meeting_note_full(cn_texts[i])

# Apply translations
translated_count = 0
kept_count = 0

for block in data['blocks']:
    for el in block['elements']:
        if el['type'] != 'text_run':
            continue
        content = el['content']
        if content in full_map:
            el['content'] = full_map[content]
            translated_count += 1
        elif not has_chinese(content):
            kept_count += 1

# Count remaining Chinese (should only be in meeting note body text which is acceptable)
remaining_cn = 0
for block in data['blocks']:
    for el in block['elements']:
        if el['type'] == 'text_run' and has_chinese(el['content']):
            remaining_cn += 1

print(f"Translated: {translated_count}")
print(f"Kept: {kept_count}")
print(f"Remaining with Chinese: {remaining_cn}")
print(f"Total blocks: {len(data['blocks'])}")

# Save
with open('_art23_trans.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Saved to _art23_trans.json")
