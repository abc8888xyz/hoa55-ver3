# -*- coding: utf-8 -*-
"""Build translation dict from keys, apply to orig, save trans."""
import json, copy, re, sys

with open('_art4_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('_art4_keys.json', 'r', encoding='utf-8') as f:
    keys = json.load(f)

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

# Build translations list in same order as keys
# Index: key -> translation
T = {}

for k in keys:
    T[k] = k  # default: keep unchanged

# Now set translations for all Chinese content
# Using a helper to avoid quote issues
def t(key, val):
    if key in T:
        T[key] = val

# === TITLE ===
t("AI\u5207\u78cb\u5927\u4f1a22\u671f 3\u670829\u65e5-\u9f99\u867e\u8857\u533a",
  "\u0110\u1ea1i h\u1ed9i giao l\u01b0u AI k\u1ef3 22 ng\u00e0y 29/3 - Khu ph\u1ed1 T\u00f4m h\u00f9m")

# I'll use a simpler approach - read the translations from a Python module
# Let me just build the mapping programmatically

# Map of all translations
translations_list = [
    # Format: (original_chinese, vietnamese_translation)
]

# Let me write all translations directly
# This is more reliable than JSON with special chars

print(f"Total keys: {len(keys)}")
print(f"Keys with Chinese: {sum(1 for k in keys if has_chinese(k))}")
print(f"Keys without Chinese: {sum(1 for k in keys if not has_chinese(k))}")
