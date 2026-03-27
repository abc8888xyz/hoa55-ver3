# -*- coding: utf-8 -*-
"""
Auto-translate a Lark document: read → translate → write back → cleanup.
Pipeline hoàn toàn in-memory, không tạo file trung gian.

Usage:
    python auto_translate.py <url> <mapping_file> [options]

Options:
    --dry-run           Chỉ đọc và kiểm tra mapping, không ghi lên Lark
    --keep-unmapped     Giữ file _unmapped.json để debug (mặc định: xóa)
    --record-id <id>    Record ID trong Bitable để cập nhật tiến độ
"""
import json, sys, re, os, time
from dotenv import load_dotenv
from lark_api import LarkAPI, TEXT_BLOCK_TYPES, SKIP_BLOCK_TYPES

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

load_dotenv()

LARK_APP_ID = os.getenv("LARK_APP_ID")
LARK_APP_SECRET = os.getenv("LARK_APP_SECRET")

# Temp files cần dọn dẹp
TEMP_FILES = ['_temp_read.json', '_temp_write.json', '_unmapped.json']


def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff\u3400-\u4dbf]', text))


def read_doc(api, url):
    """Đọc tài liệu Lark trực tiếp qua API, trả về data trong RAM."""
    doc_id, err = api.resolve_doc_id(url)
    if err:
        print(f"ERROR: {err}")
        sys.exit(1)

    doc_info = api.get_document_info(doc_id)
    if doc_info.get("code") != 0:
        print(f"ERROR: Không thể đọc tài liệu: {doc_info}")
        sys.exit(1)

    doc_data = doc_info.get("data", {}).get("document", {})
    title = doc_data.get("title", "")
    revision = doc_data.get("revision_id", -1)

    blocks, block_err = api.get_all_blocks(doc_id)
    if block_err:
        print(f"ERROR: Không thể đọc blocks: {block_err}")
        sys.exit(1)

    translatable = api.extract_translatable_blocks(blocks)

    return {
        "doc_id": doc_id,
        "url": url,
        "title": title,
        "revision": revision,
        "total_blocks": len(blocks),
        "translatable_blocks": len(translatable),
        "blocks": translatable
    }


def extract_chinese(data):
    """Trích xuất danh sách đoạn text tiếng Trung (in-memory)."""
    segments = []
    for bi, block in enumerate(data.get('blocks', [])):
        for ei, elem in enumerate(block.get('elements', [])):
            content = elem.get('content', '')
            if content.strip() and has_chinese(content):
                segments.append({'bi': bi, 'ei': ei, 'content': content})
    return segments


def apply_mapping(data, mapping):
    """Áp dụng bản dịch vào data (in-memory). Trả về (translated, kept, errors)."""
    translated = 0
    kept = 0
    errors = 0
    unmapped = []

    for block in data.get('blocks', []):
        for elem in block.get('elements', []):
            content = elem.get('content', '')
            if not content.strip():
                continue
            if has_chinese(content):
                if content in mapping:
                    elem['content'] = mapping[content]
                    translated += 1
                else:
                    errors += 1
                    unmapped.append(content)
            else:
                kept += 1

    if data.get('title') in mapping:
        data['title'] = mapping[data['title']]

    return translated, kept, errors, unmapped


def write_doc(api, doc_id, blocks):
    """Ghi trực tiếp từng block lên Lark, không qua file trung gian."""
    total = len(blocks)
    success_count = 0
    fail_count = 0

    print(f"Bắt đầu ghi {total} blocks...")

    for i, block in enumerate(blocks):
        block_id = block["block_id"]
        elements = block["elements"]

        max_retries = 5
        for attempt in range(max_retries):
            result = api.update_block_text(doc_id, block_id, elements)
            if result.get("code") == 0:
                success_count += 1
                print(f"  [{i+1}/{total}] ok {block_id[:16]}...")
                break
            elif result.get("code") == 99991400:
                wait_time = (attempt + 1) * 3
                print(f"  [{i+1}/{total}] rate-limited, wait {wait_time}s (attempt {attempt+1})")
                time.sleep(wait_time)
            else:
                fail_count += 1
                print(f"  [{i+1}/{total}] FAIL {block_id[:16]}: {result.get('msg', '')[:60]}")
                break
        else:
            fail_count += 1
            print(f"  [{i+1}/{total}] FAIL {block_id[:16]}: max retries")

        if i < total - 1:
            time.sleep(1.0)

    print(f"\nKết quả ghi: {success_count}/{total} thành công, {fail_count} lỗi")
    return success_count, fail_count


def cleanup(keep_unmapped=False):
    """Xóa tất cả temp files."""
    for f in TEMP_FILES:
        if f == '_unmapped.json' and keep_unmapped:
            continue
        if os.path.exists(f):
            os.remove(f)
            print(f"  Đã xóa: {f}")


