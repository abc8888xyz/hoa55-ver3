# -*- coding: utf-8 -*-
"""Build translation map for article 23 by processing the CN texts list."""
import json, sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('_art23_cn_texts.json', 'r', encoding='utf-8') as f:
    cn_texts = json.load(f)

trans_map = {}

# Helper: translate dates like 2026年2月27日 -> ngày 27 tháng 2 năm 2026
def translate_date(text):
    def replace_date(m):
        y, mo, d = m.group(1), m.group(2), m.group(3)
        return f"ngày {int(d)} tháng {int(mo)} năm {y}"
    return re.sub(r'(\d{4})年(\d{1,2})月(\d{1,2})日', replace_date, text)

# Helper: translate common prefixes
def translate_meeting_note(text):
    """Translate 智能纪要 style entries - keep most content, translate prefix and dates"""
    result = text
    # Replace 智能纪要 prefix
    result = result.replace('智能纪要：', 'Biên bản thông minh: ')
    result = result.replace('智能纪要:', 'Biên bản thông minh: ')
    # Replace WaytoAGI晚8点共学
    result = result.replace('WaytoAGI晚8点共学', 'WaytoAGI Học chung lúc 8 giờ tối')
    # Translate dates
    result = translate_date(result)
    # Common Chinese phrases in meeting notes
    result = result.replace('特邀嘉宾', 'Khách mời đặc biệt')
    result = result.replace('直播亮点', 'Điểm nổi bật livestream')
    result = result.replace('直播核心亮点', 'Điểm nổi bật core livestream')
    result = result.replace('直播嘉宾', 'Khách mời livestream')
    result = result.replace('主持人', 'MC')
    result = result.replace('主持团', 'Nhóm MC')
    result = result.replace('分享嘉宾', 'Khách mời chia sẻ')
    result = result.replace('讲师', 'Giảng viên')
    result = result.replace('视频教程', 'Video hướng dẫn')
    return result

# ===== MAIN CONTENT (indices 0-92) =====

# 0: Page title
trans_map[cn_texts[0]] = "02-27 Phát lại livestream | Hải Tân A Văn: Tôi đã tạo một không gian làm việc trực quan cho Tôm Hùm WaytoAGI Học chung lúc 8 giờ tối ngày 27 tháng 2 năm 2026"

# 1: Meeting topic
trans_map[cn_texts[1]] = "Chủ đề cuộc họp: 02-27 | Hải Tân: Tôi đã tạo một không gian làm việc trực quan cho Tôm Hùm WaytoAGI Học chung lúc 8 giờ tối"

# 2: Meeting time
trans_map[cn_texts[2]] = "Thời gian cuộc họp: Ngày 27 tháng 2 năm 2026 (Thứ Sáu) 19:55 - 21:05 (GMT+08)"

# 3: 回放
trans_map[cn_texts[3]] = "Phát lại"

# 4: PPT
trans_map[cn_texts[4]] = "PPT của Hải Tân A Văn:"

# 5: 直播回放
trans_map[cn_texts[5]] = "Phát lại livestream:"

# 6: 总结
trans_map[cn_texts[6]] = "Tóm tắt"

# 7: Summary paragraph
trans_map[cn_texts[7]] = "Cuộc họp lần này xoay quanh Tôm Hùm - một agent đang rất hot. Leo đã chia sẻ kinh nghiệm và các trường hợp sử dụng Tôm Hùm, Hải Tân và A Văn trình bày dự án xây dựng văn phòng trực tuyến cho Tôm Hùm, ngoài ra còn thảo luận về lựa chọn mô hình, mẹo sử dụng và giá trị ứng dụng của Tôm Hùm. Nội dung như sau:"

# 8-9: Bullet headers
trans_map[cn_texts[8]] = "Tổng quan và trải nghiệm sử dụng Tôm Hùm"
trans_map[cn_texts[9]] = "Đặc điểm và mức độ phổ biến của Tôm Hùm"

# 10: Evolution ability
trans_map[cn_texts[10]] = "Khả năng tiến hóa độc đáo: Leo cho biết Tôm Hùm là agent hot nhất năm 2026, tác giả đã thiết lập nó như một sinh vật có thể tiến hóa. Nó có thể ghi nhớ lời người dùng nói, khi có điều kiện mới kích hoạt sẽ chạy lại lịch sử, điều này khác với các agent trước đây, mang đến cảm giác mới mẻ cho người dùng."

