# -*- coding: utf-8 -*-
"""Final translator for art31 - reads CN texts from JSON, applies translations"""
import json, sys, re, copy
sys.stdout.reconfigure(encoding='utf-8')

with open('_art31_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('_art31_cn_texts.json', 'r', encoding='utf-8') as f:
    cn_texts = json.load(f)

# Build unique set
unique_cn = list(dict.fromkeys(cn_texts))

# Vietnamese translations indexed by position in unique_cn list
# We'll build the map by reading the CN keys and providing translations
# using a comprehensive ordered list

# Read existing translations from _art30_trans.json pattern if available
# Build map: key = CN text, value = VI text

vi_translations = [None] * len(unique_cn)

# I'll provide translations as indexed entries
# Format: index -> Vietnamese text
# This avoids embedding Chinese in source code

indexed_vi = {
    0: "Sau khi cài xong Tôm Hùm: Hướng dẫn cấu hình hoàn chỉnh mà học sinh tiểu học cũng hiểu được",
    1: "🔗 Link bài gốc: ",
    2: "Nguyên tác: Tiểu Hỗ đáng thương - Tiểu Hỗ AI",
    3: "Ngày 9 tháng 3 năm 2026, 08:53 - An Huy",
    4: "Sau khi cài xong Tôm Hùm: Hướng dẫn cấu hình hoàn chỉnh",
    5: "Bài trước đã hướng dẫn bạn cài đặt Tôm Hùm từng bước, nhưng nhiều người vẫn không biết cấu hình, Tôm Hùm coi như bị tàn phế",
    6: "Bài này sẽ dạy bạn cách biến nó thành trợ lý cá nhân thực sự hữu dụng.",
    7: "Cũng không cần biết lập trình, chỉ cần copy paste là được, học sinh tiểu học cũng đọc hiểu...",
    8: "Xem lại bài trước↓",
    9: "Cài đặt OpenClaw Tôm Hùm từ con số 0: Hướng dẫn chi tiết mà học sinh tiểu học cũng hiểu",
    10: "Kết nối Tôm Hùm với bảng tính AI DingTalk, có thể tiếp quản công việc của bạn...",
    11: "Trước khi bắt đầu: Một nguyên tắc quan trọng nhất",
    12: "Trước khi bắt tay vào làm, hãy nhớ một điều:",
    13: "Tất cả cấu hình được hướng dẫn bên dưới, bạn đều có thể hoàn thành bằng cách chat với Tôm Hùm.",
    14: "Đúng vậy, bạn không cần tự đi tìm từng file, sửa từng cấu hình, bạn cũng tìm không ra đâu. Bạn có thể trực tiếp nói với Tôm Hùm trong khung chat:",
    15: "\"Giúp tôi tạo một file SOUL.md, thiết lập tính cách là trợ lý hiệu quả\"",
    16: "\"Giúp tôi cài đặt kỹ năng Tavily Search\"",
    17: "\"Giúp tôi đổi tần suất heartbeat thành 10 phút một lần\"",
    18: "\"Giúp tôi xem kết nối Feishu có vấn đề gì không\"",
    19: "Nó sẽ tự tạo file, sửa cấu hình, cài đặt kỹ năng.",
    20: "Vì vậy trong hướng dẫn này tuy sẽ dạy bạn cách thao tác thủ công (giúp bạn hiểu nguyên lý), nhưng khi thực tế thao tác, ",
    21: "việc gì Tôm Hùm làm được thì kiên quyết không tự làm, việc gì bạn không biết thì để nó làm, hỏi nó, để nó dạy bạn.",
    22: "Mối quan hệ giữa bạn và Tôm Hùm nên là quan hệ sếp và trợ lý, thậm chí là quan hệ chủ và tớ😁: bạn chỉ cần nói \"tôi muốn hiệu quả gì\", nó sẽ lo cách thực hiện.",
    23: "Ví dụ: ",
    24: "Bạn muốn Tôm Hùm mỗi sáng giúp bạn xem email. Bạn không cần học cách viết file HEARTBEAT.md, trực tiếp nói với nó \"tôi muốn bạn mỗi sáng lúc 9 giờ tự động giúp tôi kiểm tra email, có gì quan trọng thì thông báo cho tôi\". Nó sẽ tự tạo file, viết cấu hình, đặt tần suất. Bạn chỉ cần xác nhận \"đúng, đúng như vậy\" là xong.",
    25: "Được rồi, nhớ nguyên tắc này, chúng ta bắt đầu.",
    26: "Tại sao cài xong rồi còn phải \"cấu hình\"?",
    27: "Bạn có cảm giác này không: Tôm Hùm cài xong rồi, chat vài câu, cảm thấy cũng chẳng khác gì ChatGPT?",
    28: "Đó là vì bạn mới chỉ hoàn thành \"cài đặt\", chưa hoàn thành \"cấu hình\".",
    29: "Ví dụ: bạn mua một con robot hút bụi, mở hộp bấm nút, nó đúng là quét được sàn. Nhưng bạn chưa nói cho nó phòng nào cần quét, góc nào đừng đụng, mỗi ngày mấy giờ bắt đầu quét. Nên nó chỉ quay vòng tại chỗ, chẳng khác gì cái chổi 100 nghìn.",
    30: "Tôm Hùm cũng vậy. Cài xong nó đúng là chat được, nhưng nó không biết bạn là ai, bạn thích kiểu trả lời nào, bạn cần nó giúp gì. Cấu hình chính là nói cho nó những điều này.",
    31: "Những việc cần cấu hình, tổng cộng chỉ có mấy việc này:",
    32: "Việc bạn cần làm",
    33: "Ví von",
    34: "Hiệu quả",
    35: "Thiết lập nhân vật cho nó",
    36: "Nói với trợ lý mới \"tính cách của bạn nên như thế nào\"",
    37: "Nó biết mình là ai, biết bạn là ai, cách nói phù hợp với sở thích của bạn",
    38: "Cài kỹ năng cho nó",
    39: "Cài App cho điện thoại",
    40: "Nó có thể giúp bạn tìm thông tin, quản lý email, thu thập web, không chỉ là chat",
    41: "Kết nối công cụ chat của bạn",
    42: "Cài WeChat, Feishu cho điện thoại",
    43: "Bạn có thể trực tiếp @nó làm việc trong Feishu, Telegram",
    44: "Đặt tác vụ định kỳ",
    45: "Xếp lịch trực cho trợ lý",
    46: "Mỗi ngày nó tự động giúp bạn kiểm tra email, nhắc lịch, không cần bạn nói",
    47: "Dạy nó nhớ bạn",
    48: "Cho trợ lý ghi chép",
    49: "Lần chat sau không cần giới thiệu lại từ đầu",
    50: "Tiếp theo, chúng ta đi từng phần một.",
    51: "Bước một: Cho nó một linh hồn (cấu hình nhân vật)",
    52: "Đây là bước đơn giản nhất nhưng hiệu quả rõ rệt nhất. Dành 10 phút cấu hình xong, Tôm Hùm của bạn lập tức chuyển từ \"AI chung ai cũng dùng được\" thành \"trợ lý riêng chỉ phục vụ bạn\".",
    53: "File nhân vật là gì?",
    54: "Trong thư mục làm việc của Tôm Hùm (mặc định là ",
    55: " ), có vài file ",
    56: ". Mỗi lần khởi động, việc đầu tiên nó làm là đọc các file này, để hiểu rõ \"tôi là ai\" \"tôi đang giúp ai\" \"tôi nên làm gì\".",
    57: "Bạn có thể hiểu nó như một bộ \"tài liệu đào tạo nhân viên mới\". Nhân viên mới ngày đầu đi làm, bạn đưa cho họ một tài liệu, nói \"bạn tên gì, sếp bạn là ai, phong cách làm việc nên ngắn gọn trực tiếp, những việc này bạn có thể tự quyết, việc nào phải hỏi trước\". Tôm Hùm đọc các file này xong sẽ làm theo những gì bạn viết.",
    58: "Bộ sưu tập đầy đủ các file nhân vật",
    59: "Hệ thống nhân vật của Tôm Hùm có nhiều file, nhưng bạn không cần cấu hình hết một lần. Trước tiên hãy hiểu mỗi file dùng để làm gì:",
    60: "File",
    61: "Giải thích một câu",
    62: "Ví von",
    63: "Bắt buộc cấu hình?",
    64: "Tính cách và quy tắc hành vi của nó",
    65: "\"Tam quan\" của người này",
    66: "Khuyến khích mạnh",
    67: "Thông tin cá nhân và sở thích của bạn",
    68: "Hồ sơ cá nhân của sếp",
    # 69 = duplicate of 66
    69: "Khuyến khích mạnh",
    70: "Tên và hình ảnh bên ngoài của nó",
    71: "Danh thiếp",
    72: "Khuyến khích",
    73: "Quy trình làm việc và quy tắc an toàn",
    74: "Sổ tay nhân viên",
    75: "Tùy chọn (có giá trị mặc định)",
    76: "Tác vụ tự động thực hiện định kỳ",
    77: "Bảng trực",
    78: "Sẽ nói riêng ở phần sau",
    79: "Bộ nhớ dài hạn",
    80: "Sổ ghi chép công việc",
    81: "Tự động tạo, sẽ nói riêng ở phần sau",
    82: "Cấu hình tối thiểu: chỉ cần SOUL.md + USER.md. ",
    83: "Dành 10 phút, hiệu quả thấy ngay.",
    84: "SOUL.md: Tam quan của nó",
    85: "Đây là file cốt lõi nhất, quyết định tính cách, cách nói chuyện và quy tắc hành vi của trợ lý AI.",
    86: "Tạo như thế nào?",
    87: "Cách 1: Để Tôm Hùm tự tạo (khuyến khích)",
    88: "Nói trực tiếp trong khung chat:",
    89: "Nó sẽ tự động tạo file cho bạn, nội dung cũng viết sẵn. Bạn xem qua, ưng thì thôi, không ưng thì nói \"sửa xxx đi\".",
    90: "Cách 2: Tự tạo thủ công (phù hợp người dùng nâng cao)",
    91: "Nhập trong terminal:",
    92: "nano là gì? ",
    93: "Nó là một trình soạn thảo văn bản trong terminal, mở ra bạn có thể gõ trực tiếp. Nếu bạn không quen dùng trình soạn thảo terminal, cũng có thể dùng \"TextEdit\" (Mac) hoặc \"Notepad\" (Windows) mở ",
    94: " để chỉnh sửa.",
    95: "Sau đó copy paste nội dung bên dưới vào. ",
    96: "Tôi đã chuẩn bị ba bộ template, chọn cái phù hợp nhất với bạn:",
    97: "Template A: Trợ lý hiệu quả (phù hợp với công việc)",
    98: "Phù hợp với người dùng Tôm Hùm để quản lý công việc, tạo nội dung, xử lý việc hàng ngày.",
    99: "Template B: Bạn học tập (phù hợp với người đang học)",
}

# I notice this will take too many entries to fit here.
# Let me use the approach of writing the FIRST ~100 indexed entries,
# then extending in subsequent runs.
# But actually, there's a much smarter approach:
# For any entry NOT in indexed_vi, check if we already covered it
# in a previous article's translation approach, or skip it.

# Actually - let me just save what I have and check coverage
trans_map = {}
for i, cn in enumerate(unique_cn):
    if i in indexed_vi:
        trans_map[cn] = indexed_vi[i]

# Save partial map
with open('_art31_map.json', 'w', encoding='utf-8') as f:
    json.dump(trans_map, f, ensure_ascii=False, indent=2)

print(f"Map entries: {len(trans_map)} / {len(unique_cn)}")
print(f"Remaining: {len(unique_cn) - len(trans_map)}")
