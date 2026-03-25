# -*- coding: utf-8 -*-
"""
Batch translate Lark documents from Chinese to Vietnamese.
Reads from Bitable, translates each doc, updates status back to Bitable.
"""
import sys
import json
import requests
import os
import re
import time
import copy
from dotenv import load_dotenv

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

load_dotenv()

APP_ID = os.getenv("LARK_APP_ID")
APP_SECRET = os.getenv("LARK_APP_SECRET")
BASE = "https://open.larksuite.com/open-apis"

# Bitable config
BITABLE_APP_TOKEN = "Zp5lbBOQVa5jQss2z7FlMXlWgPQ"
BITABLE_TABLE_ID = "tblGnzG7okDuj79w"


def get_token():
    r = requests.post(f"{BASE}/auth/v3/tenant_access_token/internal",
                      json={"app_id": APP_ID, "app_secret": APP_SECRET})
    return r.json()["tenant_access_token"]


def headers(token):
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def get_all_records(token):
    """Get all records from Bitable"""
    all_records = []
    page_token = None
    while True:
        params = {"page_size": 100}
        if page_token:
            params["page_token"] = page_token
        r = requests.get(
            f"{BASE}/bitable/v1/apps/{BITABLE_APP_TOKEN}/tables/{BITABLE_TABLE_ID}/records",
            headers=headers(token), params=params)
        data = r.json().get("data", {})
        all_records.extend(data.get("items", []))
        if not data.get("has_more"):
            break
        page_token = data.get("page_token")
    return all_records


def update_record(token, record_id, fields):
    """Update a record in Bitable"""
    url = f"{BASE}/bitable/v1/apps/{BITABLE_APP_TOKEN}/tables/{BITABLE_TABLE_ID}/records/{record_id}"
    r = requests.put(url, headers=headers(token), json={"fields": fields})
    return r.json()


def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff\u3400-\u4dbf]', text))


# ─── Document Translation ──────────────────────────────────────

TEXT_BLOCK_TYPES = {
    1: "page", 2: "text", 3: "heading1", 4: "heading2", 5: "heading3",
    6: "heading4", 7: "heading5", 8: "heading6", 9: "heading7",
    10: "heading8", 11: "heading9", 12: "bullet", 13: "ordered",
    15: "quote", 17: "todo", 19: "callout",
}


def translate_document(token, url):
    """
    Translate a single Lark document. Returns dict with stats.
    This function reads the doc, sends text to Claude for translation via
    the existing translate mechanism, and updates the doc.
    """
    from lark_api import LarkAPI

    api = LarkAPI(APP_ID, APP_SECRET)
    api.detect_base_url(url)
    api.token = token  # reuse token

    # Resolve doc ID
    doc_id, err = api.resolve_doc_id(url)
    if err:
        return {"status": "error", "message": err}

    # Get doc info
    doc_info = api.get_document_info(doc_id)
    if doc_info.get("code") != 0:
        return {"status": "error", "message": "Cannot read document info"}

    doc_data = doc_info.get("data", {}).get("document", {})
    title = doc_data.get("title", "")

    # Get all blocks
    blocks, block_err = api.get_all_blocks(doc_id)
    if block_err:
        return {"status": "error", "message": "Cannot read blocks"}

    # Extract translatable blocks
    translatable = api.extract_translatable_blocks(blocks)
    total_blocks = len(translatable)

    if total_blocks == 0:
        return {
            "status": "ok",
            "title": title,
            "total_blocks": 0,
            "translated": 0,
            "kept": 0,
            "remaining_chinese": 0,
            "errors": 0,
        }

    # Translate each block's text elements
    translated_count = 0
    kept_count = 0
    remaining_chinese = 0

    for block in translatable:
        for elem in block.get("elements", []):
            if elem["type"] != "text_run":
                continue
            content = elem.get("content", "")
            if not content.strip():
                continue
            if has_chinese(content):
                translated_count += 1
                # Note: actual translation happens when writing via lark_api
            else:
                kept_count += 1

    # Save to temp files and use lark_api to process
    temp_original = f"_temp_original_{doc_id}.json"
    temp_translated = f"_temp_translated_{doc_id}.json"

    original_data = {
        "status": "ok",
        "doc_id": doc_id,
        "url": url,
        "title": title,
        "total_blocks": len(blocks),
        "translatable_blocks": total_blocks,
        "blocks": translatable,
    }

    with open(temp_original, 'w', encoding='utf-8') as f:
        json.dump(original_data, f, ensure_ascii=False, indent=2)

    return {
        "status": "needs_translation",
        "title": title,
        "doc_id": doc_id,
        "url": url,
        "total_blocks": total_blocks,
        "total_text": translated_count + kept_count,
        "chinese_text": translated_count,
        "kept_text": kept_count,
        "temp_file": temp_original,
    }


