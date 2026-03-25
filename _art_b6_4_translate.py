"""Translate _art_b6_4_orig.json from Chinese to Vietnamese"""
import json, sys, re, copy

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

with open('_art_b6_4_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Deep copy to preserve structure
trans = copy.deepcopy(data)

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

def is_pure_url(text):
    t = text.strip()
    return t.startswith('http://') or t.startswith('https://')

def is_pure_code_or_name(text):
    """Check if text is a technical name that should NOT be translated"""
    t = text.strip()
    # Pure English/code identifiers
    if re.match(r'^[a-zA-Z0-9_\-./]+$', t):
        return True
    return False

# Translation mapping: Chinese text -> Vietnamese text
# Block-by-block translation
translations = {}

# Build a mapping of block_index -> list of (element_index, original, translated)
block_translations = {}

for bi, block in enumerate(data['blocks']):
    element_trans = []
    for ei, el in enumerate(block['elements']):
        if el['type'] != 'text_run':
            element_trans.append((ei, None, None))  # skip non-text
            continue

        content = el['content']

        # Skip pure URLs
        if is_pure_url(content):
            element_trans.append((ei, content, content))
            continue

        # Skip pure code/technical names
        if is_pure_code_or_name(content):
            element_trans.append((ei, content, content))
            continue

        # Skip if no Chinese characters
        if not has_chinese(content):
            element_trans.append((ei, content, content))
            continue

        # Mark for translation
        element_trans.append((ei, content, None))

    block_translations[bi] = element_trans

# Now define all translations inline
# I'll process each block and translate

def t(bi, ei, vi_text):
    """Set translation for block bi, element ei"""
    for item in block_translations[bi]:
        if item[0] == ei:
            idx = block_translations[bi].index(item)
            block_translations[bi][idx] = (ei, item[1], vi_text)
            return

# Block 0: page title
t(0, 0, "Hướng dẫn đầy đủ 53 kỹ năng chính thức của OpenClaw: Giải thích chức năng + Đánh giá rủi ro + Đề xuất cài đặt")

# Block 1: quote with link
t(1, 0, "🔗 Link bài gốc: ")

# Block 2: author info
t(2, 0, "Nguyên tác Kiều Tỷ Kiều Tỷ Kiều Tỷ nói về giới AI")
t(2, 1, "Ngày 18 tháng 2 năm 2026 15:59 Giang Tây")

# Block 3
t(3, 0, "Các bạn cũng có thể triển khai thông qua Alibaba Cloud Bailian ")

# Block 4
t(4, 0, "Mua lần đầu chỉ từ 7.9 tệ, gia hạn giảm từ 50%, hỗ trợ Qwen3.5, Qwen3-max, Qwen3-coder, GLM-5, GLM-4.7, Kimi-k2.5 và các mô hình khác")

# Block 5
t(5, 0, "👉 Nhấn link trực tiếp: https://t.aliyun.com/U/0iiOuy")

# Block 6
t(6, 0, "👉 Xem hướng dẫn triển khai chi tiết: https://t.aliyun.com/U/MNkA9b")

# Block 7
t(7, 0, "Chỉ cần tối đa ba bước, bạn có thể sở hữu trợ lý AI trực tuyến 24/7, phản hồi mọi lúc")

# Block 8
t(8, 0, "Trong hơn 5700 kỹ năng trên ClawHub, chỉ có 53 kỹ năng là do chính thức tích hợp sẵn. Bài viết này phân tích từng kỹ năng về chức năng, nền tảng, mức độ rủi ro, giúp bạn đưa ra lựa chọn an toàn nhất.")

# Block 9: quote - security notice
t(9, 0, "Lưu ý: ")
t(9, 1, "Tháng 2 năm 2026, đội ngũ nghiên cứu bảo mật phát hiện 341 kỹ năng độc hại trên ClawHub (sự kiện ClawHavoc), chiếm khoảng 12% tổng số. 53 kỹ năng tích hợp chính thức được giới thiệu trong bài viết này là lựa chọn an toàn nhất. Hãy luôn kiểm tra mã nguồn trước khi cài đặt bất kỳ kỹ năng bên thứ ba nào.")

# Block 10: heading2
t(10, 0, "Trước tiên hãy hiểu rõ: Sự khác biệt giữa Tool và Skill")

# Block 11
t(11, 0, "Nhiều người nhầm lẫn hai khái niệm này, thực ra rất đơn giản:")

# Block 12
t(12, 0, "Tool (Công cụ) là \"cơ quan\" — quyết định OpenClaw có thể làm được việc gì đó hay không. Ví dụ read và write cho phép nó truy cập file, exec cho phép nó thực thi lệnh. Không có công cụ, giống như không có tay, không làm được gì cả.")

# Block 13
t(13, 0, "Skill (Kỹ năng) là \"sách giáo khoa\" — dạy OpenClaw cách kết hợp sử dụng các công cụ để hoàn thành nhiệm vụ. Cài đặt Skill không cấp quyền mới, nó chỉ là một bản hướng dẫn sử dụng.")

# Block 14: quote
t(14, 0, "Trọng điểm: ")
t(14, 1, "Các kỹ năng chính thức mặc định đều được tự động tải. Khuyến nghị mạnh mẽ sử dụng chế độ danh sách trắng skills.allowBundled, chỉ bật những kỹ năng bạn cần.")

# Block 15
t(15, 0, "Cấu hình tối thiểu được đề xuất (chỉ bật 9 kỹ năng cốt lõi):")

# Block 16: heading2
t(16, 0, "I. Loại ghi chú (4 kỹ năng)")

# Block 17
t(17, 0, "Quản lý ứng dụng ghi chú của bạn, hỗ trợ nhiều nền tảng ghi chú phổ biến. Chọn cái nào phụ thuộc vào cách triển khai — nếu OpenClaw chạy trên VM, chỉ có Notion trên đám mây là không bị giới hạn.")

# Block 18-21: table headers
t(18, 0, "Kỹ năng")
t(19, 0, "Nền tảng")
t(20, 0, "Rủi ro")
t(21, 0, "Mô tả")

# Block 22-25: obsidian row
# 22: obsidian - keep
# 23: Obsidian - keep
t(24, 0, "Thấp")
t(25, 0, "Quản lý kho ghi chú Obsidian cục bộ, bao gồm tạo, chỉnh sửa, tìm kiếm ghi chú. Thao tác file cục bộ, cần công cụ read/write. Nếu OpenClaw ở trên VM mà kho ghi chú ở Mac cục bộ thì không thể sử dụng trực tiếp.")

# Block 26-29: notion row
# 26: notion - keep
# 27: Notion - keep
t(28, 0, "Trung bình")
t(29, 0, "Tích hợp sâu Notion, quản lý ghi chú, cơ sở dữ liệu và trang. Dịch vụ đám mây, không giới hạn triển khai, là lựa chọn tốt nhất cho môi trường VM. Cần Notion API token.")

# Block 30-33: apple-notes row
# 30: apple-notes - keep
t(31, 0, "Apple Ghi chú")
t(32, 0, "Thấp")
t(33, 0, "Tích hợp Apple Ghi chú. Chỉ chạy cục bộ trên Mac, không sử dụng được trong VM.")

# Block 34-37: bear-notes row
# 34: bear-notes - keep
# 35: Bear - keep
t(36, 0, "Thấp")
t(37, 0, "Tích hợp ứng dụng ghi chú Bear. Tương tự chỉ chạy cục bộ trên Mac.")

# Block 38: heading2
t(38, 0, "II. Loại quản lý tác vụ (3 kỹ năng)")

# Block 39
t(39, 0, "Quản lý tác vụ và nhắc nhở. Nếu đã cài gog, Google Tasks đã bao gồm trong đó, không cần cài thêm.")

# Block 40-43: table headers
t(40, 0, "Kỹ năng")
t(41, 0, "Nền tảng")
t(42, 0, "Rủi ro")
t(43, 0, "Mô tả")

# Block 44-47: things-mac
# 44: things-mac - keep
# 45: Things 3 - keep
t(46, 0, "Thấp")
t(47, 0, "Tích hợp ứng dụng quản lý tác vụ Things 3. Chỉ chạy cục bộ trên Mac.")

# Block 48-51: apple-reminders
# 48: apple-reminders - keep
t(49, 0, "Apple Nhắc nhở")
t(50, 0, "Thấp")
t(51, 0, "Tích hợp Apple Nhắc nhở. Chỉ dùng cục bộ trên Mac.")

# Block 52-55: trello
# 52: trello - keep
# 53: Trello - keep
t(54, 0, "Trung bình")
t(55, 0, "Tích hợp bảng Trello, quản lý thẻ, danh sách và cộng tác nhóm. Cần Trello API key.")

# Block 56: heading2
t(56, 0, "III. Loại văn phòng/email (2 kỹ năng)")

# Block 57
t(57, 0, "Tích hợp bộ công cụ văn phòng bao gồm email, lịch, tài liệu. Đây là danh mục có tần suất sử dụng hàng ngày cao nhất.")

# Block 58-61: table headers
t(58, 0, "Kỹ năng")
t(59, 0, "Nền tảng")
t(60, 0, "Rủi ro")
t(61, 0, "Mô tả")

# Block 62-66: gog
# 62: gog - keep
# 63: Google Workspace - keep
t(64, 0, "Trung bình")
t(65, 0, "【Bắt buộc cài】")
t(66, 0, "Tích hợp toàn bộ Google Workspace thông qua gog CLI: Gmail, Calendar, Tasks, Drive, Docs, Sheets. Có thể thu hồi quyền truy cập bất cứ lúc nào trong cài đặt tài khoản Google. Sau khi cài đặt, hỗ trợ các lệnh ngôn ngữ tự nhiên như \"hôm nay có cuộc họp nào\" \"gửi email theo dõi cho Sarah\". Được nhiều người đánh giá liệt kê là \"nếu chỉ cài một cái thì cài cái này\".")

# Block 67-70: himalaya
# 67: himalaya - keep
t(68, 0, "Email IMAP/SMTP")
t(69, 0, "Cao")
t(70, 0, "Ứng dụng email đa năng, sử dụng giao thức IMAP/SMTP để nhận và gửi email. Phù hợp cho người dùng email không phải Google. Rủi ro cao vì cần lưu trữ mật khẩu email.")

# Block 71: heading2
t(71, 0, "IV. Loại tin nhắn/mạng xã hội (7 kỹ năng)")

# Block 72: quote
t(72, 0, "Lưu ý: ")
t(72, 1, "Các kỹ năng này cung cấp quyền truy cập đầy đủ vào dữ liệu nền tảng (tìm kiếm lịch sử tin nhắn, đồng bộ hội thoại, quản lý kênh), hoàn toàn khác với công cụ message (chỉ gửi tin nhắn). Tin nhắn AI gửi nhân danh bạn không thể thu hồi, khuyến nghị cài đặt thận trọng.")

# Block 73-76: table headers
t(73, 0, "Kỹ năng")
t(74, 0, "Nền tảng")
t(75, 0, "Rủi ro")
t(76, 0, "Mô tả")

# Block 77-80: wacli
# 77: wacli - keep
# 78: WhatsApp - keep
t(79, 0, "Rất cao")
t(80, 0, "Tích hợp sâu WhatsApp, có thể đọc lịch sử tin nhắn, gửi tin nhắn, v.v. Truy cập đầy đủ dữ liệu WhatsApp của bạn.")

# Block 81-84: imsg
# 81: imsg - keep
# 82: iMessage - keep
t(83, 0, "Rất cao")
t(84, 0, "Tích hợp iMessage, có thể đọc và gửi tin nhắn iMessage. Chỉ dùng trên Mac.")

# Block 85-88: bluebubbles
# 85: bluebubbles - keep
t(86, 0, "iMessage (bên ngoài)")
t(87, 0, "Cao")
t(88, 0, "Truy cập iMessage thông qua máy chủ BlueBubbles, không giới hạn ở Mac cục bộ.")

# Block 89-92: slack
# 89: slack - keep
# 90: Slack - keep
t(91, 0, "Trung bình")
t(92, 0, "Tích hợp workspace Slack, đăng cập nhật, trả lời thread, quản lý kênh. Hỗ trợ rich text và Block Kit.")

# Block 93-96: discord
# 93: discord - keep
# 94: Discord - keep
t(95, 0, "Trung bình")
t(96, 0, "Tích hợp máy chủ Discord, quản lý kênh, gửi tin nhắn, tự động hóa quản lý cộng đồng.")

# Block 97-100: bird (X/Twitter)
# 97: bird - keep
t(98, 0, "X (Twitter)")
t(99, 0, "Rất cao")
t(100, 0, "Tích hợp X/Twitter, có thể đăng bài, tìm kiếm, tương tác. Nội dung AI đăng không thể thu hồi, và được đăng nhân danh bạn.")

# Block 101: heading2
t(101, 0, "V. Loại công cụ phát triển (4 kỹ năng)")

# Block 102
t(102, 0, "Phát triển mã, quản lý phiên bản và quản lý terminal. Một trong những danh mục thực dụng nhất cho lập trình viên hàng ngày.")

# Block 103-106: table headers
t(103, 0, "Kỹ năng")
t(104, 0, "Nền tảng")
t(105, 0, "Rủi ro")
t(106, 0, "Mô tả")

# Block 107-111: github
# 107: github - keep
# 108: GitHub - keep
t(109, 0, "Trung bình")
t(110, 0, "【Lập trình viên bắt buộc cài】")
t(111, 0, "Thao tác GitHub thông qua gh CLI, quản lý Issue, PR, repository. Hỗ trợ OAuth, quyền có thể kiểm soát. Có thể kiểm tra lỗi CI/CD từ xa qua điện thoại — khi ra ngoài chỉ cần hỏi \"kiểm tra tại sao PR này build thất bại\", nó sẽ kéo log lỗi GitHub Actions và cho bạn biết nguyên nhân.")

# Block 112-115: coding-agent
# 112: coding-agent - keep
t(113, 0, "Trợ lý lập trình AI")
t(114, 0, "Trung bình")
t(115, 0, "Gọi các trợ lý lập trình AI khác (Codex, Claude Code, v.v.) để thực hiện nhiệm vụ ở nền. Có thể thực hiện quy trình \"AI điều phối AI\" — thông qua Telegram nói \"clone repo này, nghiên cứu nó, làm một trang web demo\", nó sẽ tự động hoàn thành.")

# Block 116-119: tmux
# 116: tmux - keep
t(117, 0, "Phiên terminal")
t(118, 0, "Thấp")
t(119, 0, "Quản lý nhiều phiên terminal, thực hiện nhiệm vụ song song.")

# Block 120-123: session-logs
# 120: session-logs - keep
t(121, 0, "Tìm kiếm nhật ký")
t(122, 0, "Thấp")
t(123, 0, "Tìm kiếm và phân tích nhật ký hội thoại trước đó, thuận tiện cho việc xem lại các thao tác lịch sử.")

# Block 124: heading2
t(124, 0, "VI. Loại âm nhạc (4 kỹ năng)")

# Block 125
t(125, 0, "Điều khiển phát nhạc và thiết bị âm thanh. Tất cả đều rủi ro thấp.")

# Block 126-129: table headers
t(126, 0, "Kỹ năng")
t(127, 0, "Nền tảng")
t(128, 0, "Rủi ro")
t(129, 0, "Mô tả")

# Block 130-133: spotify-player
# 130: spotify-player - keep
# 131: Spotify - keep
t(132, 0, "Thấp")
t(133, 0, "Điều khiển phát Spotify, tìm kiếm nhạc, phát/tạm dừng, quản lý danh sách phát.")

# Block 134-137: sonoscli
# 134: sonoscli - keep
t(135, 0, "Loa Sonos")
t(136, 0, "Thấp")
t(137, 0, "Điều khiển hệ thống loa thông minh Sonos.")

# Block 138-141: blucli
# 138: blucli - keep
t(139, 0, "Thiết bị BluOS")
t(140, 0, "Thấp")
t(141, 0, "Điều khiển thiết bị âm thanh BluOS.")

# Block 142-145: songsee
# 142: songsee - keep
t(143, 0, "Trực quan hóa âm thanh")
t(144, 0, "Thấp")
t(145, 0, "Công cụ trực quan hóa âm thanh, tạo biểu đồ dạng sóng âm thanh, v.v.")

# Block 146: heading2
t(146, 0, "VII. Loại nhà thông minh (2 kỹ năng)")

# Block 147-150: table headers
t(147, 0, "Kỹ năng")
t(148, 0, "Nền tảng")
t(149, 0, "Rủi ro")
t(150, 0, "Mô tả")

# Block 151-154: openhue
# 151: openhue - keep
# 152: Philips Hue - keep
t(153, 0, "Thấp")
t(154, 0, "Điều khiển hệ thống đèn thông minh Philips Hue, điều chỉnh độ sáng, màu sắc, cảnh.")

# Block 155-158: eightctl
# 155: eightctl - keep
# 156: Eight Sleep - keep
t(157, 0, "Thấp")
t(158, 0, "Điều khiển nhiệt độ nệm thông minh Eight Sleep.")

# Block 159: heading2
t(159, 0, "VIII. Loại đặt đồ ăn (2 kỹ năng)")

# Block 160-163: table headers
t(160, 0, "Kỹ năng")
t(161, 0, "Nền tảng")
t(162, 0, "Rủi ro")
t(163, 0, "Mô tả")

# Block 164-167: food-order
# 164: food-order - keep
t(165, 0, "Đặt đồ ăn đa nền tảng")
t(166, 0, "Cao")
t(167, 0, "Đặt đồ ăn đa nền tảng. Rủi ro cao vì liên quan đến thao tác thanh toán.")

# Block 168-171: ordercli
# 168: ordercli - keep
# 169: Foodora - keep
t(170, 0, "Trung bình")
t(171, 0, "Đặt đồ ăn thông qua nền tảng Foodora.")

# Block 172: heading2
t(172, 0, "IX. Loại sáng tạo/hình ảnh (5 kỹ năng)")

# Block 173
t(173, 0, "Tạo hình ảnh AI, xử lý video và tìm kiếm GIF. Tất cả đều rủi ro thấp.")

# Block 174-177: table headers
t(174, 0, "Kỹ năng")
t(175, 0, "Nền tảng")
t(176, 0, "Rủi ro")
t(177, 0, "Mô tả")

# Block 178-181: openai-image-gen
# 178: openai-image-gen - keep
# 179: OpenAI DALL-E - keep
t(180, 0, "Thấp")
t(181, 0, "Sử dụng API tạo hình ảnh của OpenAI để tạo ảnh. Cần OpenAI API key.")

# Block 182-185: nano-banana-pro
# 182: nano-banana-pro - keep
t(183, 0, "Hình ảnh Gemini")
t(184, 0, "Thấp")
t(185, 0, "Sử dụng Google Gemini để tạo hình ảnh.")

# Block 186-189: video-frames
# 186: video-frames - keep
t(187, 0, "Trích xuất khung hình video")
t(188, 0, "Thấp")
t(189, 0, "Trích xuất các khung hình chính từ video.")

# Block 190-193: gifgrep
# 190: gifgrep - keep
t(191, 0, "Tìm kiếm GIF")
t(192, 0, "Thấp")
t(193, 0, "Tìm kiếm và gửi ảnh động GIF.")

# Block 194-197: canvas
# 194: canvas - keep
t(195, 0, "Canvas Bảng vẽ")
t(196, 0, "Thấp")
t(197, 0, "Thao tác bảng vẽ trực quan, dùng cho biểu đồ và sơ đồ luồng.")

# Block 198: heading2
t(198, 0, "X. Loại giọng nói (5 kỹ năng)")

# Block 199
t(199, 0, "Chuyển văn bản thành giọng nói (TTS) và chuyển giọng nói thành văn bản (STT).")

# Block 200-203: table headers
t(200, 0, "Kỹ năng")
t(201, 0, "Nền tảng")
t(202, 0, "Rủi ro")
t(203, 0, "Mô tả")

# Block 204-207: sag
# 204: sag - keep
# 205: ElevenLabs TTS - keep
t(206, 0, "Thấp")
t(207, 0, "Sử dụng ElevenLabs để tạo giọng nói chất lượng cao. Cần API key.")

# Block 208-211: openai-whisper
# 208: openai-whisper - keep
t(209, 0, "Whisper STT cục bộ")
t(210, 0, "Thấp")
t(211, 0, "Chạy nhận dạng giọng nói OpenAI Whisper cục bộ.")

# Block 212-215: openai-whisper-api
# 212: openai-whisper-api - keep
t(213, 0, "Whisper STT đám mây")
t(214, 0, "Thấp")
t(215, 0, "Sử dụng OpenAI Whisper API để nhận dạng giọng nói trên đám mây.")

# Block 216-219: sherpa-onnx-tts
# 216: sherpa-onnx-tts - keep
t(217, 0, "TTS ngoại tuyến")
t(218, 0, "Thấp")
t(219, 0, "Chuyển văn bản thành giọng nói hoàn toàn ngoại tuyến, không cần mạng.")

# Block 220-223: voice-call
# 220: voice-call - keep
t(221, 0, "Cuộc gọi thoại")
t(222, 0, "Cao")
t(223, 0, "Cho phép OpenClaw thực hiện cuộc gọi thoại. Rủi ro cao vì liên quan đến giao tiếp thời gian thực.")

# Block 224: heading2
t(224, 0, "XI. Loại quản lý mật khẩu (1 kỹ năng)")

# Block 225-228: table headers
t(225, 0, "Kỹ năng")
t(226, 0, "Nền tảng")
t(227, 0, "Rủi ro")
t(228, 0, "Mô tả")

# Block 229-232: 1password
# 229: 1password - keep
# 230: 1Password - keep
t(231, 0, "Rất cao")
t(232, 0, "Truy cập kho mật khẩu 1Password — tìm mật khẩu, tự động đăng nhập, điền biểu mẫu. Mô hình quyền là tất cả hoặc không: một khi ủy quyền, có thể truy cập tất cả mục trong toàn bộ kho mật khẩu. Nếu thực sự cần, khuyến nghị tạo \"kho mật khẩu chuyên dụng cho AI\", chỉ đặt những mật khẩu bạn sẵn lòng cho AI xem.")

# Block 233: heading2
t(233, 0, "XII. Loại mô hình AI (3 kỹ năng)")

# Block 234-237: table headers
t(234, 0, "Kỹ năng")
t(235, 0, "Nền tảng")
t(236, 0, "Rủi ro")
t(237, 0, "Mô tả")

# Block 238-241: gemini
# 238: gemini - keep
# 239: Google Gemini - keep
t(240, 0, "Thấp")
t(241, 0, "Tích hợp Google Gemini, dùng cho các nhiệm vụ nghiên cứu cần kết quả tìm kiếm thời gian thực. Sử dụng như AI bổ sung — đặc biệt hữu ích khi bạn cần tin tức mới nhất, đánh giá sản phẩm, quy định mới nhất và các thông tin thời gian thực khác.")

# Block 242-245: oracle
# 242: oracle - keep
t(243, 0, "Oracle CLI")
t(244, 0, "Thấp")
t(245, 0, "Tích hợp công cụ dòng lệnh Oracle.")

# Block 246-249: mcporter
# 246: mcporter - keep
t(247, 0, "Tích hợp MCP")
t(248, 0, "Trung bình")
t(249, 0, "Tích hợp Model Context Protocol, kết nối với các dịch vụ MCP khác.")

# Block 250: heading2
t(250, 0, "XIII. Loại hệ thống/công cụ (6 kỹ năng)")

# Block 251
t(251, 0, "Quản lý hệ thống, kiểm tra sức khỏe và công cụ đa năng. Đây là \"cơ sở hạ tầng\" sử dụng hàng ngày.")

# Block 252-255: table headers
t(252, 0, "Kỹ năng")
t(253, 0, "Nền tảng")
t(254, 0, "Rủi ro")
t(255, 0, "Mô tả")

# Block 256-260: summarize
# 256: summarize - keep
t(257, 0, "Tóm tắt nội dung")
t(258, 0, "Thấp")
t(259, 0, "【Bắt buộc cài】")
t(260, 0, "Tóm tắt thông minh trang web, PDF, podcast, bài viết dài. Podcast 40 phút chỉ cần 20 giây để ra bản tóm tắt, PDF 15 trang tóm tắt điểm chính trong một đoạn. Có người dùng cho biết tiết kiệm hơn 5 giờ mỗi tuần.")

# Block 261-265: weather
# 261: weather - keep
t(262, 0, "Dự báo thời tiết")
t(263, 0, "Thấp")
t(264, 0, "【Bắt buộc cài】")
t(265, 0, "Miễn phí, không cần API key, cài là dùng ngay. Lấy dự báo thời tiết địa phương, kết hợp với bản tin hàng ngày rất hiệu quả.")

# Block 266-269: clawhub
# 266: clawhub - keep
t(267, 0, "Quản lý kỹ năng")
t(268, 0, "Thấp")
t(269, 0, "Quản lý cài đặt, cập nhật và xóa kỹ năng ClawHub.")

# Block 270-273: skill-creator
# 270: skill-creator - keep
t(271, 0, "Tạo kỹ năng")
t(272, 0, "Thấp")
t(273, 0, "Tạo kỹ năng tùy chỉnh, cho phép OpenClaw học khả năng mới.")

# Block 274-277: healthcheck
# 274: healthcheck - keep
t(275, 0, "Kiểm tra sức khỏe")
t(276, 0, "Thấp")
t(277, 0, "Kiểm tra trạng thái hoạt động và cấu hình của OpenClaw.")

# Block 278-281: peekaboo
# 278: peekaboo - keep
t(279, 0, "Điều khiển UI macOS")
t(280, 0, "Cao")
t(281, 0, "Chụp và tự động hóa giao diện người dùng macOS. Chỉ dùng trên Mac.")

# Block 282: heading2
t(282, 0, "XIV. Loại địa điểm/điều hướng (2 kỹ năng)")

# Block 283-286: table headers
t(283, 0, "Kỹ năng")
t(284, 0, "Nền tảng")
t(285, 0, "Rủi ro")
t(286, 0, "Mô tả")

# Block 287-290: goplaces
# 287: goplaces - keep
# 288: Google Places - keep
t(289, 0, "Thấp")
t(290, 0, "Tìm kiếm nhà hàng, cửa hàng, điểm tham quan gần đây, v.v.")

# Block 291-294: local-places
# 291: local-places - keep
t(292, 0, "Đại lý cục bộ")
t(293, 0, "Thấp")
t(294, 0, "Dịch vụ đại lý địa điểm cục bộ.")

# Block 295: heading2
t(295, 0, "XV. Loại phương tiện/giám sát (3 kỹ năng)")

# Block 296-299: table headers
t(296, 0, "Kỹ năng")
t(297, 0, "Nền tảng")
t(298, 0, "Rủi ro")
t(299, 0, "Mô tả")

# Block 300-303: camsnap
# 300: camsnap - keep
t(301, 0, "Camera RTSP")
t(302, 0, "Trung bình")
t(303, 0, "Truy cập camera giám sát giao thức RTSP, chụp ảnh và giám sát.")

# Block 304-307: blogwatcher
# 304: blogwatcher - keep
t(305, 0, "Giám sát RSS")
t(306, 0, "Thấp")
t(307, 0, "Giám sát nguồn RSS, theo dõi cập nhật blog và tin tức.")

# Block 308-311: model-usage
# 308: model-usage - keep
t(309, 0, "Theo dõi sử dụng")
t(310, 0, "Thấp")
t(311, 0, "Theo dõi lượng sử dụng và chi phí mô hình AI.")

# Block 312: heading2
t(312, 0, "XVI. Loại tài liệu (1 kỹ năng)")

# Block 313-316: table headers
t(313, 0, "Kỹ năng")
t(314, 0, "Nền tảng")
t(315, 0, "Rủi ro")
t(316, 0, "Mô tả")

# Block 317-320: nano-pdf
# 317: nano-pdf - keep
t(318, 0, "Chỉnh sửa PDF")
t(319, 0, "Thấp")
t(320, 0, "Chỉnh sửa và xử lý file PDF.")

# Block 321: heading2
t(321, 0, "Tổng hợp mức độ rủi ro")

# Block 322-324: table headers
t(322, 0, "Rủi ro")
t(323, 0, "Số lượng")
t(324, 0, "Mô tả")

# Block 325-327: low risk
t(325, 0, "Rủi ro thấp")
t(326, 0, "30 cái")
t(327, 0, "An toàn khi sử dụng, ảnh hưởng tối thiểu đến hệ thống và dữ liệu")

# Block 328-330: medium risk
t(328, 0, "Rủi ro trung bình")
t(329, 0, "12 cái")
t(330, 0, "Liên quan đến API dịch vụ bên ngoài, cần cung cấp thông tin xác thực")

# Block 331-333: high risk
t(331, 0, "Rủi ro cao")
t(332, 0, "6 cái")
t(333, 0, "Liên quan đến dữ liệu nhạy cảm, thanh toán hoặc giao tiếp thời gian thực")

# Block 334-336: extreme risk
t(334, 0, "Rủi ro rất cao")
t(335, 0, "5 cái")
t(336, 0, "Truy cập đầy đủ vào dữ liệu cá nhân hoặc kho mật khẩu của bạn, AI có thể đăng nội dung không thể thu hồi nhân danh bạn")

# Block 337: heading2
t(337, 0, "Đề xuất cài đặt: Bật theo từng giai đoạn")

# Block 338: heading3
t(338, 0, "Tuần đầu tiên: Top 3 bắt buộc cài")

# Block 339: quote
t(339, 0, "Thành công: ")
t(339, 1, "Cài ba cái này trước, dùng một tuần, rồi thêm theo nhu cầu.")

# Block 340: quote
t(340, 0, "gog — Bộ Google đầy đủ (email + lịch + tài liệu)")

# Block 341: quote
t(341, 0, "summarize — Tóm tắt nội dung (tiết kiệm 5+ giờ mỗi tuần)")

# Block 342: quote
t(342, 0, "weather — Dự báo thời tiết (miễn phí, cài là dùng ngay)")

# Block 343: heading3
t(343, 0, "Tuần thứ hai: Thêm theo vai trò")

# Block 344
t(344, 0, "Lập trình viên: github + tmux + session-logs + coding-agent")

# Block 345
t(345, 0, "Người dùng ghi chú: notion (đám mây) hoặc obsidian (cục bộ)")

# Block 346
t(346, 0, "Người dùng tự động hóa: Kết hợp với công cụ cron + message để tạo bản tin hàng ngày")

# Block 347: heading3
t(347, 0, "Kỹ năng cần cân nhắc kỹ trước khi cài")

# Block 348: quote
t(348, 0, "Lưu ý: ")
t(348, 1, "Hãy suy nghĩ kỹ trước khi cài các kỹ năng sau:")

# Block 349: quote
t(349, 0, "Loại mạng xã hội (wacli, imsg, bird) — Nội dung AI đăng không thể thu hồi")

# Block 350: quote
t(350, 0, "1password — Truy cập toàn bộ kho, không thể giới hạn từng mục")

# Block 351: quote
t(351, 0, "Loại đặt đồ ăn (food-order) — Liên quan đến thao tác thanh toán")

# Block 352: heading2
t(352, 0, "Ba nguyên tắc an toàn")

# Block 353
t(353, 0, "Nguyên tắc một: Không nghĩ ra mục đích sử dụng thì không bật. 53 kỹ năng mặc định đều được tải, dùng danh sách trắng chỉ giữ lại những gì cần thiết.")

# Block 354
t(354, 0, "Nguyên tắc hai: Năng lực càng lớn, quản lý càng nghiêm. Bật phê duyệt cho exec, message chỉ gửi cho chính mình.")

# Block 355
t(355, 0, "Nguyên tắc ba: Bước cuối cùng luôn làm thủ công. Thanh toán, gửi tin nhắn ra ngoài, đăng công khai — bất kỳ thao tác không thể hoàn tác nào đều do chính bạn thực hiện.")

# Block 356
t(356, 0, "Về loạt bài liên quan đến OpenClaw, có thể tham khảo như sau:")

# Block 357
t(357, 0, "Hướng dẫn cấu hình đa tác nhân OpenClaw: Để nhóm AI giúp bạn làm nhiều việc cùng lúc")

# Block 358
t(358, 0, "Hướng dẫn đầy đủ OpenClaw: Xây dựng đội ngũ nhân viên AI từ số không")

# Block 359
t(359, 0, "ClawHub: \"Cửa hàng ứng dụng\" cài kỹ năng cho nhân viên AI của bạn")

# Block 360
t(360, 0, "Cách đăng ký Brave Search API key và cấu hình OpenClaw")

# Block 361
t(361, 0, "Hướng dẫn thực chiến OpenClaw: 12 trường hợp ứng dụng phổ biến với hướng dẫn chi tiết")

# Block 362
t(362, 0, "Sổ tay lệnh đầy đủ OpenClaw")

# Block 363
t(363, 0, "Đã dùng OpenClaw, có thể giao tiếp hai chiều với Telegram rồi")

# Block 364
t(364, 0, "【Bài viết này do OpenClaw xuất】Hướng dẫn cài đặt OpenClaw cực đơn giản và miễn phí")

# Block 365
t(365, 0, "Hôm nay chia sẻ đến đây, theo dõi Kiều Tỷ, liên tục chia sẻ kiến thức và tin tức AI.")


# Now apply translations to the trans data
translated_count = 0
kept_count = 0
total_text_runs = 0

for bi, block in enumerate(trans['blocks']):
    if bi not in block_translations:
        continue
    for item in block_translations[bi]:
        ei, orig, vi = item
        if vi is None:
            continue  # non-text element

        el = block['elements'][ei]
        if el['type'] != 'text_run':
            continue

        total_text_runs += 1
        if vi != orig:
            el['content'] = vi
            translated_count += 1
        else:
            kept_count += 1

# Add spaces between adjacent Vietnamese text_runs
for block in trans['blocks']:
    elements = block['elements']
    for i in range(len(elements) - 1):
        el = elements[i]
        next_el = elements[i + 1]
        if el['type'] == 'text_run' and next_el['type'] == 'text_run':
            # Check if current ends without space and next starts without space
            curr = el['content']
            nxt = next_el['content']
            if curr and nxt:
                # If current doesn't end with space/newline and next doesn't start with space
                if not curr[-1].isspace() and not nxt[0].isspace():
                    # Check both are Vietnamese text (not pure URLs or code)
                    if not is_pure_url(curr) and not is_pure_url(nxt):
                        # Only add space if they contain Vietnamese/text characters
                        if has_chinese(curr) or re.search(r'[a-zA-ZÀ-ỹ]', curr):
                            if has_chinese(nxt) or re.search(r'[a-zA-ZÀ-ỹ]', nxt):
                                el['content'] = curr + ' '

# Save
with open('_art_b6_4_trans.json', 'w', encoding='utf-8') as f:
    json.dump(trans, f, ensure_ascii=False, indent=2)

print(f"Total text_runs: {total_text_runs}")
print(f"Translated: {translated_count}")
print(f"Kept original: {kept_count}")
print(f"Saved to _art_b6_4_trans.json")
