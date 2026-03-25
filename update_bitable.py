"""Helper to update Bitable records via Lark API"""
import sys, json, os, requests
from dotenv import load_dotenv

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

load_dotenv()

APP_ID = os.getenv("LARK_APP_ID")
APP_SECRET = os.getenv("LARK_APP_SECRET")
BASE = "https://open.larksuite.com/open-apis"

def get_token():
    r = requests.post(f"{BASE}/auth/v3/tenant_access_token/internal", json={"app_id": APP_ID, "app_secret": APP_SECRET})
    return r.json()["tenant_access_token"]

def update_record(app_token, table_id, record_id, fields):
    token = get_token()
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    url = f"{BASE}/bitable/v1/apps/{app_token}/tables/{table_id}/records/{record_id}"
    r = requests.put(url, headers=headers, json={"fields": fields})
    return r.json()

if __name__ == "__main__":
    app_token = sys.argv[1]
    table_id = sys.argv[2]
    record_id = sys.argv[3]
    fields = json.loads(sys.argv[4])
    result = update_record(app_token, table_id, record_id, fields)
    print(json.dumps(result, ensure_ascii=False, indent=2))
