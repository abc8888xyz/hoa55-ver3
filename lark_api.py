"""
Lark API Helper - Đọc và cập nhật tài liệu Lark Docx/Wiki
Usage:
    python lark_api.py auth                          # Test xác thực
    python lark_api.py read <url> [--output file]    # Đọc nội dung tài liệu
    python lark_api.py write <url> <json_file>       # Cập nhật tài liệu đã dịch
"""

import requests
import json
import sys
import os
import re
import time
from dotenv import load_dotenv

# Fix Windows encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

load_dotenv()

LARK_APP_ID = os.getenv("LARK_APP_ID")
LARK_APP_SECRET = os.getenv("LARK_APP_SECRET")

# Block types chứa text có thể dịch được
# Key: block_type number, Value: tên field trong block JSON
TEXT_BLOCK_TYPES = {
    1: "page",
    2: "text",
    3: "heading1",
    4: "heading2",
    5: "heading3",
    6: "heading4",
    7: "heading5",
    8: "heading6",
    9: "heading7",
    10: "heading8",
    11: "heading9",
    12: "bullet",
    13: "ordered",
    15: "quote",
    17: "todo",
    19: "callout",
}

# Block types KHÔNG dịch (code, diagram, v.v.)
SKIP_BLOCK_TYPES = {14}  # code block


class LarkAPI:
    def __init__(self, app_id, app_secret):
        self.app_id = app_id
        self.app_secret = app_secret
        self.base_url = "https://open.larksuite.com/open-apis"
        self.token = None

    def detect_base_url(self, url):
        """Tự động detect Feishu vs Lark dựa trên URL"""
        if "feishu.cn" in url:
            self.base_url = "https://open.feishu.cn/open-apis"
        else:
            self.base_url = "https://open.larksuite.com/open-apis"

    def auth(self):
        """Lấy tenant_access_token"""
        url = f"{self.base_url}/auth/v3/tenant_access_token/internal"
        resp = requests.post(url, json={
            "app_id": self.app_id,
            "app_secret": self.app_secret
        })
        data = resp.json()
        if data.get("code") == 0:
            self.token = data["tenant_access_token"]
            return True, data
        return False, data

    def headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def parse_url(self, url):
        """Parse Lark URL để lấy loại tài liệu và ID"""
        self.detect_base_url(url)

        # Wiki URL
        wiki_match = re.search(r'/wiki/([A-Za-z0-9]+)', url)
        if wiki_match:
            return "wiki", wiki_match.group(1)

        # Docx URL
        docx_match = re.search(r'/docx/([A-Za-z0-9]+)', url)
        if docx_match:
            return "docx", docx_match.group(1)

        # Old doc URL
        doc_match = re.search(r'/docs/([A-Za-z0-9]+)', url)
        if doc_match:
            return "doc", doc_match.group(1)

        return None, None

    def get_wiki_node(self, token):
        """Lấy thông tin thực của tài liệu từ wiki token"""
        url = f"{self.base_url}/wiki/v2/spaces/get_node"
        resp = requests.get(url, headers=self.headers(), params={"token": token})
        data = resp.json()
        if data.get("code") == 0:
            node = data["data"]["node"]
            return node.get("obj_token"), node.get("obj_type")
        return None, None

    def resolve_doc_id(self, url):
        """Từ URL, resolve ra doc_id thực tế"""
        doc_type, doc_token = self.parse_url(url)

        if doc_type == "wiki":
            obj_token, obj_type = self.get_wiki_node(doc_token)
            if not obj_token:
                return None, "Không thể lấy thông tin wiki node"
            return obj_token, None
        elif doc_type == "docx":
            return doc_token, None
        elif doc_type == "doc":
            return None, "Chưa hỗ trợ old docs format. Vui lòng chuyển sang docx."
        else:
            return None, f"Không nhận dạng được URL: {url}"

    def get_document_info(self, doc_id):
        """Lấy thông tin tài liệu (title, revision, v.v.)"""
        url = f"{self.base_url}/docx/v1/documents/{doc_id}"
        resp = requests.get(url, headers=self.headers())
        return resp.json()

    def get_all_blocks(self, doc_id):
        """Lấy tất cả blocks trong tài liệu (có phân trang)"""
        url = f"{self.base_url}/docx/v1/documents/{doc_id}/blocks"
        all_blocks = []
        page_token = None

        while True:
            params = {"page_size": 500}
            if page_token:
                params["page_token"] = page_token
            resp = requests.get(url, headers=self.headers(), params=params)
            data = resp.json()

            if data.get("code") != 0:
                return None, data

            items = data.get("data", {}).get("items", [])
            all_blocks.extend(items)

            page_token = data.get("data", {}).get("page_token")
            if not page_token:
                break

        return all_blocks, None

    def extract_translatable_blocks(self, blocks):
        """Trích xuất các block có text cần dịch"""
        result = []

        for block in blocks:
            block_type = block.get("block_type")

            # Bỏ qua code blocks và block types không hỗ trợ
            if block_type in SKIP_BLOCK_TYPES:
                continue
            if block_type not in TEXT_BLOCK_TYPES:
                continue

            field_name = TEXT_BLOCK_TYPES[block_type]
            content = block.get(field_name, {})
            elements = content.get("elements", [])

            if not elements:
                continue

            # Trích xuất elements
            text_elements = []
            has_translatable_text = False

            for el in elements:
                if "text_run" in el:
                    text_content = el["text_run"].get("content", "")
                    style = el["text_run"].get("text_element_style", {})

                    text_elements.append({
                        "type": "text_run",
                        "content": text_content,
                        "style": style
                    })

                    # Kiểm tra xem có text thực sự cần dịch không
                    if text_content.strip():
                        has_translatable_text = True

                elif "mention_user" in el:
                    text_elements.append({
                        "type": "mention_user",
                        "data": el["mention_user"]
                    })
                elif "mention_doc" in el:
                    text_elements.append({
                        "type": "mention_doc",
                        "data": el["mention_doc"]
                    })
                elif "reminder" in el:
                    text_elements.append({
                        "type": "reminder",
                        "data": el["reminder"]
                    })
                elif "equation" in el:
                    text_elements.append({
                        "type": "equation",
                        "data": el["equation"]
                    })
                else:
                    # Giữ nguyên element không nhận dạng
                    text_elements.append({
                        "type": "unknown",
                        "data": el
                    })

            if has_translatable_text:
                result.append({
                    "block_id": block["block_id"],
                    "block_type": block_type,
                    "block_type_name": field_name,
                    "elements": text_elements
                })

        return result

    def update_block_text(self, doc_id, block_id, elements):
        """Cập nhật text elements của một block"""
        # Chuyển đổi elements về format API
        api_elements = []
        for el in elements:
            if el["type"] == "text_run":
                api_el = {
                    "text_run": {
                        "content": el["content"]
                    }
                }
                # Thêm style nếu có (loại bỏ null values)
                if el.get("style"):
                    clean_style = {}
                    for k, v in el["style"].items():
                        if v is not None and v != "" and v is not False:
                            clean_style[k] = v
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

        body = {
            "update_text_elements": {
                "elements": api_elements
            }
        }

        url = f"{self.base_url}/docx/v1/documents/{doc_id}/blocks/{block_id}"
        params = {"document_revision_id": -1}
        resp = requests.patch(url, headers=self.headers(), json=body, params=params)
        return resp.json()