# 11: Surpassing other products
trans_map[cn_texts[11]] = "Vượt xa các sản phẩm khác: Mức độ phổ biến của nó vượt xa các sản phẩm đã có lợi nhuận như Manus, Claude code, Leo cho rằng năm nay không dùng Tôm Hùm thì không tính là người trong giới AI, khuyến khích mọi người thử."

# 12: Installation
trans_map[cn_texts[12]] = "Cài đặt và cấu hình Tôm Hùm"

# 13: Installation cost
trans_map[cn_texts[13]] = "Chi phí và thời gian cài đặt: Tôm Hùm của Leo được cài trên một chiếc Mac mini trị giá 6000 nhân dân tệ, việc cài đặt mất hai ngày."

# 14: Model selection
trans_map[cn_texts[14]] = "Lựa chọn mô hình: Tôm Hùm rất kén chọn mô hình, Claude code 4.6 là lựa chọn tốt hơn, nếu không sử dụng được, các mô hình trong nước như Kimi, Minimax, Zhipu GLM 5 cũng là phương án thay thế. Trong đó, Minimax giá rẻ, mô hình M2.5 còn có thể chạy cục bộ, phù hợp cho người mới bắt đầu."

# 15: Avoid changing models
trans_map[cn_texts[15]] = "Tránh tự đổi mô hình: Để Tôm Hùm tự đổi mô hình dễ khiến nó bị treo, khuyến nghị người dùng tự thao tác thủ công."

# 16: Functions
trans_map[cn_texts[16]] = "Chức năng và các trường hợp ứng dụng của Tôm Hùm"

# 17: Web browsing
trans_map[cn_texts[17]] = "Lướt web và thu thập thông tin: Sau khi cài plugin Browser wind, Tôm Hùm có khả năng lướt web, có thể mở trình duyệt Chrome để tìm kiếm, thu thập thông tin, còn có thể tự động xem tin tức trên 36Kr và tóm tắt, lọc thông tin nhiễu."

# 18: Podcast
trans_map[cn_texts[18]] = "Tạo podcast: Tôm Hùm có thể sử dụng API podcast trong list Tab để tạo podcast, tự động chọn giọng nói, còn có thể đặt tác vụ định thời, hàng ngày đẩy bản tin podcast buổi sáng."

# 19: Drawing & voice
trans_map[cn_texts[19]] = "Vẽ tranh và nhận dạng giọng nói: Sau khi cài mô hình stable diffusion cục bộ, Tôm Hùm có khả năng vẽ tranh; thông qua sử dụng mô hình Gemini, có thể đọc trực tiếp giọng nói, kết hợp các kỹ năng TTS, vẽ tranh, làm podcast trong list Hub, dùng âm thanh và hình ảnh để thể hiện ý tưởng."

# 20: Disadvantages
trans_map[cn_texts[20]] = "Nhược điểm và nguyên tắc sử dụng Tôm Hùm"

# 21: Easy to crash
trans_map[cn_texts[21]] = "Dễ bị treo: Tôm Hùm phụ thuộc vào mạng và mô hình ổn định, dễ bị treo, và khi tự tiến hóa cũng thường thất bại."

# 22: Memory issues
trans_map[cn_texts[22]] = "Vấn đề trí nhớ: Tuy có khả năng ghi nhớ nhưng thường xuyên quên việc, cần người dùng nhắc nhở."

# 23: Usage principle
trans_map[cn_texts[23]] = "Nguyên tắc sử dụng: Leo khuyến nghị người dùng không cần suy nghĩ Tôm Hùm có thể làm được hay không, nên giao tất cả nhiệm vụ cho nó, sẽ nhận được nhiều bất ngờ."

