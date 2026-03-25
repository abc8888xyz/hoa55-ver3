"""
Reusable article translation pipeline.
Usage: python translate_article.py <url> <record_id> <vi_title> <translations_file>
"""
import json, sys, os, re, requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("LARK_APP_ID")
APP_SECRET = os.getenv("LARK_APP_SECRET")
BASE = "https://open.larksuite.com/open-apis"
APP_TOKEN = "Zp5lbBOQVa5jQss2z7FlMXlWgPQ"
TABLE_ID = "tblGnzG7okDuj79w"

def get_token():
    r = requests.post(f"{BASE}/auth/v3/tenant_access_token/internal",
                      json={"app_id": APP_ID, "app_secret": APP_SECRET})
    return r.json()["tenant_access_token"]

def update_bitable(record_id, fields):
    token = get_token()
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    url = f"{BASE}/bitable/v1/apps/{APP_TOKEN}/tables/{TABLE_ID}/records/{record_id}"
    r = requests.put(url, headers=headers, json={"fields": fields})
    return r.json()

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

def apply_translations(data, translations):
    stats = {"total_blocks": len(data["blocks"]), "translated": 0, "kept": 0,
             "total_text": 0, "errors": []}
    for i, block in enumerate(data["blocks"]):
        for j, elem in enumerate(block.get("elements", [])):
            content = elem.get("content", "")
            if not content.strip():
                continue
            stats["total_text"] += 1
            key = f"B{i}E{j}"
            if key in translations:
                elem["content"] = translations[key]
                stats["translated"] += 1
            elif not has_chinese(content):
                stats["kept"] += 1
            else:
                stats["errors"].append(key)
    return stats
