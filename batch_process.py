# -*- coding: utf-8 -*-
"""
Read a Lark doc, extract Chinese segments to a numbered list for manual translation.
Usage: python batch_process.py read <url> <num>
       python batch_process.py apply <num>
       python batch_process.py write <url> <num>
       python batch_process.py stats <num>
"""
import json, sys, re, subprocess, time
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff\u3400-\u4dbf]', text))

def cmd_read(url, num):
    subprocess.run([sys.executable, 'lark_api.py', 'read', url, '--output', f'orig_{num}.json'],
                   encoding='utf-8')
    with open(f'orig_{num}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    segs = []
    for block in data.get('blocks', []):
        for elem in block.get('elements', []):
            content = elem.get('content', '')
            if content.strip() and has_chinese(content):
                segs.append(content)
    with open(f'segs_{num}.json', 'w', encoding='utf-8') as f:
        json.dump(segs, f, ensure_ascii=False, indent=2)
    print(f"Doc {num}: {data.get('title', '')}")
    print(f"  Blocks: {data.get('translatable_blocks', 0)}, Chinese segments: {len(segs)}")

def cmd_apply(num):
    with open(f'orig_{num}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open(f'map_{num}.json', 'r', encoding='utf-8') as f:
        mapping = json.load(f)

    translated = kept = errors = 0
    for block in data.get('blocks', []):
        for elem in block.get('elements', []):
            content = elem.get('content', '')
            if not content.strip(): continue
            if has_chinese(content):
                if content in mapping:
                    elem['content'] = mapping[content]
                    translated += 1
                else:
                    errors += 1
                    print(f"  UNMAPPED: {content[:80]}")
            else:
                kept += 1
    if data.get('title') in mapping:
        data['title'] = mapping[data['title']]

    with open(f'trans_{num}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    total = translated + kept + errors
    blocks = data.get('translatable_blocks', len(data.get('blocks', [])))
    print(f"  Translated: {translated}, Kept: {kept}, Errors: {errors}")
    return blocks, translated, kept, errors, total

def cmd_write(url, num):
    result = subprocess.run(
        [sys.executable, '-u', 'lark_api.py', 'write', url, f'trans_{num}.json'],
        capture_output=True, text=True, encoding='utf-8', timeout=300
    )
    out = result.stdout + result.stderr
    # Parse result
    if '"status": "ok"' in out:
        print(f"  Write: ALL blocks OK")
        return True
    else:
        # Find success/failed counts
        try:
            idx = out.rindex('{')
            j = json.loads(out[idx:])
            print(f"  Write: {j.get('success',0)} ok, {j.get('failed',0)} failed")
            if j.get('failed', 0) > 0:
                time.sleep(10)
                # Retry
                result2 = subprocess.run(
                    [sys.executable, '-u', 'lark_api.py', 'write', url, f'trans_{num}.json'],
                    capture_output=True, text=True, encoding='utf-8', timeout=300
                )
                out2 = result2.stdout + result2.stderr
                if '"status": "ok"' in out2:
                    print(f"  Retry: ALL blocks OK")
                    return True
        except:
            pass
    return False

def cmd_table_resize(url):
    subprocess.run([sys.executable, 'lark_api.py', 'table-resize', url],
                   encoding='utf-8', timeout=60)

if __name__ == '__main__':
    action = sys.argv[1]
    if action == 'read':
        cmd_read(sys.argv[2], sys.argv[3])
    elif action == 'apply':
        cmd_apply(sys.argv[2])
    elif action == 'write':
        cmd_write(sys.argv[2], sys.argv[3])
    elif action == 'resize':
        cmd_table_resize(sys.argv[2])
