# -*- coding: utf-8 -*-
import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

import json
from _tmap import T

with open('_art_b6_7_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

stats = {"translated": 0, "kept": 0, "total": 0, "missing": 0}
missing_list = []

for block in data["blocks"]:
    for el in block["elements"]:
        if el["type"] == "text_run":
            stats["total"] += 1
            content = el["content"]
            if content.startswith("http") or content == "openclaw.ai":
                stats["kept"] += 1
                continue
            if content in T:
                el["content"] = T[content]
                stats["translated"] += 1
            else:
                cn_chars = sum(1 for c in content if '\u4e00' <= c <= '\u9fff')
                if cn_chars == 0:
                    stats["kept"] += 1
                else:
                    stats["missing"] += 1
                    missing_list.append(content[:80])

if missing_list:
    print("MISSING translations:")
    for m in missing_list:
        print(f"  {m}")

print(f"\nStats: translated={stats['translated']}, kept={stats['kept']}, missing={stats['missing']}, total={stats['total']}")

data["title"] = T.get(data["title"], data["title"])

with open('_art_b6_7_trans.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Saved _art_b6_7_trans.json")