def update_bitable(record_id, vi_title, stats):
    """Cập nhật tiến độ vào Bitable (nếu có record_id)."""
    if not record_id:
        return
    try:
        from bitable_update import update
        result = update(record_id, {
            'Trạng thái': 'Đã dịch',
            'Tên tiếng Việt': vi_title,
            'Tổng số block': stats['total_blocks'],
            'Đã dịch thành công': stats['success_blocks'],
            'Block lỗi': stats['failed_blocks'],
            'Tổng đoạn text': stats['total_text'],
            'Đoạn đã dịch': stats['translated'],
            'Đoạn giữ nguyên': stats['kept'],
            'Tiếng Trung còn lại': stats['errors'],
        })
        print(f"Bitable: {result.get('code', -1)} {result.get('msg', '')}")
    except Exception as e:
        print(f"Bitable update failed: {e}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    url = sys.argv[1]
    mapping_file = sys.argv[2]
    dry_run = '--dry-run' in sys.argv
    keep_unmapped = '--keep-unmapped' in sys.argv

    record_id = None
    if '--record-id' in sys.argv:
        idx = sys.argv.index('--record-id')
        if idx + 1 < len(sys.argv):
            record_id = sys.argv[idx + 1]

    # Load mapping
    with open(mapping_file, 'r', encoding='utf-8') as f:
        mapping = json.load(f)
    print(f"Mapping: {len(mapping)} entries")

    # Init API
    api = LarkAPI(LARK_APP_ID, LARK_APP_SECRET)
    api.detect_base_url(url)
    success, _ = api.auth()
    if not success:
        print("ERROR: Xác thực Lark thất bại")
        sys.exit(1)

    # 1. Đọc tài liệu (in-memory)
    print(f"\n[1/4] Đọc tài liệu...")
    data = read_doc(api, url)
    print(f"  Title: {data['title']}")
    print(f"  Blocks: {data['total_blocks']} tổng, {data['translatable_blocks']} cần dịch")

    # 2. Phân tích & áp dụng mapping (in-memory)
    print(f"\n[2/4] Áp dụng bản dịch...")
    segments = extract_chinese(data)
    print(f"  Đoạn tiếng Trung: {len(segments)}")

    translated, kept, errors, unmapped = apply_mapping(data, mapping)
    print(f"  Đã dịch: {translated}, Giữ nguyên: {kept}, Chưa có bản dịch: {errors}")

    if unmapped and keep_unmapped:
        with open('_unmapped.json', 'w', encoding='utf-8') as f:
            json.dump(unmapped, f, ensure_ascii=False, indent=2)
        print(f"  Lưu {len(unmapped)} đoạn chưa dịch vào _unmapped.json")
    elif unmapped:
        print(f"  {len(unmapped)} đoạn chưa dịch (dùng --keep-unmapped để xem chi tiết)")

    # 3. Ghi lên Lark (trực tiếp, không qua file)
    success_blocks = 0
    failed_blocks = 0
    if dry_run:
        print(f"\n[3/4] DRY-RUN — bỏ qua ghi lên Lark")
        success_blocks = data['translatable_blocks']
    else:
        print(f"\n[3/4] Ghi lên Lark...")
        success_blocks, failed_blocks = write_doc(api, data['doc_id'], data['blocks'])

    # 4. Cập nhật Bitable & dọn dẹp
    print(f"\n[4/4] Hoàn tất...")
    total_text = translated + kept + errors
    stats = {
        'total_blocks': data['translatable_blocks'],
        'success_blocks': success_blocks,
        'failed_blocks': failed_blocks,
        'total_text': total_text,
        'translated': translated,
        'kept': kept,
        'errors': errors,
    }

    if not dry_run and record_id:
        update_bitable(record_id, data.get('title', ''), stats)

    cleanup(keep_unmapped)

    # Summary table
    pct_blocks = (success_blocks / data['translatable_blocks'] * 100) if data['translatable_blocks'] else 0
    pct_text = (translated / total_text * 100) if total_text else 0

    print(f"\n{'='*60}")
    print(f"  BẢNG THỐNG KÊ DỊCH THUẬT")
    print(f"{'='*60}")
    print(f"  {'Tài liệu:':<25} {data['title']}")
    print(f"  {'URL:':<25} {url}")
    print(f"{'─'*60}")
    print(f"  {'Hạng mục':<30} {'Số lượng':>10} {'Tỷ lệ':>10}")
    print(f"{'─'*60}")
    print(f"  {'Tổng blocks tài liệu':<30} {data['total_blocks']:>10}")
    print(f"  {'Blocks cần dịch':<30} {data['translatable_blocks']:>10}")
    print(f"  {'Blocks ghi thành công':<30} {success_blocks:>10} {pct_blocks:>9.1f}%")
    print(f"  {'Blocks ghi lỗi':<30} {failed_blocks:>10}")
    print(f"{'─'*60}")
    print(f"  {'Tổng đoạn text':<30} {total_text:>10}")
    print(f"  {'Đoạn đã dịch':<30} {translated:>10} {pct_text:>9.1f}%")
    print(f"  {'Đoạn giữ nguyên (EN/URL)':<30} {kept:>10}")
    print(f"  {'Đoạn chưa có bản dịch':<30} {errors:>10}")
    print(f"{'─'*60}")
    print(f"  {'Temp files:':<25} đã dọn sạch")
    print(f"{'='*60}")
    print(f"\n  Link tài liệu: {url}")

    print(f"\nSTATS:total_blocks={data['translatable_blocks']},translated={translated},kept={kept},errors={errors},total_text={total_text}")
