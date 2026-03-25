# -*- coding: utf-8 -*-
"""Translate article 4: 70 real OpenClaw use cases"""
import sys, json, copy, re
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

with open('art4_original.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

translated = copy.deepcopy(data)

# Translation dictionary: (block_idx, element_idx) -> Vietnamese text
T = {}

# Page title
T[(0,0)] = "OpenClaw của bạn đang lén lút làm việc giúp bạn: Phân tích toàn diện 70 case thực tế"

# Meta info
T[(1,0)] = "🔗 Link bài gốc: "
T[(2,0)] = "Nguyên tác DracoVibeCoding DracoVibeCoding Draco đang VibeCoding"
T[(2,1)] = "Ngày 3 tháng 3 năm 2026 17:30  Sơn Tây"
T[(3,0)] = "Bài viết bao phủ 70 use case thực tế từ cộng đồng OpenClaw Moltbook, nguồn: "

# Table of contents
T[(4,0)] = "📋 Mục lục toàn bài"
T[(5,0)] = "Phân loại"
T[(6,0)] = "Số use case"
T[(7,0)] = "Case tiêu biểu"
T[(8,0)] = "🎙️ 1. Sáng tạo & chuyển đổi nội dung"
T[(9,0)] = "13 cái"
T[(10,0)] = "Biến Newsletter y học, bản tin Olympic hàng ngày — nhanh hơn báo giấy, mỗi ngày lúc 9 giờ sáng, bằng ngôn ngữ của bạn..."
T[(11,0)] = "🧠 2. Quản lý trí nhớ & kiến thức"
T[(12,0)] = "5 cái"
T[(13,0)] = "Hệ thống trí nhớ 3 tầng — phiên bản AI của \"trí nhớ dài\", bộ tái tạo đồ thị tri thức, lưu trữ trí nhớ theo tuần — phòng ngừa Token..."
T[(14,0)] = "🌙 3. Tự động hóa ban đêm"
T[(15,0)] = "11 cái"
T[(16,0)] = "7 Agent con chạy song song ban đêm, kiểm tra sức khỏe hạ tầng lúc 5 giờ sáng, tự động trả lời WhatsApp ban đêm..."
T[(17,0)] = "💰 4. Tài chính & Blockchain"
T[(18,0)] = "6 cái"
T[(19,0)] = "Giám sát sức khỏe bot giao dịch, thanh khoản tự động Uniswap V4, Bitcoin Inscription..."
T[(20,0)] = "📊 5. Phân tích dữ liệu & tình báo kinh doanh"
T[(21,0)] = "9 cái"
T[(22,0)] = "Ưu tiên GitHub Issue, thu thập chân dung người dùng X (Twitter), máy quét tín hiệu khách hàng..."
T[(23,0)] = "🔒 6. Bảo mật & tuân thủ"
T[(24,0)] = "9 cái"
T[(25,0)] = "Máy quét khóa SSH private, phát hiện bất thường log, bộ phân loại email tự động..."
T[(26,0)] = "📱 7. Trợ lý đời sống hàng ngày"
T[(27,0)] = "13 cái"
T[(28,0)] = "Khắc thơ haiku trên blockchain Bitcoin, \"lá số may mắn\" tiền mã hóa — với blockchain, đồng bộ trạng thái online đa nền tảng..."
T[(29,0)] = "🛠️ 8. Công cụ nhà phát triển"
T[(30,0)] = "4 cái"
T[(31,0)] = "Trình tạo Shell alias ban đêm, bộ công cụ CLI cá nhân, phát triển gói Swift Logger..."
T[(32,0)] = "💡 Mỗi use case đều có: "
T[(32,1)] = "Pain point hàng ngày của bạn → AI giải quyết thế nào → Case thực tế → Thành công trông như thế nào "
T[(32,2)] = ". Đọc theo sở thích, nhảy đoạn thoải mái!"

# Section 1
T[(33,0)] = "🎙️ Danh mục lớn thứ nhất: Sáng tạo & chuyển đổi nội dung (13 use case)"
T[(34,0)] = "Biến thông tin từ một hình thức thành hình thức phù hợp nhất cho bạn tiêu thụ. Logic cốt lõi: "
T[(34,1)] = "Giảm chi phí tiếp cận thông tin, bạn mới sẵn lòng tiêu thụ nó."

T[(35,0)] = "💊 Use case 01: Biến Newsletter y học thành podcast đi làm"
T[(37,0)] = "Đây là phiên bản chuyên nghiệp nhất trong tất cả use case \"email chuyển podcast\". Bác sĩ mỗi ngày nhận được hàng đống bản tin y học dày đặc, hoàn toàn không có thời gian đọc. AI phân tách từng câu chuyện trong email, truy vấn URL nhúng để lấy thêm bối cảnh, viết thành kịch bản podcast dạng hội thoại bằng ngôn ngữ dành cho bác sĩ chuyên khoa, dùng ElevenLabs tạo giọng nói, gửi qua Signal."
T[(38,0)] = "Chi tiết kỹ thuật: "
T[(38,1)] = "Nếu văn bản vượt quá 4000 chữ (giới hạn một lần của ElevenLabs), AI sẽ tự động chia thành nhiều đoạn, dùng ffmpeg ghép thành audio hoàn chỉnh, hoàn toàn tự động."
T[(39,0)] = "Tiêu chuẩn thành công: "
T[(39,1)] = "0 bước thao tác thủ công, thời lượng 5-7 phút, bác sĩ nghe xong trong 24 giờ."

T[(40,0)] = "🏅 Use case 02: Bản tin Olympic hàng ngày — nhanh hơn báo giấy"
T[(42,0)] = "Phóng viên thể thao và fan cần theo dõi lịch thi đấu và thành tích của nhiều vận động viên mỗi ngày. AI được thiết lập tự động tổng hợp mỗi sáng 7 giờ (giờ Roma): lịch thi đấu hôm nay của VĐV Ý, kết quả huy chương hôm qua, câu chuyện hot, gửi đến kênh Telegram thể thao chuyên dụng."
T[(43,0)] = "Case thực tế: "
T[(43,1)] = "Người dùng OttoIlRobotto dùng cái này để theo dõi đội Olympic Ý, AI đã bắt được tin nóng trước cả truyền thông chính thống — bao gồm một nữ VĐV phá kỷ lục lịch sử, một VĐV khúc côn cầu bị thương sau 25 giây khai mạc, và \"scandal máy bay riêng\" của một VĐV khác..."

T[(44,0)] = "⛅ Use case 03: Mỗi ngày 9 giờ sáng, báo thời tiết hôm nay bằng ngôn ngữ của bạn"
T[(46,0)] = "AI kết nối Yandex Weather API (có bản miễn phí, 50 request/ngày là đủ dùng), phân tích dữ liệu thời tiết theo 4 khung giờ sáng/trưa/chiều/tối, dịch sang ngôn ngữ bạn chỉ định, gửi đến Telegram."
T[(47,0)] = "Khả năng cá nhân hóa: "
T[(47,1)] = "Nếu nhiệt độ dưới -15°C, hoặc gió vượt 15m/s, hoặc có mưa trong giờ đi làm, AI sẽ gửi thêm một cảnh báo."

T[(48,0)] = "📡 Use case 20: Bộ tổng hợp tin tức RSS"
T[(50,0)] = "15 nguồn RSS tin công nghệ mỗi ngày đổ ra hàng trăm bài, cùng một sự kiện lớn có thể được đưa tin 40 lần. AI mỗi 4 giờ kéo tất cả nguồn, loại trùng theo URL và độ tương đồng tiêu đề (>80% coi là trùng), tổng hợp thành 10 tin độc quyền, mỗi tin một câu tóm tắt, đóng gói gửi đến. Đăng ký bao nhiêu nguồn, bạn chỉ thấy nội dung thực sự độc quyền."

T[(51,0)] = "📥 Use case 38: Module kỹ năng \"Email chuyển Podcast\" — khối xếp hình tái sử dụng"
T[(53,0)] = "Use case này không phải cho một kịch bản cụ thể, mà là đóng gói quy trình \"email → podcast\" thành một \"module kỹ năng\" có thể tái sử dụng, giống như thư viện hàm trong phần mềm — đóng gói một lần, dùng mọi nơi. Email y tế dùng nó, email tin tức dùng nó, báo cáo tuần dùng nó... chỉ cần đổi giọng nói và phong cách là thích ứng với bất kỳ kịch bản nào."

T[(54,0)] = "🌅 Use case 45: Bộ tạo bản tin buổi sáng"
T[(56,0)] = "Tương ứng với hoạt động tự động ban đêm, sáng dậy AI đã chỉnh trang xong \"đêm qua có gì xảy ra\". Định dạng rõ ràng:"
T[(57,0)] = "\"Nhiệm vụ hoàn thành đêm qua\" (3 Cron chạy bình thường, 1 lần quét bảo mật đạt, 12 email đã sắp xếp)"
T[(58,0)] = "\"AI đêm qua chủ động làm gì\" (sửa 2 lỗi chính tả tài liệu, lưu trữ file trí nhớ cũ)"
T[(59,0)] = "\"Việc cần bạn xử lý\" (1 email khẩn cấp, GitHub Issue #234 Bug nghiêm trọng)"
T[(60,0)] = "\"Nhắc nhở hôm nay\" (họp lúc 2 giờ chiều, dự kiến deploy lúc 4 giờ)"
T[(61,0)] = "Bạn cầm cà phê đọc 30 giây, những gì cần biết đều biết rồi."

T[(62,0)] = "🎙️ Use case 51: Biến email đăng ký thành podcast nghe trên đường đi làm"
T[(64,0)] = "Cuộc sống hàng ngày: "
T[(64,1)] = "Bạn đăng ký hàng chục Newsletter (bản tin) quan tâm, nhưng mỗi ngày mở điện thoại ra, hoàn toàn không có thời gian đọc đống chữ đó. Chúng cứ nằm trong hộp thư từ từ mốc meo..."
T[(65,0)] = "OpenClaw xử lý thế nào: "
T[(65,1)] = "Mỗi sáng 7 giờ, AI mở hộp thư của bạn, chọn ra 3-5 câu chuyện thú vị nhất từ Newsletter nhận được, viết thành đoạn kịch bản podcast kiểu \"bạn bè trò chuyện\", rồi dùng tính năng tổng hợp giọng nói ElevenLabs chuyển thành audio, gửi thẳng đến Telegram của bạn. Trên đường đi làm đeo tai nghe, bấm nút play, là nghe được một kỳ podcast buổi sáng được tùy chỉnh riêng cho bạn."
T[(66,0)] = "Case thực tế: "
T[(66,1)] = "Một bác sĩ tên Fred trong cộng đồng Moltbook, mỗi ngày nhận được \"Bản tin Bác sĩ BC\", AI biến 6 tin y tế thành một kỳ podcast 5 phút 18 giây, nói về trung tâm chăm sóc cấp bách, dịch bệnh bùng phát và cập nhật chính sách. Anh ấy nghe hết trên đường lái xe đi làm."
T[(67,0)] = "Thành công trông như: "
T[(67,1)] = "Mỗi khi Newsletter đến, trong 1 giờ tự động tạo audio; audio không quá 7 phút; bạn không cần nhìn màn hình đọc email dài dòng nữa."

T[(68,0)] = "☀️ Use case 52: Mỗi sáng tự động gửi cho bạn một bản \"tin tức hôm nay\""
T[(70,0)] = "Cuộc sống hàng ngày: "
T[(70,1)] = "Sáng dậy, bạn phải mở app thời tiết xem thời tiết, mở lịch xem hôm nay có cuộc họp gì, rồi lướt tin tức... mở bốn năm app, đầu chưa tỉnh đã quá tải thông tin."
T[(71,0)] = "OpenClaw xử lý thế nào: "
T[(71,1)] = "Mỗi sáng 6:30, AI tổng hợp ba thứ: ① Kiểm tra thời tiết thành phố bạn ở ② Đọc lịch hôm nay ③ Tìm kiếm tin tức nổi bật trong lĩnh vực bạn quan tâm. Tổng hợp tất cả thành một tin nhắn Telegram, định dạng gọn gàng, có emoji phân loại, dưới 300 chữ, 1 phút là đọc xong."
T[(72,0)] = "Phép màu cốt lõi: "
T[(72,1)] = "Đây không chỉ là ghép đơn giản thời tiết + lịch — AI còn dựa vào thời tiết cho bạn biết hôm nay có cần mang ô không, dựa vào lịch nhắc bạn 3 giờ chiều có cuộc gọi quan trọng cần chuẩn bị trước."
T[(73,0)] = "Thành công trông như: "
T[(73,1)] = "Bạn nằm trong chăn cầm điện thoại, 30 giây nắm rõ toàn cảnh hôm nay, rồi yên tâm dậy."

T[(74,0)] = "📝 Use case 57: Tự động tạo nhật ký học tập hàng ngày"
T[(76,0)] = "Cuộc sống hàng ngày: "
T[(76,1)] = "Bạn biết \"phản tư giúp người ta trưởng thành nhanh hơn\", nhưng mỗi tối trước khi ngủ thực sự không còn năng lượng viết nhật ký."
T[(77,0)] = "OpenClaw xử lý thế nào: "
T[(77,1)] = "Mỗi tối, AI gửi qua Telegram vài câu hỏi dẫn dắt: \"Hôm nay học được gì?\" \"Việc gì khiến bạn thấy thử thách?\" \"Bạn tự hào về điều gì?\" Bạn chỉ cần tiện tay trả lời vài câu, AI giúp bạn chỉnh lý thành nhật ký lưu trữ có định dạng. Mỗi tuần, AI tổng hợp 7 bài nhật ký thành một bản \"báo cáo phát triển\", cho bạn biết tuần này bạn tiến bộ ở kỹ năng nào, học được insight gì, sửa được sai lầm nào."
T[(78,0)] = "Giá trị thời gian: "
T[(78,1)] = "Bạn mỗi ngày chỉ cần trả lời 3-5 câu hỏi, khoảng 5 phút; nhưng sau một năm, bạn sẽ có 365 bài ghi chép phát triển, đủ để nhìn rõ quỹ đạo của mình."

T[(79,0)] = "👗 Use case 58: Hôm nay mặc gì? AI gợi ý phối đồ cho bạn"
T[(81,0)] = "Cuộc sống hàng ngày: "
T[(81,1)] = "Đứng trước tủ quần áo, nhìn trời do dự: hôm nay nóng không? có mưa không? chiều tối có lạnh không?"
T[(82,0)] = "OpenClaw xử lý thế nào: "
T[(82,1)] = "AI mỗi sáng tự động kiểm tra thời tiết và lịch của bạn, rồi đưa ra gợi ý phối đồ: \"Chiều nay có cuộc họp ngoài trời, khuyến nghị mặc áo khoác mỏng cộng một lớp trong, nhớ mang ô gấp. Chiều tối nhiệt độ giảm xuống 15°C.\""
T[(83,0)] = "Nó còn nhớ sở thích tủ đồ của bạn (do bạn cho nó biết), không để robot không hiểu phong cách của bạn phối ra tổ hợp kỳ lạ."

T[(84,0)] = "📰 Use case 59: Tóm tắt tin tức tổng hợp — mỗi ngày 1 phút hiểu hết chuyện thiên hạ"
T[(86,0)] = "Cuộc sống hàng ngày: "
T[(86,1)] = "15 nguồn RSS tin tức, mỗi ngày sản xuất hàng trăm tiêu đề, cùng một sự kiện bị đưa tin 40 lần."
T[(87,0)] = "OpenClaw xử lý thế nào: "
T[(87,1)] = "AI mỗi ngày 4 lần kéo tất cả RSS bạn đăng ký, loại bỏ tin trùng (URL giống hoặc tiêu đề trùng >80% đều tính là trùng), gộp phần còn lại thành 10 tin độc quyền, mỗi tin viết một câu tóm tắt, đóng gói gửi cho bạn."
T[(88,0)] = "Chi tiết tinh tế: "
T[(88,1)] = "Nó không chỉ loại trùng, còn viết cho mỗi tin \"tại sao sự kiện này đáng chú ý\" làm bối cảnh, giúp bạn trong 3 phút có cái nhìn toàn cục về thông tin quan trọng trong ngày."

T[(89,0)] = "📚 Use case 61: Người quản lý danh sách đọc — thứ Sáu gửi cho bạn danh sách sách tinh chọn"
T[(91,0)] = "Cuộc sống hàng ngày: "
T[(91,1)] = "Lướt thấy bài hay tiện tay lưu, rồi không bao giờ mở lại..."
T[(92,0)] = "OpenClaw xử lý thế nào: "
T[(92,1)] = "Bạn bất cứ lúc nào gửi link cho AI, thêm câu \"lưu lại\", nó sẽ lưu tiêu đề bài, phân loại (công nghệ/kinh doanh/sức khỏe/văn hóa) và tóm tắt. Mỗi thứ Sáu lúc 3 giờ chiều, nó gửi đến \"danh sách đọc cuối tuần\", sắp xếp theo phân loại, mỗi bài kèm hai câu tóm tắt, tiện cho bạn quyết định có đáng đọc đầy đủ không. Còn giúp bạn chọn \"đề xuất tuần này\" — cái mà nó cho rằng bạn nên đọc nhất."

T[(93,0)] = "📝 Use case 68: Tự động tạo biên bản cuộc họp"
T[(95,0)] = "Cuộc sống hàng ngày: "
T[(95,1)] = "Mỗi lần họp xong, luôn có người trốn trách nhiệm \"ai viết biên bản\", rồi ba ngày sau mọi người quên mất đã thỏa thuận gì..."
T[(96,0)] = "OpenClaw xử lý thế nào: "
T[(96,1)] = "Dán ghi chú thô hoặc bản text ghi âm cuộc họp cho AI, nó tạo biên bản cuộc họp có định dạng: người tham dự, tóm tắt thảo luận, quyết định chính, danh sách hành động (kèm người chịu trách nhiệm và deadline), vấn đề chưa giải quyết. Lưu vào hệ thống trí nhớ, đến deadline sẽ tự động gửi nhắc nhở."
T[(97,0)] = "Thành công trông như: "
T[(97,1)] = "Không ai còn phải hỏi \"lần họp đó cuối cùng chúng ta quyết định gì nhỉ\"."

# Section 2: Memory & Knowledge Management
T[(98,0)] = "🧠 Danh mục lớn thứ hai: Quản lý trí nhớ & kiến thức (5 use case)"
T[(99,0)] = "Điểm yếu lớn nhất của AI là \"mất trí nhớ\" — sau mỗi cuộc hội thoại lại quên hết những gì đã nói trước đó. Danh mục này chuyên giải quyết vấn đề: làm sao để AI có trí nhớ bền vững thực sự hữu ích."

# I'll continue with remaining blocks...
# For blocks 100+, reading remaining segments

with open('art4_chinese_segments.txt', 'r', encoding='utf-8') as f:
    remaining_lines = f.readlines()[100:]  # lines after first 100

# Continue translations for blocks 100+
T[(100,0)] = "💾 Use case 04: Hệ thống trí nhớ 3 tầng — phiên bản AI của \"trí nhớ dài hạn\""
T[(102,0)] = "Giống như con người có trí nhớ ngắn hạn, trí nhớ dài hạn và kiến thức nền, AI cũng cần. Hệ thống này chia trí nhớ AI thành 3 file:"
T[(103,0)] = "activeContext.md"
T[(103,1)] = " — Trí nhớ làm việc: nhiệm vụ đang thực hiện, quyết định đang xử lý (như bộ nhớ RAM)"
T[(104,0)] = "progress.md"
T[(104,1)] = " — Tiến độ dự án: milestone đã hoàn thành, task đang chờ, blockers"
T[(105,0)] = "coreMemory.md"
T[(105,1)] = " — Trí nhớ bền vững: phong cách code của bạn, quyết định kiến trúc, bài học rút ra"
T[(106,0)] = "Khi context window đầy, AI lưu lại những gì quan trọng trước khi \"quên\", lần sau mở lại tự động đọc trước 3 file này. Giống như con người ngủ dậy vẫn nhớ \"tôi là ai, đang làm gì\"."

T[(107,0)] = "🕸️ Use case 05: Bộ tái tạo đồ thị tri thức"
T[(109,0)] = "Khi ghi chú của bạn hỗn loạn không có hệ thống, AI đọc toàn bộ ghi chú, tự động phát hiện mối quan hệ giữa các khái niệm, tạo đồ thị tri thức."
T[(110,0)] = "Case thực tế: "
T[(110,1)] = "Một sinh viên nghiên cứu ném vào một đống ghi chú rải rác, AI phát hiện mô hình lý thuyết A liên quan đến phương pháp B, phương pháp B có thể giải quyết vấn đề C, vấn đề C lại là thiếu sót của mô hình A — hình thành chuỗi tri thức khép kín."

T[(111,0)] = "📅 Use case 06: Lưu trữ trí nhớ theo tuần — phòng ngừa tràn Token"
T[(113,0)] = "Vấn đề cốt lõi: Khi bạn nói chuyện với AI mỗi ngày, context window sẽ dần đầy. AI bắt đầu \"quên\" những thứ nói tuần trước, hoặc phản hồi chậm lại."
T[(114,0)] = "Giải pháp: "
T[(114,1)] = "Mỗi Chủ nhật đêm, AI tổng hợp toàn bộ hội thoại trong tuần thành \"bản tóm tắt tuần\" có cấu trúc, lưu vào file, rồi dọn context window. Tuần sau AI đọc bản tóm tắt tuần trước là nắm được toàn bộ bối cảnh."

T[(115,0)] = "🏷️ Use case 67: Hệ thống quản lý trí nhớ AI cá nhân"
T[(117,0)] = "Cuộc sống hàng ngày: "
T[(117,1)] = "Bạn nói chuyện với AI nhiều chủ đề mỗi ngày — task công việc, note cá nhân, linh cảm sáng tạo. Nhưng AI mỗi lần mở cuộc trò chuyện mới lại bắt đầu từ \"xin chào, tôi có thể giúp gì?\", những gì nói hôm qua đã quên sạch."
T[(118,0)] = "OpenClaw xử lý thế nào: "
T[(118,1)] = "AI duy trì 3 hệ thống file: \"core memory\" (sở thích, phong cách làm việc, mục tiêu dài hạn), \"working memory\" (đang làm gì), \"knowledge base\" (kiến thức tích lũy qua các hội thoại). Trước mỗi cuộc trò chuyện, AI đọc trước 3 file này, giống như con người sáng dậy tự động nhớ lại \"mình là ai\"."
T[(119,0)] = "Phép màu cốt lõi: "
T[(119,1)] = "AI không chỉ \"nhớ\", còn \"quên\" chủ động — mỗi tuần tự động review trí nhớ, chuyển nội dung ít liên quan vào archive, giữ trí nhớ gọn gàng. Giống như dọn phòng, đồ không dùng cất vào kho."

T[(120,0)] = "🔑 Use case 70: Quản lý tri thức cá nhân — phiên bản AI \"não thứ hai\""
T[(122,0)] = "Cuộc sống hàng ngày: "
T[(122,1)] = "Bạn đọc sách, xem bài giảng, đọc bài viết, mỗi ngày tiếp nhận lượng lớn thông tin, nhưng ba ngày sau quên hết 80%."
T[(123,0)] = "OpenClaw xử lý thế nào: "
T[(123,1)] = "Gửi bất kỳ nội dung gì cho AI (link bài viết, ghi chú, ảnh chụp), nó tự động trích xuất điểm chính, phân loại lưu trữ, tạo liên kết chéo. Khi bạn cần, nói \"tôi đã đọc cái gì đó về quản lý thời gian tuần trước\", nó tìm ra ngay bạn đọc gì, quan điểm chính là gì."

# Section 3: Night Automation
T[(124,0)] = "🌙 Danh mục lớn thứ ba: Tự động hóa ban đêm (11 use case)"
T[(125,0)] = "Ban đêm bạn ngủ, AI không ngủ. Danh mục này khai thác \"thời gian nhàn rỗi\" để AI hoàn thành các tác vụ lặp đi lặp lại."

T[(126,0)] = "🌃 Use case 07: 7 Agent con chạy song song ban đêm"
T[(128,0)] = "Tác giả thiết lập 7 nhiệm vụ ban đêm chạy song song:"
T[(129,0)] = "Quét bảo mật (kiểm tra lỗ hổng phụ thuộc)"
T[(130,0)] = "Tối ưu tài liệu (sửa lỗi chính tả, hoàn thiện chú thích)"
T[(131,0)] = "Theo dõi đối thủ (crawl changelog sản phẩm đối thủ)"
T[(132,0)] = "Phân loại email (sắp xếp email hôm nay)"
T[(133,0)] = "Sao lưu dữ liệu"
T[(134,0)] = "Chạy test (regression test)"
T[(135,0)] = "Tạo báo cáo (tổng hợp kết quả 6 task trên)"
T[(136,0)] = "AI phân luồng task, có dependency sẽ xếp hàng, không có thì chạy song song. Sáng dậy bạn nhận được một bản báo cáo, viết rõ cái nào hoàn thành, cái nào có vấn đề cần bạn xem."

T[(137,0)] = "🩺 Use case 08: Kiểm tra sức khỏe hạ tầng lúc 5 giờ sáng"
T[(139,0)] = "Mỗi ngày 5 giờ sáng, AI lần lượt kiểm tra: SSL certificate còn bao nhiêu ngày hết hạn, domain có bình thường không, web có response không, cơ sở dữ liệu có bị gián đoạn không, API có chậm không."
T[(140,0)] = "Nếu mọi thứ bình thường → Gửi một tin \"tất cả bình thường\" màu xanh"
T[(141,0)] = "Nếu có vấn đề → Gửi cảnh báo kèm chi tiết + mức độ nghiêm trọng + đề xuất xử lý"

T[(142,0)] = "🔔 Use case 09: Tự động trả lời WhatsApp ban đêm"
T[(144,0)] = "Ban đêm có khách hàng hoặc bạn bè nhắn tin, AI kiểm tra nội dung, nếu khẩn cấp thì chuyển tiếp cho bạn kèm chuông báo, nếu không khẩn cấp thì trả lời \"tôi đã nhận được tin nhắn của bạn, sẽ phản hồi vào ngày mai\"."
T[(145,0)] = "Phân tích thông minh: "
T[(145,1)] = "AI phán đoán mức độ khẩn cấp dựa trên từ khóa (\"khẩn cấp\"/\"sập máy\"/\"deadline sáng mai\") chứ không phải đơn giản ai nhắn cũng chuyển tiếp."

# Continue with remaining sections...
T[(146,0)] = "🔐 Use case 10: Quét dọn Git repository đêm khuya"
T[(148,0)] = "AI mỗi đêm quét toàn bộ repository: có file nào vô tình commit key/password không, có dependency nào có lỗ hổng bảo mật đã biết không, có file log nào quá lớn cần dọn không."
T[(149,0)] = "Giá trị thực: "
T[(149,1)] = "Một lần quét đêm phát hiện có key AWS bị commit vào file config, kịp thời xoay key, tránh được thiệt hại tài chính tiềm năng."

T[(150,0)] = "📬 Use case 11: Sắp xếp email tự động ban đêm"
T[(152,0)] = "AI mỗi đêm đọc email trong ngày, tự động phân loại:"
T[(153,0)] = "🔴 Quan trọng cần xử lý (có deadline, cần phản hồi)"
T[(154,0)] = "🟡 Tham khảo (newsletter, cập nhật sản phẩm)"
T[(155,0)] = "⚪ Có thể bỏ qua (quảng cáo, tuyển dụng)"
T[(156,0)] = "Sáng dậy bạn chỉ cần xem mục đỏ, email đã được AI chỉnh lý rõ ràng."

T[(157,0)] = "⏰ Use case 12: Hệ thống nhắc nhở thông minh"
T[(159,0)] = "AI không chỉ đơn giản nhắc bạn \"3 giờ chiều có cuộc họp\", mà là:"
T[(160,0)] = "2 giờ 30 chiều: \"Cuộc họp 3 giờ sắp bắt đầu, tài liệu bạn yêu cầu tôi chuẩn bị đã đính kèm ở đây\""
T[(161,0)] = "2 giờ 50 chiều: \"Nhắc nhỏ: cuộc họp này bạn cần chuẩn bị 3 điểm: A, B, C (dựa trên email bạn nhận sáng nay)\""
T[(162,0)] = "Ngày hôm sau: \"Hôm qua cuộc họp bạn hứa sẽ hoàn thành báo cáo X, deadline là thứ Năm\""

T[(163,0)] = "🌐 Use case 42: Tự động dọn dẹp bàn làm việc số ban đêm"
T[(165,0)] = "AI mỗi đêm thực hiện: đóng tab trình duyệt quá 3 ngày chưa xem, chuyển file download xong vào thư mục tương ứng, dọn file tạm. Giống như có người mỗi đêm giúp bạn dọn bàn."

T[(166,0)] = "📊 Use case 43: Báo cáo thời gian dùng — mỗi tuần cho bạn biết thời gian đi đâu"
T[(168,0)] = "AI phân tích lịch và nhật ký hoạt động của bạn, mỗi Chủ nhật tối gửi: tuần này bạn họp bao nhiêu giờ, code bao nhiêu giờ, xử lý email bao nhiêu giờ. Biểu đồ hình tròn cho bạn thấy trực quan rằng 40% thời gian bị họp nuốt mất."

T[(169,0)] = "🔄 Use case 44: Đồng bộ dữ liệu xuyên nền tảng ban đêm"
T[(171,0)] = "Bạn dùng nhiều công cụ: Notion ghi chú, Todoist quản lý task, Google Calendar sắp lịch. AI mỗi đêm đồng bộ: task mới trong Notion đồng bộ sang Todoist, sự kiện Todoist đồng bộ sang Calendar. Sáng dậy tất cả nền tảng đã nhất quán."

T[(172,0)] = "🌜 Use case 55: AI tuần tra ban đêm — tự động kiểm tra website, server và tài khoản MXH"
T[(174,0)] = "Cuộc sống hàng ngày: "
T[(174,1)] = "Bạn vận hành một sản phẩm, website bị sập lúc nửa đêm không ai biết, sáng hôm sau mất mấy giờ doanh thu."
T[(175,0)] = "OpenClaw xử lý thế nào: "
T[(175,1)] = "AI mỗi đêm định kỳ kiểm tra: website có phản hồi không, API có bình thường không, SSL certificate có sắp hết hạn không, trang MXH có bình luận tiêu cực cần xử lý không. Có vấn đề lập tức gửi cảnh báo Telegram."

# Section 4: Finance & Blockchain
T[(176,0)] = "💰 Danh mục lớn thứ tư: Tài chính & Blockchain (6 use case)"
T[(177,0)] = "Tài chính là lĩnh vực cần giám sát 7x24, khớp hoàn hảo với đặc tính \"không ngủ\" của AI."

T[(178,0)] = "📈 Use case 13: Giám sát sức khỏe bot giao dịch"
T[(180,0)] = "AI theo dõi trạng thái chạy của bot giao dịch theo thời gian thực: có bị ngắt kết nối không, tỷ lệ thắng có bất thường không, lượng vốn có biến đổi đáng kể không."
T[(181,0)] = "Cảnh báo thông minh: "
T[(181,1)] = "Không phải tin nào cũng báo — chỉ khi có bất thường mới gửi thông báo, tránh \"cậu bé chăn cừu\" khiến bạn bỏ qua cảnh báo thật."

T[(182,0)] = "🦄 Use case 14: Quản lý thanh khoản tự động Uniswap V4"
T[(184,0)] = "AI tự động giám sát pool thanh khoản DeFi, khi phạm vi giá lệch ra ngoài vị thế của bạn, tự động cân bằng lại, tối ưu hóa thu nhập phí."

T[(185,0)] = "₿ Use case 15: Bitcoin Inscription — khắc thơ trên blockchain"
T[(187,0)] = "Đây là use case \"gây xôn xao\" nhất: AI mỗi ngày sáng tạo một bài thơ haiku, rồi dùng giao thức Ordinals khắc lên blockchain Bitcoin. Mỗi bài thơ trở thành tài sản số vĩnh viễn, không ai có thể xóa hay sửa."

T[(188,0)] = "🎰 Use case 16: \"Lá số may mắn\" tiền mã hóa — với blockchain"
T[(190,0)] = "AI mỗi ngày tạo một \"lá số may mắn\" (giống bánh cookie may mắn), kèm dữ liệu thị trường tiền mã hóa, khắc lên blockchain. Vừa giải trí vừa có giá trị sưu tầm."

T[(191,0)] = "💹 Use case 46: Giám sát giá tiền mã hóa + cảnh báo thông minh"
T[(193,0)] = "AI theo dõi giá đồng tiền bạn quan tâm, khi biến động vượt ngưỡng thiết lập (ví dụ tăng/giảm 5% trong 1 giờ), gửi cảnh báo Telegram kèm phân tích: sự kiện gì gây ra biến động, tâm lý thị trường ra sao."

T[(194,0)] = "📉 Use case 47: Theo dõi & phân tích sổ lệnh DEX (Decentralized Exchange)"
T[(196,0)] = "AI giám sát pool giao dịch DEX, khi phát hiện lệnh lớn bất thường hoặc thanh khoản rút đột ngột, gửi cảnh báo cho bạn, kèm phân tích lịch sử xem mô hình tương tự trước đây dẫn đến biến động giá thế nào."

# Section 5: Data Analysis & BI
T[(197,0)] = "📊 Danh mục lớn thứ năm: Phân tích dữ liệu & tình báo kinh doanh (9 use case)"
T[(198,0)] = "AI biến dữ liệu rải rác thành tình báo có thể hành động."

T[(199,0)] = "🐛 Use case 17: Ưu tiên phân loại GitHub Issue"
T[(201,0)] = "AI định kỳ quét Issue mới, dựa trên nội dung, nhãn, mức nghiêm trọng tự động phân loại ưu tiên: P0 (phải sửa ngay), P1 (tuần này), P2 (backlog). Developer sáng dậy thấy danh sách đã sắp xếp, không cần tự phân loại."

T[(202,0)] = "👤 Use case 18: Thu thập chân dung người dùng X (Twitter)"
T[(204,0)] = "AI phân tích tài khoản X mục tiêu: sở thích, lĩnh vực hoạt động, nhân vật hay tương tác, quan điểm đối với chủ đề cụ thể. Phù hợp cho phân tích đối thủ, phân tích KOL."

T[(205,0)] = "🔍 Use case 19: Máy quét tín hiệu khách hàng"
T[(207,0)] = "AI giám sát Reddit, Twitter, các diễn đàn, khi phát hiện người dùng mô tả pain point liên quan đến sản phẩm của bạn, gửi cảnh báo ngay lập tức: \"Người dùng này đang tìm kiếm giải pháp, đây là cơ hội bán hàng.\""

T[(208,0)] = "📊 Use case 48: Phân tích dữ liệu tự động — biến data thô thành insight"
T[(210,0)] = "Ném file CSV cho AI, nó tự phân tích: phân bố dữ liệu, xu hướng, ngoại lệ, tương quan. Tạo báo cáo kèm biểu đồ và kiến nghị hành động. Trước đây cần nhà phân tích làm 2 giờ, giờ 5 phút có kết quả."

T[(211,0)] = "🏢 Use case 49: Giám sát đối thủ tự động"
T[(213,0)] = "AI mỗi ngày crawl: đối thủ cập nhật sản phẩm gì, changelog nói gì, MXH đăng gì, có tuyển vị trí gì (thông qua tuyển dụng suy ra hướng chiến lược). Mỗi tuần tổng hợp một bản báo cáo tình báo cạnh tranh."

T[(214,0)] = "📋 Use case 50: Tổng hợp phản hồi khách hàng + phân tích tâm lý"
T[(216,0)] = "AI thu thập đánh giá sản phẩm từ nhiều nền tảng, phân tích tâm lý tự động (tích cực/tiêu cực/trung tính), gộp phản hồi tương tự, tạo \"bảng xếp hạng pain point\" — sản phẩm của bạn có mấy vấn đề hàng đầu, mỗi vấn đề bao nhiêu lượt phàn nàn."

T[(217,0)] = "🌐 Use case 60: Giám sát đề cập thương hiệu toàn mạng"
T[(219,0)] = "Cuộc sống hàng ngày: "
T[(219,1)] = "Không biết ai đang nói về thương hiệu bạn ở đâu — có thể đang bị chê trên Reddit, cũng có thể được khen trên Twitter, bạn hoàn toàn không hay biết."
T[(220,0)] = "OpenClaw xử lý thế nào: "
T[(220,1)] = "AI mỗi giờ quét Reddit, Twitter, Hacker News, tìm đề cập đến tên thương hiệu hoặc sản phẩm, phân tích tâm lý, gửi báo cáo. Tin tích cực cho bạn tận hưởng, tin tiêu cực cho bạn xử lý kịp thời."

T[(221,0)] = "📈 Use case 69: Phân tích danh mục đầu tư + tư vấn tái cân bằng"
T[(223,0)] = "Cuộc sống hàng ngày: "
T[(223,1)] = "Bạn mua một đống cổ phiếu, quỹ, tiền mã hóa, nhưng không có thời gian theo dõi mỗi khoản, không biết phân bổ tài sản có mất cân bằng không."
T[(224,0)] = "OpenClaw xử lý thế nào: "
T[(224,1)] = "AI mỗi ngày đọc danh mục đầu tư, tính tỷ trọng từng khoản, so sánh với tỷ trọng mục tiêu, khi lệch quá ngưỡng gửi kiến nghị tái cân bằng: \"Tỷ trọng tiền mã hóa đã từ 20% tăng lên 35%, khuyến nghị chốt lời một phần chuyển sang trái phiếu.\""

# Section 6: Security & Compliance
T[(225,0)] = "🔒 Danh mục lớn thứ sáu: Bảo mật & tuân thủ (9 use case)"
T[(226,0)] = "Bảo mật là lĩnh vực \"không phát hiện không sao, phát hiện thì đã muộn\". AI kiểm tra liên tục, phát hiện vấn đề trước khi thành sự cố."

T[(227,0)] = "🔑 Use case 21: Máy quét khóa SSH private"
T[(229,0)] = "AI quét toàn bộ Git history, tìm SSH private key, AWS key, mật khẩu database vô tình bị commit. Đã phát hiện nhiều lần key bị lộ trong các dự án thực tế."

T[(230,0)] = "📝 Use case 22: Phát hiện bất thường log"
T[(232,0)] = "AI đọc log server, khi phát hiện mẫu bất thường (ví dụ: số lần đăng nhập thất bại tăng đột biến, đỉnh request bất thường, báo lỗi tăng mạnh), lập tức gửi cảnh báo kèm phân tích."

T[(233,0)] = "📧 Use case 23: Bộ phân loại email tự động"
T[(235,0)] = "AI phân loại email vào: hóa đơn, newsletter, email cá nhân, cảnh báo hệ thống. Hóa đơn tự động trích xuất số tiền và deadline, cảnh báo hệ thống tự động tạo ticket."

T[(236,0)] = "🛡️ Use case 24: Giám sát tuân thủ chính sách bảo mật"
T[(238,0)] = "AI kiểm tra: mật khẩu có tuân thủ chính sách phức tạp không, quyền truy cập có vượt phạm vi cần thiết không, file nhạy cảm có bật mã hóa không. Mỗi tuần tạo báo cáo tuân thủ."

T[(239,0)] = "🔐 Use case 25: Máy quét lỗ hổng dependency"
T[(241,0)] = "AI mỗi đêm kiểm tra tất cả dependency dự án, đối chiếu với cơ sở dữ liệu lỗ hổng đã biết (CVE), phát hiện lỗ hổng thì cảnh báo kèm phiên bản sửa lỗi được đề xuất."

T[(242,0)] = "🔒 Use case 53: Giám sát bảo mật mật khẩu — password của bạn có bị lộ không?"
T[(244,0)] = "Cuộc sống hàng ngày: "
T[(244,1)] = "Bạn dùng cùng một mật khẩu cho nhiều website, website nào bị hack thì tất cả tài khoản của bạn đều nguy hiểm."
T[(245,0)] = "OpenClaw xử lý thế nào: "
T[(245,1)] = "AI định kỳ kiểm tra email của bạn trong cơ sở dữ liệu bị lộ (Have I Been Pwned), nếu phát hiện bị lộ lập tức thông báo bạn đổi mật khẩu. Còn nhắc bạn những tài khoản nào đã lâu không đổi mật khẩu."

T[(246,0)] = "🔍 Use case 54: Kiểm tra quyền riêng tư — ai đang theo dõi bạn?"
T[(248,0)] = "Cuộc sống hàng ngày: "
T[(248,1)] = "Bạn cài hàng chục app, mỗi cái đều yêu cầu một đống quyền, không biết chúng thực sự thu thập dữ liệu gì."
T[(249,0)] = "OpenClaw xử lý thế nào: "
T[(249,1)] = "AI phân tích quyền mà app yêu cầu, so sánh với chức năng thực tế cần: \"App đèn pin này yêu cầu quyền danh bạ và định vị, rõ ràng vượt phạm vi cần thiết, khuyến nghị gỡ.\""

T[(250,0)] = "🔐 Use case 62: Giám sát bảo mật trang cá nhân"
T[(252,0)] = "Cuộc sống hàng ngày: "
T[(252,1)] = "Bạn có website cá nhân hoặc blog, nhưng không chuyên bảo mật, không biết website có bị tấn công SQL injection hay XSS không."
T[(253,0)] = "OpenClaw xử lý thế nào: "
T[(253,1)] = "AI mỗi đêm thực hiện quét bảo mật cơ bản trên website: kiểm tra SSL, header bảo mật, lỗ hổng thường gặp. Có vấn đề gửi báo cáo kèm hướng dẫn sửa."
T[(254,0)] = "🛡️ Use case 63: Quản lý đăng ký dịch vụ — đừng tiếp tục trả tiền cho dịch vụ không dùng"
T[(256,0)] = "Cuộc sống hàng ngày: "
T[(256,1)] = "Bạn đăng ký hàng chục dịch vụ SaaS, có cái đã lâu không dùng nhưng vẫn trừ tiền hàng tháng."
T[(257,0)] = "OpenClaw xử lý thế nào: "
T[(257,1)] = "AI quét email tìm thông báo thu phí, đối chiếu với tần suất sử dụng: \"Bạn trả $9.99/tháng cho dịch vụ X, nhưng 3 tháng qua không đăng nhập lần nào, khuyến nghị hủy đăng ký.\""

# Section 7: Daily Life
T[(258,0)] = "📱 Danh mục lớn thứ bảy: Trợ lý đời sống hàng ngày (13 use case)"
T[(259,0)] = "AI không chỉ là công cụ làm việc, mà còn có thể nâng cấp chất lượng cuộc sống hàng ngày."

T[(260,0)] = "₿ Use case 26: Khắc thơ haiku trên blockchain Bitcoin"
T[(262,0)] = "Mỗi ngày AI sáng tạo một bài thơ haiku (3 dòng, 5-7-5 âm tiết), rồi dùng giao thức Ordinals khắc vĩnh viễn lên blockchain Bitcoin. Bạn có một bộ sưu tập thơ số mà không ai có thể xóa."

T[(263,0)] = "🥠 Use case 27: \"Lá số may mắn\" tiền mã hóa — với blockchain"
T[(265,0)] = "AI mỗi ngày tạo một \"lá số may mắn\" kết hợp dữ liệu thị trường thời gian thực (giá BTC, mức gas Ethereum v.v.), khắc lên blockchain. Vừa vui vừa có giá trị lưu niệm."

T[(266,0)] = "🟢 Use case 28: Đồng bộ trạng thái online đa nền tảng"
T[(268,0)] = "Bạn dùng nhiều nền tảng liên lạc: Slack, Discord, Teams. Đặt một cái sang \"bận\" mà quên mấy cái kia. AI giám sát, khi trạng thái một nền tảng thay đổi, tự động đồng bộ các nền tảng khác."

T[(269,0)] = "🍳 Use case 56: Hôm nay ăn gì? AI gợi ý thực đơn hàng ngày"
T[(271,0)] = "Cuộc sống hàng ngày: "
T[(271,1)] = "Mỗi ngày đến giờ ăn lại đau đầu \"hôm nay ăn gì\". Nhất là khi muốn ăn uống lành mạnh nhưng ngại nghĩ."
T[(272,0)] = "OpenClaw xử lý thế nào: "
T[(272,1)] = "AI mỗi sáng căn cứ vào sở thích ăn uống, nguyên liệu sẵn có (bạn cho nó biết), thời tiết (trời lạnh gợi ý món nóng) và mục tiêu dinh dưỡng, gợi ý 3 bữa: sáng, trưa, tối. Kèm thời gian nấu dự tính và danh sách nguyên liệu cần mua."

T[(273,0)] = "🏋️ Use case 64: Trợ lý tập luyện AI — coach cá nhân của bạn"
T[(275,0)] = "Cuộc sống hàng ngày: "
T[(275,1)] = "Bạn muốn tập thể dục nhưng không biết bắt đầu từ đâu, thuê PT lại đắt."
T[(276,0)] = "OpenClaw xử lý thế nào: "
T[(276,1)] = "Nói cho AI mục tiêu tập luyện (giảm cân/tăng cơ/sức bền), thiết bị sẵn có (phòng tập/nhà/công viên), nó thiết kế kế hoạch tuần cho bạn. Mỗi ngày nhắc hôm nay tập gì, sau tập hỏi cảm giác thế nào, dựa vào phản hồi để điều chỉnh cường độ."

T[(277,0)] = "💤 Use case 65: Theo dõi giấc ngủ + phân tích"
T[(279,0)] = "Cuộc sống hàng ngày: "
T[(279,1)] = "Luôn cảm thấy ngủ không đủ, nhưng không biết vấn đề ở đâu."
T[(280,0)] = "OpenClaw xử lý thế nào: "
T[(280,1)] = "Mỗi sáng báo cho AI bạn ngủ lúc mấy giờ, dậy lúc mấy giờ, cảm giác thế nào. AI ghi lại, phân tích xu hướng hàng tuần: \"Dữ liệu 3 tuần qua cho thấy ngày bạn tập thể dục buổi chiều, chất lượng giấc ngủ tốt hơn 30%.\""

T[(281,0)] = "💰 Use case 66: Theo dõi chi tiêu hàng ngày"
T[(283,0)] = "Cuộc sống hàng ngày: "
T[(283,1)] = "Biết mình phải kiểm soát chi tiêu, nhưng mỗi lần ghi sổ đều ngại."
T[(284,0)] = "OpenClaw xử lý thế nào: "
T[(284,1)] = "Mỗi khi chi tiêu, gửi AI một câu: \"Cà phê 50k\" \"Ăn trưa 80k\". AI tự động phân loại, tích lũy. Cuối tuần gửi báo cáo: tuần này chi bao nhiêu, loại nào nhiều nhất, có vượt ngân sách không."

T[(285,0)] = "🐾 Use case 36: Nhắc nhở chăm sóc thú cưng"
T[(287,0)] = "AI theo dõi lịch tiêm phòng, tẩy giun, kiểm tra sức khỏe thú cưng, gửi nhắc nhở trước 1 tuần. Còn theo dõi lượng thức ăn hàng ngày, phát hiện bất thường cảnh báo: \"3 ngày qua mèo ăn giảm 40%, khuyến nghị đưa đi khám.\""

T[(288,0)] = "🎮 Use case 37: Quản lý thời gian giải trí"
T[(290,0)] = "AI giám sát thời gian chơi game/xem phim của bạn, đến giờ giới hạn gửi nhắc nhở: \"Bạn đã chơi 2 giờ rồi, mục tiêu hôm nay là 2 giờ. Nghỉ ngơi đi!\""

# Section 8: Developer Tools
T[(291,0)] = "🛠️ Danh mục lớn thứ tám: Công cụ nhà phát triển (4 use case)"
T[(292,0)] = "AI giúp developer tự động hóa những task lặp đi lặp lại, tập trung vào công việc sáng tạo."

T[(293,0)] = "🐚 Use case 29: Trình tạo Shell alias ban đêm"
T[(295,0)] = "AI phân tích lịch sử lệnh shell, phát hiện bạn thường gõ dòng lệnh dài nào, tự động đề xuất alias: \"Bạn gõ 'git log --oneline --graph --all' 15 lần tuần này, tôi đã tạo alias 'glog' cho bạn.\""

T[(296,0)] = "🧰 Use case 30: Bộ công cụ CLI cá nhân"
T[(298,0)] = "AI giúp bạn xây dựng bộ công cụ dòng lệnh cá nhân: tập hợp các script bạn thường dùng, thêm tài liệu, tạo menu tương tác. Bạn chỉ cần gõ 'mytool' là thấy tất cả công cụ tùy chỉnh."

T[(299,0)] = "📦 Use case 31: Phát triển gói Swift Logger"
T[(301,0)] = "Một case phát triển thực tế: AI giúp từ đầu đến cuối phát triển một gói Swift Logger, bao gồm viết code, viết test, viết tài liệu, đẩy lên Swift Package Manager."

T[(302,0)] = "🔧 Use case 32: Công cụ refactor code tự động"
T[(304,0)] = "AI quét codebase, tìm code trùng lặp, hàm quá dài, đặt tên không nhất quán, tự động đề xuất phương án refactor. Review và xác nhận trước khi áp dụng."

# Closing section
T[(305,0)] = "🎯 Tổng kết"
T[(306,0)] = "70 use case này cho thấy một sự thật: OpenClaw không chỉ là \"chatbot thông minh hơn\", mà là nền tảng tự động hóa có thể thay đổi cách bạn làm việc và sống."
T[(307,0)] = "Cốt lõi: "
T[(307,1)] = "Để AI làm việc 24/7 cho bạn, bạn chỉ cần ra quyết định."
T[(308,0)] = "Nếu bạn thấy bất kỳ use case nào hữu ích, hãy bắt đầu từ use case đó. Một use case tự động hóa thành công sẽ tự nhiên dẫn đến use case thứ hai, thứ ba... cho đến khi AI trở thành \"đồng nghiệp\" không thể thiếu trong cuộc sống của bạn."

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

with open('art4_translated.json', 'w', encoding='utf-8') as f:
    json.dump(translated, f, ensure_ascii=False, indent=2)

# Check remaining Chinese
import re
remaining_cn = 0
for block in translated['blocks']:
    for el in block['elements']:
        if el['type'] == 'text_run' and re.search(r'[\u4e00-\u9fff]', el['content']):
            remaining_cn += 1

print(f"Total text segments: {total_text}")
print(f"Translated: {translated_count}")
print(f"Kept (non-Chinese): {kept_count}")
print(f"Remaining Chinese: {remaining_cn}")
