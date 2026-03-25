import json, sys, copy

sys.stdout.reconfigure(encoding='utf-8')

with open('_art33_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Translation map: block_index -> list of translations for text_run elements
# None = keep original (for URLs, code, brand names, etc.)
translations = {
    0: ['Clawdbot quá dữ! Hướng dẫn từng bước kết nối với Feishu, đưa trợ lý AI vào cộng đồng'],
    1: ['🔗 Link gốc: ', None],
    2: ['⏰ Thời gian đăng: 2026-01-28 09:01:00 (UTC+8)'],
    3: ['Tác giả: Bút ký AI của Lâm Nguyệt Bán Tử'],
    4: ['Gần đây Clawdbot (', None, ') bùng nổ, mạng xã hội tràn ngập bài giới thiệu.'],
    5: ['Các bạn có thể triển khai thông qua Alibaba Cloud Bailian ', None, ' để triển khai', ':'],
    6: ['Mua lần đầu chỉ từ 7,9 tệ, gia hạn giảm từ 50%, hỗ trợ các mô hình Qwen3.5, Qwen3-max, Qwen3-coder, GLM-5, GLM-4.7, Kimi-k2.5'],
    7: ['👉 Nhấn link truy cập: ', None],
    8: ['👉 Xem hướng dẫn triển khai chi tiết: ', None],
    9: ['Chỉ cần tối đa ba bước, bạn sẽ có trợ lý AI hoạt động 24/7, phản hồi mọi lúc'],
    10: ['Hướng dẫn cài đặt cơ bản đã có rất nhiều, các cao thủ đã giải thích rất chi tiết, mình không lặp lại nữa, ai chưa cài xong thì đi bổ sung trước.'],
    11: ['Hôm nay nói về một kịch bản thiết thực, nhiều nhóm dùng Feishu để cộng tác, vậy làm sao kết nối Clawdbot với Feishu?'],
    12: ['Danh sách plugin chính thức không có Feishu.'],
    13: ['Nhưng điều đó không làm khó chúng ta, mình đã tổng hợp toàn bộ quy trình, giúp bạn tránh bẫy, dưới đây là thao tác thực tế.'],
    14: ['Bước 1: Chuẩn bị nền tảng mở Feishu.'],
    15: ['Trước tiên làm "chứng minh thư" cho robot, đăng nhập nền tảng mở Feishu, tạo ứng dụng mới.'],
    16: ['Sau khi tạo xong, kích hoạt khả năng robot.'],
    17: ['Cấu hình quyền rất quan trọng, để robot có thể gửi và nhận tin nhắn, cần mở các quyền liên quan, cách nhanh nhất là nhập hàng loạt, dán đoạn mã JSON sau.'],
    18: ['Xác nhận xong, nhập hàng loạt là được.'],
    19: ['Bước 2: Cài đặt plugin Feishu.'],
    20: ['Quay lại phía ClawdBot.'],
    21: ['Như đã nói ở trên, kho plugin chính thức không có Feishu, chúng ta cần sử dụng dự án cộng đồng ', None, None, ' để thực hiện.'],
    22: ['Thực thi lệnh cài đặt trong terminal.'],
    23: ['Bước 3: Cấu hình tương tác.'],
    24: ['Sau khi cài plugin xong, chạy ', None, ' để vào trình hướng dẫn, có một loạt lựa chọn tương tác, làm theo hình của mình.'],
    25: ['Môi trường chạy: mình triển khai local, nhấn Enter chọn mặc định local.'],
    26: ['Chọn kênh: chọn channels, tức là kênh chat.'],
    27: ['Thêm cấu hình: tiếp tục thêm cấu hình Channels.'],
    28: ['Chọn channel: chọn Feishu.'],
    29: ['Nhập khóa bí mật: quay lại nền tảng mở Feishu, tìm AppID và AppSecret điền vào.'],
    30: ['Tùy chọn tiếp theo: phiên bản Feishu chọn mặc định trong nước'],
    31: ['Chiến lược chat nhóm chọn Open để tiện kiểm thử'],
    32: ['Nhấn Enter liên tục đến finished.'],
    33: ['Cuối cùng nó sẽ hỏi chúng ta có muốn gửi tin nhắn trực tiếp cho nó không? Chúng ta chọn yes'],
    34: ['Bước 4: Kiểm thử kết nối một chiều (ClawdBot -> Feishu)'],
    35: ['Sau khi cấu hình xong, chúng ta kiểm thử xem robot có thể gửi tin nhắn ra ngoài không. ', 'Bước này nếu thành công, nghĩa là App ID và Secret của bạn không điền sai.'],
    36: ['Tạo một nhóm trên Feishu, kéo robot vừa kích hoạt vào nhóm.'],
    37: ['Trong cài đặt nhóm, sao chép ', None, ' (ID hội thoại).'],
    38: ['Trong giao diện cấu hình ClawdBot, thử gửi một tin nhắn đến nhóm này.'],
    39: ['Có thể thấy nhóm Feishu đã nhận được tin nhắn:'],
    40: ['Kết luận: Đường truyền ClawdBot -> Feishu là OK.'],
    41: ['Bước 5: Khai thông "nhâm đốc nhị mạch".'],
    42: ['Lúc này, nếu bạn hào hứng @robot trong nhóm Feishu nói một câu, bạn sẽ phát hiện: ', 'Bạn không nhận được phản hồi từ ClawdBot.'],
    43: ['Tại sao?'],
    44: ['Vì Feishu không biết đẩy tin nhắn đi đâu, triển khai local không có IP công cộng, chúng ta cần cấu hình ', 'kết nối dài hạn (WebSocket)', ', đây cũng là bước quan trọng nhất.'],
    45: ['Bật kết nối dài hạn ở backend Feishu, vào sự kiện và callback, chọn kết nối dài hạn, nhấn lưu.'],
    46: ['Đồng thời cần thêm đăng ký sự kiện, trong cấu hình sự kiện, thêm sự kiện nhận tin nhắn, robot mới nghe được bạn nói.'],
    47: ['Cuối cùng, đừng quên nhấn phát hành phiên bản, nếu không cấu hình sẽ không có hiệu lực.'],
    48: ['Sửa file cấu hình local, mở file cấu hình local ', None, '.'],
    49: ['Trong trường feishu, thêm thủ công hai dòng, báo cho ClawdBot dùng chế độ kết nối dài hạn.'],
    50: ['Sau khi cấu hình xong, khởi động lại ClawdBot.'],
    51: ['Bước 6: Nghiệm thu cuối cùng hai chiều'],
    52: ['Sẵn sàng.'],
    53: ['Chúng ta gửi tin nhắn cho robot trong nhóm, @robot trong nhóm, nếu thấy biểu tượng robot nhấp nháy, nghĩa là đang ở trạng thái hoạt động.'],
    54: ['Đợi một chút, nó phản hồi bạn, nghĩa là đường truyền Feishu đến ClawdBot cũng OK rồi.'],
    55: ['Đến đây ClawdBot đã nhập hội Feishu thành công, có thể tận hưởng trải nghiệm AI mượt mà, chat riêng chat nhóm đều có thể túc trực 24 giờ.'],
    56: ['Nhanh đi thử nào.'],
    57: ['Mình là Lâm Nguyệt Bán Tử, theo dõi mình, cùng nhau khám phá khả năng vô hạn của tự động hóa quy trình công việc.'],
}

# Build translated data
trans_data = copy.deepcopy(data)

stats = {'total_text': 0, 'translated': 0, 'kept': 0}

for block_idx, block in enumerate(trans_data['blocks']):
    text_run_idx = 0
    for el in block['elements']:
        if el['type'] == 'text_run':
            stats['total_text'] += 1
            if block_idx in translations:
                trans_list = translations[block_idx]
                if text_run_idx < len(trans_list):
                    if trans_list[text_run_idx] is not None:
                        el['content'] = trans_list[text_run_idx]
                        stats['translated'] += 1
                    else:
                        stats['kept'] += 1
                else:
                    stats['kept'] += 1
            else:
                stats['kept'] += 1
            text_run_idx += 1

with open('_art33_trans.json', 'w', encoding='utf-8') as f:
    json.dump(trans_data, f, ensure_ascii=False, indent=2)

print(f'Done: {stats["total_text"]} text elements, {stats["translated"]} translated, {stats["kept"]} kept')
print(f'Blocks: {len(trans_data["blocks"])}')