# 24-31: Office project section
trans_map[cn_texts[24]] = "Chia sẻ dự án Văn phòng Tôm Hùm"
trans_map[cn_texts[25]] = "Bối cảnh dự án và nguồn cảm hứng"
trans_map[cn_texts[26]] = "Trải nghiệm trò chuyện không tốt: Lý Hạo Văn cho biết, người không có nền tảng lập trình gặp khó khăn khi dùng dòng lệnh để trò chuyện với Tôm Hùm, khi trò chuyện trên Feishu hoặc Telegram, Tôm Hùm không trả lời tin nhắn khiến người dùng không chắc chắn về trạng thái của nó, trải nghiệm không trực quan."
trans_map[cn_texts[27]] = "Cảm hứng tham khảo: Lấy cảm hứng từ một dự án plugin của Claude code, họ quyết định xây dựng một văn phòng trực tuyến cho Tôm Hùm để hiển thị trạng thái của nó."
trans_map[cn_texts[28]] = "Quá trình thực hiện dự án"
trans_map[cn_texts[29]] = "Trao đổi nhu cầu: Lý Hạo Văn trước tiên thảo luận với Tôm Hùm, xác định nhu cầu là tạo một bảng trạng thái phong cách pixel, chiếu trạng thái của Tôm Hùm thành hoạt hình và cảnh, đồng thời để Tôm Hùm tóm tắt trạng thái hàng ngày của nó, phân chia các khu vực chức năng."
trans_map[cn_texts[30]] = "Triển khai chức năng: Tôm Hùm đã thực hiện toàn bộ dự án, bao gồm vẽ giao diện văn phòng, cung cấp liên kết công khai, triển khai tên miền, v.v. Lý Hạo Văn còn cung cấp các phòng mẫu phong cách khác nhau, thông qua Feishu để Tôm Hùm thay đổi nền."
trans_map[cn_texts[31]] = "Hiệu quả và phản hồi dự án"
trans_map[cn_texts[32]] = "Hiển thị trạng thái trực quan: Thông qua giao diện văn phòng, có thể nhìn thấy trực quan trạng thái của Tôm Hùm, như nghỉ ngơi, làm việc, báo lỗi, v.v., tránh người dùng phải hỏi liên tục."
trans_map[cn_texts[33]] = "Phản hồi cộng đồng tốt: Sau khi dự án mã nguồn mở, lượt xem trên Twitter vượt 100.000, trên GitHub có hơn 120 sao, nhận được nhiều phản hồi tích cực từ cộng đồng, mọi người cho rằng dự án này khiến AI thân thiện hơn với người bình thường, cung cấp giá trị cảm xúc."

# 34-38: Design section
trans_map[cn_texts[34]] = "Tư duy thiết kế và kỹ thuật dự án"
trans_map[cn_texts[35]] = "Xử lý phần tử: A Văn giới thiệu, biến hình ảnh do Nano Banana tạo trở lại phòng thô, trích xuất phần tử nội thất, thu được hình PNG độc lập."
trans_map[cn_texts[36]] = "Tạo nhân vật và làm hoạt hình: Chuyển đổi avatar Tôm Hùm thành hình ảnh phong cách pixel 16x16, mở rộng các động tác và trạng thái biểu cảm khác nhau, thông qua VO 3.1 tạo video, sau đó dùng honeycam xử lý thành GIF trong suốt."
trans_map[cn_texts[37]] = "Ứng dụng sprite sheet: Tôm Hùm chuyển GIF thành sprite sheet để tải lên, A Văn lấy cảm hứng từ đây, áp dụng định dạng sprite sheet cho các phần tử khác, thực hiện chuyển đổi trạng thái nội thất tùy ý."
trans_map[cn_texts[38]] = "Chia sẻ tài nguyên: Lý Hạo Văn chia sẻ thư viện thành phần mã nguồn mở Lynx và tài nguyên AI Town, v.v., có thể lấy miễn phí tài nguyên pixel và cách chơi nhân vật AI."

