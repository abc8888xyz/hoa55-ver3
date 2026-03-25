import json, sys, re, copy
sys.stdout.reconfigure(encoding='utf-8')

with open('_art_b5_9_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Deep copy for translation
trans = copy.deepcopy(data)

# Chinese character detection
def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

def is_keep(text):
    """Check if text should be kept as-is (URLs, code, pure punctuation, etc.)"""
    t = text.strip()
    if not t:
        return True
    if t.startswith('http://') or t.startswith('https://'):
        return True
    # Pure punctuation/symbols
    if re.match(r'^[\s\.\,\;\:\!\?\-\_\=\+\(\)\[\]\{\}\<\>\~\`\@\#\$\%\^\&\*\/\\\"\']+$', t):
        return True
    return False

# Translation map: block_index -> element_index -> translated_content
# We translate ALL Chinese text_run content

translations = {
    # Block 0: page title
    (0, 0): "Binzi: Giải cứu trí nhớ Lobster, Chuỗi bài về sự phát triển hệ thống bộ nhớ OpenClaw (Phần 3) — Xây dựng công cụ tìm kiếm bộ nhớ",
    # Block 1: quote - link label
    (1, 0): "🔗 Link bài gốc: ",
    # Block 1 el 1: URL - keep as is
    # Block 2: author info
    (2, 0): "Bản gốc Binzi Binzi AI Agent Làng tân binh",
    (2, 1): "20/03/2026 16:16  Chiết Giang",
    # Block 3
    (3, 0): "Hai bài trước đã xây xong nền tảng bộ nhớ, hoàn thiện tuyến phòng thủ ghi chép. Ghi lại chỉ là công việc chuẩn bị, tìm kiếm nhanh - chính xác - ổn định mới là kết quả chúng ta thực sự muốn.",
    # Block 4
    (4, 0): "Mở đầu bài thứ ba, tôi muốn đưa ra một quan điểm cá nhân: nếu việc nâng cấp và cải tạo của chúng ta là đang chống lại sự phát triển phiên bản của chính Lobster, thậm chí chắc chắn sẽ xung đột với bản nâng cấp chính thức trong tương lai, thì nên dừng lại suy nghĩ cho kỹ trước đã.",
    # Block 5
    (5, 0): "Đã chọn dựa trên OpenClaw để trải nghiệm hành trình tiến hóa của AI agent cá nhân, thì mọi tùy chỉnh cải tạo, tốt nhất đều có thể hưởng lợi từ mỗi lần nâng cấp của nó. Dù có một vài phiên bản nhỏ bị lùi giữa chừng, xu hướng dài hạn cũng nên là thuận chiều đi lên, đừng càng sửa càng lệch rồi cuối cùng phải hard fork.",
    # Block 6
    (6, 0): "Vì vậy trước khi thực sự bắt tay tối ưu hệ thống bộ nhớ, cần hiểu lý niệm nền tảng của OpenClaw: ",
    (6, 1): "Local First, Files are the source of truth, File Over App ",
    (6, 2): ".",
    # Block 7
    (7, 0): "Tất cả lấy file có thể tra cứu, truy vết, giải thích tại local làm nguồn thông tin chân thực duy nhất.",
    # Block 8
    (8, 0): "Đồng ý với lý niệm này, các phương án cải tạo sau mới có thể hòa nhập tốt hơn. Cũng chính dưới sự hướng dẫn này, trong hai bài trước tôi đã khuyên mọi người làm hai việc trước:",
    # Block 9
    (9, 0): "Xây dựng cấu trúc hóa file bộ nhớ",
    # Block 10
    (10, 0): "Hoàn thiện cơ chế kích hoạt ghi nhớ",
    # Block 11
    (11, 0): "Mục đích cốt lõi chỉ có một, đảm bảo tối đa khi file Markdown là nguồn thông tin chân thực ở tầng thấp nhất, rõ ràng và đầy đủ.",
    # Block 12
    (12, 0): "Sau khi làm được bước này, tính đầy đủ của log từ 60% nâng lên 95%, quyết định, bài học, trạng thái dự án đều có logic ghi chép tự động hóa và vị trí lưu trữ rõ ràng.",
    # Block 13
    (13, 0): "Việc tiếp theo cần làm tự nhiên kế thừa lên, tối ưu tầng tìm kiếm, để nó thực sự phát huy ưu thế của hệ thống file này. Ghi chép dù đầy đủ đến mấy, tìm không ra cũng vô ích.",
    # Block 14: heading2
    (14, 0): "Điều chỉnh Memory Core cho dễ dùng",
    # Block 15
    (15, 0): "Module bộ nhớ mặc định của OpenClaw là Memory Core.",
    # Block 16
    (16, 0): "Cài đặt mặc định thực ra hơi dở, nếu hoàn toàn không cấu hình thì trông có vẻ dùng được, nhưng rất tầm thường.",
    # Block 17: heading3
    (17, 0): "Tư duy tối ưu",
    # Block 18
    (18, 0): "Memory Core thực ra có thể làm tìm kiếm hỗn hợp:",
    # Block 19
    (19, 0): "BM25 phụ trách khớp từ khóa",
    # Block 20
    (20, 0): "Tìm kiếm vector phụ trách triệu hồi ngữ nghĩa",
    # Block 21
    (21, 0): "Kết quả hai nhánh hợp nhất rồi xếp hạng có trọng số",
    # Block 22
    (22, 0): "Cuối cùng có thể tùy chọn làm xếp hạng lại đa dạng MMR và suy giảm theo thời gian",
    # Block 23
    (23, 0): "Nghĩa là, nếu cài đặt đúng cách, nó có thể từ \"tìm kiếm toàn văn\" đơn thuần, biến thành một chuỗi tìm kiếm hoàn chỉnh kết hợp từ khóa, ngữ nghĩa, loại trùng, đa dạng và tính thời sự.",
    # Block 24
    (24, 0): "Nhiều bạn mới hoàn toàn không nghĩ đến việc cấu hình embedding provider, mà không cấu hình cái này, Memory Core rất vô dụng.",
    # Block 25
    (25, 0): "Nếu Lobster không phát hiện được mô hình embedding local hoặc API từ xa, Memory Core sẽ thoái hóa sang chế độ FTS-only, chỉ còn tìm kiếm BM25 dựa trên full-text index.",
    # Block 26
    (26, 0): "Chỉ khi file được mô hình embedding tạo vector nhúng, Memory Core mới có thể lưu các vector này vào SQLite (",
    (26, 1): "ưu tiên sử dụng sqlite-vec, phiên bản mới đã tích hợp dependency sẵn",
    (26, 2): "), khả năng tìm kiếm ngữ nghĩa mới thực sự thành lập.",
    # Block 27
    (27, 0): "Sau khi khả năng tìm kiếm ngữ nghĩa OK, việc cấu hình thêm chiến lược tìm kiếm mới có ý nghĩa thực tế, nếu không thì điều chỉnh bao nhiêu tham số cũng chỉ xoay vòng trên tìm kiếm từ khóa.",
    # Block 28: heading3
    (28, 0): "Tham khảo cấu hình",
    # Block 29
    (29, 0): "~/.openclaw/openclaw.json :",
    # Block 30
    (30, 0): "Tư duy của bộ cấu hình này là: làm cho bộ nhớ tiếng Trung chính xác hơn, ưu tiên bộ nhớ mới, kết quả đa dạng hơn. Giải thích bên dưới.",
    # Block 31: heading3
    (31, 0): "Giải thích tham số",
    # Block 32
    (32, 0): "Qwen Embedding",
    # Block 33
    (33, 0): "Lobster mặc định khuyên dùng embedding của OpenAI, nội dung của chúng ta cơ bản đều là tiếng Trung, có thể thay bằng embedding của Qwen3. Provider vẫn ghi openai, baseUrl trỏ đến endpoint tương thích của Alibaba Cloud là được.",
    # Block 34
    (34, 0): "Phiên bản mới nhất text-embedding-v4, hỗ trợ đa ngôn ngữ đồng thời hiểu ngữ nghĩa tiếng Trung và truy xuất văn bản ổn định hơn, hiệu quả hơn, có 1 triệu token miễn phí trong ba tháng có thể tận dụng, kể cả trả phí thì 1 triệu token mới năm hào, gần như miễn phí.",
    # Block 35
    (35, 0): "Nếu có điều kiện triển khai local, không muốn qua cloud, cũng có thể đổi provider thành ollama, chạy dòng Qwen3 embedding làm thay thế, cũng rất tiện.",
    # Block 36
    (36, 0): "vectorWeight: 0.7, textWeight: 0.3",
    # Block 37
    (37, 0): "Đây là phân bổ trọng số của tìm kiếm ngữ nghĩa và tìm kiếm từ khóa trong xếp hạng hỗn hợp. Tỷ lệ 7:3 khá phù hợp cho tìm kiếm bộ nhớ thông thường.",
    # Block 38
    (38, 0): "Các câu hỏi chúng ta hỏi Lobster hàng ngày, phần lớn là truy vấn kiểu khái niệm, ví dụ \"phương án lần trước chúng ta định là gì\", trọng số ngữ nghĩa cao hơn một chút sẽ phù hợp hơn với tình huống sử dụng thực tế, tìm kiếm từ khóa cũng giữ lại một ít để bảo đảm an toàn.",
    # Block 39
    (39, 0): "candidateMultiplier: 4",
    # Block 40
    (40, 0): "Tham số này kiểm soát kích thước pool ứng viên, mặc định gấp 4 lần thường khá cân bằng. Ví dụ, muốn trả về Top-6, thì giai đoạn tìm kiếm sẽ lấy trước 6x4=24 ứng viên, rồi hợp nhất, loại trùng, xếp hạng lại, cuối cùng lấy 6 kết quả đầu. Pool ứng viên đủ lớn, giai đoạn xếp hạng tinh mới có không gian chọn lọc; cũng không cần quá lớn, nếu không chi phí tính toán cho xếp hạng sau sẽ bị đẩy lên vô ích.",
    # Block 41
    (41, 0): "MMR lambda: 0.7",
    # Block 42
    (42, 0): "MMR dùng để giải quyết vấn đề \"kết quả quá giống nhau\". Ví dụ bạn tìm \"OpenClaw\", nếu không làm xếp hạng lại đa dạng, có thể vài kết quả đầu đều nói về bước cài đặt, nhưng trong tình huống thực tế, chúng ta thường mong muốn tìm được kết quả từ nhiều khía cạnh khác nhau như cấu hình, lỗi đã gặp, thực hành, v.v. Nhận được một đống mục tương tự nhau, mật độ thông tin thường giảm đi.",
    # Block 43
    (43, 0): "lambda = 0.7 có thể hiểu đơn giản là, 70% xem mức độ liên quan, 30% xem tính đa dạng. Mức độ liên quan là chủ đạo, nhưng kết quả có tính đến đa dạng.",
    # Block 44
    (44, 0): "temporalDecay halfLifeDays: 30",
    # Block 45
    (45, 0): "Suy giảm theo thời gian, để nội dung mới dễ dàng được xếp hạng lên trước hơn. Chu kỳ bán rã đặt 30 ngày, nghĩa là nội dung khoảng một tháng trước trọng số sẽ suy giảm còn một nửa.",
    # Block 46
    (46, 0): "Nhưng ở đây có một chi tiết đáng chú ý: suy giảm theo thời gian nhắm vào các file log có thuộc tính ngày, ví dụ loại ghi chép hàng ngày memory/YYYY-MM-DD.md. Còn các file kiến thức dài hạn như MEMORY.md, decisions/, lessons/ thì không bị ảnh hưởng bởi suy giảm theo thời gian.",
    # Block 47
    (47, 0): "Điều này khá giống cách con người nhớ, những điều quan trọng thì ghi nhớ mãi, dòng chảy hàng ngày theo thời gian phai nhạt, cái suy giảm đi là nhiễu, cái lắng đọng lại là phán đoán.",
    # Block 48
    (48, 0): "remote.batch + cache",
    # Block 49
    (49, 0): "Hai tham số này chủ yếu tiết kiệm thời gian, tiết kiệm tiền, remote.batch thực hiện embedding theo lô, giảm số lần request, hiệu quả hơn. cache tái sử dụng tối đa các chunk đã được nhúng, tránh tiêu tốn token lặp lại.",
    # Block 50
    (50, 0): "Lobster lấy file local làm lõi bộ nhớ, mỗi ngày đều thêm xóa sửa lượng lớn file, bật hai mục này là rất cần thiết, có thể giảm rõ rệt các lần gọi không cần thiết.",
    # Block 51
    (51, 0): "Sau khi cấu hình xong, lần khởi động đầu tiên có thể cần một chút thời gian để hoàn thành index ban đầu, điều này là bình thường. Sau đó là cập nhật tăng dần, chỉ khi file có thay đổi mới kích hoạt nhúng lại, sử dụng hàng ngày gần như không cảm nhận được quá trình index đang chạy.",
    # Block 52
    (52, 0): "Lúc này trong cuộc trò chuyện với Lobster, chỉ cần kích hoạt mô tả liên quan đến tìm kiếm bộ nhớ, tìm kiếm nội dung, memory_search tích hợp sẽ bắt đầu thực thi, quy trình đại khái như sau:",
    # Block 53
    (53, 0): "Cấu hình xong nhớ restart gateway, cấu hình embedding provider không phải hot-update.",
    # Block 54
    (54, 0): "Theo cấu trúc file bộ nhớ và chu kỳ ghi nhớ xây dựng ở hai bài trước, rất khớp với Memory Core của Lobster. Ghi chép rõ ràng đầy đủ, chiến lược tìm kiếm cấu hình xong, cảm nhận về hiệu quả triệu hồi bộ nhớ cải thiện rất rõ. Có thể để Lobster xem log memory_search mà nó tự gọi để so sánh phân tích hiệu quả.",
    # Block 55: heading2
    (55, 0): "QMD: Quản lý bộ nhớ tiềm năng hơn",
    # Block 56
    (56, 0): "Tiếp theo nói về một phương án khác mà tôi thực tế đang sử dụng.",
    # Block 57
    (57, 0): "Trong memory backend của OpenClaw, ngoài Memory Core mặc định, còn có một tùy chọn khác: ",
    (57, 1): "QMD ",
    (57, 2): "(Quick Markdown Database).",
    # Block 58
    (58, 0): "Peter - cha đẻ của Lobster cũng đã đề cập trong tweet:",
    # Block 59
    (59, 0): "If the stock memory feature isn't great for you, check out the qmd memory plugin!",
    # Block 60
    (60, 0): "Câu này thể hiện rất rõ ràng, trong phản hồi thực tế mà team chính thức thu thập được, hiệu quả bộ nhớ của QMD có thể tổng thể tốt hơn phương án native, là một lộ trình bộ nhớ Opt-in được chính thức chấp nhận, khác với các phương án bộ nhớ khác của cộng đồng.",
    # Block 61
    (61, 0): "Từ trải nghiệm thực tế của tôi, ở giai đoạn hiện tại QMD trên Mac mini kết nối với OpenClaw vẫn có một số lỗi, không thể kết luận đơn giản rằng chắc chắn mạnh hơn Memory Core, nhưng nó có vài đặc điểm mà tôi rất kỳ vọng:",
    # Block 62 (ordered, multi-element)
    (62, 0): "Phù hợp với lý niệm của OpenClaw ",
    (62, 1): ": file Markdown là nguồn thông tin chân thực duy nhất, chỉ có tầng tìm kiếm, bộ nhớ white-box, có thể kiểm tra và xác minh",
    # Block 63
    (63, 0): "Không phá vỡ hệ thống file hiện có ",
    (63, 1): ": chuyển backend sang, hình thức và cấu trúc file bộ nhớ không cần thay đổi, cũng không tự nhiên thêm tầng trừu tượng black-box",
    # Block 64
    (64, 0): "Phù hợp cho tìm kiếm thống nhất xuyên App ",
    (64, 1): ": có thể trên một máy chủ, quản lý riêng Memory của Lobster và kho ghi chú Obsidian, nhưng tìm kiếm liên hợp",
    # Block 65
    (65, 0): "Điểm thứ ba đặc biệt hấp dẫn tôi. Trong bài đầu tiên tôi đã giới thiệu file bộ nhớ Lobster của tôi chia thành hai phần, nội bộ và gắn ngoài: ngoài các file trong thư mục memory/, còn có ObsidianVault ghi chú Obsidian. Obsidian chủ yếu chứa các bài viết dài như nghiên cứu, tổng kết, không phù hợp cho tìm kiếm bộ nhớ hàng ngày gọi thường xuyên, mà chủ yếu tồn tại cho tìm kiếm chuyên sâu trong các tình huống cụ thể.",
    # Block 66
    (66, 0): "Thiết kế multi-Collection của QMD rất phù hợp để quản lý thống nhất các nội dung từ nguồn khác nhau, vừa có thể tìm kiếm chung, vừa giữ nguyên ranh giới riêng.",
    # Block 67
    (67, 0): "Trải qua nhiều phiên bản cập nhật, dù giai đoạn hiện tại QMD kết nối vào OpenClaw còn hơi vất vả, nó vẫn là một lộ trình rất tiềm năng trong hệ thống bộ nhớ native của Lobster, đáng theo dõi.",
    # Block 68: heading3
    (68, 0): "Chế độ query của QMD",
    # Block 69
    (69, 0): "QMD đã tăng cường native ở cả hai đầu trước và sau tìm kiếm hỗn hợp:",
    # Block 70
    (70, 0): "Mở rộng truy vấn",
    # Block 71
    (71, 0): "Chế độ query của QMD sẽ mở rộng truy vấn của người dùng trước, có một mô hình nhỏ chuyên phụ trách việc này.",
    # Block 72
    (72, 0): "Ví dụ",
    # Block 73
    (73, 0): "Thiết kế này giải quyết một vấn đề rất thực tế, khi chúng ta tìm kiếm, từ nghĩ ra chưa chắc là từ đã dùng khi ghi chép. Dùng một truy vấn để tìm, rất dễ bỏ sót nội dung vì diễn đạt không khớp. Mở rộng thành nhiều biến thể, tương đương thả nhiều lưới bắt cá, xác suất bắt được cá tự nhiên tăng lên.",
    # Block 74
    (74, 0): "Reranker xếp hạng lại",
    # Block 75
    (75, 0): "QMD còn thực hiện một lần xếp hạng lại mức độ liên quan mạnh hơn trên kết quả ứng viên. Ở đây có mô hình nhỏ chuyên dụng, dùng Cross-Encoder ghép nối truy vấn và kết quả mã hóa, tính toán mức độ khớp ngữ nghĩa chi tiết hơn, hiệu quả xếp hạng tinh tốt hơn đáng kể so với chấm điểm trọng số đơn giản.",
    # Block 76: heading3
    (76, 0): "Chế độ multi-Collection",
    # Block 77
    (77, 0): "Memory Core giống kiểu quét đệ quy đường dẫn đơn lẻ hơn, QMD là thu thập song song nhiều Collection. Điều này rất tiện lợi cho chúng ta đưa vào hoặc loại bỏ các file Markdown từ nguồn khác nhau trong cùng một hệ thống tìm kiếm, đồng thời giữ tính cách ly và khả năng mở rộng riêng.",
    # Block 78
    (78, 0): "Như vậy rất trực quan biết collection tương ứng với những file nào, có thể chỉ định tìm kiếm ghi chú nghiên cứu chỉ trong obsidian collection, cũng có thể tìm toàn cục, các tình huống khác nhau chuyển đổi theo nhu cầu.",
    # Block 79: heading3
    (79, 0): "Hướng dẫn cấu hình QMD",
    # Block 80
    (80, 0): "Khi kết nối lần đầu, có thể tham khảo cấu hình openclaw.json dưới đây:",
    # Block 81
    (81, 0): "Tạo Collection",
    # Block 82
    (82, 0): "Sau khi cài dependency cần thiết (ví dụ bun và qmd), khi includeDefaultMemory đặt là true, OpenClaw sau khi khởi động lại sẽ tự động tạo cấu hình index mặc định, bao gồm ba collection này:",
    # Block 83
    (83, 0): "Nếu thêm đường dẫn bổ sung qua paths, ví dụ thư mục Obsidian, cũng sẽ tự động tạo collection tương ứng theo cấu hình:",
    # Block 84
    (84, 0): "Tạo nhúng",
    # Block 85
    (85, 0): "Sau khi cấu hình lần đầu, cần đợi QMD thực hiện embed toàn bộ file, quá trình này tùy lượng file cần một chút thời gian. Xong rồi thì không cần quan tâm nữa, QMD sẽ theo update.interval định kỳ cập nhật tăng dần, file mới thêm hoặc sửa đổi tự động đồng bộ.",
    # Block 86
    (86, 0): "QMD có ba mô hình nhỏ: mở rộng truy vấn, Reranker xếp hạng lại, và Embedding ở đây. Mặc định là embeddinggemma, trong ngữ cảnh tiếng Trung tôi khuyên đổi sang Qwen3-embedding-0.6b, ngữ nghĩa tiếng Trung chính xác hơn.",
    # Block 87
    (87, 0): "Sau khi embedding hoàn tất, trong cuộc trò chuyện chỉ cần kích hoạt mô tả liên quan đến tìm kiếm bộ nhớ, memory_search sẽ gọi khả năng tìm kiếm của QMD. Có thực thi thành công hay không, cũng như toàn bộ quy trình tìm kiếm và hiệu quả cuối cùng, cũng có thể để Lobster tự xem log, so sánh đánh giá.",
    # Block 88: heading2
    (88, 0): "Sự thỏa hiệp của QMD",
    # Block 89
    (89, 0): "Khá đáng tiếc là, searchMode = \"query\" - chế độ tìm kiếm lý tưởng nhất, trên Mac mini luôn có lỗi không lấp hết được.",
    # Block 90
    (90, 0): "Trước phiên bản 2.0, query sẽ crash trực tiếp do bug liên quan Metal trên chip Apple. Lúc đó tôi tưởng cấu hình mình bị sai chỗ nào, mày mò hai ngày, phát hiện ra là lỗi upstream cũng không tránh được. Còn có vấn đề khoảng trắng tiếng Trung gây search trả về rỗng cũng rất vô lý. Đến sau 2.0, ổn định hơn nhiều, query được rồi, nhưng lại gặp vấn đề khác, mỗi lần gọi tốn quá lâu.",
    # Block 91
    (91, 0): "Nguyên nhân gốc là ở chế độ CLI, mỗi lần chạy query đều phải cold start từ đầu, tải lại toàn bộ mô hình liên quan đến mở rộng truy vấn và Reranker. Trên Mac mini, cold start này mất hơn hai mươi giây. Kết quả thường là chưa chạy xong đã timeout, rồi fallback về Memory Core, loay hoay một vòng, công cốc.",
    # Block 92
    (92, 0): "Nên giai đoạn hiện tại tôi đặt searchMode thành vsearch, lấy tìm kiếm vector làm chủ, đảm bảo ổn định sử dụng được trước.",
    # Block 93
    (93, 0): "Còn query - con đường chất lượng cao nhưng chi phí cao, tôi chọn đi vòng bằng cách khác.",
    # Block 94: heading3
    (94, 0): "MCP Wrapper",
    # Block 95
    (95, 0): "Biến QMD query từ chạy được thành dùng được",
    # Block 96
    (96, 0): "Team QMD có lẽ cũng nhận ra ảnh hưởng của cold start đến tính thực dụng của query, trong phiên bản mới cung cấp chế độ MCP server. Giải pháp là, đã biết CLI mỗi lần cold start rất chậm, thì cho service chạy thường trực, chỉ khởi tạo một lần. Tôi thấy tính năng mới này lập tức nâng cấp.",
    # Block 97
    (97, 0): "Thực tế trải nghiệm, cách này tăng tốc query rất rõ rệt, từ hơn hai mươi giây giảm thẳng xuống khoảng một giây.",
    # Block 98
    (98, 0): "Vấn đề lại tới, phiên bản mới nhất của OpenClaw cũng chưa tích hợp cách đi qua MCP của QMD. Nhưng tôi rất muốn dùng được, may là cái Mac mini này đều do Lobster quản, nên đi đường vòng:",
    # Block 99
    (99, 0): "Chạy thường trực một QMD MCP Server ở local, tự khởi động cùng máy",
    # Block 100
    (100, 0): "Viết một wrapper script làm MCP Client để gọi service",
    # Block 101
    (101, 0): "Trong Lobster đóng gói một skill qmd-query-pro, chuyên được kích hoạt trong tình huống tìm kiếm chuyên sâu",
    # Block 102
    (102, 0): "Như vậy, chuỗi tìm kiếm chính chạy vsearch giữ ổn định, khi thực sự cần tìm kiếm chuyên sâu, query cũng có thể lên bất cứ lúc nào.",
    # Block 103
    (103, 0): "Đường chính HTTP + stdio dự phòng",
    # Block 104
    (104, 0): "QMD MCP service có hai phương thức giao tiếp. Chế độ stdio đơn giản hơn, nhưng thực tế trải nghiệm luôn có vài vấn đề, stdin/stdout dễ xung đột, thỉnh thoảng dữ liệu bị lộn xộn. HTTP ổn định hơn nhiều, nhưng service cũng có thể thỉnh thoảng bị sập. Nên HTTP ưu tiên, stdio dự phòng, giữ cả hai đường.",
    # Block 105
    (105, 0): "Quy trình cốt lõi đại khái như sau:",
    # Block 106
    (106, 0): "Tự khởi động",
    # Block 107
    (107, 0): "Đã làm service thường trực, cách tiện nhất trên Mac là giao cho launchd, tự động kéo lên khi bật máy, không cần lúc sử dụng mới kiểm tra service có bình thường không.",
    # Block 108
    (108, 0): "Trước tiên viết script khởi động ~/.openclaw/scripts/start-qmd-mcp.sh :",
    # Block 109
    (109, 0): "Sau đó viết launchd plist:",
    # Block 110
    (110, 0): "Load và khởi động:",
    # Block 111
    (111, 0): "KeepAlive đặt là true, service crash cũng tự khởi động lại, dùng không cần quan tâm.",
    # Block 112
    (112, 0): "qmd-query-pro skill",
    # Block 113
    (113, 0): "Phần cuối cùng là đóng gói một skill chuyên dụng trong Lobster, để nó tìm kiếm chuyên sâu trong tình huống chỉ định, hoặc khi memory_search không tìm được nội dung hiệu quả, thì thay thế lên, tìm kiếm liên hợp.",
    # Block 114
    (114, 0): "Hiệu quả cuối cùng",
    # Block 115
    (115, 0): "Qua qmd status, có thể trực tiếp xem collection, số lượng file, trạng thái vector, mô tả ngữ cảnh và các thông tin khác",
    # Block 116
    (116, 0): "Qua qmd query, tôi cũng có thể tìm, qua OpenClaw + skill, Lobster cũng có thể tìm.",
    # Block 117
    (117, 0): "Như vậy rất thoải mái. Tôi và Lobster trên cùng một máy, chia sẻ cùng một hệ thống kiến thức bộ nhớ Markdown, nó viết tôi có thể tìm, tôi viết nó có thể tra.",
    # Block 118
    (118, 0): "Kể cả sau này thêm vài agent nữa, thêm bộ nhớ riêng vào cũng không bị loạn, vì nền tảng toàn là file, mọi trạng thái luôn có thể đọc và xác minh, cảm giác đây mới thực sự là File Over App.",
    # Block 119: heading2
    (119, 0): "Lời kết",
    # Block 120
    (120, 0): "Các bạn mới tiếp xúc Lobster, cấu hình embedding và tìm kiếm hỗn hợp của Memory Core cho tốt, dùng ngay được, ổn định cao, đã có thể giải quyết đại đa số vấn đề bộ nhớ. Khi chạy một thời gian, file bộ nhớ ngày càng nhiều, có ý muốn tìm tòi, thì có thể cùng nhau thử QMD, chất lượng tìm kiếm của QMD có trần cao hơn, tính linh hoạt multi-Collection là thứ Memory Core không thể cung cấp.",
    # Block 121
    (121, 0): "Tôi từ khi QMD mới Opt-in đã bắt đầu kết nối, đến crash quay về Memory Core, đến gần đây kết nối lại QMD và thực hiện khá nhiều tùy chỉnh. Tuy phần lớn mang tính thí nghiệm, lỗi cũng không ít, nhưng cập nhật phiên bản thực sự chăm chỉ, trải nghiệm tổng thể, tôi cho rằng QMD là một phương án quản lý và tìm kiếm tài liệu quy mô lớn dựa trên local rất tuyệt vời, cũng là người bạn đồng hành rất tốt cho hệ thống xây dựng bộ nhớ dựa trên file của Lobster.",
    # Block 122
    (122, 0): "Bài tiếp theo sẽ nói về cơ chế slot tùy chỉnh Context Engine được cập nhật trong các phiên bản gần đây của Lobster, để tối ưu quản lý ngữ cảnh, nâng cao chất lượng bộ nhớ trong Session, có thể cải thiện rõ rệt khả năng hiểu liên tục của Lobster trong cuộc trò chuyện dài. Context engineering cũng đặt nền tảng dữ liệu có cấu trúc tốt hơn cho việc nâng cao chất lượng các tác vụ như phản tư của Lobster sau này.",
}

# Stats
total_text_runs = 0
translated_runs = 0
kept_runs = 0

for bi, block in enumerate(trans['blocks']):
    for ei, el in enumerate(block['elements']):
        if el['type'] != 'text_run':
            continue
        total_text_runs += 1
        key = (bi, ei)
        if key in translations:
            el['content'] = translations[key]
            translated_runs += 1
        else:
            # Not in map - check if it needs translation
            if has_chinese(el['content']) and not is_keep(el['content']):
                print(f"WARNING: Untranslated Chinese in Block {bi} el {ei}: {el['content'][:80]}")
            kept_runs += 1

# Add spaces between adjacent Vietnamese text_runs
for block in trans['blocks']:
    elements = block['elements']
    for i in range(len(elements) - 1):
        el = elements[i]
        next_el = elements[i + 1]
        if el['type'] == 'text_run' and next_el['type'] == 'text_run':
            # Add space if current doesn't end with space and next doesn't start with space
            # and both have actual text content
            curr = el['content']
            nxt = next_el['content']
            if curr and nxt and not curr.endswith(' ') and not nxt.startswith(' '):
                # Check if it's Vietnamese text that needs spacing
                if not curr[-1] in '。，、；：！？）】》' and not nxt[0] in '。，、；：！？（【《':
                    # Don't add space before punctuation
                    if not nxt[0] in '.,;:!?)]}>' and not curr[-1] in '([{<':
                        el['content'] = curr + ' '

print(f"\nTotal text_runs: {total_text_runs}")
print(f"Translated: {translated_runs}")
print(f"Kept as-is: {kept_runs}")

with open('_art_b5_9_trans.json', 'w', encoding='utf-8') as f:
    json.dump(trans, f, ensure_ascii=False, indent=2)

print("Saved to _art_b5_9_trans.json")
