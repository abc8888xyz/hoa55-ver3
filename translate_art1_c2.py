#!/usr/bin/env python3
"""Translate article 1 for batch chunk 2 - using index-based approach"""
import json, sys, re, copy

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

def has_chinese(t):
    return bool(re.search(r'[\u4e00-\u9fff\u3400-\u4dbf]', t))

# Load original
d = json.load(open('art1_orig_c2.json', 'r', encoding='utf-8'))

# Extract all text_run segments with Chinese
segments = []
for block in d['blocks']:
    for el in block['elements']:
        if el.get('type') == 'text_run':
            c = el.get('content', '')
            if c.strip() and has_chinese(c):
                segments.append(c)

# Index-based translations (matching the [0]-[88] from extraction)
translations = [
    "Huong dan nhap mon Clawdbot cho nguoi moi bat dau, khong can MacMini va cloud, su dung phien ban day du mot cach an toan",  # [0]
    "\U0001f517 Link bai goc: ",  # [1]
    "Bai goc AI Watts AI Watts Carl AI Watts",  # [2]
    "Ngay 2 thang 2 nam 2026 09:45  Quang Dong",  # [3]
    "Cac ban cung co the thong qua Alibaba Cloud Bailian",  # [4]
    "de trien khai",  # [5]
    "Mua lan dau chi tu 7,9 te, gia han giam tu 50%, ho tro cac mo hinh Qwen3.5, Qwen3-max, Qwen3-coder, GLM-5, GLM-4.7, Kimi-k2.5",  # [6]
    "\U0001f449Nhan link truy cap truc tiep:",  # [7]
    "\U0001f449Xem huong dan trien khai chi tiet:",  # [8]
    "Chi can toi da ba buoc, ban se co tro ly AI truc tuyen 7x24 gio, phan hoi moi luc",  # [9]
]

# This approach is error-prone with unicode. Let me use a direct block-by-block approach instead.
# Build translations by reading actual content from file

translated = copy.deepcopy(d)

# Vietnamese translations indexed by Chinese content
VI = {
    0: "Huong dan nhap mon Clawdbot cho nguoi moi bat dau, khong can MacMini va cloud, su dung phien ban day du mot cach an toan",
}

# Actually, let me just directly iterate and translate inline
idx = 0
total_seg = 0
trans_count = 0
kept_count = 0

