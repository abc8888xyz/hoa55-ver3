# -*- coding: utf-8 -*-
"""Quick Bitable updater - pass record_id and fields as args"""
import sys, json, requests, os
from dotenv import load_dotenv

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

load_dotenv()
APP_ID = os.getenv('LARK_APP_ID')
APP_SECRET = os.getenv('LARK_APP_SECRET')
BASE = 'https://open.larksuite.com/open-apis'
BITABLE_APP = 'Zp5lbBOQVa5jQss2z7FlMXlWgPQ'
BITABLE_TABLE = 'tblGnzG7okDuj79w'

def get_token():
    r = requests.post(f'{BASE}/auth/v3/tenant_access_token/internal',
                      json={'app_id': APP_ID, 'app_secret': APP_SECRET})
    return r.json()['tenant_access_token']

def update(record_id, fields):
    token = get_token()
    h = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    url = f'{BASE}/bitable/v1/apps/{BITABLE_APP}/tables/{BITABLE_TABLE}/records/{record_id}'
    r = requests.put(url, headers=h, json={'fields': fields})
    return r.json()

if __name__ == '__main__':
    # Usage: python bitable_update.py <record_id> <status|complete> [vi_title] [stats...]
    record_id = sys.argv[1]
    action = sys.argv[2]

    if action == 'status':
        status_val = sys.argv[3]
        result = update(record_id, {'Trạng thái': status_val})
    elif action == 'complete':
        vi_title = sys.argv[3]
        total_blocks = int(sys.argv[4])
        success_blocks = int(sys.argv[5])
        failed_blocks = int(sys.argv[6])
        total_text = int(sys.argv[7])
        translated_text = int(sys.argv[8])
        kept_text = int(sys.argv[9])
        result = update(record_id, {
            'Trạng thái': 'Đã dịch',
            'Tên tiếng Việt': vi_title,
            'Tổng số block': total_blocks,
            'Đã dịch thành công': success_blocks,
            'Block lỗi': failed_blocks,
            'Tổng đoạn text': total_text,
            'Đoạn đã dịch': translated_text,
            'Đoạn giữ nguyên': kept_text,
            'Tiếng Trung còn lại': 0,
        })

    code = result.get('code', -1)
    msg = result.get('msg', 'unknown')
    print(f'{code} {msg}')
