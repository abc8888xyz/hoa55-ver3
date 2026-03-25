# -*- coding: utf-8 -*-
"""Build translation mapping from Chinese to Vietnamese."""
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Read original blocks to get all unique texts
with open('original_blocks.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Collect all unique content texts in order
all_texts = []
seen = set()
for block in data['blocks']:
    for elem in block.get('elements', []):
        c = elem.get('content', '')
        if c.strip() and c not in seen:
            all_texts.append(c)
            seen.add(c)

# Build mapping - translate every Chinese text
mapping = {}

for text in all_texts:
    mapping[text] = text  # default: keep original

# Now apply all translations
translations = [
    ("\U0001f3ac Seedance 2.0 \u4f7f\u7528\u624b\u518c\uff08\u5168\u65b0\u591a\u6a21\u6001\u521b\u4f5c\u4f53\u9a8c\uff09",
     "\U0001f3ac Seedance 2.0 H\u01b0\u1edbng d\u1eabn s\u1eed d\u1ee5ng (Tr\u1ea3i nghi\u1ec7m s\u00e1ng t\u1ea1o \u0111a ph\u01b0\u01a1ng th\u1ee9c ho\u00e0n to\u00e0n m\u1edbi)"),
    ("\u89c6\u9891 Seedance 2.0 \u6b63\u5f0f\u4e0a\u7ebf\uff01",
     "Video Seedance 2.0 ch\u00ednh th\u1ee9c ra m\u1eaft!"),
]

# Instead of hardcoding hundreds of escaped strings, let me use a simpler approach
# Read the texts_to_translate.json and create translations inline

with open('texts_to_translate.json', 'r', encoding='utf-8') as f:
    texts_list = json.load(f)

# Index-based translations (matching the order in texts_to_translate.json)
vi_translations = [
    "\U0001f3ac Seedance 2.0 H\u01b0\u1edbng d\u1eabn s\u1eed d\u1ee5ng (Tr\u1ea3i nghi\u1ec7m s\u00e1ng t\u1ea1o \u0111a ph\u01b0\u01a1ng th\u1ee9c ho\u00e0n to\u00e0n m\u1edbi)",  # 0
    " Sao ch\u00e9p",  # 1 - keep
    "\U0001f300 ",  # 2 - keep emoji
    "Video Seedance 2.0 ch\u00ednh th\u1ee9c ra m\u1eaft!",  # 3
    "  Kill the game\uff01",  # 4 - keep
    "C\u00f2n nh\u1edb t\u1eeb ng\u00e0y ch\u1ec9 c\u00f3 th\u1ec3 d\u00f9ng v\u0103n b\u1ea3n v\u00e0 khung h\u00ecnh \u0111\u1ea7u/cu\u1ed1i \u0111\u1ec3 \"k\u1ec3 chuy\u1ec7n\", ch\u00fang t\u00f4i \u0111\u00e3 mu\u1ed1n t\u1ea1o ra m\u1ed9t m\u00f4 h\u00ecnh video th\u1ef1c s\u1ef1 hi\u1ec3u \u0111\u01b0\u1ee3c c\u00e1ch b\u1ea1n di\u1ec5n \u0111\u1ea1t. H\u00f4m nay, n\u00f3 th\u1ef1c s\u1ef1 \u0111\u00e3 \u0111\u1ebfn!",  # 5
    "Seedance 2.0 hi\u1ec7n h\u1ed7 tr\u1ee3 b\u1ed1n lo\u1ea1i \u0111\u1ea7u v\u00e0o \u0111a ph\u01b0\u01a1ng th\u1ee9c: h\u00ecnh \u1ea3nh, video, \u00e2m thanh, v\u0103n b\u1ea3n \u2014 c\u00e1ch di\u1ec5n \u0111\u1ea1t phong ph\u00fa h\u01a1n, vi\u1ec7c t\u1ea1o n\u1ed9i dung c\u0169ng d\u1ec5 ki\u1ec3m so\u00e1t h\u01a1n",  # 6
]

# This approach is too tedious with escapes. Let me write translations directly.
print("Building mapping with direct text...")

# Create a comprehensive mapping file by writing translations directly
direct_map = {}

# Read all texts and create translations
# I'll write a simpler version that processes the JSON directly

# Map of Chinese -> Vietnamese translations
zh_vi = {
    "使用手册": "Hướng dẫn sử dụng",
    "全新多模态创作体验": "Trải nghiệm sáng tạo đa phương thức hoàn toàn mới",
    "正式上线": "chính thức ra mắt",
    "还记得": "Còn nhớ",
    "讲故事": "kể chuyện",
    "视频模型": "mô hình video",
}

# Actually, let me just write the full mapping as a JSON file directly
# by processing the original texts

print("Done - will use full_translate.py instead")
