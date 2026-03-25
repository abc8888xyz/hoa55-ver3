# -*- coding: utf-8 -*-
"""Translate _art_b5_10_orig.json Chinese -> Vietnamese"""
import json, sys, copy

sys.stdout.reconfigure(encoding='utf-8')

with open('_art_b5_10_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Translation map: Chinese text -> Vietnamese text
# We translate element by element, preserving structure/style/links
# For elements with inline_code or links, we keep those intact

trans = {}

# Block 0 - page title
trans[('0','0')] = "Lộc Đạo: OpenClaw không tốt? Đó là vì bạn chưa dùng Cursor để ma cải Tôm Hùm Lớn \"Tà Tu Đại Pháp Tập 1\""

# Block 1
trans[('1','0')] = "Loạt hướng dẫn | Zero code | Phù hợp cho tất cả những ai muốn sử dụng tốt OpenClaw"

# Block 2 - multiple elements
trans[('2','0')] = "Điều kiện tiên quyết"
trans[('2','1')] = ": Đã cài đặt OpenClaw và cập nhật lên phiên bản "
trans[('2','2')] = "2.9"
trans[('2','3')] = ", đã hoàn thành onboard, nếu chưa hoàn thành hãy xem "
trans[('2','4')] = "hướng dẫn"

# Block 3 - heading1
trans[('3','0')] = "Tập 1: Cho Tôm Hùm Lớn (OpenClaw) sở hữu trí nhớ \"quá mắt không quên\""

# Block 4 - heading2
trans[('4','0')] = "🛑 Đừng vội đập bàn phím, nghe tôi nói đã"

# Block 5
trans[('5','0')] = "Nhiều người lần đầu dùng OpenClaw (mà chúng ta hay gọi là \"Tôm Hùm Lớn\") đều được các cao thủ công nghệ giới thiệu."

# Block 6
trans[('6','0')] = "Trên Twitter, trong group đều tung hô: \"Chấn động! AI lại bị lật đổ rồi!\", \"AI có thể tự tiến hóa\", \"Tiêu diệt loài người chỉ là vấn đề thời gian\"."

# Block 7
trans[('7','0')] = "Thế là bạn theo trend cài một cái, hào hứng kể hết nội dung công việc cho nó, hy vọng nó ghi nhớ, kết quả......."

# Block 8
trans[('8','0')] = "Ngày hôm sau mở ra, nó quên sạch."

# Block 9
trans[('9','0')] = "Bạn: "
trans[('9','1')] = "\"Hôm qua chẳng phải đã nói rồi sao?\""

# Block 10
trans[('10','0')] = "Tôm Hùm Lớn: "
trans[('10','1')] = "\"Xin lỗi, tôi không tìm thấy ký ức liên quan.\""

# Block 11
trans[('11','0')] = "Bạn: \""
trans[('11','1')] = "???"
trans[('11','2')] = "\""

# Block 12
trans[('12','0')] = "Bực hơn nữa là, có thể nó còn treo luôn không trả lời bạn. Bạn xem trong thư mục "
trans[('12','1')] = "`~/.openclaw/workspace/memory/` "
trans[('12','2')] = "rõ ràng có một đống file ký ức, nhưng Tôm Hùm Lớn chẳng tìm được gì."

# Block 13
trans[('13','0')] = "Đừng nóng, không phải Tôm Hùm Lớn ngu, mà là engine tìm kiếm ký ức của nó chưa được khởi động."

# Block 14 - heading2
trans[('14','0')] = " Vấn đề nằm ở đâu?"

# Block 15
trans[('15','0')] = "Muốn sửa bộ não của nó, bạn phải biết bộ não nó đã trải qua gì. Hệ thống ký ức của OpenClaw thực ra đã trải qua hai giai đoạn:"

# Block 16 - heading3
trans[('16','0')] = "Thời nguyên thủy: "
trans[('16','1')] = "MEMORY.md"
trans[('16','2')] = " kỷ nguyên"  # if there's a 3rd element

# Block 17
trans[('17','0')] = "Ở phiên bản OpenClaw thời kỳ đầu (khoảng trước v2.2), cách ghi nhớ của Tôm Hùm Lớn rất nguyên thủy, chỉ là dùng văn bản thuần túy."

# Block 18
trans[('18','0')] = "Nó sẽ tạo một file "
trans[('18','1')] = "MEMORY.md"
trans[('18','2')] = " trong "
trans[('18','3')] = "workspace"
trans[('18','4')] = " của bạn. Mỗi lần bạn nói chuyện với nó, nó sẽ "
trans[('18','5')] = "đọc file này từ đầu đến cuối một lần"
trans[('18','6')] = "."

# Block 19
trans[('19','0')] = "Giống như bạn có một thư ký, bạn hỏi nó: "
trans[('19','1')] = "\"Dự án sếp nói tuần trước thế nào rồi?\" "
trans[('19','2')] = "Nó không trả lời trực tiếp, mà lôi từ trong túi ra một cuốn nhật ký 500 trang, "
trans[('19','3')] = "đọc từ trang đầu tiên"
trans[('19','4')] = ", đọc đến trang cuối cùng, rồi mới nói: "
trans[('19','5')] = "\"Ồ, ở đây nè.\""

# Block 20
trans[('20','0')] = "Điểm đau rất rõ ràng:"

# Block 21 - bullet
trans[('21','0')] = "Đắt"
trans[('21','1')] = ": Mỗi lần hội thoại đều tiêu tốn lượng Token khổng lồ."

# Block 22 - bullet
trans[('22','0')] = "Chậm"
trans[('22','1')] = ": File càng lớn, phản hồi càng chậm."

# Block 23 - bullet
trans[('23','0')] = "Ngu"
trans[('23','1')] = ": Một khi file vượt quá giới hạn ngữ cảnh của AI, hoặc báo lỗi, hoặc trực tiếp cắt bỏ ký ức phía trước."

# Block 24 - heading3
trans[('24','0')] = "Văn minh hiện đại: Giới thiệu tìm kiếm vector (RAG)"

# Block 25
trans[('25','0')] = "Sau đó phía chính thức cũng nhận ra không thể tiếp tục như vậy, nên đã đưa vào công nghệ "
trans[('25','1')] = "RAG (Retrieval-Augmented Generation)"
trans[('25','2')] = ". Nói đơn giản, là trang bị cho Tôm Hùm Lớn một \"thủ thư\"."

# Block 26
trans[('26','0')] = "Bây giờ khi bạn hỏi, nó không còn ngốc nghếch đọc cả cuốn sách nữa, mà trước tiên đi tìm "
trans[('26','1')] = "kiếm"
trans[('26','2')] = " các đoạn liên quan trong chỉ mục, chỉ đọc vài đoạn đó vào bộ não."

# Block 27
trans[('27','0')] = "Để thực hiện chức năng này, OpenClaw cung cấp hai con đường:"

# Block 28 - heading4
trans[('28','0')] = "🔴 Con đường 1: Embedding"

# Block 29
trans[('29','0')] = "OpenClaw mặc định sử dụng API đám mây của Google để xử lý ký ức."

# Block 30 - bullet
trans[('30','0')] = "Ưu điểm"
trans[('30','1')] = ": Nhanh, chính xác, server đều ở đám mây, không chiếm tài nguyên máy tính của bạn."

# Block 31 - bullet
trans[('31','0')] = "Nhược điểm"
trans[('31','1')] = ": "
trans[('31','2')] = "Tốn tiền!"
trans[('31','3')] = " Mỗi ký ức, mỗi lần tìm kiếm đều phải tính tiền. Hơn nữa dữ liệu riêng tư của bạn đều phải upload lên đám mây xử lý."

# Block 32 - heading4 with link
trans[('32','0')] = "🟢 Hướng dẫn này chọn con đường 2: "
trans[('32','1')] = "QMD (Quantum Memory Daemon)"

# Block 33
trans[('33','0')] = "Đây là một dự án mã nguồn mở độc lập trên Github, chuyên làm tìm kiếm knowledge base Markdown cục bộ."

# Block 34
trans[('34','0')] = "Chúng ta cần sửa QMD. Tại sao?"

# Block 35 - ordered
trans[('35','0')] = "Không tốn tiền. "
trans[('35','1')] = "(Tất nhiên, với tư cách là developer cao quý, chúng ta chắc chắn không phải tiếc mấy đồng phí API, chủ yếu là vì... quyền riêng tư! Đúng, là vì quyền riêng tư!)"

# Block 36 - ordered
trans[('36','0')] = "Chạy hoàn toàn cục bộ. "
trans[('36','1')] = "Chỉ cần cấu hình xong, rút dây mạng vẫn chạy được."

# Block 37 - ordered
trans[('37','0')] = "OpenClaw 2026.2.9  "
trans[('37','1')] = "đã sửa hệ thống tìm kiếm ký ức cục bộ của QMD. "

# Block 38
trans[('38','0')] = "Nguyên lý của nó là:"

# Block 39
trans[('39','0')] = "Tôm Hùm Lớn sau khi cập nhật đã khôn hơn, \"tải một lần, cả nhà dùng chung\". Chỉ cần tải model một lần, tất cả Agent đều trực tiếp tái sử dụng cache, không tải lại nữa."

# Block 40
trans[('40','0')] = "Tin xấu là"
trans[('40','1')] = ": Tính năng này là "
trans[('40','2')] = "Optional (tùy chọn)"

# Block 41
trans[('41','0')] = "Nếu bạn nâng cấp từ phiên bản cũ (trước v2.9) lên, hoặc khi cài đặt không đặc biệt chọn, file cấu hình của bạn "
trans[('41','1')] = "hoàn toàn không bật nó"
trans[('41','2')] = "."

# Block 42
trans[('42','0')] = "Tôm Hùm Lớn mặc định chạy ở \"chế độ không ký ức\", và nó "
trans[('42','1')] = "hoàn toàn không thông báo cho bạn"
trans[('42','2')] = "."

# Block 43
trans[('43','0')] = "Nghĩa là muốn bật nó, bạn phải chui sâu vào hệ thống, tìm file cấu hình ẩn "
trans[('43','1')] = "~/.openclaw/openclaw.json"
trans[('43','2')] = ", thêm mục cấu hình thủ công, rồi phải đổi "
trans[('43','3')] = "memory.backend"
trans[('43','4')] = " thành "
trans[('43','5')] = "qmd"
trans[('43','6')] = "."

# Block 43 elem 6 is just "。" -> "."

# Block 44
trans[('44','0')] = "—— Điều này đối với người không biết code thì nói thật là "
trans[('44','1')] = "khuyên quay đầu luôn"
trans[('44','2')] = "."

# Block 45
trans[('45','0')] = "Tin tốt là: "
trans[('45','1')] = "Đã là \""
trans[('45','2')] = "Tà Tu"
trans[('45','3')] = "\", chúng ta không đi đường thường."

# Block 46 - heading2
trans[('46','0')] = "Tà Tu: Cursor ma cải Tôm Hùm Lớn"

# Block 47
trans[('47','0')] = "Thông thường gặp lỗi, tài liệu chính thức sẽ bảo bạn sửa cấu hình, chạy script, xem log..."

# Block 48
trans[('48','0')] = "Nếu bạn thử để OpenClaw "
trans[('48','1')] = "tự sửa chính mình"
trans[('48','2')] = " (ví dụ dán lỗi vào hộp chat bảo nó sửa), nó sẽ giống một bác sĩ phẫu thuật say rượu tự mổ não mình, càng sửa càng hỏng, cuối cùng sập luôn, tức đến muốn đập máy."

# Block 49
trans[('49','0')] = "Vì vậy, hôm nay chúng ta dùng một chiêu \"tấn công giáng chiều\" kiểu Tà Tu: "
trans[('49','1')] = "Để Cursor phẫu thuật cho Tôm Hùm Lớn."

# Block 50 - heading3
trans[('50','0')] = "Tại sao lại là Cursor?"

# Block 51
trans[('51','0')] = "Vì các IDE khác cũng khiến newbie nản, Cursor là cái mà tôi thấy thân thiện nhất với người không phải lập trình viên, tất nhiên nếu bạn có CLI khác cũng dùng được."

# Block 52
trans[('52','0')] = "Vì Cursor đứng ở \"góc nhìn Thượng Đế\". Chúng ta không cần tự hiểu code, chỉ cần dùng Cursor Pro bật "
trans[('52','1')] = "Claude Sonnet 4.5"
trans[('52','2')] = ", quăng lỗi bạn không hiểu cho nó, để nó thao tác terminal thay bạn, sửa file thay bạn."

# Block 53 - heading2
trans[('53','0')] = "4 bước Tà Tu:"

# Block 54 - heading4
trans[('54','0')] = "Bước 1: Kiểm tra trạng thái QMD"

# Block 55
trans[('55','0')] = "Gửi đoạn sau cho Cursor AI:"

# Block 56
trans[('56','0')] = "Kết quả bạn có thể thấy:"

# Block 57
trans[('57','0')] = "Nếu thấy bất kỳ dòng nào ở trên, nghĩa là bạn đã dính. Tiếp tục xuống dưới."

# Block 58 - heading4
trans[('58','0')] = "Bước 2: Xây dựng chỉ mục"

# Block 59
trans[('59','0')] = "Gửi đoạn sau cho Cursor AI:"

# Block 60
trans[('60','0')] = "Cursor AI sẽ giúp bạn thực thi lệnh. Bạn sẽ thấy quá trình tương tự như sau:"

# Block 61
trans[('61','0')] = "Sau đó là tạo vector:"

# Block 62 - heading4
trans[('62','0')] = "Bước 3: Kích hoạt một lần tìm kiếm đầy đủ (tải các model còn lại)"

# Block 63
trans[('63','0')] = "Gửi đoạn sau cho Cursor AI:"

# Block 64
trans[('64','0')] = "Bước này sẽ tải thêm hai model cục bộ:"

# Block 65
trans[('65','0')] = "Tổng cộng khoảng "
trans[('65','1')] = "2.2GB"
trans[('65','2')] = ", nhưng chỉ tải một lần, sau đó dùng trực tiếp cache cục bộ."

# Block 66
trans[('66','0')] = "Sau khi tải xong, bạn sẽ thấy kết quả tìm kiếm, tương tự:"

# Block 67
trans[('67','0')] = "Thấy kết quả tìm kiếm nghĩa là đã thành công!"

# Block 68 - heading4
trans[('68','0')] = "Bước 4: Xác minh"

# Block 69
trans[('69','0')] = "Gửi đoạn sau cho Cursor AI:"

# Block 70
trans[('70','0')] = "Bạn sẽ thấy:"

# Block 71 - heading3
trans[('71','0')] = "Nó tự động duy trì cập nhật như thế nào?"

# Block 72
trans[('72','0')] = "Bạn không cần chạy thủ công mỗi lần. Gateway của OpenClaw đã tích hợp cơ chế tự động cập nhật:"

# Block 73
trans[('73','0')] = "Hành động"

# Block 74
trans[('74','0')] = "Tần suất "

# Block 75
trans[('75','0')] = "Mô tả"

# Block 76
trans[('76','0')] = "Lập chỉ mục file mới"

# Block 77
trans[('77','0')] = "Mỗi 5 phút"

# Block 78
trans[('78','0')] = "Tự động phát hiện file ký ức mới"

# Block 79
trans[('79','0')] = " Tạo vector"

# Block 80
trans[('80','0')] = "Mỗi 60 phút"

# Block 81
trans[('81','0')] = "Tự động tạo vector tìm kiếm cho file mới"

# Block 82
trans[('82','0')] = "Bảo vệ chống rung"

# Block 83
trans[('83','0')] = "15 giây"

# Block 84
trans[('84','0')] = "Khi ghi liên tục sẽ không kích hoạt lặp lại"

# Block 85
trans[('85','0')] = "Nói dễ hiểu là:"

# Block 86
trans[('86','0')] = "1. Bạn chat với Tôm Hùm Lớn"

# Block 87
trans[('87','0')] = "2. Tôm Hùm Lớn ghi nội dung quan trọng vào "
trans[('87','1')] = "`~/.openclaw/workspace/memory/2026-xx-xx.md`"

# Block 88
trans[('88','0')] = "3. Sau 5 phút, QMD tự động quét phát hiện file mới, thêm vào chỉ mục"

# Block 89
trans[('89','0')] = "4. Sau 60 phút, tự động tạo vector"

# Block 90
trans[('90','0')] = "5. Lần sau bạn hỏi câu hỏi liên quan, Tôm Hùm Lớn sẽ tìm được ký ức trước đó"

# Block 91
trans[('91','0')] = "Trước đó không dùng được chính là vì lần đầu cần tải model, bị timeout. Chúng ta chạy thủ công một lần, sau đó mọi thứ hoàn toàn tự động."

# Block 92 - heading3
trans[('92','0')] = "Câu hỏi thường gặp"

# Block 93 - heading4
trans[('93','0')] = "Q: Có tốn tiền không? Có cần API key không?"

# Block 94
trans[('94','0')] = "Lộc Đạo: Hoàn toàn không cần. "
trans[('94','1')] = "Ba model AI mà QMD dùng đều là mã nguồn mở, tự động tải từ HuggingFace, chạy trên máy tính của bạn. Không tốn phí, không phụ thuộc mạng (sau khi tải xong model)."

# Block 95 - heading4
trans[('95','0')] = "Q: Máy tính của tôi chạy nổi không?"

# Block 96
trans[('96','0')] = "Lộc Đạo: Đây đều là model nhỏ (lớn nhất mới 1.7B tham số), MacBook Air cũng chạy được. Không cần card đồ họa, CPU là đủ. Thực tế tìm kiếm một lần khoảng 2-5 giây."

# Block 97 - heading4
trans[('97','0')] = "Q: File ký ức lưu ở đâu?"

# Block 98
trans[('98','0')] = "Bạn có thể mở trực tiếp bằng trình soạn thảo văn bản, đều là định dạng Markdown, con người đọc được."

# Block 99 - heading4
trans[('99','0')] = "Q: Tôi muốn thêm một ký ức thủ công thì làm sao?"

# Block 100
trans[('100','0')] = "Lộc Đạo: Trực tiếp tạo một file `.md` mới trong "
trans[('100','1')] = "`~/.openclaw/workspace/memory/` "
trans[('100','2')] = ", viết nội dung bạn muốn Tôm Hùm Lớn ghi nhớ vào. Sau 5 phút QMD sẽ tự động lập chỉ mục cho nó."

# Block 101 - heading4
trans[('101','0')] = "Q: Hiệu quả tìm kiếm không tốt thì làm sao?"

# Block 102
trans[('102','0')] = "Lộc Đạo: Có thể điều chỉnh "
trans[('102','1')] = "`~/.openclaw/openclaw.json` "
trans[('102','2')] = "các tham số trong đó:"

# Block 103 - heading3
trans[('103','0')] = "Q: Dữ liệu chỉ mục lưu ở đâu? Chiếm bao nhiêu dung lượng?"

# Block 104
trans[('104','0')] = "Nếu ổ cứng hạn chế, model là phần duy nhất chiếm dung lượng. Xóa đi thì lần sau sẽ tải lại."

# Block 105 - heading1
trans[('105','0')] = "Lời kết"

# Block 106
trans[('106','0')] = "Hệ thống ký ức của Tôm Hùm Lớn thực ra đã được cấu hình sẵn, chỉ là lần khởi động đầu tiên tải model bị timeout dẫn đến \"tịt ngòi\"."

# Block 107
trans[('107','0')] = "Dùng Cursor chạy thủ công một lần "
trans[('107','1')] = "`qmd update` + `qmd embed`"
trans[('107','2')] = " + một lần tìm kiếm, sau khi tải xong tất cả model cục bộ, mọi thứ sẽ tự động vận hành."

# Block 108
trans[('108','0')] = "Từ nay Tôm Hùm Lớn của bạn sẽ quá mắt không quên."

# Block 109
trans[('109','0')] = "Dự báo tập tiếp theo"
trans[('109','1')] = ": Dùng Cursor ma cải bộ phân tích model của Tôm Hùm Lớn, để Google Antigravity cũng chạy được Claude Opus 4.6"

# Block 110
trans[('110','0')] = "Nội dung trước đó:"

# Block 111 - with link
trans[('111','0')] = "OpenClaw + Gemini 3 Flash + Feishu Hướng dẫn triển khai đầy đủ"

# Block 112 - with link
trans[('112','0')] = "Khi OpenClaw tiếp quản toàn bộ quyền Feishu, hiện trường bùng nổ năng suất 10 vị trí"

# Block 113 - with link
trans[('113','0')] = "Dùng ngay: 9 kỹ năng tự động hóa OpenClaw + Feishu, tiết kiệm 400 đô chi phí thử nghiệm token"

# Block 114
trans[('114','0')] = "Thêm nhiều phương pháp Tà Tu lập trình AI hãy tiếp tục theo dõi, liên hệ Lộc Đạo hãy thêm: "
trans[('114','1')] = "Ludao112"


# Now apply translations
translated_count = 0
kept_count = 0
total_text_runs = 0

out = copy.deepcopy(data)

for i, block in enumerate(out['blocks']):
    for j, elem in enumerate(block.get('elements', [])):
        total_text_runs += 1
        key = (str(i), str(j))
        if key in trans:
            elem['content'] = trans[key]
            translated_count += 1
        else:
            # Keep original (code, numbers, etc.)
            kept_count += 1

# Add spaces between adjacent Vietnamese text_runs
for block in out['blocks']:
    elements = block.get('elements', [])
    if len(elements) <= 1:
        continue
    for j in range(len(elements) - 1):
        curr = elements[j]
        nxt = elements[j + 1]
        # If current doesn't end with space and next doesn't start with space
        # and neither is inline_code with backticks
        curr_content = curr.get('content', '')
        nxt_content = nxt.get('content', '')
        if not curr_content:
            continue
        if not nxt_content:
            continue
        # Check if they are Vietnamese text (not pure code/numbers)
        curr_is_code = curr.get('style', {}).get('inline_code', False)
        nxt_is_code = nxt.get('style', {}).get('inline_code', False)
        # Add space between adjacent Vietnamese text runs if needed
        if not curr_content.endswith(' ') and not nxt_content.startswith(' '):
            if not curr_content.endswith('"') and not nxt_content.startswith('"'):
                if not curr_content.endswith('\"') and not nxt_content.startswith('\"'):
                    if not curr_is_code and not nxt_is_code:
                        curr['content'] = curr_content + ' '

# Update title
out['title'] = trans[('0','0')]

with open('_art_b5_10_trans.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print(f"Total blocks: {len(out['blocks'])}")
print(f"Total text runs: {total_text_runs}")
print(f"Translated: {translated_count}")
print(f"Kept original: {kept_count}")
print(f"Saved to _art_b5_10_trans.json")
