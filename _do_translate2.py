# -*- coding: utf-8 -*-
"""Translate _art_b6_7_orig.json CN->VI and save as _art_b6_7_trans.json"""
import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

import json

with open('_art_b6_7_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Build translation map from original keys
# Read all unique text_run contents
all_contents = []
for block in data['blocks']:
    for el in block['elements']:
        if el['type'] == 'text_run':
            all_contents.append(el['content'])

# Translation by index position in all_contents list (206 items)
# None = keep original (URL, non-Chinese, etc.)
vi = [None] * len(all_contents)

vi[0] = "H\u01b0\u1edbng d\u1eabn to\u00e0n di\u1ec7n OpenClaw: S\u1ed5 tay \u0111\u00e0o t\u1ea1o nh\u00e2n vi\u00ean AI 24/7 t\u1eeb c\u00e0i \u0111\u1eb7t \u0111\u1ebfn th\u1ef1c chi\u1ebfn"
vi[1] = "\U0001f517 Link g\u1ed1c: "
# vi[2] = URL, keep
vi[3] = "C\u00e1c b\u1ea1n c\u0169ng c\u00f3 th\u1ec3 tri\u1ec3n khai th\u00f4ng qua Alibaba Cloud Bailian"
# vi[4] = "Coding Plan ", keep as is
vi[5] = " \u0111\u1ec3 tri\u1ec3n khai"
vi[6] = ":"
vi[7] = "Mua l\u1ea7n \u0111\u1ea7u ch\u1ec9 t\u1eeb 7.9 CNY, gia h\u1ea1n gi\u1ea3m 50%, h\u1ed7 tr\u1ee3 c\u00e1c m\u00f4 h\u00ecnh Qwen3.5, Qwen3-max, Qwen3-coder, GLM-5, GLM-4.7, Kimi-k2.5"
vi[8] = "\U0001f449 Nh\u1ea5n link truy c\u1eadp: "
# vi[9] = URL, keep
vi[10] = "\U0001f449 Xem h\u01b0\u1edbng d\u1eabn tri\u1ec3n khai chi ti\u1ebft: "
# vi[11] = URL, keep
vi[12] = "Ch\u1ec9 c\u1ea7n t\u1ed1i \u0111a ba b\u01b0\u1edbc, b\u1ea1n s\u1ebd c\u00f3 tr\u1ee3 l\u00fd AI tr\u1ef1c tuy\u1ebfn 7x24 gi\u1edd, ph\u1ea3n h\u1ed3i m\u1ecdi l\u00fac"

# OK, this unicode escape approach is terrible. Let me just write the translations inline.
# Python source files support UTF-8 natively with the encoding declaration.
# The issue was with bash heredocs, not with .py files written by the Write tool.

print("Starting translation...")

# I'll build T dict using a different method - read from a Python module
# Actually let me just hardcode translations inline since Write tool handles UTF-8
T = {}

# I'll populate T programmatically
lines = [
    ("OpenClaw \u5b8c\u5168\u6307\u5357:\u4ece\u5b89\u88c5\u5230\u5b9e\u6218\u7684 24/7 AI \u5458\u5de5\u517b\u6210\u624b\u518c", "H\u01b0\u1edbng d\u1eabn to\u00e0n di\u1ec7n OpenClaw: S\u1ed5 tay \u0111\u00e0o t\u1ea1o nh\u00e2n vi\u00ean AI 24/7 t\u1eeb c\u00e0i \u0111\u1eb7t \u0111\u1ebfn th\u1ef1c chi\u1ebfn"),
]
# This is still painful. Let me try yet another approach.

# APPROACH: Read orig, for each text_run that has Chinese, look up by block_id + element index
# and apply translation from a CSV-like structure

# Actually the simplest approach: write translations as a Python list of tuples in a separate .py file
# and import it. But that has the same encoding issues.

# FINAL APPROACH: Just do the translation directly in this script using the index approach
# Map from index in all_contents -> Vietnamese translation

print(f"Total text_runs: {len(all_contents)}")
print("Script needs to be populated with translations. Aborting.")
sys.exit(1)