# 39-54: Other content and planning
trans_map[cn_texts[39]] = "Các nội dung liên quan khác về việc sử dụng Tôm Hùm"
trans_map[cn_texts[40]] = "Cơ chế sử dụng nhiều người"
trans_map[cn_texts[41]] = ": Leo đề cập, gửi ID Telegram của Tôm Hùm cho bạn bè có thể chơi cùng, nhưng sẽ xuất hiện vấn đề rối loạn trí nhớ. Có thể để Tôm Hùm thiết kế cơ chế ủy quyền, bạn bè cần sao chép mã do Tôm Hùm gửi cho chủ nhân, sau khi chủ nhân phê duyệt bạn bè mới có thể giao tiếp với Tôm Hùm."
trans_map[cn_texts[42]] = "Ứng dụng Feishu và giới hạn API"
trans_map[cn_texts[43]] = "Feishu hỗ trợ: Trương Nghiễn cho biết Feishu hỗ trợ ứng dụng Tôm Hùm, Leo dự định thử kết hợp Feishu và Volcengine, và xem xét viết bài hướng dẫn mọi người bắt đầu một cách đơn giản."
trans_map[cn_texts[44]] = "Đăng ký API: Trong dịp Tết Nguyên đán phát hiện việc sử dụng Tôm Hùm trên Feishu trong nước có giới hạn API, đã mở đăng ký API không giới hạn, liên kết đăng ký sẽ được gửi vào nhóm, kích hoạt trong vòng 24 giờ."
trans_map[cn_texts[45]] = "Giá trị ứng dụng và chi phí dự án"
trans_map[cn_texts[46]] = "Giá trị sử dụng: Lý Hạo Văn cho rằng sự hỗ trợ trực tiếp của dự án đối với công việc hàng ngày chủ yếu là cung cấp trạng thái trực quan của Tôm Hùm, cho phép người dùng nắm bắt tình hình làm việc của nó, thân thiện hơn với người dùng không thuộc ngành code, tương lai có thể nâng cấp thành giao diện trò chuyện trực tiếp, truy vấn tệp Feishu, v.v."
trans_map[cn_texts[47]] = "Tình hình chi phí: Hiện tại API của dự án tiêu thụ khoảng 5 USD mỗi ngày, chi phí nuôi một Tôm Hùm khoảng 30 nhân dân tệ, có thể chọn gói API hàng tháng coding plan của Volcengine."
trans_map[cn_texts[48]] = "Kế hoạch công việc tiếp theo"
trans_map[cn_texts[49]] = "Cải tiến dự án"
trans_map[cn_texts[50]] = ": Lý Hạo Văn và A Văn dự định fork một phiên bản trang trí tải lên GitHub để mọi người tham khảo, có thể sẽ thêm API của Nano và mở cho mọi người."
trans_map[cn_texts[51]] = "Chia sẻ kinh nghiệm"
trans_map[cn_texts[52]] = ": Leo xem xét viết bài hướng dẫn mọi người bắt đầu ứng dụng Tôm Hùm một cách đơn giản."
trans_map[cn_texts[53]] = "Giải đáp thắc mắc"
trans_map[cn_texts[54]] = ": AJ sau khi hạ cánh sẽ chia sẻ phát lại cuộc họp, các bạn trong cộng đồng hỗ trợ hướng dẫn trả lời các câu hỏi trong nhóm."

# 55: Smart chapters heading
trans_map[cn_texts[55]] = "Chương thông minh"

# 56-57: Opening
trans_map[cn_texts[56]] = "  Khai mạc"
trans_map[cn_texts[57]] = "Khai mạc"

# 58-85: Smart chapter titles and summaries
trans_map[cn_texts[58]] = '  Trải nghiệm sử dụng Tôm Hùm "Quất Bảo", vấn đề và khoảnh khắc tỏa sáng đầu tiên'
trans_map[cn_texts[59]] = 'Trong chương này, Leo chia sẻ trải nghiệm sử dụng "Tôm Hùm" (orange bot Quất Bảo), cài đặt trên Mac mini tốn 6000 nhân dân tệ và hai ngày, thay đổi file cấu hình và tự đổi mô hình dễ bị treo. Còn đề cập Gateway thường xuyên treo, dự định thử nền tảng Volcengine. Lần đầu tiên anh chạy thành công với GLM 4.7, Tôm Hùm có thể ghi nhớ thông tin, xử lý lịch sử sau khi kích hoạt điều kiện, một lần gửi 5 tin nhắn, biểu hiện "hướng ngoại" này khiến anh - một người "hướng nội" - cảm thấy rất tốt.'