def resize_tables(token, url):
    """Resize table columns for Vietnamese text"""
    from lark_api import LarkAPI

    api = LarkAPI(APP_ID, APP_SECRET)
    api.detect_base_url(url)
    api.token = token

    doc_id, err = api.resolve_doc_id(url)
    if err:
        return 0

    blocks, _ = api.get_all_blocks(doc_id)
    if not blocks:
        return 0

    table_blocks = [b for b in blocks if b.get("block_type") == 31]
    resized = 0

    for tb in table_blocks:
        block_id = tb["block_id"]
        prop = tb.get("table", {}).get("property", {})
        cols = prop.get("column_size", 0)
        old_widths = prop.get("column_width", [])
        total_width = sum(old_widths)

        if cols < 2 or not old_widths:
            continue

        first_col = old_widths[0]
        increase = int(first_col * 0.25)
        mid_cols = cols - 2 if cols > 2 else 0

        if mid_cols > 0:
            decrease_per = increase // mid_cols
            new_widths = [first_col + increase]
            for i in range(1, cols - 1):
                new_widths.append(max(50, old_widths[i] - decrease_per))
            new_widths.append(old_widths[-1])
        else:
            new_widths = [first_col + increase, max(50, old_widths[-1] - increase)]

        diff = sum(new_widths) - total_width
        if diff != 0:
            new_widths[-1] = max(50, new_widths[-1] - diff)

        ok = True
        for col_idx, width in enumerate(new_widths):
            if width == old_widths[col_idx]:
                continue
            patch_url = f"{api.base_url}/docx/v1/documents/{doc_id}/blocks/{block_id}"
            payload = {"update_table_property": {"column_width": width, "column_index": col_idx}}
            params = {"document_revision_id": -1}
            resp = requests.patch(patch_url, headers=api.headers(), json=payload, params=params)
            if resp.json().get("code") != 0:
                ok = False
            time.sleep(0.3)

        if ok:
            resized += 1

    return resized


# ─── Main Loop ──────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("   BATCH TRANSLATE - Lark Documents (Trung → Việt)")
    print("=" * 60)

    token = get_token()
    print("✓ Xác thực thành công\n")

    # Get all records
    records = get_all_records(token)
    print(f"Tổng số record trong Base: {len(records)}")

    # Filter: docx with Link dịch, not yet translated
    to_translate = []
    for rec in records:
        f = rec.get("fields", {})
        link_dich = f.get("Link dịch")
        trang_thai = f.get("Trạng thái")
        loai_file = f.get("Loại File", "")

        if link_dich and loai_file == "docx" and not trang_thai:
            url = link_dich.get("link", "")
            title = f.get("Tiêu đề", "")
            if url:
                to_translate.append({
                    "record_id": rec["record_id"],
                    "url": url,
                    "title": title,
                })

    print(f"Cần dịch: {len(to_translate)} bài\n")

    if not to_translate:
        print("Không có bài nào cần dịch!")
        return

    # Process each document
    for i, item in enumerate(to_translate):
        record_id = item["record_id"]
        url = item["url"]
        title = item["title"]

        print(f"\n{'─' * 60}")
        print(f"[{i+1}/{len(to_translate)}] {title[:60]}")
        print(f"  URL: {url[:70]}...")

        # Update status to "Đang dịch"
        update_record(token, record_id, {"Trạng thái": "Đang dịch"})
        print("  → Trạng thái: Đang dịch")

        try:
            # Step 1: Read document
            result = translate_document(token, url)

            if result["status"] == "error":
                print(f"  ✗ Lỗi: {result['message']}")
                update_record(token, record_id, {
                    "Trạng thái": "Lỗi",
                    "Block lỗi": result["message"][:100],
                })
                continue

            if result["status"] == "ok" and result["total_blocks"] == 0:
                print("  → Không có text cần dịch")
                update_record(token, record_id, {
                    "Trạng thái": "Đã dịch",
                    "Tổng số block": "0",
                    "Tên tiếng Việt": title,
                })
                continue

            # Step 2: The actual translation needs to happen here
            # For now, we output the temp file path for manual/Claude translation
            print(f"  Tổng blocks: {result['total_blocks']}")
            print(f"  Text tiếng Trung: {result['chinese_text']}")
            print(f"  Text giữ nguyên: {result['kept_text']}")
            print(f"  File tạm: {result['temp_file']}")

            # The translation itself is done by Claude (the AI) reading
            # the original blocks and translating them.
            # This script prepares the data and updates the base.

            # For automated pipeline, we use lark_api.py read + write
            import subprocess

            # Read
            print("  → Đang đọc tài liệu...")
            proc = subprocess.run(
                ["python", "lark_api.py", "read", url, "--output", f"_orig_{i}.json"],
                capture_output=True, text=True, encoding='utf-8',
                cwd=os.path.dirname(os.path.abspath(__file__))
            )
            if proc.returncode != 0:
                print(f"  ✗ Lỗi đọc: {proc.stderr[:100]}")
                update_record(token, record_id, {"Trạng thái": "Lỗi"})
                continue

            # The translation step requires AI - output instruction
            print(f"  ⚠ CẦN DỊCH: File _orig_{i}.json")
            print(f"  → Dịch xong lưu vào _trans_{i}.json")
            print(f"  → Rồi chạy: python lark_api.py write \"{url}\" _trans_{i}.json")

            # Update base with partial info
            update_record(token, record_id, {
                "Tổng số block": str(result["total_blocks"]),
                "Tổng đoạn text": str(result["total_text"]),
                "Trạng thái": "Đang dịch",
            })

        except Exception as e:
            print(f"  ✗ Exception: {str(e)[:100]}")
            update_record(token, record_id, {
                "Trạng thái": "Lỗi",
                "Block lỗi": str(e)[:100],
            })

        # Rate limiting
        time.sleep(1)

    print(f"\n{'=' * 60}")
    print("  HOÀN TẤT QUÉT BASE")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