# ─── CLI Commands ───────────────────────────────────────────────

def cmd_auth():
    """Test xác thực với Lark"""
    api = LarkAPI(LARK_APP_ID, LARK_APP_SECRET)
    success, data = api.auth()
    if success:
        print(json.dumps({
            "status": "ok",
            "message": "Xác thực thành công",
            "expire": data.get("expire")
        }, ensure_ascii=False, indent=2))
    else:
        print(json.dumps({
            "status": "error",
            "message": "Xác thực thất bại",
            "data": data
        }, ensure_ascii=False, indent=2))
        sys.exit(1)


def cmd_read(url, output_file=None):
    """Đọc tài liệu Lark và xuất JSON chứa text cần dịch"""
    api = LarkAPI(LARK_APP_ID, LARK_APP_SECRET)
    api.detect_base_url(url)

    # Auth
    success, auth_data = api.auth()
    if not success:
        print(json.dumps({
            "status": "error",
            "message": "Xác thực thất bại",
            "data": auth_data
        }, ensure_ascii=False, indent=2))
        sys.exit(1)

    # Resolve doc ID
    doc_id, err = api.resolve_doc_id(url)
    if err:
        print(json.dumps({
            "status": "error",
            "message": err
        }, ensure_ascii=False, indent=2))
        sys.exit(1)

    # Lấy thông tin tài liệu
    doc_info = api.get_document_info(doc_id)
    if doc_info.get("code") != 0:
        print(json.dumps({
            "status": "error",
            "message": "Không thể đọc thông tin tài liệu",
            "data": doc_info
        }, ensure_ascii=False, indent=2))
        sys.exit(1)

    doc_data = doc_info.get("data", {}).get("document", {})
    title = doc_data.get("title", "")
    revision = doc_data.get("revision_id", -1)

    # Lấy tất cả blocks
    blocks, block_err = api.get_all_blocks(doc_id)
    if block_err:
        print(json.dumps({
            "status": "error",
            "message": "Không thể đọc blocks",
            "data": block_err
        }, ensure_ascii=False, indent=2))
        sys.exit(1)

    # Trích xuất blocks cần dịch
    translatable = api.extract_translatable_blocks(blocks)

    result = {
        "status": "ok",
        "doc_id": doc_id,
        "url": url,
        "title": title,
        "revision": revision,
        "total_blocks": len(blocks),
        "translatable_blocks": len(translatable),
        "blocks": translatable
    }

    output = json.dumps(result, ensure_ascii=False, indent=2)

    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"Đã lưu {len(translatable)} blocks cần dịch vào {output_file}")
    else:
        print(output)