trans_map[cn_texts[60]] = "  Chức năng và ưu thế ứng dụng của AI Agent Tôm Hùm đang bùng nổ năm 2026"
trans_map[cn_texts[61]] = 'Trong chương này, Leo giới thiệu agent "Tôm Hùm" hot nhất năm 2026, cho biết cảm giác sử dụng khác với các sản phẩm AI trước đây, giống như thú cưng có thể tiến hóa. Anh đề cập việc cài plugin Browser wind cho Tôm Hùm, giúp nó có thể lướt web, tìm kiếm, tóm tắt tin tức, còn có thể lọc nhiễu. Ngoài ra, Tôm Hùm có thể sử dụng API của list Tab để tạo hình ảnh, podcast, và có thể đặt tác vụ định thời, thu thập thông tin website một cách hợp pháp.'

trans_map[cn_texts[62]] = "  Lựa chọn mô hình, sử dụng và chia sẻ đặc tính của Tôm Hùm"
trans_map[cn_texts[63]] = "Trong chương này, Leo chia sẻ nội dung liên quan đến Tôm Hùm. Về lựa chọn mô hình, đề xuất Claude code, nếu không sử dụng được, có thể cân nhắc Kimi, Minimax, Zhipu GLM 5 trong nước. Còn giới thiệu cấu hình Tôm Hùm, cách chơi chia sẻ với bạn bè, kết nối nền tảng, v.v. Nhấn mạnh tầm quan trọng của plugin, như Crawley crawler. Ngoài ra, đề cập kỹ năng của Tôm Hùm, đặc điểm file soul, chỉ ra rằng nó khác với các agent trước đây, có năng lực và có sự gắn kết, còn không khuyến nghị dùng một phần mềm nào đó."

trans_map[cn_texts[64]] = "  Chia sẻ ưu nhược điểm của Tôm Hùm và trải nghiệm sử dụng, chia sẻ bàn giao tiếp theo"
trans_map[cn_texts[65]] = "Trong chương này, Leo chia sẻ ưu nhược điểm của Tôm Hùm. Nhược điểm là dễ treo, phụ thuộc mạng ổn định, tiến hóa thường thất bại, còn hay quên. Ưu điểm là đáng chơi, là bổ sung cho flowcode, tự mang khả năng coding khá mạnh, có thể mang đến cảm giác bất ngờ, khá có tình người, nhiều người nuôi sinh ra tình cảm. Sau đó Leo hỏi Lý Hạo Văn bug đã sửa xong chưa, rồi chuyển phần chia sẻ cho An Hải Tân và A Văn."

trans_map[cn_texts[66]] = "  Chia sẻ thực hành tương tác với Tôm Hùm và nguồn cảm hứng văn phòng trực tuyến"
trans_map[cn_texts[67]] = 'Trong chương này, Lý Hạo Văn chia sẻ thực hành skill với các "phụ huynh" Tôm Hùm, hỏi mọi người cách trò chuyện với Tôm Hùm, đề cập thường thấy qua dòng lệnh, Telegram, Feishu, cho rằng dòng lệnh không thân thiện với người không có nền tảng lập trình. Điều thu hút họ chơi Tôm Hùm là khả năng tích hợp trên Telegram và Feishu. Nhưng trò chuyện trên Feishu không trực quan, nên muốn làm văn phòng trực tuyến cho Tôm Hùm, cảm hứng từ một plugin của Claude code.'

trans_map[cn_texts[68]] = "  Openclaw thực hiện giao diện game hóa và nhận được sự quan tâm cao"
trans_map[cn_texts[69]] = "Chương này chủ yếu kể về Lý Hạo Văn lấy cảm hứng từ một dự án, thử làm giao diện game hóa cho Openclaw. Anh giao tiếp với Openclaw trên cloud qua Feishu, đề xuất ý tưởng làm giao diện UI phong cách pixel, Openclaw xác nhận nhu cầu và cho biết có thể thực hiện, còn liệt kê trạng thái, vẽ giao diện, hoàn thành logic. Lý Hạo Văn cung cấp phòng mẫu, trình diễn demo chạy. Kết quả cuối cùng hoàn thành đơn giản, còn triển khai lên mạng công cộng, lượt xem trên Twitter vượt 100.000, anh cũng đã mã nguồn mở các skill liên quan."

