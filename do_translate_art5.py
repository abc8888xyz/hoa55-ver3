# -*- coding: utf-8 -*-
import sys, json, copy
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

with open('art5_original.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

translated = copy.deepcopy(data)

T = {}
T[(0,0)] = "Tìm bạn đồng hành cho tôm hùm Openclaw"
T[(1,0)] = "🔗 Link bài gốc: "
T[(2,0)] = "Tự tay làm một thiết bị nhỏ có thể hiển thị trạng thái thực thi thời gian thực của tôm hùm.\nCái board này là diễn viên kỳ cựu rồi.\n"
T[(2,1)] = "Có thể xem quá trình thực thi, nội dung phản hồi, WiFi, Gateway, và mức tiêu thụ token. Cùng một số thông tin khác."

translated_count = 0
kept_count = 0
total_text = 0
for i, block in enumerate(translated['blocks']):
    for j, el in enumerate(block['elements']):
        if el['type'] == 'text_run':
            total_text += 1
            if (i,j) in T:
                el['content'] = T[(i,j)]
                translated_count += 1
            else:
                kept_count += 1

with open('art5_translated.json', 'w', encoding='utf-8') as f:
    json.dump(translated, f, ensure_ascii=False, indent=2)

print(f"Total: {total_text}, Translated: {translated_count}, Kept: {kept_count}")