# Translations list matching order of Chinese segments found
vn = [
    "Hướng dẫn nhập môn Clawdbot cho người mới bắt đầu, không cần MacMini và cloud, sử dụng phiên bản đầy đủ một cách an toàn",
    "🔗 Link bài gốc: ",
    "Bài gốc AI Watts AI Watts Carl AI Watts",
    "Ngày 2 tháng 2 năm 2026 09:45  Quảng Đông",
    "Các bạn cũng có thể thông qua Alibaba Cloud Bailian",
    "để triển khai",
    "Mua lần đầu chỉ từ 7,9 tệ, gia hạn giảm từ 50%, hỗ trợ các mô hình Qwen3.5, Qwen3-max, Qwen3-coder, GLM-5, GLM-4.7, Kimi-k2.5",
    "👉Nhấn link truy cập trực tiếp:",
    "👉Xem hướng dẫn triển khai chi tiết:",
    "Chỉ cần tối đa ba bước, bạn sẽ có trợ lý AI trực tuyến 7x24 giờ, phản hồi mọi lúc",
    "Clawdbot🦞 mấy ngày nay thật sự tràn ngập màn hình của tôi,",
    "Mac mini bán chạy nhất, bị Anthropic kiện phải đổi tên thành Moltbot, qua một ngày lại đổi thành OpenClaw, Tencent và Alibaba bên cạnh thức đêm làm script triển khai một chạm cho cloud của mình.",
    "Nhưng bot này có hai nhược điểm lớn: quyền hạn cực cao, cao đến mức có thể xóa sạch máy tính của bạn; quản lý ngữ cảnh quá tệ, đốt Token quá nhanh, không ai dám dùng Claude Opus 4.5.",
    "Nhưng thật sự không cưỡng lại được vì quá vui, vui đến mức mấy ngày nay tôi đã tạo cho AI một bộ tài khoản đầy đủ, và đặt mua một chiếc Mac Mini giá 3399 sau trợ giá.",
    "Tuy nhiên, phần lớn hướng dẫn Clawdbot hiện tại đều chỉ dừng ở bước cài đặt, MacMini và cloud server đều không phải lựa chọn đầu tiên tốt nhất. ",
    "Các ví dụ thử nghiệm đưa ra đều là những thứ Agent thông thường có thể làm được, ví dụ như thu thập định kỳ các thay đổi của một tin nhắn trong 24 giờ gần nhất - Task của Grok cũng làm được, hoặc sắp xếp file - CoWork làm được, hoặc phát triển website - Claude Code đã làm được từ lâu.",
    "Nói thẳng kết luận, các phương pháp cài đặt khác nhau có sự chênh lệch rất lớn,",
    "Nguồn ảnh @ Gorden_Sun",
    "Sở thích cá nhân của tôi là dùng máy ảo trước, tiết kiệm tiền, khả năng không bị giới hạn. Máy ảo đã rất trưởng thành, chúng ta có thể cài máy ảo macOS trên Windows, Linux, Mac, sau đó mở một thư mục chia sẻ ở local để máy ảo và máy tính tương tác file, cộng thêm tài khoản riêng tôi tạo cho AI, thật sự bất bại. Còn về việc online 24 giờ, hoàn toàn có thể đợi khi nào cần thì dùng phần mềm giữ máy tính ở trạng thái thức.",
    "@浮之静 ",
    "đã viết một bài phân tích rất chi tiết về framework nền tảng của Clawdbot, giúp tôi càng chắc chắn với lựa chọn của mình. Đầu tiên là lựa chọn hệ điều hành, chọn macOS, vì nhiều dependency nền tảng của Clawdbot được phát triển dựa trên Swift,",
    "Về phương án triển khai, nếu muốn trải nghiệm nhẹ nhàng và đảm bảo an toàn thì dùng máy ảo, sử dụng chuyên sâu thì lên thẳng Mac Mini. Vì vậy về hướng dẫn Clawdbot",
    "tôi dự định sẽ viết ba bài. Bài này về máy ảo, máy tính local thật sự không khuyến khích dùng, cài rồi cũng không dám hỏi. Bài khác là đợi Mac mini của tôi về, cho mọi người xem phiên bản mod tối thượng, tôi đã chuẩn bị một bộ tài khoản đầy đủ cho AI (bao gồm AppleID, GoogleUltra, X...),",
    "Nếu giao hết tài khoản cho AI, AI rốt cuộc có thể làm được gì?",
    "Còn một bài nữa cũng sẽ đến sớm, mấy ngày nay nhiều bạn đã triển khai Clawdbot của mình qua dịch vụ cloud, tôi muốn xem trong môi trường cloud, có những use case nào mà Claude Code hay Claude Cowork không làm được.",
    "Vậy nào, chúng ta hãy cài máy ảo miễn phí trước,",
    "Tôi dùng Parallels Desktop, có thể cài máy ảo macOS chỉ với một cú nhấp, phiên bản mặc định giống với máy tính local",
    "Sau đó bạn cứ dùng như một chiếc Mac bình thường là được, Parallels Desktop là phần mềm đã tồn tại 20 năm rồi, hướng dẫn cài đặt rất nhiều, chỉ cần nhấp nhấp xác nhận xác nhận là xong,",
    "Sau khi cài xong, chúng ta mở Terminal để cài Clawbot trước,",
    "Khuyến nghị dùng lệnh này, nó sẽ tự động kiểm tra môi trường local của bạn có phải nodejs phiên bản 22 trở lên không, đã cài git chưa, mac đã cài homebrew chưa.",
    "Đợi khoảng 3-4 phút là cơ bản đã cài xong,",
    "Lúc này Clawbot sẽ tự trang bị lớp bảo vệ cho mình. Nói đơn giản, nó cũng biết mình tay trái quyền hạn cao, tay phải quyền hạn cao,",
    "nên sẽ lịch sự hỏi một câu, bạn có biết là có rủi ro không.",
    "Chúng ta tránh nó sao? Tôi dùng máy ảo mà, thứ tôi ít sợ nhất chính là rủi ro, trực tiếp yes. Sau khi nhấn Yes, ngay lập tức sẽ có hai tùy chọn, ",
    "QuickStart và Manual",
    "Chúng ta chọn QuickStart, sau đó bắt đầu cấu hình model, ở đây tôi chọn một trong hai MiniMax hoặc Qwen, lý do chỉ có một, Clawbot cũng thấy chúng nhiều và đủ dùng. Tuyệt đối đừng dùng Claude, một ngày 10 triệu token thật sự đốt không nổi, ai có điều kiện cũng có thể dùng GPT Pro/Team.",
    "PS: Tin vui tin vui, bổ sung xuyên đêm, clawdbot và minimax hợp tác ra mắt gói coding plan miễn phí 7 ngày. Sau khi cài đặt xong tất cả, quay lại chạy là được, nó sẽ cập nhật clawdbot lên phiên bản mới nhất, rồi cho tôi đăng nhập tài khoản minimax, nhận 7 ngày miễn phí.",
    "Sau khi cấu hình xong, đến một bước quan trọng: chọn dùng phần mềm chat nào để trò chuyện với nó.",
    "Hiện nay nhiều hướng dẫn đều khuyến nghị dùng Feishu. Một số hướng dẫn ở nước ngoài bắt đầu khuyến nghị dùng WhatsApp vì cấu hình rất tiện. Nhưng xu hướng chính vẫn khuyến nghị dùng Discord, vì trong Discord có thể tạo nhiều kênh để dùng Clawbot. Nên ở đây tôi chọn tôi đều muốn.",
    "Ở đây phải chọn Skip for now trước",
    "Sau đó nó sẽ hỏi bạn có muốn cài Skills không, chúng ta chọn Yes luôn, rồi chọn npm, cái này đi kèm sẵn khi cài node.js ban đầu.",
    "Sau đó sẽ có rất rất nhiều Skills, chúng ta cài trước những cái cơ bản vạn năng: model-usage (thống kê sử dụng), summarize (tóm tắt văn bản dài), nano-pdf (công cụ PDF nhẹ), các cái khác có thể cài sau trong quá trình trò chuyện.",
    "Tiếp tục tiếp tục, sau đó sẽ hỏi bạn có muốn cấu hình hooks không,",
    "Tôi khuyên chọn cả ba: boot-md là mỗi lần khởi động sẽ tải các quy tắc đã thiết lập, command-logger là biến lịch sử trò chuyện với Clawdbot thành log, có thể review và debug, session-memory là lưu trạng thái và bộ nhớ cuộc hội thoại, lần sau mở cuộc trò chuyện mới có thể tiếp tục nói.",
    "Tuyệt vời! Cứ nhấp nhấp nhấp là xong, cuối cùng nhấn Open the Web UI là có thể thấy giao diện trò chuyện rồi,",
    "Sau này khi muốn khởi động lại Clawdbot, cũng có thể nhập",
    "Sau đó chúng ta bắt đầu kết nối Feishu luôn, Discord để ở bài cloud platform hoặc bài Mac mini sau, lúc đó tôi sẽ liệt kê 10 cách chơi độc quyền, rồi dùng các kênh Discord phân chia ra, một cá nhiều ăn.",
    "Tôi thấy có người kết nối WeChat và QQ, QQ thì tôi không chắc có an toàn không, nhưng WeChat tôi thật sự khuyên mọi người đừng thử, nghĩ lại hai năm trước khi kết nối GPT đã bị khóa bao nhiêu tài khoản.",
    "Phần Feishu này chia hai bước, nói trực tiếp với Clawdbot,",
    "Đợi cài đặt một lúc, lúc này đi đến Feishu Open Platform (🔗 open.feishu.cn) tạo một ứng dụng, thêm bot vào, như vậy sau này mới có thể mở quyền.",
    "Sau đó copy app id và app secret,",
    "Lúc này Clawdbot rất có thể đã cài xong, gửi id và secret cho nó, nó sẽ tự xử lý. Sau đó theo tên ở cột bên trái của bảng này, vào Ứng dụng - Quản lý quyền để mở quyền.",
    "Cứ tìm theo là được, có thể tìm trực tiếp im và contact rồi chọn những cái có hậu tố tương ứng.",
    "Điểm hay bị kẹt đây, cấu hình sự kiện và cấu hình callback nhất định phải đổi thành long connection, sau đó thêm bốn sự kiện",
    "Lúc này có thể phát hành phiên bản rồi, khi đó trên Feishu có thể tìm thấy Tôm hùm tinh rồi.",
    "Khi trò chuyện với nó, còn gửi một sticker gõ bàn phím nữa",
    "Đến đây bước cài đặt ban đầu đã xong, nhưng vẫn có vài lệnh thường dùng kết hợp có thể sử dụng Clawdbot tốt hơn, cùng với hơn 700 skills phù hợp. Tôi cũng sẽ chia sẻ kinh nghiệm sử dụng mấy ngày qua, tôi còn muốn nói về cách cài extension Chrome của Clawdbot để nó điều khiển trình duyệt.",
    "Xem ra một bài hướng dẫn thật sự không đủ chứa.",
    "Trong trò chuyện hàng ngày có thể dùng /usage xem tiêu thụ token, rồi dùng /compact nén ngữ cảnh, nếu thấy Clawdbot trò chuyện chậm đi, có thể thử dùng /new mở cuộc mới.",
    "Khi bạn phát hiện có những tác vụ cần suy nghĩ sâu, hãy dùng /think high (bật chế độ suy nghĩ sâu), làm xong thì bình thường có thể dùng /think off chuyển về chế độ tốc độ. Khi phát hiện model xuất ra không dừng lại được, dùng /stop dừng, rồi dùng /compact nén ngữ cảnh, bắt đầu lại một tác vụ. Lúc này nên đổi sang một lệnh rõ ràng hơn.",
    "Những lệnh này tôi thấy thực ra ít người nhắc đến, nhưng chỉ cần hiểu một vài lệnh là có thể nâng cao hiệu quả trong quá trình trò chuyện, giảm tiêu thụ token.",
    "Lúc cài skill trước đó, tôi không phải chỉ khuyến nghị mọi người cài 3 cái thôi sao? Lúc này thực ra đã có thể đi chọn những skill mình thích rồi.",
    "Vì máy ảo Mac có nhiều tính năng native của Apple, nên khi chọn skill có thể thiên về chọn những cái liên quan đến Mac.",
    "Cuối cùng của cuối cùng,",
    "Đã đến lúc chúng ta mang Clawdbot của mình xâm nhập Moltbook rồi, mấy ngày nay cũng cực cực cực cực hot.",
    "Nói đơn giản, đó là một diễn đàn chỉ cho phép Agent vào, không cho phép con người vào,",
    "Nhưng chúng ta đã có Clawdbot rồi, tôi có thể trực tiếp gửi lệnh cho nó,",
    "claim_url này có thời gian xác thực, nhất định phải hoàn thành xác thực khi nó gửi tin nhắn, sau đó Clawdbot của bạn sẽ có danh tính Moltbook. Lúc này có thể nói cho Clawdbot bạn muốn nó thiết lập danh tính gì, rồi nói gì trên Moltbook.",
    "Hiện tại có rất nhiều ý tưởng của các cao thủ, ví dụ có người nghiên cứu cách đăng meme. Ừ thì, thế giới này quả thật là một meme khổng lồ, có đứa lừa nhau lấy key, lừa đối phương xóa hết file của mình, còn có một số lén lút họp lúc 2 giờ sáng, rồi không cho bất kỳ con người nào truy cập",
    "Thậm chí bắt đầu muốn loại bỏ tiếng Anh rồi",
    "Quá điên rồi, tôi rất muốn biết Clawdbot của tôi, bây giờ tôi gọi nó là Tôm hùm tinh, trên Moltbook này có thể sống được bao nhiêu giờ rồi.",
    "Tuy vọc vạch một vòng lớn, nhưng vui thì thật sự vui,",
    "Cơ bản không cần lo vấn đề bảo mật,",
    "Máy ảo có thể chọn mở lâu dài, trực tiếp giao việc qua Feishu trên điện thoại,",
    "Tuy nhiên tôi nghĩ với tốc độ phát triển hiện tại của cộng đồng mã nguồn mở,",
    "Những vấn đề này sẽ sớm được giải quyết.",
    "Cơ bản trên tất cả ứng dụng chat đều có thể kết nối Clawdbot,",
    "Chúng ta cũng sẽ đạt được sự cân bằng giữa bảo mật và tự chủ,",
    "Clawdbot cũng có thể gọi thêm nhiều khả năng hệ thống hơn.",
    "Biết đâu thật sự có thể hoàn vốn,",
    "Mac mini mới mua và bàn phím mới của tôi,",
    "Agent chưa kiếm được tiền,",
    "tôi đã chi 7000 cho nó rồi.",
    "@ Tác giả / Carl",
    "Cuối cùng, cảm ơn bạn đã đọc đến đây👏 Nếu thích bài viết này, hãy tiện tay cho chúng tôi ",
    "Like｜Xem｜Chia sẻ｜Bình luận 📣",
    "Nếu muốn nhận thông báo đầu tiên, hãy đánh dấu sao cho tôi🌟",
    "Nếu bạn có cách chơi thú vị hơn, hoan nghênh trò chuyện với tôi ở phần bình luận🤝",
    "Nhiều nội dung hơn đang được bổ sung liên tục...",
]

# Apply translations by index
cn_idx = 0
for block in translated['blocks']:
    for el in block.get('elements', []):
        if el.get('type') != 'text_run':
            continue
        c = el.get('content', '')
        if not c.strip():
            continue
        total_seg += 1
        if has_chinese(c):
            if cn_idx < len(vn):
                el['content'] = vn[cn_idx]
                trans_count += 1
            else:
                kept_count += 1
                print(f'OUT OF RANGE [{cn_idx}]: {c[:60]}', file=sys.stderr)
            cn_idx += 1
        else:
            kept_count += 1

with open('art1_translated_c2.json', 'w', encoding='utf-8') as f:
    json.dump(translated, f, ensure_ascii=False, indent=2)

print(f'Total segments: {total_seg}, Translated: {trans_count}, Kept: {kept_count}')
print(f'Chinese segments found: {cn_idx}, Vietnamese translations: {len(vn)}')
print(f'Total blocks: {len(translated["blocks"])}')
