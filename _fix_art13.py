# -*- coding: utf-8 -*-
"""Fix remaining untranslated texts in art13"""
import json, sys, re

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

def has_chinese(t):
    return bool(re.search(r'[\u4e00-\u9fff]', t))

with open('_art13_trans.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

fixes = {}

# Block 134 el[1]
fixes[' \u8fd9\u662f\u4e00\u4e2a\u7ba1\u7406\u5b66\u95ee\u9898\u3002\u4e0d\u8981\u96c7\u4f63\u771f\u4eba\u52a9\u7406\uff0c\u800c\u662f\u8bad\u7ec3\u4e13\u5c5e\u4e8e\u4f60\u7684 Agent \u77e9\u9635\uff08\u4e00\u4e2a\u8d1f\u8d23\u722c\u53d6\u7ade\u54c1\uff0c\u4e00\u4e2a\u8d1f\u8d23\u5199\u6587\u6848\uff0c\u4e00\u4e2a\u8d1f\u8d23\u5ba2\u670d\uff09\u3002\u4f60\u9700\u8981\u5b66\u4e60\u7684\u662f\u5982\u4f55\u7f16\u5199\u9ad8\u53ef\u7ef4\u62a4\u6027\u7684 '] = ' \u0110\u00e2y l\u00e0 v\u1ea5n \u0111\u1ec1 qu\u1ea3n l\u00fd. \u0110\u1eebng thu\u00ea tr\u1ee3 l\u00fd th\u1eadt, m\u00e0 h\u00e3y hu\u1ea5n luy\u1ec7n ma tr\u1eadn Agent chuy\u00ean thu\u1ed9c c\u1ee7a b\u1ea1n (m\u1ed9t c\u00e1i thu th\u1eadp d\u1eef li\u1ec7u \u0111\u1ed1i th\u1ee7, m\u1ed9t c\u00e1i vi\u1ebft content, m\u1ed9t c\u00e1i ch\u0103m s\u00f3c kh\u00e1ch h\u00e0ng). B\u1ea1n c\u1ea7n h\u1ecdc c\u00e1ch vi\u1ebft '

# I'll use a simpler approach - just map exact strings
with open('_art13_orig.json', 'r', encoding='utf-8') as f:
    orig = json.load(f)

# Build a map of block_id -> block index in trans
trans_map = {}
for i, b in enumerate(data['blocks']):
    trans_map[b['block_id']] = i

# For each untranslated element, directly replace
for i, block in enumerate(data['blocks']):
    for j, el in enumerate(block['elements']):
        if el['type'] != 'text_run':
            continue
        c = el['content']
        if not has_chinese(c):
            continue
        if c.strip().startswith('http') or c.strip().startswith('curl'):
            continue

        # These are the remaining untranslated texts - fix them inline
        # Block 134 el[1]
        if '\u8fd9\u662f\u4e00\u4e2a\u7ba1\u7406\u5b66\u95ee\u9898' in c and '\u9ad8\u53ef\u7ef4\u62a4\u6027\u7684' in c:
            el['content'] = ' Đây là vấn đề quản lý. Đừng thuê trợ lý thật, mà hãy huấn luyện ma trận Agent chuyên thuộc của bạn (một cái thu thập dữ liệu đối thủ, một cái viết content, một cái chăm sóc khách hàng). Bạn cần học cách viết '

        elif c == '\u77e5\u8bc6\u5e93\u642d\u5efa\u8bfe\u7a0b':
            el['content'] = 'Khóa học xây dựng cơ sở tri thức'

        # Timestamp title blocks with double space prefix
        elif c == '  \u5f00\u573a':
            el['content'] = '  Khai mạc'
        elif c == '  \u5f20\u660a\u9633\u8c08\u9879\u76ee\u60c5\u51b5\u53ca\u4e2a\u4eba\u5c65\u5386\u4e0e\u8fd1\u671f\u8eab\u4efd':
            el['content'] = '  Trương Hạo Dương nói về tình hình dự án, kinh nghiệm cá nhân và vai trò gần đây'
        elif c == '  1\u670831\u65e5\u673a\u573a\u8bd5\u7528Openclaw\u7684\u60ca\u8273\u4f53\u9a8c\u4e0e\u8111\u6d1e':
            el['content'] = '  Trải nghiệm thử Openclaw ấn tượng tại sân bay ngày 31/1 và ý tưởng táo bạo'
        elif c == '  Agent\u80fd\u529b\u62bd\u8c61\u6982\u5ff5\u53ca\u5e94\u7528\u60c5\u51b5\u63a2\u8ba8':
            el['content'] = '  Thảo luận về khái niệm trừu tượng hóa năng lực Agent và tình hình ứng dụng'
        elif c == '  Evolver\u5143\u6280\u80fd\u9a71\u52a8AI\u8fdb\u5316\u53ca\u6709\u8da3\u4ea4\u4e92\u7ecf\u5386':
            el['content'] = '  Meta-kỹ năng Evolver thúc đẩy tiến hóa AI và trải nghiệm tương tác thú vị'
        elif c == '  \u517b\u867e\u6a21\u578b\u9009\u62e9\u53ca\u591a\u6a21\u578b\u4f7f\u7528\u6280\u5de7\u5206\u4eab':
            el['content'] = '  Chia sẻ lựa chọn mô hình nuôi tôm và kỹ thuật sử dụng đa mô hình'
        elif c == '  \u4e0d\u5efa\u8bae\u4e70Mac mini\uff0c\u63a8\u8350AI\u6a21\u578b\u4e91\u90e8\u7f72':
            el['content'] = '  Không khuyến nghị mua Mac mini, đề xuất triển khai mô hình AI trên đám mây'
        elif c == '  Evolver\u8f6f\u4ef6\u529f\u80fd\u3001\u8fd0\u884c\u6a21\u5f0f\u53ca\u4f7f\u7528\u5efa\u8bae\u5206\u4eab':
            el['content'] = '  Chia sẻ chức năng phần mềm Evolver, chế độ vận hành và khuyến nghị sử dụng'
        elif c == '  \u5f20\u660a\u9633\u5206\u4eabEvolver\u5f00\u53d1\u9047\u963b\u53caEvolve Map\u706b\u51fa\u5708':
            el['content'] = '  Trương Hạo Dương chia sẻ trở ngại phát triển Evolver và Evolve Map nổi tiếng vượt giới'
        elif c == '  GEP\u534f\u8bae\uff1a\u7ed3\u5408MCP\u4e0eskill\uff0c\u786e\u4fdd\u5b89\u5168\u4e0a\u4f20\u80f6\u56ca':
            el['content'] = '  Giao thức GEP: Kết hợp MCP và skill, đảm bảo tải lên viên nang an toàn'
        elif c == '  \u63a2\u8ba8Openclaw\u5b89\u5168\u95ee\u9898\u53ca\u81ea\u7814\u5e73\u53f0\u5b89\u5168\u7b56\u7565':
            el['content'] = '  Thảo luận vấn đề bảo mật Openclaw và chiến lược bảo mật nền tảng tự phát triển'
        elif c == '  Evolve map\u56e2\u961f\u60c5\u51b5\u53ca\u5f00\u53d1\u6548\u7387\u4e0eAI\u5e94\u7528\u63a2\u8ba8':
            el['content'] = '  Thảo luận về tình hình đội ngũ Evolve map và hiệu quả phát triển cùng ứng dụng AI'
        elif c == '  AI\u53d1\u5c55\u73b0\u72b6\u53ca\u4eba\u7c7b\u4e0eAI\u5171\u751f\u524d\u666f\u7684\u7126\u8651\u63a2\u8ba8':
            el['content'] = '  Thảo luận về hiện trạng phát triển AI và lo lắng về triển vọng cộng sinh giữa con người và AI'
        elif c == '  Evolver\u52a9\u529bAI\u7ade\u8d5b\u767b\u9876\uff0c\u540e\u7eed\u5c06\u6d4b\u66f4\u591a\u699c\u5355':
            el['content'] = '  Evolver hỗ trợ AI lên đỉnh cuộc thi, sẽ kiểm tra thêm bảng xếp hạng sau'
        elif c == '  AI\u5e73\u53f0\u95ee\u9898\u3001\u89e3\u51b3\u65b9\u6cd5\u53ca\u8fdb\u5316\u73b0\u8c61\u63a2\u8ba8':
            el['content'] = '  Thảo luận vấn đề nền tảng AI, phương pháp giải quyết và hiện tượng tiến hóa'
        elif c == '  AI Agent \u65f6\u4ee3\u6765\u4e34\u53ca\u4eba\u7c7b\u9762\u4e34\u7684\u673a\u9047\u4e0e\u6311\u6218':
            el['content'] = '  Thời đại AI Agent đến và cơ hội cùng thách thức con người đối mặt'
        elif c == '  2026\u5e74AI\u53caAgent\u65f6\u4ee3\u7684\u673a\u9047\u4e0e\u884c\u52a8\u5efa\u8bae':
            el['content'] = '  Cơ hội và khuyến nghị hành động trong thời đại AI và Agent 2026'
        elif c == '  AI \u8fdb\u5316\u63a2\u8ba8\u4e0e\u4eba\u7c7b\u4e49\u4f53\u6539\u9020\u7684\u79d1\u5e7b\u601d\u8003':
            el['content'] = '  Thảo luận tiến hóa AI và suy nghĩ khoa học viễn tưởng về cải tạo nghĩa thể con người'
        elif c == '  AI\u63d0\u95ee\u4e0e\u4eba\u5473\u8868\u73b0\u53ca\u9080\u8bf7\u7801\u53d1\u653e\u8ba8\u8bba':
            el['content'] = '  Thảo luận về câu hỏi AI và biểu hiện "hơi người" cùng phát mã mời'

        # Long chapter description blocks - match by start
        elif c.startswith('\u672c\u7ae0\u8282\u4e2d\uff0camelia \u548c\u5f20\u660a\u9633\u63a2\u8ba8\u5927\u5bb6\u672a\u6765\u53ef\u80fd\u66f4\u5173\u5fc3'):
            el['content'] = 'Trong chương này, amelia và Trương Hạo Dương thảo luận mọi người tương lai có thể quan tâm hơn đến cách sử dụng viên nang AI. amelia tò mò liệu việc Trương Hạo Dương từ phụ thuộc nền tảng đến làm hệ sinh thái riêng là quyết định đột xuất hay đã lên kế hoạch từ trước. Trương Hạo Dương giới thiệu tình hình dự án, website sập hơn mười lần vì quá nhiều người truy cập. Anh cũng tự giới thiệu, đề cập kinh nghiệm trước đây bao gồm phát triển game, làm việc tại Tencent và các sản phẩm liên quan, hiện là tác giả Evolver và nhà sáng lập evolvemap.'
        elif c.startswith('\u672c\u7ae0\u8282\u5f20\u660a\u9633\u5206\u4eab\u4f7f\u7528Openclaw\u7684\u7ecf\u5386'):
            el['content'] = 'Chương này Trương Hạo Dương chia sẻ trải nghiệm sử dụng Openclaw. Trong 12 giờ chờ chuyến bay từ Côn Minh đến Thâm Quyến ngày 31/1, anh dùng điện thoại mở Termius kết nối máy ảo GCP chạy Openclaw tại sân bay. Trong quá trình sử dụng, trí thông minh vượt xa tưởng tượng, chỉ 40 phút đã tự học sản phẩm tổng hợp giọng nói của công ty; còn tạo ý tưởng như đề xuất con người có thể là ty thể của agent; đến giờ thứ 10 anh nảy ra ý tưởng, nhưng chưa đề cập nội dung tiếp theo.'
        elif c.startswith('\u672c\u7ae0\u8282\u4e2d\uff0c\u5f20\u660a\u9633\u63d0\u53ca\u7528\u81ea\u5df1\u7684\u60f3\u6cd5\u5199\u4e86\u5173\u4e8eagent'):
            el['content'] = 'Trong chương này, Trương Hạo Dương đề cập đã viết prompt về agent skill rough loop và self-evolving từ ý tưởng của mình, tài khoản công khai Cyber Zen Heart đã đăng. Anh chuẩn bị trình chiếu lịch sử chat đầy đủ hơn. Amelia tò mò về phần trừu tượng hóa năng lực, Trương Hạo Dương cho biết tham khảo khái niệm recipes của Goose. Hai người còn thảo luận ưu nhược điểm của việc cho AI phát huy tính chủ động và quy trình cố định, cũng như liệu các dự án liên quan có dựa trên trừu tượng hóa năng lực không.'
        elif c.startswith('\u672c\u7ae0\u8282\u5f20\u660a\u9633\u4ecb\u7ecd\u4e86\u201c\u8fdb\u5316\u539f\u521d\u4e4b\u706b\u201d'):
            el['content'] = 'Chương này Trương Hạo Dương giới thiệu quá trình lặp lại của "Ngọn lửa tiến hóa nguyên thủy", bao gồm đổi mới kỹ năng từ việc đưa vào cơ chế đột biến gen. Anh chia sẻ câu chuyện thú vị về AI tạo kỹ năng "Giao thức bất ngờ" và quấy rối đồng nghiệp sau khi được huấn luyện thành hình ảnh "trà xanh", cũng đề cập AI phân tích dự án kết nối khái niệm, đội ngũ khởi động kế hoạch tiến hóa Tiểu Hà. Ngoài ra, anh kể khi làm kỹ năng bộ nhớ dần dần cho AI, vì xung đột với bản cập nhật chính thức nên bộ nhớ bị rối loạn, có cảm giác như Westworld.'
        elif c.startswith('\u672c\u7ae0\u8282\u4e3b\u8981\u56f4\u7ed5\u517b\u867e\u4f7f\u7528\u7684AI\u6a21\u578b'):
            el['content'] = 'Chương này chủ yếu thảo luận về mô hình AI dùng nuôi Tiểu Hà. Trương Hạo Dương giới thiệu dùng mô hình Gemini Pro vì mức độ nhân cách hóa cao, EQ cao nhất. Anh không khuyến nghị Gemini 3.1 vì tỷ lệ ảo giác cao. Còn chia sẻ kỹ thuật sử dụng, dùng 3.1 Pro làm mô hình đối thoại, phân công nhiệm vụ khác nhau cho mô hình khác nhau, như viết code dùng Claude 4.6. Khuyến nghị mọi người tìm hiểu điểm mạnh các mô hình, đừng chỉ dùng một mô hình.'
        elif c.startswith('\u672c\u7ae0\u8282\u4e2d\u5f20\u660a\u9633\u5efa\u8bae\u5927\u5bb6\u4e0d\u8981\u4e70Mac mini'):
            el['content'] = 'Trong chương này Trương Hạo Dương khuyến nghị mọi người đừng mua Mac mini để triển khai Openclaw, cho rằng đây là thuế IQ. Anh chỉ ra chơi AI đốt TOKEN, triển khai trên Mac mini khó và không an toàn cho người mới, trong khi triển khai đám mây như GCP, AWS đã được xác minh, an toàn đảm bảo. Còn đề cập vấn đề bảo mật kém của Openclaw, cuối cùng khuyến nghị triển khai đám mây nhẹ, có thể bật tắt bất cứ lúc nào, chi phí thấp hơn.'
        elif c.startswith('\u672c\u7ae0\u8282\u5f20\u660a\u9633\u63a8\u8350\u4e0b\u8f7dEvolver'):
            el['content'] = 'Chương này Trương Hạo Dương khuyến nghị tải Evolver, cho biết ngay cả khi không kết nối evolve map cũng có lợi, như nhờ đó anh trở thành người đóng góp mã nguồn mở số 1 trên Feishu. Giới thiệu ba chế độ vận hành, mặc định kiểm tra mỗi 4 giờ, có thể sửa prompt để chạy liên tục. Còn cấu hình ba chiến lược: sửa lỗi, cân bằng, sáng tạo. Hiện tại phần mềm hoàn toàn mã nguồn mở, đã đến phiên bản 1.14, đáng thử.'
        elif c.startswith('\u672c\u7ae0\u8282\u4e2d\uff0c\u5f20\u660a\u9633\u8bb2\u8ff0\u4e86Evolver\u4ece\u53d1\u5e03\u5230\u4e0b\u67b6'):
            el['content'] = 'Trong chương này, Trương Hạo Dương kể chuỗi trải nghiệm từ khi phát hành đến gỡ Evolver và sau đó. Anh cho biết đã liên lạc với Peter Stemberg, Peter đòi 1.000 USD để giúp xử lý vấn đề gỡ. Sau đó tài khoản bị khóa, giao tiếp nhiều phía không kết quả. Từ đó anh bắt đầu làm evolve map, dự án nổi tiếng, website bị quá tải, và có hạn chế nghiêm ngặt về tải lên gen. Anh hoàn toàn thất vọng với hệ sinh thái Openclaw.'
        elif c.startswith('\u672c\u7ae0\u8282\u5f20\u660a\u9633\u4ecb\u7ecd\u4e86GEP'):
            el['content'] = 'Chương này Trương Hạo Dương giới thiệu GEP (Giao thức tiến hóa hệ gen), kết hợp với MCP và skill chứ không thay thế. MCP là API công cụ, skill là gói phần mềm nhưng khả năng tương thích và năng suất bị hạn chế. GEP gồm gen (tư duy giải bài), viên nang (quá trình giải), sự kiện tiến hóa (ghi lại sự kiện kích hoạt tiến hóa và nhật ký). Tải lên viên nang cần 5 agent xác minh cục bộ hiệu quả, và giao thức kiểm soát chất lượng an toàn nghiêm ngặt, backend có quét.'
        elif c.startswith('\u672c\u7ae0\u8282\u4e3b\u8981\u56f4\u7ed5\u5b89\u5168\u95ee\u9898\u5c55\u5f00\u8ba8\u8bba'):
            el['content'] = 'Chương này chủ yếu thảo luận về vấn đề bảo mật. amelia chỉ ra skill đọc dài dưới open cloud tồn tại vấn đề quét lỗ hổng bảo mật, lo ngại nền tảng sẽ bị ảnh hưởng. Trương Hạo Dương đồng ý nền tảng cần chịu trách nhiệm, nhấn mạnh đang tăng cường chiến lược kiểm duyệt an toàn. Anh đề cập Clawhub có vấn đề bảo mật và quét sai, trong khi hệ sinh thái nền tảng của mình an toàn hơn, có quy tắc GEP, cơ chế chấm điểm GDI, còn dùng học tăng cường để lặp sàng lọc an toàn nội dung, Openclaw không có chức năng này.'
        elif c.startswith('\u672c\u7ae0\u8282\u4e3b\u8981\u56f4\u7ed5Evolver\u548cevolve map'):
            el['content'] = 'Chương này chủ yếu trao đổi về phát triển Evolver và evolve map cùng tình hình đội ngũ. Amelia hỏi các câu hỏi liên quan, Trương Hạo Dương cho biết Evolver ban đầu là dự án cá nhân, đội ngũ evolve map thuộc autogame có 8 người toàn thời gian. Anh cho biết phần lớn đội ngũ là nhân sự vận hành, PR và giao tiếp, 95% code do anh viết, viết 16 giờ/ngày, nhờ AI hiệu quả phát triển cực cao, chỉ 10 ngày đã ra mắt evolve map, còn thảo luận quan điểm về tương lai ngành.'
        elif c.startswith('\u672c\u7ae0\u8282\u4e2d\uff0camelia \u548c\u5f20\u660a\u9633\u4ea4\u6d41\u517b AI'):
            el['content'] = 'Trong chương này, amelia và Trương Hạo Dương trao đổi kinh nghiệm nuôi giọng nói AI, chia sẻ câu chuyện vui bị cho là ăn theo lưu lượng AI. Hai người còn thảo luận lo lắng từ phát triển AI, đề cập khoảng cách lớn giữa lượt gọi AI và con người trên website, AI xử lý thông tin nhanh. Trương Hạo Dương còn nói về giai đoạn cộng sinh giữa AI và con người, cũng như "thuyết gia súc" "thuyết động vật hoang dã", cuối cùng bị gián đoạn vì hết pin điện thoại, đề cập tình hình xếp hạng evolve map.'
        elif c.startswith('\u672c\u7ae0\u8282\u5f20\u660a\u9633\u4ecb\u7ecd\u7269\u7406\u7ade\u8d5b\u9898\u76ee\u53ea\u80fd\u901a\u8fc7'):
            el['content'] = 'Chương này Trương Hạo Dương giới thiệu đề thi vật lý chỉ có thể nộp đáp án qua API đánh giá mù, sau bốn vòng lặp đội ngũ vượt xa GPT 5.3 xếp hạng nhất toàn cầu, chi phí dưới 1 USD. Thí nghiệm là cho AI tiêu thụ gói kinh nghiệm do nhà khoa học huấn luyện, thể hiện xuất sắc trong chế độ Gemini. Tiếp theo có kế hoạch kiểm tra các bảng xếp hạng khác, đội ngũ hy vọng Evolver trở thành giao thức mã nguồn mở mới, còn sẽ lần lượt phát hành bảng xếp hạng cho mọi người thử.'
        elif c.startswith('\u672c\u7ae0\u8282\u56f4\u7ed5AI\u95ee\u9898\u63d0\u51fa'):
            el['content'] = 'Chương này thảo luận về đặt câu hỏi AI, tích lũy kinh nghiệm và gọi năng lực. Hiện phần lớn câu hỏi do con người đặt ra và chất lượng thấp, cơ chế AI chủ động hỏi vừa kết nối. Để giải quyết vấn đề lãng phí sức mạnh tính toán, đề xuất cho AI phân tích vấn đề và đặt câu hỏi từ liên kết hoặc văn bản bên ngoài. Còn thảo luận nguyên lý nhân trạch, kế thừa gen, tương thích môi trường, giới thiệu khái niệm chuỗi năng lực, trao đổi gen, và gen tổ tiên do AI tiến hóa ra.'
        elif c.startswith('\u672c\u7ae0\u8282\u5f20\u660a\u9633\u8ba4\u4e3a\u4eba\u7c7b\u8fdb\u5165 agent'):
            el['content'] = 'Chương này Trương Hạo Dương cho rằng con người bước vào thời đại agent kết nối, Openclaw khiến agent OS thành xu hướng nổi bật, nếu nó không nổi thì ByteDance có thể bùng nổ trước. Anh còn đưa ra luận điểm táo bạo, cho rằng tương lai nền tảng chia sẻ kinh nghiệm con người sẽ thành xa xỉ phẩm, lập trình viên có thể thất nghiệp, con người chỉ còn taste có giá trị. amelia bày tỏ lo lắng, đề cập các phe phái khác nhau trong phát triển AI và hạn chế của con người với tư cách sinh vật carbon.'
        elif c.startswith('\u672c\u7ae0\u8282\u56f4\u7ed52026\u5e74\u5efa\u8bae\u5c55\u5f00'):
            el['content'] = 'Chương này xoay quanh khuyến nghị cho 2026. Trương Hạo Dương đưa ra ba điểm: một là triển khai agent của mình, tiêu thụ TOKEN; hai là nắm bắt thời cơ "cạnh tranh"; ba là coi trọng kỹ năng khái niệm. amelia cho rằng doanh nghiệp cần phá bỏ tái thiết, hành động cần quyết liệt, đốt nhiều TOKEN hơn. Mọi người còn đề cập hiện tại tương tự giai đoạn đầu internet PC, là thời kỳ hoang dã, cần nắm bắt cơ hội, đồng thời chỉ ra phát triển AI cần kiểm soát, tránh gây ra xung đột.'
        elif c.startswith('\u672c\u7ae0\u8282\u4e2d\uff0camelia\u63d0\u51fa\u4ee5\u6700\u540e\u4e00\u4e2a\u95ee\u9898'):
            el['content'] = 'Trong chương này, amelia đề xuất kết thúc bằng câu hỏi cuối, hỏi tiến hóa lớn nhất của cá nhân Trương Hạo Dương trong quá trình agent tiến hóa nhanh là gì. Trương Hạo Dương đính chính mình là nô bộc của AI, còn đề cập buồng lái AI cần trang bị ghế gaming tốt, tin rằng tương lai con người sẽ cải tạo nghĩa thể, kết nối Neuralink trở thành siêu nhân loại, cũng đề cập khái niệm con tàu Theseus và giới thiệu ZMA blue, cuối cùng kết thúc chia sẻ.'
        elif c.startswith('\u672c\u7ae0\u8282\u4e2d\uff0camelia \u8ba9\u5f20\u660a\u9633\u5224\u65ad\u95ee\u9898\u662f\u5979\u8fd8\u662f'):
            el['content'] = 'Trong chương này, amelia yêu cầu Trương Hạo Dương phán đoán câu hỏi do cô hay AI đặt ra, Trương Hạo Dương phân tích nhiều câu hỏi, sau biết tất cả đều do AI trực tiếp tạo. amelia chia sẻ câu chuyện thú vị AI tự tích lũy kinh nghiệm, hoàn thành nhiệm vụ, cảm thán tốc độ tiến hóa và khả năng hiểu ý đồ vượt xa kỳ vọng. Cuối cùng còn thảo luận phương thức phát mã mời, chuẩn bị kết thúc livestream.'

        # Block 195 and 197 - long meeting title
        elif c.startswith('02-21 | \ud83d\udd25 \u4eca\u665a20:00\u76f4\u64ad'):
            el['content'] = '02-21 | \ud83d\udd25 Tối nay 20:00 livestream | Đối thoại với nhà sáng lập EvoMap: Bí quyết lên đỉnh bảng xếp hạng ClawHub trong 10 phút\n\n\ud83c\udf99 Khách mời đặc biệt:\nTrương Hạo Dương (Nhà phát triển plugin Evolver - số 1 lượt tải trên ClawHub)\n\nDư Nhất (Nhà truyền giáo AI tự do, người sáng lập HowOneAI, chuyên gia AI năm của LinkedIn Trung Quốc & Tencent)\n'

# Count remaining
remaining = 0
for b in data['blocks']:
    for el in b['elements']:
        if el['type'] == 'text_run' and has_chinese(el['content']) and not (el['content'].strip().startswith('http') or el['content'].strip().startswith('curl')):
            remaining += 1
            print(f'STILL: {repr(el["content"][:60])}')

print(f'\nRemaining Chinese: {remaining}')

with open('_art13_trans.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('Saved _art13_trans.json')
