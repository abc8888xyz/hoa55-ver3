# -*- coding: utf-8 -*-
"""Resume writing translated blocks from a given index"""
import json, sys, time, requests, os
from dotenv import load_dotenv

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

load_dotenv()

LARK_APP_ID = os.getenv("LARK_APP_ID")
LARK_APP_SECRET = os.getenv("LARK_APP_SECRET")
BASE_URL = "https://open.larksuite.com/open-apis"

# Get token
resp = requests.post(f"{BASE_URL}/auth/v3/tenant_access_token/internal",
                     json={"app_id": LARK_APP_ID, "app_secret": LARK_APP_SECRET})
token = resp.json()["tenant_access_token"]
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

# Load trans json
with open('_art18_trans.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

doc_id = data["doc_id"]
blocks = data["blocks"]
start_idx = int(sys.argv[1]) if len(sys.argv) > 1 else 234
total = len(blocks)

print(f"Resuming from block {start_idx}/{total}, doc_id={doc_id}")

success_count = 0
fail_count = 0

for i in range(start_idx, total):
    block = blocks[i]
    block_id = block["block_id"]
    elements = block["elements"]

    # Build API elements
    api_elements = []
    for el in elements:
        if el["type"] == "text_run":
            api_el = {"text_run": {"content": el["content"]}}
            if el.get("style"):
                clean_style = {k: v for k, v in el["style"].items() if v is not None and v != "" and v is not False}
                if clean_style:
                    api_el["text_run"]["text_element_style"] = clean_style
            api_elements.append(api_el)
        elif el["type"] == "mention_user":
            api_elements.append({"mention_user": el["data"]})
        elif el["type"] == "mention_doc":
            api_elements.append({"mention_doc": el["data"]})
        elif el["type"] == "reminder":
            api_elements.append({"reminder": el["data"]})
        elif el["type"] == "equation":
            api_elements.append({"equation": el["data"]})
        elif el["type"] == "unknown":
            api_elements.append(el["data"])

    body = {"update_text_elements": {"elements": api_elements}}
    url = f"{BASE_URL}/docx/v1/documents/{doc_id}/blocks/{block_id}"
    params = {"document_revision_id": -1}

    max_retries = 5
    for attempt in range(max_retries):
        resp = requests.patch(url, headers=headers, json=body, params=params)
        result = resp.json()
        if result.get("code") == 0:
            success_count += 1
            print(f"  [{i+1}/{total}] OK {block_id}")
            break
        elif result.get("code") == 99991400:
            wait_time = (attempt + 1) * 3
            print(f"  [{i+1}/{total}] Rate limited, wait {wait_time}s (attempt {attempt+1})")
            time.sleep(wait_time)
        elif result.get("code") == 99991401:
            # Token expired, refresh
            resp2 = requests.post(f"{BASE_URL}/auth/v3/tenant_access_token/internal",
                                  json={"app_id": LARK_APP_ID, "app_secret": LARK_APP_SECRET})
            token = resp2.json()["tenant_access_token"]
            headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
            print(f"  [{i+1}/{total}] Token refreshed, retrying...")
        else:
            fail_count += 1
            print(f"  [{i+1}/{total}] FAIL {block_id}: {result.get('msg', '')[:80]}")
            break
    else:
        fail_count += 1
        print(f"  [{i+1}/{total}] MAX RETRIES {block_id}")

    if i < total - 1:
        time.sleep(1.0)

print(f"\nDone! Success: {success_count}, Failed: {fail_count}")
