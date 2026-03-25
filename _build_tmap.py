# -*- coding: utf-8 -*-
import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
import json

with open('_art_b6_7_keys.json', 'r', encoding='utf-8') as f:
    keys = json.load(f)

# Build translation pairs: (original, translated)
pairs = [
    ("OpenClaw \u5b8c\u5168\u6307\u5357:\u4ece\u5b89\u88c5\u5230\u5b9e\u6218\u7684 24/7 AI \u5458\u5de5\u517b\u6210\u624b\u518c",
     "H\u01b0\u1edbng d\u1eabn to\u00e0n di\u1ec7n OpenClaw: S\u1ed5 tay \u0111\u00e0o t\u1ea1o nh\u00e2n vi\u00ean AI 24/7 t\u1eeb c\u00e0i \u0111\u1eb7t \u0111\u1ebfn th\u1ef1c chi\u1ebfn"),
    ("\U0001f517 \u539f\u6587\u94fe\u63a5\uff1a ",
     "\U0001f517 Link g\u1ed1c: "),
    ("\u5c0f\u4f19\u4f34\u4eec\u4e5f\u53ef\u4ee5\u901a\u8fc7\u963f\u91cc\u4e91\u767e\u70bc",
     "C\u00e1c b\u1ea1n c\u0169ng c\u00f3 th\u1ec3 tri\u1ec3n khai th\u00f4ng qua Alibaba Cloud Bailian"),
    ("\u6765\u90e8\u7f72",
     " \u0111\u1ec3 tri\u1ec3n khai"),
    ("\uff1a", ":"),
    ("\u9996\u8d2d\u4f4e\u81f3 7.9 \u5143\uff0c\u7eed\u8d39 5 \u6298\u8d77\uff0c\u652f\u6301Qwen3.5\u3001Qwen3-max\u3001Qwen3-coder\u3001GLM-5\u3001GLM-4.7\u3001Kimi-k2.5\u7b49\u6a21\u578b",
     "Mua l\u1ea7n \u0111\u1ea7u ch\u1ec9 t\u1eeb 7.9 CNY, gia h\u1ea1n gi\u1ea3m 50%, h\u1ed7 tr\u1ee3 c\u00e1c m\u00f4 h\u00ecnh Qwen3.5, Qwen3-max, Qwen3-coder, GLM-5, GLM-4.7, Kimi-k2.5"),
    ("\U0001f449\u6233\u94fe\u63a5\u76f4\u8fbe\uff1a",
     "\U0001f449 Nh\u1ea5n link truy c\u1eadp: "),
    ("\U0001f449\u67e5\u770b\u8be6\u7ec6\u90e8\u7f72\u6559\u7a0b\uff1a",
     "\U0001f449 Xem h\u01b0\u1edbng d\u1eabn tri\u1ec3n khai chi ti\u1ebft: "),
]

# This is getting tedious with unicode escapes. Let me just map index->translation
# Read the original keys file and map by exact content match

T = {}

# I'll create pairs from the original keys list directly
# The keys list has 206 entries, let me map each Chinese one
vi = [None] * 206  # translations indexed by position

vi[0] = "H\u01b0\u1edbng d\u1eabn to\u00e0n di\u1ec7n OpenClaw: S\u1ed5 tay \u0111\u00e0o t\u1ea1o nh\u00e2n vi\u00ean AI 24/7 t\u1eeb c\u00e0i \u0111\u1eb7t \u0111\u1ebfn th\u1ef1c chi\u1ebfn"

# OK this approach with unicode escapes is going to be extremely painful.
# Let me just write raw UTF-8 strings using a different approach.
print("This approach won't work well. Using direct file write instead.")