trans_map[cn_texts[70]] = "  Dự án GitHub nhận phản hồi tích cực, cộng đồng sáng tạo mở rộng cách chơi"
trans_map[cn_texts[71]] = "Trong chương này, Lý Hạo Văn giới thiệu tình hình dự án, dự án có hơn 120 sao trên GitHub, nhận được nhiều phản hồi từ cộng đồng, mọi người cho rằng nó dễ thương, trực quan và cung cấp giá trị cảm xúc. Sau khi mã nguồn mở kho lưu trữ, cộng đồng mạng triển khai và chỉnh sửa cục bộ, có các phiên bản văn phòng Tôm Hùm phong cách khác nhau, còn tích hợp với các nền tảng khác, thậm chí trên nền tảng đó làm loạt multi-agent, thể hiện sức sáng tạo mạnh mẽ."

trans_map[cn_texts[72]] = "  Lý Hạo Văn giới thiệu cài đặt đặc sắc của văn phòng sau khi nâng cấp dự án"
trans_map[cn_texts[73]] = "Trong chương này, Lý Hạo Văn giới thiệu tiến triển dự án, cho biết sau khi A Văn tham gia dự án trở nên ấn tượng. Anh trình diễn văn phòng sau nâng cấp, giới thiệu vật trang trí Tôm Hùm có tên Bảo Thạch Hải Tân, mô tả biểu hiện của nó ở các trạng thái làm việc khác nhau, như nghỉ ngơi, làm việc, đồng bộ tệp, báo bug, v.v. Còn đề cập nhiều chi tiết A Văn làm, như thực vật, poster, mèo và các phần tử khác đều có thể nhấp và liên tục chuyển đổi."

trans_map[cn_texts[74]] = "  Demo trò chuyện với Tôm Hùm và thiết lập nhiệm vụ kiểm tra tình hình phản hồi"
trans_map[cn_texts[75]] = 'Trong chương này, Lý Hạo Văn cho biết sẽ demo thực tế tình hình trò chuyện với Tôm Hùm. Anh gửi tin nhắn cho Tôm Hùm qua điện thoại, hiển thị cửa sổ đối thoại với Tôm Hùm, cửa sổ này được làm thành trạng thái robot Feishu. Anh thiết kế nhiệm vụ cho Tôm Hùm, cứ hai giờ hỏi A Văn tình hình công việc. Sau đó anh gửi "hello" để kiểm tra, gặp giật lag và Tôm Hùm không phản hồi, anh dự định gửi tin nhắn cho Tôm Hùm từ điện thoại.'

trans_map[cn_texts[76]] = "  Chia sẻ thiết kế ngôi nhà và mẹo sử dụng Open Call qua Feishu"
trans_map[cn_texts[77]] = "Trong chương này, Lý Hạo Văn (A Văn) chia sẻ tình hình thiết kế ngôi nhà. Anh đề cập sẽ tìm màn hình để hiển thị nội dung công việc theo thời gian thực. Còn chỉ ra việc gọi open call trên Feishu có độ trễ, và khi ngữ cảnh mở rộng độ trễ tăng nặng, ví dụ thay thế hình ảnh nửa tiếng không phản hồi. Anh chia sẻ mẹo, khi ngữ cảnh hộp thoại quá dài có thể mở cửa sổ chat mới để nó đọc lại dự án. Phía sau dùng là 5.3 CODEX, nó hỗ trợ ngữ cảnh tốt, có thể nhanh chóng định vị và sửa lỗi."

trans_map[cn_texts[78]] = "  Chia sẻ cách làm hoạt hình Nano Banana và tư duy thay thế phần tử biệt thự"
trans_map[cn_texts[79]] = "Trong chương này, Lý Hạo Văn chia sẻ cách thêm hoạt hình nhỏ, trước tiên biến phòng hoàn thiện trở lại thô, trích xuất phần tử thành PNG độc lập. Tạo nhân vật phong cách pixel, dùng Nano Banana mở rộng động tác rồi tạo video, sau đó dùng honeycam xử lý thành GIF trong suốt dung lượng nhỏ. Sử dụng chức năng hiển thị tọa độ của Tôm Hùm để định vị vị trí tài nguyên. Còn giới thiệu ứng dụng sprite sheet và phương pháp thay thế, kế hoạch tiếp theo để Tôm Hùm tự thiết kế, kết nối API tăng tốc cải tiến."

