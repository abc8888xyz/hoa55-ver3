# -*- coding: utf-8 -*-
import sys, json, copy
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

with open('art1_original.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

translated = copy.deepcopy(data)

# Translation map: (block_idx, element_idx) -> Vietnamese text
T = {}
T[(0,0)] = "Dùng OpenClaw xây dựng đội ngũ TMĐT xuyên biên giới: 5 nhân viên AI, chạy thông ma trận đa nền tảng!"
T[(1,0)] = "\U0001f517 Link bài gốc: "
# 1,1 is URL - keep
T[(2,0)] = "Nguyên tác Binggan Gege Binggan Gege Binggan Gege AGI"
T[(2,1)] = "Ngày 2 tháng 3 năm 2026 10:48  Mỹ"
T[(3,0)] = "Tôi đã triển khai OpenClaw trên Mac mini tại local, sau đó thiết kế một Multi Agent Team: "
T[(3,1)] = "5 nhân viên số AI độc lập, trực tiếp tiếp quản việc nghiên cứu chọn sản phẩm TMĐT xuyên biên giới, tạo video UGC TikTok, thu hút lưu lượng qua Reddit và vận hành Amazon."
T[(4,0)] = "Trước đây một team làm cả tuần, giờ chỉ trong thời gian uống một ly cà phê, 5 Agent này đã tự động chạy xong ở nền."
T[(5,0)] = "Hôm nay chia sẻ toàn bộ kiến trúc nền tảng, logic phối hợp và hướng dẫn cấu hình Lark chi tiết từ A-Z của bộ \"dây chuyền xuyên biên giới đa Agent\" này, xem xong có thể áp dụng ngay."
T[(6,0)] = "Cuối bài đính kèm các câu hỏi thường gặp về cấu hình multi agent."
# 7,0 = "01" - keep
T[(8,0)] = "5 nhân viên cốt lõi này là ai?"
T[(9,0)] = "Tổng quản (lead) "
T[(9,1)] = ": Đầu mối duy nhất giao tiếp với con người trên Lark, chịu trách nhiệm phân tích yêu cầu, gọi sessions_send để phân phối nhiệm vụ xuyên node."
T[(10,0)] = "Chuyên viên phân tích thị trường VOC (voc-analyst) "
T[(10,1)] = ": Thu thập dữ liệu đánh giá trên toàn mạng, trích xuất pain point của người dùng và điểm yếu của đối thủ."
T[(11,0)] = "Chuyên viên tối ưu nội dung GEO (geo-optimizer) "
T[(11,1)] = ": Chịu trách nhiệm viết nội dung cho Amazon và website độc lập."
T[(12,0)] = "Chuyên gia marketing Reddit (reddit-spec) "
T[(12,1)] = ": Chịu trách nhiệm thực hiện quy trình SOP nuôi tài khoản nghiêm ngặt trong 5 tuần. Lặn lội, tương tác tại các board chính xác như r/BuyItForLife, r/SkincareAddiction."
T[(13,0)] = "Biên đạo video hot TikTok (tiktok-director) "
T[(13,1)] = ": Chịu trách nhiệm phân tích logic video trending trên TikTok."
T[(14,0)] = "Sau khi cấu hình xong, đại khái trông như thế này"
# 15,0 = "02" - keep
T[(16,0)] = "Logic phối hợp đa Agent: Họ phối hợp với nhau như thế nào?"
T[(17,0)] = "Mô hình AI đơn thể truyền thống không giải quyết được vấn đề chuỗi dài, dễ xuất hiện \"ảo giác công cụ\". Kiến trúc OpenClaw sử dụng logic \"máy trạng thái bất đồng bộ\", phân tách các nghiệp vụ xuyên biên giới phức tạp thành dây chuyền sản xuất."
T[(18,0)] = "Ví dụ: Quảng bá một chiếc giường gấp cắm trại"
T[(19,0)] = "Kích hoạt nhiệm vụ "
T[(19,1)] = ": Trong group Lark @Tổng quản: \"Phân tích thị trường giường gấp cắm trại và triển khai nội dung đa kênh.\""
T[(20,0)] = "Phân tích VOC "
T[(20,1)] = ": Tổng quản chuyển lệnh cho voc-analyst. Nó tự động thu thập đánh giá tiêu cực của đối thủ trên Amazon, đưa ra kết luận: \"Pain point của người dùng là khả năng chịu tải không đủ và gập lại bất tiện.\""
T[(21,0)] = "Đầu ra tối ưu GEO "
T[(21,1)] = ": Dữ liệu được đồng bộ cho geo-optimizer. Nó viết blog sản phẩm cho website độc lập, để phù hợp với các công cụ tìm kiếm AI như ChatGPT, bổ sung dữ liệu định lượng cụ thể như \"chịu tải 450 pound\" vào bài viết, đồng thời trích dẫn rõ ràng nguồn đánh giá từ các website outdoor uy tín."
T[(22,0)] = "Chiếm lưu lượng Reddit "
T[(22,1)] = ": Tổng quản đồng thời đánh thức reddit-spec. Nó lên Google tìm các bài cũ, tìm những bài thảo luận liên quan có thứ hạng cao. Bình luận chân thành dưới các bài cũ, giới thiệu sản phẩm mới của chúng ta, nhấn mạnh rằng nó đã giải quyết các pain point của phiên bản cũ, thành công chiếm lưu lượng long-tail."
T[(23,0)] = "Tạo video ngắn TikTok "
T[(23,1)] = ": Tổng quản gọi tiktok-director. Nó trực tiếp đọc pain point từ VOC, sử dụng Seed 2.0 tạo storyboard lưới 25 ô. Nó thiết kế chính xác 2 giây đầu với góc quay góc nhìn thứ nhất cầm tay có \"cảm giác thở\". Nó còn thiết kế cảnh cận cảnh nhấn đệm ở giây thứ 4, thể hiện rõ ràng khả năng đàn hồi và lực đỡ."
T[(24,0)] = "Cuối cùng, nó gọi nano-banana-pro để tạo hình, dùng skill seedance2.0 tạo video bán hàng 15 giây mang đậm chất UGC"
# 24,1 = "." - keep
T[(25,0)] = "Toàn bộ quy trình được xuyên suốt bất đồng bộ qua sessions_send ở tầng nền, con người chúng ta chỉ cần phê duyệt trên Lark."
# 26,0 = "03" - keep
T[(27,0)] = "Hướng dẫn cấu hình Lark từ 0 đến 1"
T[(28,0)] = "Trước hết, để chạy thông bộ phối hợp này trên local, cốt lõi nằm ở việc cách ly routing và cho phép giao tiếp của OpenClaw."
T[(29,0)] = "Cách ly vật lý workspace "
T[(29,1)] = ": Mỗi Agent phải có Workspace độc lập riêng. Báo cáo nghiên cứu thị trường của voc-analyst tuyệt đối không được trộn lẫn với nhật ký nuôi tài khoản của reddit-spec trong cùng một thư mục."
T[(30,0)] = "Routing kết nối dài đa tài khoản "
T[(30,1)] = ": Tạo 5 ứng dụng độc lập trên nền tảng mở Lark, sử dụng kết nối dài WebSocket. Thông qua mảng bindings trong openclaw.json, route chính xác accountId của Lark đến Agent local tương ứng."
T[(31,0)] = "Giao thức truyền thông tầng nền A2A "
T[(31,1)] = ": Phải bật whitelist trong tools.agentToAgent, đây là \"bus dữ liệu duy nhất\" cho phép Tổng quản ra lệnh từ nền."
T[(32,0)] = "Tiếp theo xem cách thực hiện cụ thể."
T[(33,0)] = "Bước 1: Xây dựng cấu trúc file"
T[(34,0)] = "Trong thư mục ~/.openclaw/ của bạn, tạo cấu trúc như sau:"
T[(35,0)] = "Bước 2: File cấu hình cốt lõi openclaw.json"
T[(36,0)] = "Đảm bảo routing đa tài khoản Lark và giao tiếp Agent đã được kết nối:"
T[(37,0)] = "Tham khảo "
T[(37,1)] = "cấu hình Lark trong bài viết trước "
T[(37,2)] = ", bạn cần bao nhiêu agent thì tạo bấy nhiêu ứng dụng, phần này rất đơn giản chỉ là lặp lại."
T[(38,0)] = "Sau đó ghi appid, app secret v.v. của ứng dụng vào file config."
T[(39,0)] = "Bước 3: Trao \"linh hồn\" cho AI (viết file nhân vật)"
T[(40,0)] = "Đây là yếu tố quyết định AI có làm việc được hay không. Copy trực tiếp:"
T[(41,0)] = "AGENTS.md của Tổng quản (danh bạ team)"
T[(42,0)] = "SOUL.md của Chuyên viên tối ưu GEO"
T[(43,0)] = "SOUL.md của Biên đạo TikTok"
T[(44,0)] = "Bước cuối cùng"
T[(45,0)] = "Cài đặt thư viện skill nano-banana-pro và seedance2.0 vào thư mục skills toàn cục trên local."
T[(46,0)] = "Chạy lệnh openclaw gateway restart trong terminal, kéo 4 bot Lark đã cấu hình vào một group, tag Tổng quản."
T[(47,0)] = "Chỉ cần chạy qua một lần cấu hình này, máy in tiền TMĐT xuyên biên giới tự động của bạn chính thức khởi động."
# 48,0 = "04" - keep
T[(49,0)] = "Các câu hỏi thường gặp về đa Agent"
T[(50,0)] = "Bài viết OpenClaw trước "
T[(50,1)] = ", có bạn đặt câu hỏi về đa Agent, vừa hay bài hôm nay có thể giải đáp một số."
T[(51,0)] = "Tiếp theo, trả lời thêm một số câu hỏi cụ thể."
T[(52,0)] = "Q1: Thiết kế Agent: Theo nền tảng hay theo chức năng?"
T[(53,0)] = "Kết luận: Định hướng chức năng (Role-based) tốt hơn định hướng nền tảng."
T[(54,0)] = "Không nên cấu hình riêng một Agent cho mỗi nền tảng. Thiết kế tốt hơn là: "
T[(54,1)] = "Một \"giám đốc chiến lược nội dung\" chịu trách nhiệm đầu ra toàn cục, sau đó phân phối nhiệm vụ cho \"phân thân Xiaohongshu\" hoặc \"phân thân TikTok\" để điều chỉnh định dạng."
T[(55,0)] = "Như vậy có thể đảm bảo tính nhất quán của tone thương hiệu trên các nền tảng khác nhau, đồng thời tránh phải đào tạo lặp lại 5 \"thợ khuân vác\" không hiểu sản phẩm."
T[(56,0)] = "Đối với nhiệm vụ phát triển, còn có thể "
T[(56,1)] = "cân nhắc mô hình Squad, thực hiện trách nhiệm nghiệp vụ end-to-end."
T[(57,0)] = "Q2: Cấu hình model: Não dùng đắt, tay chân dùng rẻ"
T[(58,0)] = "Kết luận: Chiến lược phân cấp là giải pháp duy nhất vừa tiết kiệm vừa hiệu quả."
T[(59,0)] = "Tầng quyết định (Lead/Strategist): "
T[(59,1)] = "Bắt buộc dùng model cao cấp (như Claude 4.6), xử lý việc điều phối xuyên Agent phức tạp và độ sâu chọn đề tài."
T[(60,0)] = "Tầng thực thi (Researcher/Formatter): "
T[(60,1)] = "Dùng model hiệu quả chi phí cao (như Gemini 3 Flash, Kimi K2.5), xử lý thu thập web, làm sạch dữ liệu và điền Emoji, chi phí có thể giảm 90%."
T[(61,0)] = "Các Agent khác nhau có thể cấu hình các model khác nhau để vận hành, cụ thể thiết lập trong config."
T[(62,0)] = "Đồng thời, bổ sung một số kinh nghiệm xương máu khi cấu hình OpenClaw đa Agent trên Lark."
T[(63,0)] = "Q3: \"Ảo tưởng\" phát hành là có hiệu lực ngay trên quyền Lark"
T[(64,0)] = "Nói đơn giản là nhất định phải "
T[(64,1)] = "tạo phiên bản mới và gửi yêu cầu phát hành, thay đổi mới có hiệu lực."
T[(65,0)] = "Q4: \"Cơ chế song song sáng-tối\": Giải quyết việc bot tag nhau không hoạt động"
T[(66,0)] = "Do Lark chính thức có cơ chế "
# 66,1 = "Bot-to-Bot Loop Prevention " - keep (English)
T[(66,2)] = "(Phòng ngừa vòng lặp bot), Agent A tag @Agent B trong group, nhưng backend của Agent B không nhận được push."
T[(67,0)] = "Vì vậy nếu bạn muốn xem hoạt động của bot trên Lark, có thể cấu hình:"
T[(68,0)] = "Q5: Bẫy \"cách ly phân cấp\" của Skill"
T[(69,0)] = "Trước đó phát hiện, Skill do Tổng quản tạo nằm ở thư mục gốc, còn của nhân viên cấp dưới nằm trong Workspace riêng, thực chất là vấn đề thứ tự ưu tiên tải."
T[(70,0)] = "- Skill công cộng (tạo ảnh, tìm ảnh) "
T[(70,1)] = ": Phải đặt ở ~/.openclaw/skills/, đảm bảo gọi xuyên Agent không bị mất gói."
T[(71,0)] = "- Skill riêng tư (công cụ đăng bài cho tài khoản cụ thể) "
T[(71,1)] = ": Đặt trong thư mục skills riêng của Agent, có thể phòng ngừa hiệu quả việc Agent bị ảo giác công cụ, gọi nhầm API key của người khác."
T[(72,0)] = "Về cách chơi đa Agent của OpenClaw, mọi người còn câu hỏi gì không? Hoan nghênh tiếp tục bình luận."
T[(73,0)] = "Với TMĐT xuyên biên giới, cuộc cạnh tranh là ai có kiến trúc Agent ổn định hơn, chi phí thấp hơn. "
T[(74,0)] = "Về cách dùng AI để tăng cường TikTok, Amazon, thậm chí làm GEO qua Reddit, chúng tôi sẽ chia sẻ thực chiến tại "
T[(74,1)] = "Đại hội NGS AI Thương mại điện tử xuyên biên giới lần thứ nhất ngày 14 tháng 3 "
T[(74,2)] = "."
T[(75,0)] = "Đọc bài này bạn sẽ biết đại khái đại hội của chúng tôi sẽ nói về gì: "
T[(75,1)] = "2026, Logic tiếp thị nội dung xuyên biên giới đã thay đổi hoàn toàn"

# Apply translations
translated_count = 0
kept_count = 0
total_text = 0

for i, block in enumerate(translated['blocks']):
    for j, el in enumerate(block['elements']):
        if el['type'] == 'text_run':
            total_text += 1
            key = (i, j)
            if key in T:
                el['content'] = T[key]
                translated_count += 1
            else:
                kept_count += 1

with open('art1_translated.json', 'w', encoding='utf-8') as f:
    json.dump(translated, f, ensure_ascii=False, indent=2)

print(f"Total text segments: {total_text}")
print(f"Translated: {translated_count}")
print(f"Kept (URLs/numbers/English/unchanged): {kept_count}")
