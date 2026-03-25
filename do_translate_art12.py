# -*- coding: utf-8 -*-
import sys, json, copy
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

with open('art12_original.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
translated = copy.deepcopy(data)

T = {}
T[(0,0)] = "Hướng dẫn của AJ đang hoàn thiện"
T[(1,0)] = "Quy trình chia sẻ ngày 25 tháng 2"
T[(2,0)] = "Toàn bộ quá trình trò chuyện với AI, để nó giúp bạn"
T[(3,0)] = " Mua cloud server"
T[(4,0)] = "Mua coding plan"
T[(5,0)] = "Cài Claude code (node.js22)"
T[(6,0)] = "Để cc cài openclaw"
T[(7,0)] = "Cấu hình đến Lark và các đầu nối khác"
T[(8,0)] = "Nuôi tôm"
T[(9,0)] = "Thiết lập biện pháp bảo mật trước"
T[(10,0)] = "soul.md và các thiết lập liên quan"
T[(12,0)] = "Làm bốn case ví dụ"
T[(13,0)] = "Gửi task định kỳ trong hội thoại"
T[(14,0)] = "Cài đặt dự án"
T[(15,0)] = "Tự làm một trang web push lên github"
T[(16,0)] = "Lưu một skill nào đó, thực thi một skill nào đó"
T[(17,0)] = "Hiển thị hình ảnh"
T[(17,1)] = "Chia sẻ skills prompt của AJ"
T[(18,0)] = "Mẹo thường gặp"
T[(19,0)] = "Claudecode chuyển đổi model"
T[(20,0)] = "Chuyển khi khởi động claude code"
T[(20,1)] = ": Thực thi"
T[(20,3)] = "để chỉ định model, ví dụ"
T[(20,5)] = "."
T[(21,0)] = "Trong cuộc hội thoại"
T[(21,1)] = ": Thực thi lệnh"
T[(21,3)] = "để chuyển model, ví dụ"
T[(21,5)] = "."
T[(22,0)] = "Link liên quan:"
T[(23,0)] = "Mua Alibaba Cloud codingplan:"
T[(24,0)] = "Hướng dẫn sử dụng Alibaba Cloud codingplan"
T[(25,0)] = "Cách lấy API key "
T[(26,0)] = "Cài cc"
T[(27,0)] = "Vấn đề"
T[(28,0)] = "claude code tôi chat thế nào cũng không sao; tôm hùm chat được một lúc là đầy, phải nén hoặc lưu vào memory.md"
T[(29,0)] = "Tài liệu Lark không ghi được"
T[(30,0)] = "Giải pháp:"
T[(31,0)] = "2026-02-26 Tôi cũng gặp vấn đề tương tự, qua gợi ý của thầy AJ, tôi đã cho con tôm hùm nhà đi học kỹ tài liệu API của feishu, xử lý hoàn hảo;"
T[(32,0)] = "｜ À, quên giới thiệu con tôm hùm nhà tôi tên Hope, bài tài liệu giải quyết vấn đề này cũng do nó viết, hy vọng giúp ích cho các bạn cũng gặp vấn đề【nội dung tài liệu feishu trống】"

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

with open('art12_translated.json', 'w', encoding='utf-8') as f:
    json.dump(translated, f, ensure_ascii=False, indent=2)
print(f"Total: {total_text}, Translated: {translated_count}, Kept: {kept_count}")
