# -*- coding: utf-8 -*-
"""Translate art18: all Chinese text_run elements to Vietnamese"""
import json, re, sys, copy

sys.stdout.reconfigure(encoding='utf-8')

with open('_art18_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

cn_pattern = re.compile(r'[\u4e00-\u9fff]')

# Translation map: block_index:element_index -> translated text
# We translate the ENTIRE content string (which may mix CN + VI + emoji)
translations = {}

def t(bi, ei, text):
    translations[(bi, ei)] = text

# Block 219, elem 1
t(219, 1, "02-22 | Khóa học chuỗi OpenClaw: Nhật ký nuôi tôm hùm tiêu hao 1 tỷ token mỗi ngày\n\n👨‍💻 Khách mời đặc biệt:\n")

# Block 222, elem 0
t(222, 0, "02-22 | Khóa học chuỗi OpenClaw: Nhật ký nuôi tôm hùm tiêu hao 1 tỷ token mỗi ngày\n\n👨‍💻 Khách mời đặc biệt:\nTrần Tài Miêu (Quản lý sản phẩm AI, Kỹ sư AI Agent, Đồng sáng lập cốt lõi WaytoAGI)\n\n💡Điểm nổi bật livestream:\nOpenClaw nhập môn từ zero, người mới cũng có thể dễ dàng bắt đầu\nPhân tích toàn bộ chuỗi huấn luyện, tiết lộ kinh nghiệm tránh bẫy và mẹo thực chiến\n")

# Block 223, elem 0
t(223, 0, "Biên bản họp liên quan")

# Block 224, elem 0
t(224, 0, "Biên bản thông minh: 03-23 | AI đồng hành đi làm: Bạn suy nghĩ, DuMate làm việc\n\nBạn vẫn tự mình sắp xếp tài liệu, tra cứu thông tin, làm bảng tính?\nTôm hùm cấp doanh nghiệp đầy đủ tính năng đầu tiên của Trung Quốc — Baidu DuMate đã ra mắt toàn diện!\nMột người + một DuMate = một nhóm nhỏ.\n\n🎬 Điểm nổi bật livestream:\n✅ Dọn dẹp ổ đĩa + Thu thập tài liệu + Trợ lý học tập, thực nghiệm ba kịch bản văn phòng\n")

t(224, 1, "✅ Từ quản lý tệp đến tổng hợp thông tin, toàn bộ quy trình AI thay bạn làm ngày 23 tháng 3 năm 2026")

# Block 225
t(225, 0, "Biên bản thông minh: 03-18 | Tối nay 21:00 livestream |「Agent Talk chuỗi số 1」: Tiết lộ các nhà khởi nghiệp YC đang dùng Agent làm gì\n\n🎤 Khách mời đặc biệt\n- Cathy: Nhà sáng lập Dedalus Labs\n- AJ: Người khởi xướng WaytoAGI\n\n💡 Điểm nổi bật cốt lõi:\n✅ Phân tích hướng Agent hot nhất Silicon Valley\n✅ Lộ trình hoàn chỉnh từ Demo đến kiếm tiền\n")
t(225, 1, "✅ Tính an toàn tương thích của Agent có thể mở rộng quy mô ngày 18 tháng 3 năm 2026")

# Block 226
t(226, 0, "Biên bản thông minh: 03-18 | Chia sẻ kinh nghiệm nuôi tôm: Tôi ngủ, tôm cắt phim\n—— Quảng cáo, sản phẩm, phim thương hiệu đều xong hết\n\nTối nay nhà phát triển Baidu Qianfan dẫn bạn mở khóa tư thế mới:\nDùng OpenClaw thực hiện chỉnh sửa video AI tự động hoàn toàn\nBạn cứ yên tâm ngủ, tôm nhỏ giúp bạn cắt phim!\n\n🎬 Điểm nổi bật livestream:\n✅ Quy trình cắt phim tự động hoàn toàn bằng AI, từ kịch bản đến thành phẩm một bước đến nơi\n✅ Video hot một chạm sao chép, một con tôm chính là một đội cắt phim\n")
t(226, 1, "✅ Giải phóng đôi tay, nâng cao hiệu suất sản xuất nội dung đáng kể ngày 18 tháng 3 năm 2026")

# Block 227
t(227, 0, "Biên bản thông minh: 03-17 | Từ khái niệm đến thực hành, hướng dẫn từng bước làm chủ GEO!\n\n🎤 Khách mời đặc biệt\n- Hướng Dương Kiều Mộc: Cựu Quản lý sản phẩm AI thương mại hóa TikTok, Nhà sáng tạo nội dung AI\n- Diêu Kim Cương: Cựu phụ trách marketing Học Nhi Tư Online của Hảo Vị Lai, CEO Liệp Hà Khoa Kỹ\n\n💡 Điểm nổi bật cốt lõi:\n🎙️ Tìm kiếm AI đang đánh cắp lưu lượng của bạn? Cùng bàn cách để AI chủ động trích dẫn bạn!\n")
t(227, 1, "🧑‍💻 Khi người dùng không còn nhấp vào liên kết mà trực tiếp xem câu trả lời AI đưa ra, nội dung của bạn còn được nhìn thấy không? WaytoAGI học chung lúc 8 giờ tối ngày 17 tháng 3 năm 2026")

# Block 228
t(228, 0, "Biên bản thông minh: 03-15 | Tiết lộ ALL-IN-ONE Agent workspace\n\n🎤 Khách mời đặc biệt\nThiếu Khanh\n- floatboat.ai Founder\n- Builder đặt món ra nước ngoài trọn gói\n- Đồng sáng tạo cộng đồng WaytoAGI\n\n💡 Điểm nổi bật cốt lõi:\n✅ Mở khóa AI workspace đầu tiên xây dựng cho công ty một người\n✅ Một chạm kết nối 3500+ công cụ, quản lý tệp local và cloud tất cả trong một\n✅ Tham gia livestream nhận mã đổi điểm cộng đồng độc quyền\n")

# Block 229
t(229, 0, "Biên bản thông minh: 03-13 | Miaoda ra mắt toàn cầu Skill tạo ứng dụng, 🦞 giúp bạn làm ứng dụng WaytoAGI học chung lúc 8 giờ tối ngày 13 tháng 3 năm 2026")

# Block 231
t(231, 0, "Biên bản thông minh: 03-07 | Tăng trưởng marketing và tối ưu SEO toàn diện\n\n🎤 Khách mời đặc biệt\nKostja\n- Nhà sáng lập Đối Chuẩn Khoa Kỹ\n- Chuyên gia tăng trưởng AI/SaaS, ba năm kinh nghiệm thực chiến, phục vụ hơn 100 sản phẩm\n- Giỏi SEO, content marketing, xây dựng backlink và chiến lược tăng trưởng\n\n💡 Điểm nổi bật cốt lõi:\n🎯 Nắm vững 144 Skill, thực hiện thu hút khách chính xác và tăng trưởng ổn định\n")
t(231, 1, "🛠️ Phân tích lại case thực chiến, mở khóa phương pháp tăng trưởng có thể tái sử dụng ngày 7 tháng 3 năm 2026")

# Block 232
t(232, 0, "Biên bản thông minh: 03-05 | Cao thủ OpenClaw chia sẻ! Từ Coze nuôi tôm đến xu hướng lớn Vibe Coding WaytoAGI học chung lúc 8 giờ tối ngày 5 tháng 3 năm 2026")

# Block 233
t(233, 0, "Biên bản thông minh: 03-04 | Xuyên 5 thành phố, 30+ đối tác cộng đồng WaytoAGI đồng sáng tạo phim chúc Tết AI 2026 《Hành trình AI dở khóc dở cười của Lão Mã》chia sẻ hậu trường ngày 4 tháng 3 năm 2026")

# Block 234
t(234, 0, "Biên bản thông minh: 03-04 | OpenClaw đã đến lúc đi làm! Thực chiến nâng cao nuôi tôm Qianfan WaytoAGI học chung lúc 8 giờ tối ngày 4 tháng 3 năm 2026")

# Block 235
t(235, 0, "Biên bản thông minh: 03-03 | Dùng 10 phút với Obsidian+OpenClaw triệt để tái cấu trúc hệ thống quản lý tri thức AI của bạn\n\n🎤 Khách mời đặc biệt\nCarl's AI Watts: Top 10 truyền thông cá nhân AI trên tài khoản công cộng, Top 30 truyền thông cá nhân AI trên video, cựu Kỹ sư thuật toán mô hình lớn của ByteDance\n\n💡 Điểm nổi bật cốt lõi:\n✅ Thực hành toàn bộ | Dẫn bạn dùng「Obsidian+OpenClaw」xây dựng hệ thống quản lý tri thức hiệu quả cao\n✅ Hướng dẫn tránh bẫy | Phân tích các điểm đau và mẹo sử dụng từng công cụ, giúp bạn ít đi đường vòng và nhanh chóng bắt đầu\n")

# Block 236
t(236, 0, "Biên bản thông minh: 03-01 | Làm sao vượt qua bế tắc phim ngắn AI nhiều mà ít tinh phẩm? 🎤 Khách mời đặc biệt\nNam Tường: Phát triển kỹ thuật AIMWISE, Giảng viên đặc biệt AIGC Học viện Mỹ thuật Trung Quốc, Tiên phong sáng tạo thiết kế số trí tuệ cấp quốc gia đợt đầu\nTONIX: Đồng sáng lập AIMWISE, blogger triệu fan, sở hữu hơn 10 năm kinh nghiệm kỹ xảo phim ảnh\n\n💡 Điểm nổi bật cốt lõi:\n✅ Phân tích quy trình sáng tạo hiệu quả cao phim ngắn AI từ kịch bản đến thành phẩm\n")
t(236, 1, "✅ Tiết lộ mẹo thực chiến và hướng dẫn tránh bẫy sáng tạo phim ngắn chất lượng cao WaytoAGI học chung lúc 8 giờ tối ngày 1 tháng 3 năm 2026")

# Block 237
t(237, 0, "Biên bản thông minh: 02-28 | Thế giới Silicon tương lai kỳ 12: Câu chuyện đằng sau CC Switch - đối tác tốt nhất của Claude Code\n")

# Block 238
t(238, 0, "Biên bản thông minh: 02-27 | Hải Tân: Tôi đã tạo cho tôm hùm một không gian làm việc trực quan hóa WaytoAGI học chung lúc 8 giờ tối ngày 27 tháng 2 năm 2026")

# Block 239
t(239, 0, "Biên bản thông minh: 02-26 | Selfware - Từ tài liệu đến sinh mệnh thể, mở ra kỷ nguyên mới tệp chính là phần mềm\n\n👨‍💻 Khách mời đặc biệt:\nThiếu Khanh — floatboat.ai Founder, Đồng sáng tạo cộng đồng WaytoAGI, Builder đặt món ra nước ngoài trọn gói\nRemy — floatboat.ai kiến trúc sư agent\n\n💡 Điểm nổi bật livestream:\n✅ Phân tích Self Instance: Mở khóa hình thái cuối cùng \"tệp chính là phần mềm\"\n✅ Kiến trúc sư đối mặt: Từ logic nền tảng đến xây dựng thực chiến, xuyên suốt toàn bộ quy trình Selfware\n")

# Block 240
t(240, 0, "Biên bản thông minh: 02-25 | Tối nay là phòng tự học WaytoAGI học chung lúc 8 giờ tối ngày 25 tháng 2 năm 2026")

# Block 241
t(241, 0, "Biên bản thông minh: 02-24 | 🦞 Lai Tân Lộ dẫn mọi người phân tích kiến trúc kỹ thuật OpenClaw, còn có thể tự tay làm một con tôm hùm nhỏ nhất WaytoAGI học chung lúc 8 giờ tối ngày 24 tháng 2 năm 2026")

# Block 242
t(242, 0, "Biên bản thông minh: 02-21 | Đối thoại với Nhà sáng lập EvoMap: Bí mật viral lên đỉnh hạng nhất ClawHub trong 10 phút")

# Block 243
t(243, 0, "Thần Nhiên Ran: 02-20 | Làm sao tạo ra video Seedance 2.0 đạt 25 triệu lượt xem? Phân tích lại bản remake kết thúc Stranger Things")

# Block 244
t(244, 0, "Biên bản thông minh: 02-13 | Để AI suy nghĩ như bạn: Dùng YouMind Skills xây dựng hệ thống nội dung của bạn, thực hiện đăng ổn định hàng ngày tăng followers WaytoAGI học chung lúc 8 giờ tối ngày 13 tháng 2 năm 2026")

# Block 245
t(245, 0, "Biên bản thông minh: 02-12 | Dùng Bách Luyện của Alibaba tạo video chúc Tết, giọng nói chúc Tết đa kịch bản, mẫu văn bản chúc Tết, một lần giải quyết hết. Một buổi livestream kết thúc, bạn có thể tự tay làm nội dung chúc Tết\n")
t(245, 1, "Khách mời livestream: Điện Ba Khúc Kỳ WaytoAGI học chung lúc 8 giờ tối ngày 12 tháng 2 năm 2026")

# Block 246
t(246, 0, "Biên bản thông minh: 02-11 | Cách dùng YouMind sở hữu nguồn đề tài liên tục không ngừng + liên tục ổn định sản xuất nội dung hot ngày 11 tháng 2 năm 2026")

# Block 247
t(247, 0, "Biên bản thông minh: 02-11 | 7 Skill phát hành bởi Baidu Qianfan, hướng dẫn từng bước triển khai một chạm trợ lý AI của riêng bạn WaytoAGI học chung lúc 8 giờ tối ngày 11 tháng 2 năm 2026")

# Block 248
t(248, 0, "Biên bản thông minh: 02-10 | Chung kết cuộc thi AI Star Plan ngày 10 tháng 2 năm 2026")

# Block 249
t(249, 0, "Biên bản thông minh: 02-10 | Làm chủ mùa xuân mới, không khí Tết bắt đầu rồi\n\n🎯 Điểm nổi bật livestream:\n✅ Bách Luyện dễ dàng bắt đầu không rào cản, thoải mái làm nội dung Năm mới\n✅ Chữ phúc AI, danh sách đồ Tết, cắt giấy hoa cửa sổ tất cả trong một giải quyết\n✅ Tiệc tất niên & bách khoa toàn thư công thức, giải quyết \"Tết ăn gì\"\n✅ Không giảng khái niệm phức tạp, trực tiếp biến AI thành hộp công cụ không khí Tết\n\n🌟 Khách mời livestream | Cô giáo Điện Ba Khúc Kỳ\nChuyên gia sản phẩm AI công ty lớn | Nhà phát triển độc lập | Blogger AI Xiaohongshu\n")

# Block 250
t(250, 0, "Biên bản thông minh: 02-08 | 🔥 Tối nay 20:00 livestream | Phân tích chuyên sâu phần cứng AI x phát triển ứng dụng AI\n\n🎤 Khách mời đặc biệt:\nNgân Hải (Quản lý sản phẩm AI)\n\n💡 Điểm nổi bật livestream:\n✅ Phân tích năng lực cốt lõi và kịch bản ứng dụng kính AI\n✅ Hướng dẫn từng bước xây dựng workflow Agent thông minh\n")

# Block 251
t(251, 0, "`Biên bản thông minh: 02-07 | Hôm nay không cạnh tranh nữa, để TRAE Skill làm việc!")

# Block 252
t(252, 0, "Biên bản thông minh: 02-06 | YouMind 0.8 chính thức phát hành, để mỗi người đều có thể trở thành nhà sáng tạo nội dung WaytoAGI học chung lúc 8 giờ tối ngày 6 tháng 2 năm 2026")

# Block 253
t(253, 0, "Biên bản thông minh: 02-05 | Lộc Diễn Vol.009: QVeris: Để AI Agent của bạn dùng một giao diện gọi hàng vạn loại dữ liệu và công cụ\n\n🌟 Khách mời đặc biệt:\nKhúc Đông Kỳ | Đối tác QVeris, Vận hành sản phẩm\n\n🌟 Người dẫn: Trương Úy\nPhụ trách ươm tạo WaytoAGI | Đối tác Tâm Lưu Capital\n")

# Block 254
t(254, 0, "Biên bản thông minh: 02-04 | Các KOL công nghệ đang dùng Miaoda làm gì ngày 4 tháng 2 năm 2026")

# Block 255
t(255, 0, "Biên bản thông minh: 02-03 | Văn phòng AI hiệu quả cao kết thúc: Mẫu Bách Luyện một chạm giải quyết công việc trước Tết WaytoAGI học chung lúc 8 giờ tối ngày 3 tháng 2 năm 2026")

# Block 256
t(256, 0, "Biên bản thông minh: 02-03 | Triển khai OpenClaw/moltbot/clawdbot trên Baidu Smart Cloud ngày 3 tháng 2 năm 2026")

# Block 257
t(257, 0, "Biên bản thông minh: 02-02 | Dùng Agent Skills Builder này sao chép hàng loạt Clawdbot  ")

# Block 258
t(258, 0, "Biên bản thông minh: 02-01 | Chiến lược thực chiến và Hướng dẫn tránh bẫy phát triển phương pháp nhập liệu AI giọng nói")

# Block 259
t(259, 0, "Biên bản thông minh: 01-31 | Thế giới Silicon tương lai kỳ 11: Truy vấn triết học và suy ngẫm dưới làn sóng thẩm mỹ AI")

# Block 260
t(260, 0, "Biên bản thông minh: 01-30 | happycapy.ai clawdbot/moltbot/openclaw trên đám mây mà người mới cũng có thể sử dụng\n")
t(260, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 30 tháng 1 năm 2026")

# Block 261
t(261, 0, "Biên bản thông minh: 01-29 | ListenHub 2.0 ra mắt: Hướng dẫn từng bước sáng tạo AI một cửa  🎤 ")

# Block 262
t(262, 0, "Biên bản thông minh: 01-28 | Văn Tâm 5.0 + Qianfan: Không rào cản chơi đùa với phát triển Agent WaytoAGI học chung lúc 8 giờ tối ngày 28 tháng 1 năm 2026")

# Block 263
t(263, 0, "Biên bản thông minh: 01-27 | Hướng dẫn triển khai Clawdbot từng bước — Tạo một trợ lý AI thực sự")

# Block 264
t(264, 0, "Biên bản thông minh: 01-26 | Trong thời đại AI, làm sao phát triển nhanh game 3D? Phúc bàn thực chiến phát triển cực hạn 48 giờ 🎤 Khách mời đặc biệt: Nhà sản xuất game toàn quy trình thế hệ 00: Tuyên Tương & Chu Kiệt zdj WaytoAGI học chung lúc 8 giờ tối ngày 26 tháng 1 năm 2026")

# Block 265
t(265, 0, "Biên bản thông minh: 01-25 | 🧑‍💻 Hướng dẫn từng bước chơi đùa với phiên bản mã nguồn mở Claude Code — Kode Agent\n\n🎤 Khách mời đặc biệt\nLai Tân Lộ: Nhà sáng lập ShareAI Lab, Nhà phát triển Kode Agent (Agent phiên bản mã nguồn mở Claude Code)\n")
t(265, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 25 tháng 1 năm 2026")

# Block 266
t(266, 0, "Biên bản thông minh: 01-24 | Phân tích chuyên sâu nguyên lý và cơ chế thiết kế Claude Code, cùng hướng dẫn bạn từ 0 đến 1 tự tay làm một mini Claude Code. Người chia sẻ: ShareAI Lai Tân Lộ WaytoAGI học chung lúc 8 giờ tối ngày 24 tháng 1 năm 2026")

# Block 267
t(267, 0, "Biên bản thông minh: 01-23 | Đánh giá chuyên sâu MiniMax Agent 2.0! Bàn làm việc gốc AI giải phóng đôi tay như thế nào?\n\n🎤 Khách mời đặc biệt\nTầm Lộ: Người phụ trách sản phẩm MiniMax Agent\n")
t(267, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 23 tháng 1 năm 2026")

# Block 268
t(268, 0, "Biên bản thông minh: 01-22 | Trại huấn luyện biến đổi cực mạnh Skill (phát sóng hai ngày liên tiếp)  ")

# Block 269
t(269, 0, "Biên bản thông minh: 01-21 | Trại huấn luyện biến đổi cực mạnh Skill (phát sóng hai ngày liên tiếp) ")

# Block 270
t(270, 0, "Biên bản thông minh: 01-20 | Coze 2.0 rốt cuộc đã cập nhật những gì. Khách mời: La Văn + Nhị Sư Huynh WaytoAGI học chung lúc 8 giờ tối ngày 20 tháng 1 năm 2026")

# Block 271
t(271, 0, "Biên bản thông minh: 01-19 | AI nơi công sở, dùng Coze thôi — Tính năng mới Coze Skill ra mắt\n")
t(271, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 19 tháng 1 năm 2026")

# Block 272
t(272, 0, "Biên bản thông minh: 01-17 | Thế giới Silicon tương lai kỳ 10: Đối thoại Nhà sáng lập「Sấm Điện Thuyết」: Hướng dẫn thực chiến sản phẩm AI ra biển quốc tế\n\n📌 Khách mời đặc biệt\nCung Chấn: Đồng sáng lập Sấm Điện Thuyết, Phụ trách tăng trưởng & thương mại hóa\nDư Mãnh: Quản lý sản phẩm & CEO Sấm Điện Thuyết\n")
t(272, 1, "Nhóm dẫn chương trình: Hướng Dương Kiều Mộc, Diêu Toàn Cương, Ni Khắc Tây, Nguyên Tử ngày 17 tháng 1 năm 2026")

# Block 273
t(273, 0, "Biên bản thông minh: 01-14 | PixVerse R1 — Mô hình thế giới tạo sinh thời gian thực đầu tiên toàn cầu chính thức ra mắt")

# Block 274
t(274, 0, "Biên bản thông minh: 01-13 | Lộc Diễn Vol.008: AOE: Không chỉ là Claude Cowork, mà là Vibe Working\n\n🎤 Khách mời đặc biệt:\nĐàm Thiếu Khanh: AOE CEO & Co-Founder\nLý Tuấn: Phụ trách tăng trưởng AOE & Co-Founder\n")
t(274, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 13 tháng 1 năm 2026")

# Block 275
t(275, 0, "Biên bản thông minh: 01-10 | Mở đầu năm bùng nổ! Hải Tân & A Văn chia sẻ workflow AI WaytoAGI học chung lúc 8 giờ tối ngày 10 tháng 1 năm 2026")

# Block 276
t(276, 0, "Biên bản thông minh: 01-10 | 👉 Chiều 15:00 livestream | Tin nóng CES 2026, giải mã chuyên sâu hai đường đua trí tuệ nhập thể và lái xe tự động\n\n📌 Khách mời đặc biệt:\n")
t(276, 1, "Vương Vĩ Oánh: Tiến sĩ Khoa học Máy tính Đại học Harvard, Nhà khoa học nghiên cứu trí tuệ nhập thể, Doanh nhân khởi nghiệp liên tục ngày 10 tháng 1 năm 2026")

# Block 277
t(277, 0, "Biên bản thông minh: 01-08 | \"Miaoda - Biến sáng tạo thành kinh doanh\" Hội bàn tròn Open Mic kỳ 5 biến hiện ứng dụng! WaytoAGI học chung lúc 8 giờ tối ngày 8 tháng 1 năm 2026")

# Block 278
t(278, 0, "Biên bản thông minh: 01-03 | Thế giới Silicon tương lai 🔍 Giải mã mật mã lưu lượng nền tảng X, 3 tuần tăng nhanh hơn 10.000 follower như thế nào?\n🎨 Chia sẻ mẹo prompt hot, dẫn bạn tránh sự đồng nhất hóa AI\n")
t(278, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 3 tháng 1 năm 2026")

# Block 279
t(279, 0, "Biên bản thông minh: 12-30 | WaytoAGI học chung lúc 8 giờ tối ngày 30 tháng 12 năm 2025")

# Block 280
t(280, 0, "Biên bản thông minh: 12-29 | 👉 Tối nay 20:00 livestream |「Trại huấn luyện phim ngắn AI」Bài bổ sung: Học nhanh mẹo thực hành công cụ video AI\n\n📌 Khách mời đặc biệt\nĐại Bàng: Kỹ sư cao cấp thiết kế nghệ thuật số AIGC | Nhà hoạt hình AI | Người giữ nghệ thuật số Tencent SSV\n\n")
t(280, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 29 tháng 12 năm 2025")

# Block 281
t(281, 0, "Biên bản thông minh: 12-28 | Khóa thực hành Lovart/Tapnow: Xuất phim hàng loạt + Phân tầng động hoàn toàn làm chủ\n\n🎙️ Khách mời đặc biệt\nChu Bằng: Đạo diễn quảng cáo/phim ngắn/hoạt hình AIGC, Blogger vạn fan trên Xiaohongshu\n")
t(281, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 28 tháng 12 năm 2025")

# Block 282
t(282, 0, "Biên bản thông minh: 12-27 | Mở khóa cách chơi mới sáng tạo phim quảng cáo AI\n\n📌 Khách mời đặc biệt\n")
t(282, 1, "Đinh Nhất: Đạo diễn phim quảng cáo/phim tài liệu / Nghệ sĩ AIGC WaytoAGI học chung lúc 8 giờ tối ngày 27 tháng 12 năm 2025")

# Block 283
t(283, 0, "Biên bản thông minh: 12-24 | \"Miaoda - Biến sáng tạo thành kinh doanh\" Kỳ 4 biến hiện ứng dụng siêu bùng nổ! ")

# Block 284
t(284, 0, "Biên bản thông minh: 12-22 | Trợ lý AI thông minh thiết kế riêng cho sáng tạo video, Medeo - Tối nay dạy bạn cách trò chuyện ra một video hay! Khách mời chia sẻ: Thần Nhiên/Quy Tàng/Mona WaytoAGI học chung lúc 8 giờ tối ngày 22 tháng 12 năm 2025")

# Block 285
t(285, 0, "Biên bản thông minh: 12-20 | Thế giới Silicon tương lai kỳ 8: Đào sâu sự thật tiến hóa AI hai năm gần đây, mở khóa danh sách công cụ AI thường dùng WaytoAGI học chung lúc 8 giờ tối ngày 20 tháng 12 năm 2025")

# Block 286
t(286, 0, "🔥 App Qianwen ra mắt tính năng mới「Nhà hát nhỏ AI」! Trải nghiệm cách chơi giống Sora2! WaytoAGI học chung lúc 8 giờ tối ngày 18 tháng 12 năm 2025")

# Block 287
t(287, 0, "Biên bản thông minh: 12-18 | \"Miaoda - Biến sáng tạo thành kinh doanh\" Chuỗi giảng dạy biến hiện ứng dụng kỳ 3 đây rồi! \n")
t(287, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 18 tháng 12 năm 2025")

# Block 288
t(288, 0, "Biên bản thông minh: 12-17 | Hướng dẫn nâng cao Claude Code: Từng bước chơi đùa MCP, Skill x và các công cụ khác!")

# Block 289
t(289, 0, "Biên bản thông minh: 12-16 | Hướng dẫn cài đặt và cấu hình toàn diện Claude Code/CodeX+Skill")

# Block 290
t(290, 0, "Biên bản thông minh: 12-15 | Yee's AI điều hương và câu chuyện đằng sau, dự án OPC phát triển trong cộng đồng\n")
t(290, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 15 tháng 12 năm 2025")

# Block 291
t(291, 0, "Biên bản thông minh: 12-13 | Lộc Diễn Vol.007: Mulan.pro: Từ bà nội trợ đến Nhà sáng lập công ty AI. Người bình thường thực sự có thể lội ngược dòng không?\n")
t(291, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 13 tháng 12 năm 2025")

# Block 292
t(292, 0, "Biên bản thông minh: 12-11 | \"Miaoda - Biến sáng tạo thành kinh doanh\" Chuỗi giảng dạy biến hiện ứng dụng kỳ 2 bùng nổ! Thứ Năm hàng tuần là thời gian Miaoda\n")
t(292, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 11 tháng 12 năm 2025")

# Block 293
t(293, 0, "Biên bản thông minh: 12-10 | 🤖 Lộc Diễn Vol.006: Refly.AI chính thức mở công khai thử nghiệm! Phát mã mời số lượng có hạn\n\n💡 Điểm nổi bật tính năng: Workflow tự động hóa AI phiên bản đơn giản của Coze/n8n, phương án đa kịch bản sao chép trực tiếp\n")
t(293, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 10 tháng 12 năm 2025")

# Block 294
t(294, 0, "Biên bản thông minh: 12-09 | Cách dùng AI làm hình ảnh IP / WaytoAGI học chung lúc 8 giờ tối ngày 9 tháng 12 năm 2025")

# Block 295
t(295, 0, "Biên bản thông minh: 12-08 | Trại huấn luyện phim ngắn AI: Khai giảng Bài 1\n《Hiện trạng ngành phim ngắn và xem phim hot》Giảng viên: Dạ Du Thần\n")
t(295, 1, "Hãy xem rõ ngành này đang \"kiếm tiền của ai\", rồi mới quyết định bạn có muốn vào không / WaytoAGI học chung lúc 8 giờ tối ngày 8 tháng 12 năm 2025")

# Block 296
t(296, 0, "Biên bản thông minh: 12-06 | AI + Giáo dục WaytoAGI học chung lúc 8 giờ tối ngày 6 tháng 12 năm 2025")

# Block 297
t(297, 0, "Biên bản thông minh: 12-06 | Gala thiếu nhi AI mùa xuân - Nhà đọc sách tranh đồng sáng tạo, poster sáng tạo của các em nhỏ ngày 6 tháng 12 năm 2025")

# Block 298
t(298, 0, "Biên bản thông minh: 12-05 | Nhập môn không nền tảng âm nhạc AI với thực hành Suno | Hướng dẫn sáng tạo cuộc thi tuyển chọn nhân vật số「AI Star Plan」của Baidu\n\n📌 Khách mời đặc biệt:\n【JKMiles】\n- Giải Vàng toàn quốc Cuộc thi sáng tạo tác phẩm AI Hoa Đằng Cup\n- Đồng sáng tạo mảng âm nhạc cộng đồng WaytoAGI\n\n")
t(298, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 5 tháng 12 năm 2025")

# Block 299
t(299, 0, "Biên bản thông minh: 12-04 | \"Miaoda - Biến sáng tạo thành kinh doanh\" Chuỗi giảng dạy biến hiện ứng dụng kỳ 1 đây rồi! WaytoAGI học chung lúc 8 giờ tối ngày 4 tháng 12 năm 2025")

# Block 300
t(300, 0, "Biên bản thông minh: 12-02 | Cuộc thi phát triển plugin MCP chiêu mộ! Đếm ngược chạy nước rút 6 ngày! Bách Bảo Hộp | Thông Nghĩa Linh Mã | 👨‍💻【Khách mời chia sẻ】\nNgô Bính: Giám đốc tài chính cấp cao công ty tư vấn bất động sản quốc tế nổi tiếng, Tiên phong tổ chức sự kiện WaytoAGI\nKhổng Lập Cương: Quản lý vận hành sau bán hàng Fortune 500, Học viên xuất sắc & Trợ giảng trại huấn luyện WaytoAGI\n")
t(300, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 2 tháng 12 năm 2025")

# Block 301
t(301, 0, "Biên bản thông minh: WaytoAGI học chung lúc 8 giờ tối ngày 29 tháng 11 năm 2025")

# Block 302
t(302, 0, "Biên bản thông minh: 11-28 | Baidu x Lạc Hoa Entertainment x WaytoAGI Cuộc thi tuyển chọn nhân vật số「AI Star Plan」chính thức khởi động!\n")
t(302, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 28 tháng 11 năm 2025")

# Block 303
t(303, 0, "Biên bản thông minh: 11-27 | WaytoAGI học chung lúc 8 giờ tối ngày 27 tháng 11 năm 2025")

# Block 304
t(304, 0, "Biên bản thông minh: 11-26 | Lộc Diễn Vol.005: Creaibo — AI sinh ra dành cho nội dung chất lượng 🎙️ WaytoAGI học chung lúc 8 giờ tối ngày 26 tháng 11 năm 2025")

# Block 305
t(305, 0, "Biên bản thông minh: 11-26 | Thử nghiệm cộng đồng App Qianwen WaytoAGI học chung lúc 8 giờ tối ngày 26 tháng 11 năm 2025")

# Block 306
t(306, 0, "Biên bản thông minh: 11-25 | Cuộc thi phát triển plugin MCP chiêu mộ! Hướng dẫn chiến lược 💰 Quỹ giải thưởng phong phú: Mở khóa thưởng tiền mặt khổng lồ 160.000 🔥 Giảng dạy kiểu bảo mẫu: Giảng giải hệ thống toàn quy trình, đánh trúng vấn đề đau đầu 📌 Không viết một dòng code: Dùng lingma dựa trên FastMCP phát triển demo triển khai một chạm lên Bách Bảo Hộp ngày 25 tháng 11 năm 2025")

# Block 307
t(307, 0, "Biên bản thông minh: 11-24 | 💥 Tối nay 20:00 | Chạy nước rút nâng cao! Hướng dẫn chiến lược nâng cao cuộc thi sáng tạo ứng dụng Đậu Bao không rào cản!\n")
t(307, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 24 tháng 11 năm 2025")

# Block 308
t(308, 0, "Biên bản thông minh: 11-23 | Thử nghiệm cộng đồng Nano Banana Pro, Khách mời trọng lượng: Thương Hà + Mộng Phi + Tiểu Oai WaytoAGI học chung lúc 8 giờ tối ngày 23 tháng 11 năm 2025")

# Block 309
t(309, 0, "Biên bản thông minh: 11-22 | Thế giới Silicon tương lai kỳ 6: AI và cuộc sống tương lai WaytoAGI học chung lúc 8 giờ tối ngày 22 tháng 11 năm 2025")

# Block 310
t(310, 0, "Biên bản thông minh: 11-21 |「Trại huấn luyện Agent AI」Kỳ 2, Bài 8: Demo Day: Giao nộp ứng dụng AI hoàn chỉnh từ 0 đến 1 ngày 21 tháng 11 năm 2025")

# Block 311
t(311, 0, "Biên bản thông minh: 11-20 | Cuộc thi phát triển plugin MCP cho kịch bản doanh nghiệp khởi động, Bách Bảo Hộp | Thông Nghĩa Linh Mã |\n")
t(311, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 20 tháng 11 năm 2025")

# Block 312
t(312, 0, "Biên bản thông minh: 11-19 |「Trại huấn luyện Agent AI」Kỳ 2, Bài 7: Chau chuốt tỉ mỉ: Tăng tốc hiệu suất & Nhân đôi trải nghiệm ngày 19 tháng 11 năm 2025")

# Block 313
t(313, 0, "Biên bản thông minh: 11-18 | Thử nghiệm cộng đồng App Qianwen WaytoAGI học chung lúc 8 giờ tối ngày 18 tháng 11 năm 2025")

# Block 314
t(314, 0, "Biên bản thông minh: 11-17 |「Trại huấn luyện Agent AI」Kỳ 2, Bài 6: Tương tác đa dạng: Card, Hình ảnh, Giọng nói phủ sóng toàn diện ngày 17 tháng 11 năm 2025")

# Block 315
t(315, 0, "Biên bản thông minh: 11-15 |「Trại huấn luyện Agent AI」Kỳ 2, Bài 5: Kho tri thức x Bộ nhớ: Tạo \"Bộ não mạnh nhất\" chuyên dụng cho Bot ngày 15 tháng 11 năm 2025")

# Block 316
t(316, 0, "Biên bản thông minh: 11-14 | Hoạt động đầu tư AI campus AIPO trình bày dự án xuất sắc toàn quốc,「Buổi trình diễn sáng tạo sinh viên」xem bạn cùng lứa chơi đùa Feishu như thế nào! Sự va chạm kỳ diệu giữa kịch bản campus + công cụ AI, mỗi dự án đều ẩn chứa bất ngờ;\n")
t(316, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 14 tháng 11 năm 2025")

# Block 317
t(317, 0, "Biên bản thông minh: 11-13 |「Trại huấn luyện Agent AI」Kỳ 2, Bài 4: Workflow nâng cao: Phân nhánh, Vòng lặp, Nhận dạng ý định, Xử lý hình ảnh nắm một tay WaytoAGI học chung lúc 8 giờ tối ngày 13 tháng 11 năm 2025")

# Block 318
t(318, 0, "Biên bản thông minh: 11-12 | Dẫn bạn chinh phục giải thưởng 200.000, Cuộc thi sáng tạo ứng dụng Đậu Bao ập đến! Không chỉ chinh phục giải, còn học mẹo cứng, 1 giờ hoàn thành bài dự thi! Giảng viên: Hứa Kiện\n")
t(318, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 12 tháng 11 năm 2025")

# Block 319
t(319, 0, "Biên bản thông minh: 11-11 |「Trại huấn luyện Agent AI」Kỳ 2, Bài 3: Kéo thả nhập môn: Không cần code xây dựng logic phức tạp bằng workflow WaytoAGI học chung lúc 8 giờ tối ngày 11 tháng 11 năm 2025")

# Block 320
t(320, 0, "11-10 | AI cũng Ngày Độc thân | Phúc lợi phiên bản \"88VIP\" của Tàng Sư Phụ đại phát WaytoAGI học chung lúc 8 giờ tối")

# Block 321
t(321, 0, "Biên bản thông minh: 11-09 |「Trại huấn luyện Agent AI」Kỳ 2, Bài 2: Phép thuật Prompt: Một câu khiến Bot hiểu tiếng người ngày 9 tháng 11 năm 2025")

# Block 322
t(322, 0, "Biên bản thông minh: 11-08 | Thế giới Silicon tương lai kỳ 5: Trò chuyện về AI và cuộc sống tương lai ngày 8 tháng 11 năm 2025")

# Block 323
t(323, 0, "Biên bản thông minh: 11-08 | Kỳ đường đua AI campus AIPO lần 3 trình bày toàn quốc ngày 8 tháng 11 năm 2025")

# Block 324
t(324, 0, "Biên bản thông minh: 11-07 |「Trại huấn luyện Agent AI」Kỳ 2 Lễ khai giảng, 8 buổi livestream dẫn bạn từ 0 đến 1 tạo ứng dụng AI có thể ra mắt! Bài 1 ngày 7 tháng 11 năm 2025")

# Block 325
t(325, 0, "11-06 | Miaoda lại ra tính năng mới rồi!\n")

# Block 326
t(326, 0, "Biên bản thông minh: 11-05 | Campus AIPO Chú Mèo giảng prompt WaytoAGI học chung lúc 8 giờ tối ngày 5 tháng 11 năm 2025")

# Block 327
t(327, 0, "Biên bản thông minh: 11-04 | Mùa cảm hứng mẫu AI CapCut — Giải thưởng 200.000 + Hàng chục triệu lưu lượng, hướng dẫn từng bước giúp bạn thắng cuộc thi!\n")
t(327, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 4 tháng 11 năm 2025")

# Block 328
t(328, 0, "Biên bản thông minh: 11-03 | Trại huấn luyện Campus AIPO WaytoAGI. Giảng viên: AJ. Workflow học AI WaytoAGI học chung lúc 8 giờ tối ngày 3 tháng 11 năm 2025")

# Block 329
t(329, 0, "Biên bản thông minh: 11-02 | Trại huấn luyện AI Kỳ 2: Trại thực chiến Agent trí tuệ, Khách mời: La Văn, Weina, Vương Lôi WaytoAGI học chung lúc 8 giờ tối ngày 2 tháng 11 năm 2025")

# Block 330
t(330, 0, "Biên bản thông minh: 11-01 | Trại huấn luyện AIPO Phần 2 - Từ 0-1 tập trung kịch bản campus xây dựng AI đồng hành của riêng bạn\n")
t(330, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 1 tháng 11 năm 2025")

# Block 331
t(331, 0, "Biên bản thông minh: 10-31 | Trại huấn luyện AI Kỳ 1: Kết thúc trại huấn luyện n8n WaytoAGI học chung lúc 8 giờ tối ngày 31 tháng 10 năm 2025")

# Block 332
t(332, 0, "Biên bản thông minh: 10-30 | Trại huấn luyện AIPO - Từ 0-1 tập trung kịch bản campus xây dựng AI đồng hành của riêng bạn\n")
t(332, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 30 tháng 10 năm 2025")

# Block 333
t(333, 0, "Biên bản thông minh: 10-29 |【Trại huấn luyện AI】Chia sẻ thực chiến dự án Agent AI WaytoAGI học chung lúc 8 giờ tối ngày 29 tháng 10 năm 2025")

# Block 334
t(334, 0, "Biên bản thông minh: 10-28 | Giải mã cuộc thi video AI lớn nhất nước ngoài Chroma Awards WaytoAGI học chung lúc 8 giờ tối ngày 28 tháng 10 năm 2025")

# Block 335
t(335, 0, "Hội nghị ra mắt AIPO lần 3")

# Block 336
t(336, 0, "Biên bản thông minh: 10-24 | Chia sẻ mẹo thực chiến lập trình AI, 30 phút từ nhập môn đến mê mẩn | Vibe Coze! Hướng dẫn cuộc thi thử thách Coze AI 💻\n \n")
t(336, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 24 tháng 10 năm 2025")

# Block 337
t(337, 0, "Biên bản thông minh: 10-23 | WaytoAGI học chung lúc 8 giờ tối ngày 23 tháng 10 năm 2025")

# Block 338
t(338, 0, "Biên bản thông minh: 10-22 | 🎙️ IndexTTS: Để giọng nói ấm áp hơn 👨‍🏫 Giảng viên: Tư Dịch: Chuyên gia thuật toán trưởng mô hình giọng nói lớn IndexTTS của bilibili / Tử Trạch: Chuyên gia vận hành sản phẩm mô hình giọng nói lớn bilibili WaytoAGI học chung lúc 8 giờ tối ngày 22 tháng 10 năm 2025")

# Block 339
t(339, 0, "Biên bản thông minh: 10-21 | Tối nay 20:00 livestream! Phân tích quyền lợi công cụ AI trị giá 1 triệu đô + Cuộc thi sáng tạo AI giải thưởng 175.000\n\n🌟 Khách mời đặc biệt:\n- Davis: Director / Producer\n- Joey: Đồng sáng lập Monet Lisa AI, Nghệ sĩ hợp tác World Expo 2025 Osaka\n")
t(339, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 21 tháng 10 năm 2025")

# Block 340
t(340, 0, "Biên bản thông minh: 10-20 | Lập trình AI & AI tự truyền thông: Tọa đàm tránh bẫy 🎯 🌟 Khách mời đặc biệt: Ngôn Đại Hiệp, 14 năm kinh nghiệm vận hành truyền thông mới, Buổi tọa đàm tránh bẫy talkshow: 10 ngày tăng 56.000 fan Xiaohongshu, 2 tuần phát triển 1 mini app bán được 100.000, đã dẫm phải những bẫy gì WaytoAGI học chung lúc 8 giờ tối ngày 20 tháng 10 năm 2025")

# Block 341
t(341, 0, "Biên bản thông minh: 10-18 |【Gợi Ý Tương Lai】Giải mã cuộc thi WaytoAGI học chung lúc 8 giờ tối ngày 18 tháng 10 năm 2025")

# Block 342
t(342, 0, "Biên bản thông minh: 10-17 | Cuốn sách đầu tiên của cộng đồng WaytoAGI【Nhập môn cực đơn giản và ứng dụng Vẽ tranh AI】chính thức ra mắt WaytoAGI học chung lúc 8 giờ tối ngày 17 tháng 10 năm 2025")

# Block 343
t(343, 0, "Biên bản thông minh: 10-16 | Cuộc thi chủ đề n8n")

# Block 344
t(344, 0, "Biên bản thông minh: 10-15 | Trại huấn luyện AI Kỳ 1 Bài 3: Phân tích case đơn hàng thương mại n8n, dẫn bạn xây dựng hệ thống workflow phức tạp WaytoAGI học chung lúc 8 giờ tối ngày 15 tháng 10 năm 2025")

# Block 345
t(345, 0, "Biên bản thông minh: 10-14 | WaytoAGI「Trại huấn luyện AI」Bài 2 Chủ đề: Các case workflow tự động hóa #n8n phổ biến WaytoAGI học chung lúc 8 giờ tối ngày 14 tháng 10 năm 2025")

# Block 346
t(346, 0, "Biên bản thông minh: 10-13 | 4 ngày nắm vững workflow n8n! WaytoAGI「Trại huấn luyện AI」Kỳ 1 khai giảng! \n")
t(346, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 13 tháng 10 năm 2025")

# Block 347
t(347, 0, "Biên bản thông minh: 10-11 |「Thế giới Silicon tương lai」Kỳ 4: Thời đại AI Agent, Tìm kiếm không còn dành cho con người 🔍")

# Block 348
t(348, 0, "Biên bản thông minh: 10-10 | Danh sách thu nhập khởi nghiệp AI của tôi và câu chuyện khởi nghiệp AI 💡\n")
t(348, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 10 tháng 10 năm 2025")

# Block 349
t(349, 0, "Biên bản thông minh: 10-09 | WaytoAGI học chung lúc 8 giờ tối ngày 9 tháng 10 năm 2025")

# Block 350
t(350, 0, "Biên bản thông minh: 10-07 | Phân tích lộ trình học tập và khoảng cách thông tin trong thời đại AI WaytoAGI học chung lúc 8 giờ tối ngày 7 tháng 10 năm 2025")

# Block 351
t(351, 0, "10-04 | Nhập môn siêu tốc AI từ 0 đến 1 · Phần Vẽ tranh WaytoAGI học chung lúc 8 giờ tối")

# Block 352
t(352, 0, "Biên bản thông minh: 10-03 | Làm sao đối thoại với mô hình ngôn ngữ lớn? (Phiên bản nhập môn siêu tốc cho người mới từ 0) WaytoAGI học chung lúc 8 giờ tối ngày 3 tháng 10 năm 2025")

# Block 353
t(353, 0, "Biên bản thông minh: 10-02 | Cuộc thi phim ngắn Sora2: Viết tại chỗ · Nộp tại chỗ · Trình diễn tại chỗ WaytoAGI học chung lúc 8 giờ tối ngày 2 tháng 10 năm 2025")

# Block 354
t(354, 0, "10-01 | Thử nghiệm thực tế Sora2, Tiếp sức mã mời, WaytoAGI học chung lúc 8 giờ tối ngày 1 tháng 10 năm 2025")

# Block 355
t(355, 0, "Biên bản thông minh: 09-27 | Hội thảo giao đấu toàn quốc ngày 27 tháng 9 năm 2025")

# Block 356
t(356, 0, "Biên bản thông minh: 09-25 | Chia sẻ sáng tạo cuộc thi đạo diễn AI 🌟 Khách mời đặc biệt Băng Ngư Tử, Tố Ngữ, Ngôn dẫn bạn mở khóa trải nghiệm đạo diễn AI trên nền tảng sáng tạo thông minh Baidu, đầy ắp kiến thức thực chiến!\n")
t(356, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 25 tháng 9 năm 2025")

# Block 357
t(357, 0, "Biên bản thông minh: 09-24 | Giải mã cuộc thi giải thưởng 100.000, Cuộc thi sáng tạo video AI theo mùa nóng Baidu · Sinh tồn · Vũ trụ khởi động! WaytoAGI học chung lúc 8 giờ tối ngày 24 tháng 9 năm 2025")

# Block 358
t(358, 0, "Biên bản thông minh: 09-23 | Cuộc thi lập trình #TrickleAI bùng nổ! Giải lớn là iPhone 17 Pro Max. Quy Tàng / Hướng Dương đồng giảng dạy: Trickle là công cụ Vibe Coding kết nối liền mạch sinh đa phương thức, dễ dùng mà mạnh mẽ\n")
t(358, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 23 tháng 9 năm 2025")

# Block 359
t(359, 0, "Biên bản thông minh: 09-22 | Cuộc thi đạo diễn AI 🌟 Kỹ sư phân tích chuyên sâu cách chơi「Sáng tạo video thông minh Baidu」WaytoAGI học chung lúc 8 giờ tối ngày 22 tháng 9 năm 2025")

# Block 360
t(360, 0, "Biên bản thông minh: 09-20 | WaytoAGI học chung lúc 8 giờ tối ngày 20 tháng 9 năm 2025")

# Block 361
t(361, 0, "Biên bản thông minh: 09-19 | WaytoAGI học chung lúc 8 giờ tối ngày 19 tháng 9 năm 2025")

# Block 362
t(362, 0, "Biên bản thông minh: 09-18 | Feishu Bitable kết nối Jimeng 4.0, tối nay Vương Đại Tiên dạy bạn chơi hết nước WaytoAGI học chung lúc 8 giờ tối ngày 18 tháng 9 năm 2025")

# Block 363
t(363, 0, "Biên bản thông minh: 09-17 | Baidu World x Xiaohongshu Tech đồng trình bày giải mã uy tín cuộc thi hackathon Miaoda WaytoAGI học chung lúc 8 giờ tối ngày 17 tháng 9 năm 2025")

# Block 364
t(364, 0, "Biên bản thông minh: 09-16 | Triển khai website chính thức từ 0 đến 1! Người mới không nền tảng cũng có thể chơi đùa lập trình AI WaytoAGI học chung lúc 8 giờ tối ngày 16 tháng 9 năm 2025")

# Block 365
t(365, 0, "Biên bản thông minh: 09-11 | Dùng Cursor+Zion xây dựng MVP ứng dụng AI, biến hiện ngay tức thì! \n")
t(365, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 11 tháng 9 năm 2025")

# Block 366
t(366, 0, "Biên bản thông minh: 09-10 | WaytoAGI học chung lúc 8 giờ tối ngày 10 tháng 9 năm 2025")

# Block 367
t(367, 0, "Biên bản thông minh: 09-09 | Giảng dạy mô hình thiết kế workflow Agent trí tuệ, WaytoAGI học chung lúc 8 giờ tối ngày 9 tháng 9 năm 2025")

# Block 368
t(368, 0, "Biên bản thông minh: 09-08 | Phân tích thí nghiệm bán hàng rong AI, Chiết xuất framework hoàn chỉnh「Kim tự tháp triển khai thương mại」WaytoAGI học chung lúc 8 giờ tối ngày 8 tháng 9 năm 2025")

# Block 369
t(369, 0, "Biên bản thông minh: 09-07 | Hướng dẫn sử dụng Qoder: Từ nhập môn đến kinh ngạc\n")
t(369, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 7 tháng 9 năm 2025")

# Block 370
t(370, 0, "Biên bản thông minh: 09-06 | WaytoAGI học chung lúc 8 giờ tối ngày 6 tháng 9 năm 2025")

# Block 371
t(371, 0, "Biên bản thông minh: 09-05 | Khóa thực chiến phát triển AI Agent trên Alibaba Cloud Bách Luyện. Giảng viên: Hứa Kiện WaytoAGI học chung lúc 8 giờ tối ngày 5 tháng 9 năm 2025")

# Block 372
t(372, 0, "Biên bản thông minh: 09-04 | Zho: Hàng triệu lưu lượng X, Hướng dẫn NanoBanana đầy đủ nhất WaytoAGI học chung lúc 8 giờ tối ngày 4 tháng 9 năm 2025")

# Block 373
t(373, 0, "Biên bản thông minh: 09-03 | WaytoAGI học chung lúc 8 giờ tối ngày 3 tháng 9 năm 2025")

# Block 374
t(374, 0, "Biên bản thông minh: 09-02 | WaytoAGI học chung lúc 8 giờ tối ngày 2 tháng 9 năm 2025")

# Block 375
t(375, 0, "Biên bản thông minh: 08-29 | Tổng hợp toàn diện công cụ Vibe Coding, chọn đúng công cụ hiệu suất nhân đôi! Người dẫn: Ben WaytoAGI học chung lúc 8 giờ tối ngày 29 tháng 8 năm 2025")

# Block 376
t(376, 0, "Biên bản thông minh: 08-28 | Mở khóa bí kíp kỹ thuật Qwen-Image và cảm hứng sáng tạo! \n")
t(376, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 28 tháng 8 năm 2025")

# Block 377
t(377, 0, "Biên bản thông minh: 08-27 | WaytoAGI học chung lúc 8 giờ tối ngày 27 tháng 8 năm 2025")

# Block 378
t(378, 0, "Biên bản thông minh: 08-26 | Mô hình tạo ảnh mạnh nhất? Thực nghiệm nano banana! WaytoAGI học chung lúc 8 giờ tối ngày 26 tháng 8 năm 2025")

# Block 379
t(379, 0, "Biên bản thông minh: 08-22 | Cộng đồng xuất hiện tại London + Workshop livestream - WaytoAGI học chung lúc 8 giờ tối ngày 22 tháng 8 năm 2025")

# Block 380
t(380, 0, "Biên bản thông minh: 08-21 | 🔥 Tối nay 8 giờ! Lộc Diễn Vol.004: OpenCreator - Canvas một cửa cho nhà sáng tạo nội dung\n")
t(380, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 21 tháng 8 năm 2025")

# Block 381
t(381, 0, "Biên bản thông minh: 08-19 | Lộc Diễn Vol.003: ListenHub: AI thay lời có thể giúp nhà sáng tạo kiếm tiền\n")
t(381, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 19 tháng 8 năm 2025")

# Block 382
t(382, 0, "Biên bản thông minh: 08-18 | Nadezhda: Hướng dẫn mới nhất video AI, Chia sẻ cuộc thi AI Bắc Kinh WaytoAGI học chung lúc 8 giờ tối ngày 18 tháng 8 năm 2025")

# Block 383
t(383, 0, "Video hướng dẫn 08-13 | Hộp công cụ siêu cấp biến sáng tạo thành hiện thực chỉ bằng một câu nói, Hướng dẫn sử dụng Miaoda WaytoAGI học chung ngày 13 tháng 8 năm 2025")

# Block 384
t(384, 0, "Biên bản thông minh: 08-11 | Một người dùng AI hoàn thành một bộ hoạt hình như thế nào - 【Rick và Morty dũng cảm đột phá Vũ trụ khuôn mẫu】WaytoAGI học chung lúc 8 giờ tối ngày 11 tháng 8 năm 2025")

# Block 385
t(385, 0, "Biên bản thông minh: 08-06 | Coze mã nguồn mở rất có thể mang đến \"Làn sóng thương mại hóa thứ hai\", cùng thảo luận, tìm cơ hội thuộc về bạn!\n")
t(385, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 6 tháng 8 năm 2025")

# Block 386
t(386, 0, "08-02 | Vibe Coding Mini Hackathon_Buổi trình diễn ý tưởng kỳ lạ - WaytoAGI học chung lúc 8 giờ tối ngày 2 tháng 8 năm 2025")

# Block 387
t(387, 0, "Biên bản thông minh: 07-31 | Nhà phát triển Agent thu nhập vạn đô mỗi tháng chia sẻ kinh nghiệm, Myshell hướng dẫn từng bước xây dựng, WaytoAGI học chung lúc 8 giờ tối ngày 31 tháng 7 năm 2025")

# Block 388
t(388, 0, "Biên bản thông minh: 07-23 | Khóa 1 sáng tạo AI+Ứng dụng: Khóa thực chiến \"Một câu xây ứng dụng\" Baidu Miaoda WaytoAGI học chung lúc 8 giờ tối ngày 23 tháng 7 năm 2025")

# Block 389
t(389, 0, "Biên bản thông minh: 07-22 | Chơi đùa Coze Space, tính năng mới thiết kế trang web ra mắt \n")
t(389, 1, "WaytoAGI học chung lúc 8 giờ tối ngày 22 tháng 7 năm 2025")

# Block 390
t(390, 0, "Biên bản thông minh: 07-16 | Jaaz - Công cụ Agent đa phương thức mã nguồn mở ra mắt đầu tiên WaytoAGI học chung lúc 8 giờ tối ngày 16 tháng 7 năm 2025")

# Block 391
t(391, 0, "Biên bản thông minh: 07-15 | Trợ lý AI dẫn bạn chơi đùa phân tích dữ liệu! Giảng dạy kiểu bảo mẫu Thông Nghĩa Linh Mã - WaytoAGI học chung lúc 8 giờ tối ngày 15 tháng 7 năm 2025")

# Block 392
t(392, 0, "Biên bản thông minh: WaytoAGI học chung lúc 8 giờ tối ngày 9 tháng 7 năm 2025")

# Block 393
t(393, 0, "Biên bản thông minh: 07-07 | WaytoAGI học chung lúc 8 giờ tối ngày 7 tháng 7 năm 2025")

# ────────────────────────────────────────────
# Now apply translations
# ────────────────────────────────────────────

trans_data = copy.deepcopy(data)
applied = 0
kept = 0
total_text = 0

for i, block in enumerate(trans_data['blocks']):
    for j, el in enumerate(block['elements']):
        if el['type'] == 'text_run':
            total_text += 1
            if (i, j) in translations:
                el['content'] = translations[(i, j)]
                applied += 1
            elif not cn_pattern.search(el['content']):
                kept += 1
            else:
                # Should not happen - we missed a Chinese text
                print(f"WARNING: Untranslated Chinese at block {i}, elem {j}: {el['content'][:80]}")

print(f"Total text_run elements: {total_text}")
print(f"Translated: {applied}")
print(f"Kept (already Vietnamese): {kept}")
print(f"Translation map size: {len(translations)}")

# Verify no Chinese remains
remaining_cn = 0
for i, block in enumerate(trans_data['blocks']):
    for j, el in enumerate(block['elements']):
        if el['type'] == 'text_run' and cn_pattern.search(el['content']):
            remaining_cn += 1
            print(f"REMAINING CN: block {i} elem {j}: {el['content'][:60]}")

print(f"\nRemaining Chinese: {remaining_cn}")

with open('_art18_trans.json', 'w', encoding='utf-8') as f:
    json.dump(trans_data, f, ensure_ascii=False, indent=2)
print("Saved _art18_trans.json")