trans_map[cn_texts[80]] = "  Chia sẻ tài nguyên chất liệu dự án và tình hình phát triển ứng dụng AI"
trans_map[cn_texts[81]] = "Trong chương này, Lý Hạo Văn chia sẻ tài nguyên được tặng trong quá trình dự án. Một là thư viện thành phần mã nguồn mở Lynx, có tài nguyên pixel miễn phí, nhưng quy định bản quyền sử dụng cần tự tra cứu; hai là dự án GitHub AI Town do A16z phát hành, có tài nguyên pixel và cách chơi nhân vật AI. Anh còn đề cập vì Openclue có thể sử dụng cục bộ, có thể cho AI kết nối vào game, và mô hình GPT 5.3 code s năng lực mạnh, vượt xa GPT 5.2."

trans_map[cn_texts[82]] = "  Chia sẻ dự án Tôm Hùm, trải nghiệm sử dụng và giải đáp các vấn đề liên quan"
trans_map[cn_texts[83]] = "Chương này chủ yếu xoay quanh dự án Tôm Hùm để trao đổi. Trương Nghiễn chia sẻ trải nghiệm sử dụng, cho rằng nó thuận tiện thú vị và kết nối với môi trường làm việc thực tế, còn đề cập việc sử dụng Feishu trong nước gặp giới hạn API đã mở đăng ký không giới hạn. Lý Hạo Văn bổ sung địa chỉ dự án là star-office-ui, nền tảng truyền thông xã hội có liên kết GitHub, tiếp theo sẽ tải lên phiên bản trang trí để tham khảo, còn có thể thêm API của Nano."

trans_map[cn_texts[84]] = "  Chức năng ứng dụng, chi phí và trao đổi chia sẻ dự án Tôm Hùm"
trans_map[cn_texts[85]] = "Chương này thảo luận xoay quanh một dự án. Đề cập dự án không giúp ích nhiều cho công việc của Ông Trác, chủ yếu có chức năng trực quan hóa, cho phép mọi người nắm bắt trạng thái agent. Hướng cải tiến tiếp theo bao gồm trò chuyện với agent trên giao diện, tra cứu tệp, v.v. Còn bàn về chi phí, ý tưởng kết nối nhiều agent, v.v. Cuối cùng giới thiệu chi phí nuôi Tôm Hùm, hoan nghênh trao đổi, fork dự án, sau khi cuộc họp kết thúc sẽ chia sẻ phát lại."

# 86-92: Golden quotes, related links, etc.
trans_map[cn_texts[86]] = "Những câu nói hay trong cuộc họp"
trans_map[cn_texts[87]] = "Liên kết liên quan"
trans_map[cn_texts[88]] = "Ghi chú thông minh: "
trans_map[cn_texts[89]] = "02-27 | Hải Tân: Tôi đã tạo một không gian làm việc trực quan cho Tôm Hùm WaytoAGI Học chung lúc 8 giờ tối"
trans_map[cn_texts[90]] = "Bản ghi văn bản"
trans_map[cn_texts[91]] = "02-27 | Hải Tân: Tôi đã tạo một không gian làm việc trực quan cho Tôm Hùm WaytoAGI Học chung lúc 8 giờ tối ngày 27 tháng 2 năm 2026"
trans_map[cn_texts[92]] = "Biên bản cuộc họp liên quan"

# ===== MEETING NOTES (indices 93+) - use programmatic translation =====
for i in range(93, len(cn_texts)):
    text = cn_texts[i]
    trans_map[text] = translate_meeting_note(text)

# Additional specific translations for common patterns in meeting notes
# These are mostly handled by translate_meeting_note already

# Save the map
with open('_art23_trans_map.json', 'w', encoding='utf-8') as f:
    json.dump(trans_map, f, ensure_ascii=False, indent=2)

print(f"Built translation map with {len(trans_map)} entries")
print(f"Total CN texts: {len(cn_texts)}")
print(f"Coverage: {len(trans_map)}/{len(cn_texts)} ({100*len(trans_map)/len(cn_texts):.1f}%)")