def cmd_write(url, json_file):
    """Cập nhật tài liệu Lark với nội dung đã dịch"""
    api = LarkAPI(LARK_APP_ID, LARK_APP_SECRET)
    api.detect_base_url(url)

    # Auth
    success, auth_data = api.auth()
    if not success:
        print(json.dumps({
            "status": "error",
            "message": "Xác thực thất bại"
        }, ensure_ascii=False, indent=2))
        sys.exit(1)

    # Resolve doc ID
    doc_id, err = api.resolve_doc_id(url)
    if err:
        print(json.dumps({
            "status": "error",
            "message": err
        }, ensure_ascii=False, indent=2))
        sys.exit(1)

    # Load JSON đã dịch
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    blocks = data.get("blocks", [])
    total = len(blocks)
    success_count = 0
    fail_count = 0
    errors = []

    print(f"Bắt đầu cập nhật {total} blocks...")

    for i, block in enumerate(blocks):
        block_id = block["block_id"]
        elements = block["elements"]

        # Retry with backoff on rate limit
        max_retries = 5
        for attempt in range(max_retries):
            result = api.update_block_text(doc_id, block_id, elements)
            if result.get("code") == 0:
                success_count += 1
                print(f"  [{i+1}/{total}] ✓ Block {block_id}")
                break
            elif result.get("code") == 99991400:
                wait_time = (attempt + 1) * 3
                print(f"  [{i+1}/{total}] ⏳ Rate limited, waiting {wait_time}s... (attempt {attempt+1}/{max_retries})")
                time.sleep(wait_time)
            else:
                fail_count += 1
                error_msg = result.get("msg", "Unknown error")
                errors.append({
                    "block_id": block_id,
                    "block_type": block.get("block_type_name", ""),
                    "error_code": result.get("code"),
                    "error_msg": error_msg
                })
                print(f"  [{i+1}/{total}] ✗ Block {block_id}: {error_msg}")
                break
        else:
            fail_count += 1
            errors.append({
                "block_id": block_id,
                "block_type": block.get("block_type_name", ""),
                "error_code": 99991400,
                "error_msg": "Max retries exceeded for rate limit"
            })
            print(f"  [{i+1}/{total}] ✗ Block {block_id}: Max retries exceeded")

        # Rate limiting - tránh bị Lark limit
        if i < total - 1:
            time.sleep(1.0)

    # Báo cáo kết quả
    report = {
        "status": "ok" if fail_count == 0 else "partial",
        "doc_id": doc_id,
        "url": url,
        "total_blocks": total,
        "success": success_count,
        "failed": fail_count,
        "errors": errors if errors else None
    }

    print("\n" + json.dumps(report, ensure_ascii=False, indent=2))


