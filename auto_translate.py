# -*- coding: utf-8 -*-
"""
Auto-translate a Lark document: read, apply mapping, write back.
Usage: python auto_translate.py <url> <mapping_file> [--dry-run]
"""
import json, sys, re, os, time, requests
from dotenv import load_dotenv

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

load_dotenv()

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff\u3400-\u4dbf]', text))

def read_doc(url):
    """Read doc using lark_api"""
    import subprocess
    result = subprocess.run(
        [sys.executable, 'lark_api.py', 'read', url, '--output', '_temp_read.json'],
        capture_output=True, text=True, encoding='utf-8'
    )
    print(result.stdout, end='')
    if result.stderr:
        print(result.stderr, end='', file=sys.stderr)
    with open('_temp_read.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_chinese(data):
    """Extract all Chinese text segments"""
    segments = []
    for bi, block in enumerate(data.get('blocks', [])):
        for ei, elem in enumerate(block.get('elements', [])):
            content = elem.get('content', '')
            if content.strip() and has_chinese(content):
                segments.append({'bi': bi, 'ei': ei, 'content': content})
    return segments

def apply_mapping(data, mapping):
    """Apply translation mapping"""
    translated = 0
    kept = 0
    errors = 0
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
            else:
                kept += 1
    if data.get('title') in mapping:
        data['title'] = mapping[data['title']]
    return translated, kept, errors

def write_doc(url, data):
    """Write doc using lark_api"""
    import subprocess
    with open('_temp_write.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Try up to 3 times
    for attempt in range(3):
        result = subprocess.run(
            [sys.executable, '-u', 'lark_api.py', 'write', url, '_temp_write.json'],
            capture_output=True, text=True, encoding='utf-8', timeout=300
        )
        output = result.stdout + result.stderr
        if '"status": "ok"' in output:
            print("  Write: ALL blocks successful")
            return True
        elif '"status": "partial"' in output:
            # Parse how many failed
            try:
                j = json.loads(output[output.index('{'):])
                failed = j.get('failed', 0)
                print(f"  Write attempt {attempt+1}: {j.get('success',0)} ok, {failed} failed")
                if failed <= 3:
                    time.sleep(10)
                    continue
            except:
                pass
        time.sleep(10)
    return False

if __name__ == '__main__':
    url = sys.argv[1]
    mapping_file = sys.argv[2]

    with open(mapping_file, 'r', encoding='utf-8') as f:
        mapping = json.load(f)

    data = read_doc(url)
    segments = extract_chinese(data)
    print(f"Chinese segments: {len(segments)}")

    translated, kept, errors = apply_mapping(data, mapping)
    print(f"Translated: {translated}, Kept: {kept}, Errors: {errors}")

    if errors > 0:
        # Dump unmapped for review
        unmapped = []
        for block in data.get('blocks', []):
            for elem in block.get('elements', []):
                content = elem.get('content', '')
                if content.strip() and has_chinese(content):
                    unmapped.append(content)
        with open('_unmapped.json', 'w', encoding='utf-8') as f:
            json.dump(unmapped, f, ensure_ascii=False, indent=2)
        print(f"Unmapped segments saved to _unmapped.json")

    if '--dry-run' not in sys.argv:
        write_doc(url, data)

    total_text = translated + kept + errors
    total_blocks = data.get('translatable_blocks', len(data.get('blocks', [])))
    print(f"STATS:total_blocks={total_blocks},translated={translated},kept={kept},errors={errors},total_text={total_text}")
