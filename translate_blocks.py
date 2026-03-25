"""Translate Chinese text in blocks JSON to Vietnamese"""
import json, re, sys, os

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

# Translation dictionary for common terms/phrases
TRANSLATIONS = {
    # Title and headers
    "龙虾生态观察V2：创业分层与演进路径": "Quan sát hệ sinh thái Tôm hùm V2: Phân tầng khởi nghiệp và lộ trình phát triển",
    "用OpenClaw搭跨境电商团队：5个AI员工，跑通全平台矩阵！": "Dùng OpenClaw xây dựng đội ngũ thương mại điện tử xuyên biên giới: 5 nhân viên AI, chạy thông ma trận đa nền tảng!",
    "02-22直播回放 |陈财猫 ：一天消耗10亿token的龙虾养成记\n": "02-22 Phát lại livestream | Trần Tài Miêu: Nhật ký nuôi tôm hùm tiêu hao 1 tỷ token mỗi ngày\n",
}

def translate_text(text):
    """Translate Chinese text to Vietnamese. Returns translated text."""
    if not text or not text.strip():
        return text
    if not has_chinese(text):
        return text
    
    # Check exact match first
    if text in TRANSLATIONS:
        return TRANSLATIONS[text]
    
    # For texts that are just Chinese, translate them
    # This is a placeholder - the actual translation will be done by replacing
    # the content in the JSON manually or via a more sophisticated method
    return text  # Will be replaced by actual translations

def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'original_blocks.json'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'translated_blocks.json'
    
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    stats = {'total_blocks': len(data['blocks']), 'translated': 0, 'kept': 0, 'total_text': 0}
    
    for block in data['blocks']:
        for elem in block.get('elements', []):
            content = elem.get('content', '')
            if content.strip():
                stats['total_text'] += 1
                translated = translate_text(content)
                if translated != content:
                    elem['content'] = translated
                    stats['translated'] += 1
                else:
                    if not has_chinese(content):
                        stats['kept'] += 1
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(json.dumps(stats))

if __name__ == '__main__':
    main()