def cmd_table_resize(url):
    """Tự động tìm và điều chỉnh chiều rộng cột bảng cho phù hợp tiếng Việt"""
    api = LarkAPI(LARK_APP_ID, LARK_APP_SECRET)
    api.detect_base_url(url)

    success, auth_data = api.auth()
    if not success:
        print(json.dumps({"status": "error", "message": "Xác thực thất bại"}, ensure_ascii=False))
        sys.exit(1)

    doc_id, err = api.resolve_doc_id(url)
    if err:
        print(json.dumps({"status": "error", "message": err}, ensure_ascii=False))
        sys.exit(1)

    blocks, block_err = api.get_all_blocks(doc_id)
    if block_err:
        print(json.dumps({"status": "error", "message": "Không thể đọc blocks"}, ensure_ascii=False))
        sys.exit(1)

    table_blocks = [b for b in blocks if b.get("block_type") == 31]
    if not table_blocks:
        print("Không tìm thấy bảng nào trong tài liệu.")
        return

    print(f"Tìm thấy {len(table_blocks)} bảng. Đang điều chỉnh chiều rộng cột...")

    success_count = 0
    fail_count = 0

    for tb in table_blocks:
        block_id = tb["block_id"]
        prop = tb.get("table", {}).get("property", {})
        cols = prop.get("column_size", 0)
        old_widths = prop.get("column_width", [])
        total_width = sum(old_widths)

        if cols == 0 or not old_widths:
            continue

        # Tính toán chiều rộng mới: mở rộng cột đầu (prompt) ~30%
        # và cột cuối (kết quả) giữ nguyên hoặc tăng nhẹ
        first_col = old_widths[0]
        last_col = old_widths[-1] if cols > 1 else 0

        # Tăng cột đầu thêm ~25%, lấy từ các cột giữa
        increase = int(first_col * 0.25)
        mid_cols = cols - 2 if cols > 2 else 0

        if mid_cols > 0:
            decrease_per = increase // mid_cols
            new_widths = [first_col + increase]
            for i in range(1, cols - 1):
                new_widths.append(max(50, old_widths[i] - decrease_per))
            new_widths.append(last_col)
        elif cols == 2:
            new_widths = [first_col + increase, max(50, last_col - increase)]
        else:
            new_widths = old_widths  # 1 cột, không cần chỉnh

        # Cân bằng tổng chiều rộng
        diff = sum(new_widths) - total_width
        if diff != 0:
            new_widths[-1] = max(50, new_widths[-1] - diff)

        print(f"\n  Bảng {block_id[:20]}... ({cols} cột)")
        print(f"    Cũ: {old_widths}")
        print(f"    Mới: {new_widths}")

        # Cập nhật từng cột
        table_ok = True
        for col_idx, width in enumerate(new_widths):
            if width == old_widths[col_idx]:
                continue
            patch_url = f"{api.base_url}/docx/v1/documents/{doc_id}/blocks/{block_id}"
            payload = {"update_table_property": {"column_width": width, "column_index": col_idx}}
            params = {"document_revision_id": -1}
            resp = requests.patch(patch_url, headers=api.headers(), json=payload, params=params)
            result = resp.json()
            if result.get("code") == 0:
                print(f"    ✓ Cột {col_idx}: {old_widths[col_idx]} → {width}px")
            else:
                print(f"    ✗ Cột {col_idx}: {result.get('msg', '')[:60]}")
                table_ok = False
                if result.get("code") == 99991400:
                    time.sleep(3)
            time.sleep(0.4)

        if table_ok:
            success_count += 1
        else:
            fail_count += 1

    print(f"\n{'='*50}")
    print(f"✅ Thành công: {success_count} bảng")
    if fail_count:
        print(f"❌ Lỗi: {fail_count} bảng")
    print(f"{'='*50}")


# ─── Main ───────────────────────────────────────────────────────

def print_usage():
    print("""
Lark API Helper - Đọc và cập nhật tài liệu Lark

Usage:
    python lark_api.py auth                              Test xác thực
    python lark_api.py read <url>                        Đọc tài liệu (stdout)
    python lark_api.py read <url> --output <file>        Đọc tài liệu (lưu file)
    python lark_api.py write <url> <json_file>           Cập nhật tài liệu
    python lark_api.py table-resize <url>                Điều chỉnh bảng cho tiếng Việt

Yêu cầu:
    - File .env chứa LARK_APP_ID và LARK_APP_SECRET
    - Lark App cần quyền: docx:document, docx:document:readonly
    - Với wiki: cần thêm quyền wiki:wiki:readonly
""")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "auth":
        cmd_auth()

    elif cmd == "read":
        if len(sys.argv) < 3:
            print("Error: Thiếu URL")
            print("Usage: python lark_api.py read <url> [--output <file>]")
            sys.exit(1)
        url = sys.argv[2]
        output_file = None
        if "--output" in sys.argv:
            idx = sys.argv.index("--output")
            if idx + 1 < len(sys.argv):
                output_file = sys.argv[idx + 1]
        cmd_read(url, output_file)

    elif cmd == "write":
        if len(sys.argv) < 4:
            print("Error: Thiếu URL hoặc JSON file")
            print("Usage: python lark_api.py write <url> <json_file>")
            sys.exit(1)
        cmd_write(sys.argv[2], sys.argv[3])

    elif cmd == "table-resize":
        if len(sys.argv) < 3:
            print("Error: Thiếu URL")
            print("Usage: python lark_api.py table-resize <url>")
            sys.exit(1)
        cmd_table_resize(sys.argv[2])

    else:
        print(f"Lệnh không hợp lệ: {cmd}")
        print_usage()
        sys.exit(1)
