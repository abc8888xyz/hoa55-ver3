#!/usr/bin/env python3
"""Parse _build_trans_map25.py to extract translations, build map, apply to article."""
import sys, json, re

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Load all CN texts
with open('_art25_cn_texts.json', 'r', encoding='utf-8') as f:
    all_cn = json.load(f)

# Parse the build script to extract t() calls
with open('_build_trans_map25.py', 'r', encoding='utf-8') as f:
    script = f.read()

def parse_t_calls(script_text):
    """Parse t() calls from the script, handling embedded quotes."""
    pairs = {}
    calls = script_text.split('\nt(')
    for call in calls[1:]:
        depth = 1
        end = -1
        for i, c in enumerate(call):
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
                if depth == 0:
                    end = i
                    break
        if end == -1:
            continue
        args_str = call[:end]
        if not args_str.startswith('"'):
            continue
        sep_patterns = ['",\n  "', '", "', '",\n"']
        best_sep = None
        best_pos = -1
        for sep in sep_patterns:
            pos = args_str.rfind(sep)
            if pos > best_pos:
                best_pos = pos
                best_sep = sep
        if best_pos == -1:
            continue
        cn = args_str[1:best_pos]
        vi_start = best_pos + len(best_sep)
        vi = args_str[vi_start:]
        if vi.endswith('"'):
            vi = vi[:-1]
        pairs[cn] = vi
    return pairs

trans = parse_t_calls(script)
print(f"Parsed {len(trans)} pairs from script")

# Meeting minutes phrase substitution
def translate_meeting(text):
    result = text
    phrases = [
        ('智能纪要：', 'Biên bản thông minh: '),
        ('特邀嘉宾', 'Khách mời đặc biệt'),
        ('直播核心亮点：', 'Điểm nổi bật của buổi livestream:'),
        ('直播核心亮点', 'Điểm nổi bật của buổi livestream'),
        ('直播亮点：', 'Điểm nổi bật livestream:'),
        ('直播亮点', 'Điểm nổi bật livestream'),
        ('直播嘉宾：', 'Khách mời livestream:'),
        ('分享嘉宾：', 'Khách mời chia sẻ:'),
        ('主持团：', 'Nhóm MC:'),
        ('主持人：', 'MC:'),
        ('视频教程', 'Video hướng dẫn'),
        ('讲师：', 'Giảng viên:'),
        ('嘉宾：', 'Khách mời:'),
        ('主讲:', 'Giảng viên chính:'),
        ('WaytoAGI晚8点共学', 'WaytoAGI Học chung lúc 8 giờ tối'),
        ('先看清这个行业在"赚谁的钱"，再决定你要不要进来', 'Trước tiên hãy hiểu rõ ngành này đang kiếm tiền của ai, rồi quyết định bạn có muốn vào không'),
        ('全国会议', 'Hội nghị toàn quốc'),
        ('功能亮点：', 'Điểm nổi bật tính năng:'),
        ('每周四秒哒时间', 'Thời gian Miaouda mỗi thứ Năm'),
        ('第三届', 'Lần thứ 3'),
        ('启动会', 'Hội nghị khởi động'),
        ('年', ' năm '),
        ('月', ' tháng '),
        ('日', ''),
    ]
    for cn, vi in phrases:
        result = result.replace(cn, vi)
    return result

# Apply meeting translations for remaining texts
for text in all_cn:
    if text not in trans and re.search(r'[\u4e00-\u9fff]', text):
        translated = translate_meeting(text)
        if translated != text:
            trans[text] = translated

# Save the map
with open('_art25_trans_map.json', 'w', encoding='utf-8') as f:
    json.dump(trans, f, ensure_ascii=False, indent=2)

covered = sum(1 for t in all_cn if t in trans)
print(f"Translation map: {len(trans)} entries")
print(f"Coverage: {covered}/{len(all_cn)} ({100*covered/len(all_cn):.1f}%)")

remaining = [t for t in all_cn if t not in trans]
if remaining:
    print(f"\nRemaining {len(remaining)} untranslated:")
    for r in remaining[:20]:
        short = r[:80].replace('\n', '\\n')
        print(f"  [{all_cn.index(r)}] {short}")
