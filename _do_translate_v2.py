# -*- coding: utf-8 -*-
import json, copy, re

with open('_art4_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

# Build translation dict by reading each unique content and mapping
T = {}

def t(k, v):
    T[k] = v

# ========== ALL TRANSLATIONS ==========
# Title and headings
t("AI\u5207\u78cb\u5927\u4f1a22\u671f 3\u670829\u65e5-\u9f99\u867e\u8857\u533a",
  "\u0110\u1ea1i h\u1ed9i giao l\u01b0u AI k\u1ef3 22 ng\u00e0y 29/3 - Khu ph\u1ed1 T\u00f4m h\u00f9m")

t("\ud83e\udde6 \u5c0f\u9f99\u867e\u8857\u533a-40\u4e2a\u57ce\u5e02\u540c\u65f6\u5f00\u5c55",
  "\ud83e\udde6 Khu ph\u1ed1 T\u00f4m h\u00f9m - Di\u1ec5n ra \u0111\u1ed3ng th\u1eddi t\u1ea1i 40 th\u00e0nh ph\u1ed1")

# OK this unicode escape approach is too tedious. Let me use a different strategy.
# I'll read the keys from the JSON file and match by index.

with open('_art4_keys.json', 'r', encoding='utf-8') as f:
    keys = json.load(f)

# Print keys with indices for building translation array
for i, k in enumerate(keys):
    if has_chinese(k):
        print(f"IDX {i}: {k[:60]}")
