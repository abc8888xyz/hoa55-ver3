import json, re

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

with open('art1_fresh.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

translations = {
    "B0E0": 'Skill "Trực quan hóa giảng dạy" mà OpenClaw cần đã có, mã nguồn mở miễn phí! Công cụ giảng dạy AI ai cũng dùng được!',
    "B1E0": "🔗 Link bài gốc: ",
    "B2E0": "Nguyên tác: Vạn Vạn Bất Năng Đích Tiểu Hiệp (万万不能的小侠) Berryxia.AI",
    "B2E1": "22/02/2026 23:30 Mỹ",
    "B3E0": "Các bạn cũng có thể triển khai qua Alibaba Cloud Bailian",
    "B3E2": "để triển khai",
    "B3E3": ":",
    "B4E0": "Mua lần đầu chỉ từ 7.9 tệ, gia hạn giảm từ 50%, hỗ trợ Qwen3.5, Qwen3-max, Qwen3-coder, GLM-5, GLM-4.7, Kimi-k2.5 và các mô hình khác",
    "B5E0": "👉Nhấn link truy cập ngay:",
    "B6E0": "👉Xem hướng dẫn triển khai chi tiết:",
    "B7E0": "Chỉ cần tối đa ba bước, bạn sẽ có trợ lý AI trực tuyến 7x24 giờ, phản hồi mọi lúc",
    "B8E0": "Bạn đã bao giờ nghĩ về một câu hỏi chưa:",
    "B9E0": "Tại sao cùng là học, xem video hướng dẫn thú vị hơn đọc sách rất nhiều? Nhưng xem trình diễn tương tác 3D lại hay hơn gấp trăm lần so với video?",
    "B10E0": "Lý do rất đơn giản: ",
    "B10E1": 'Chiều tương tác càng cao, bạn càng cảm thấy mình đang "chơi" chứ không phải đang học.',
    "B11E0": 'Và "chơi" chính là cách học bản năng nhất của con người.',
    "B12E0": 'Một lần thử nghiệm "không đúng việc"',
    "B13E0": "Câu chuyện bắt đầu từ hôm nay.",
    "B14E0": "Nhà phát triển, cũng chính là tác giả của dự án này, bản thân tôi, ban đầu không định làm công cụ giáo dục nào. Gần đây bị ấn tượng mạnh bởi khả năng của Gemini 3.1, và bắt đầu suy nghĩ: liệu có thể để bất kỳ dự án nào cũng dễ dàng có được khả năng tạo sinh bằng AI này không?",
    "B15E0": "Nghĩa là gì?",
    "B16E0": "Mô hình phát triển truyền thống là: quản lý sản phẩm đưa yêu cầu, designer vẽ hình, lập trình viên viết code. Một trang trực quan hóa đơn giản, không mất vài ngày thì không xong.",
    "B17E0": "Nhưng nếu AI đủ thông minh, bạn chỉ cần nói cho nó một chủ đề, nó sẽ tạo ra cho bạn một trang web hoàn chỉnh có thể sử dụng được thì sao?",
    "B18E0": "Ý tưởng này rất đẹp, nhưng để thực hiện cần một cây cầu nối.",
    "B19E0": "AetherViz Master chính là cây cầu đó.",
    "B20E0": 'Gemini 3.1: Mô hình AI mới nhất của Google, nổi tiếng với khả năng suy luận và tạo sinh mạnh mẽ. Nó không chỉ hiểu văn bản, mà còn hiểu code, hình ảnh, thậm chí hiểu bạn muốn kiểu "cảm giác" gì.',
    "B21E0": "Nó có thể làm gì?",
    "B22E0": "Để tôi cho bạn xem trực tiếp.",
    "B23E0": 'Bạn mở trang, nhập một chủ đề, ví dụ "Định luật II Newton".',
    "B24E0": "Vài giây sau, một trang web tương tác hoàn chỉnh xuất hiện trước mặt bạn.",
    "B25E0": "Trong cảnh 3D, xe đang chạy. Bạn có thể kéo thanh trượt thay đổi lực kéo, quan sát gia tốc thay đổi thế nào. Bạn có thể điều chỉnh hệ số ma sát, xem xe dừng lại khi nào. Thậm chí còn có bảng công thức, hiển thị quá trình suy diễn F=ma theo thời gian thực.",
    "B26E0": "Đây chính là AetherViz Master phiên bản 5.0.",
    "B27E0": "AetherViz Master: Một công cụ có thể biến bất kỳ chủ đề giảng dạy nào thành trang web tương tác 3D ngay lập tức. Bạn cho nó một topic, nó trả lại bạn một trang web có thể dùng để giảng bài ngay.",
    "B28E0": "Lấy cảm hứng từ Gemini 3.1",
    "B29E0": "Tại sao phải nhấn mạnh điều này?",
    "B30E0": "Vì nếu không có Gemini 3.1, dự án này có lẽ sẽ không xuất hiện.",
    "B31E0": 'Nhà phát triển trước đây đã thử dùng các mô hình AI khác để làm việc này, nhưng kết quả luôn không như ý. Thứ tạo ra hoặc thiếu tay thiếu chân, hoặc hoàn toàn không dùng được. Nhưng khả năng hiểu và tạo code của Gemini 3.1 cuối cùng đã đạt đến mức "có thể thực sự làm việc được".',
    "B32E0": 'Nó không chỉ đơn giản là "hỗ trợ lập trình", mà có thể hiểu những yêu cầu mơ hồ như "tôi muốn làm một thứ mà học sinh xem được, chơi được", rồi biến nó thành code có thể chạy được.',
    "B33E0": "Đây là bước nhảy vọt về chất.",
    "B34E0": "Kỹ thuật Prompt: Cách giao tiếp hiệu quả với AI, để nó hiểu bạn muốn gì. Đây là một kỹ năng chuyên môn, cùng một yêu cầu, người biết hỏi và không biết hỏi sẽ nhận được kết quả khác nhau một trời một vực.",
    "B35E0": "Năm năng lực cốt lõi",
    "B36E0": "Để tôi phân tích cho bạn, công cụ này đã trải qua 5 phiên bản lặp đi lặp lại mới ra được.",
    "B37E0": "Thứ nhất, tự động nhận diện môn học.",
    "B38E0": "Bạn nhập \"quang hợp\", nó biết chuyển sang chế độ sinh học, mô hình lục lạp, cấu trúc tế bào tự động sắp xếp.",
    "B39E0": "Bạn nhập \"chuyển động hành tinh\", nó biết chuyển sang chế độ thiên văn, nền không gian sâu, đường quỹ đạo tự động sắp xếp.",
    "B40E0": "Bạn nhập \"tìm kiếm nhị phân\", nó biết chuyển sang chế độ lập trình, trực quan hóa mảng, hoạt hình thuật toán tự động sắp xếp.",
    "B41E0": "Vật lý, hóa học, sinh học, toán học, thiên văn, lập trình - sáu lĩnh vực, nó hiểu rõ cả.",
    "B42E0": "Tự động nhận diện môn học: AI phân tích từ khóa chủ đề bạn nhập, tự động xác định thuộc lĩnh vực nào, sau đó khớp phong cách hình ảnh, tông màu và chế độ tương tác phù hợp nhất.",
    "B43E0": "Thứ hai, chế độ render thông minh.",
    "B44E0": "Một số kiến thức phù hợp hiển thị 3D, như cấu trúc phân tử, phân tích lực học. Một số kiến thức dùng SVG 2D là đủ, như đồ thị hàm số, dữ liệu thống kê. Còn một số kiến thức cần kết hợp cả 3D và 2D.",
    "B45E0": "AetherViz Master 5.0 đã thực hiện chuyển đổi liền mạch giữa ba chế độ render: Three.js 3D, SVG 2D và chế độ hỗn hợp.",
    "B46E0": "Nó sẽ tự động phán đoán: dùng cách nào trình bày thì học sinh hiểu được nhất.",
    "B47E0": "Three.js: Engine 3D trên web, có thể tạo hiệu ứng 3D rất cool trên trình duyệt, giống như Unity phiên bản web. SVG: Một định dạng đồ họa vector, hình vẽ ra dù phóng to thu nhỏ đều rõ nét, phù hợp hiển thị biểu đồ và sơ đồ minh họa.",
    "B48E0": 'Thứ ba, thực sự "Zero-code".',
    "B49E0": "Đây là điểm thực tế nhất.",
    "B50E0": "Trước đây làm trực quan hóa giảng dạy, hoặc tự học lập trình, hoặc tìm developer xếp lịch. Bây giờ không cần nữa.",
    "B51E0": "Bạn chỉ cần một ý tưởng, AI giúp bạn thực hiện. Trang web tạo ra có thể dùng ngay, không cần sửa một dòng code nào.",
    "B52E0": "Giáo viên có thể dùng để làm bài giảng, học sinh có thể dùng để tự học, trung tâm đào tạo có thể dùng để trình diễn. Bất kỳ ai, chỉ cần biết dùng trình duyệt, đều có thể sử dụng.",
    "B53E0": "Zero-code: Không cần viết bất kỳ dòng code nào để hoàn thành phát triển. Điều này hạ thấp rào cản kỹ thuật, cho phép nhiều người hơn biến ý tưởng thành hiện thực.",
    "B54E0": "Thứ tư, bộ tính năng giảng dạy đầy đủ.",
    "B55E0": 'Phiên bản 5.0 không chỉ đơn giản là "hiển thị", nó bổ sung đầy đủ các tính năng thực tế cho giảng dạy:',
    "B56E0": "Bảng công thức: KaTeX render thời gian thực, công thức toán, lý, hóa đều không thành vấn đề",
    "B57E0": "Bảng kiểm tra: Tích hợp bài tập, làm xong xuất kết quả ngay",
    "B58E0": "Điều khiển phát lại: Quá trình thí nghiệm có thể tạm dừng, kéo, phát lại, giống như xem video",
    "B59E0": 'Điều khiển tham số: Kéo thanh trượt điều chỉnh tham số thời gian thực, tự "chơi" thí nghiệm',
    "B60E0": "Những tính năng này tách riêng thì không có gì đặc biệt, nhưng tích hợp trong một file HTML đơn do AI tạo, hiện tại chỉ có duy nhất một nơi.",
    "B61E0": "KaTeX: Công cụ chuyên dùng để render công thức toán học, tốc độ render cực nhanh, hiệu quả sánh ngang với sắp chữ LaTeX.",
    "B62E0": "Thứ năm, hiệu suất cực đỉnh.",
    "B63E0": "Render mượt mà 60fps",
    "B64E0": "UI kiểu kính mờ (Glass morphism), đẹp là chính nghĩa",
    "B65E0": "OrbitControls, cảnh 3D xoay kéo tùy ý",
    "B66E0": "File HTML đơn, mở trình duyệt là dùng được, không kén môi trường",
    "B67E0": "Cách sử dụng?",
    "B68E0": "Nhanh đến mức vượt ngoài tưởng tượng của bạn.",
    "B69E0": "Cách 1: Claude Code (Khuyến nghị)",
    "B70E0": 'Nếu bạn dùng Claude Code, trực tiếp nói cho nó chủ đề bạn muốn học, ví dụ "Định lý Pythagore", "Sao chép DNA", "Tìm kiếm nhị phân". Hệ thống sẽ tự động gọi AetherViz Master tạo trang web.',
    "B71E0": "Cách 2: Chạy cục bộ",
    "B75E0": "# Mở trình duyệt tại http://localhost:8080 ",
    "B76E0": "Nhập chủ đề, đợi vài giây, một trang giảng dạy tương tác sẽ ra đời.",
    "B77E0": "Nó có ý nghĩa gì?",
    "B78E0": "Nói cho cùng, AetherViz Master giải quyết một vấn đề cốt lõi: Để cách trình bày kiến thức theo kịp độ phức tạp của chính kiến thức.",
    "B79E0": "Hệ thống kiến thức hiện tại của chúng ta đã ba chiều bốn chiều rồi. Nhưng công cụ giảng dạy vẫn ở thời đại một chiều (văn bản) hai chiều (hình ảnh video).",
    "B80E0": "Một học sinh cấp ba có thể cần hiểu hiệu ứng đường hầm lượng tử, không-thời gian tương đối tính, chỉnh sửa gene. Những khái niệm này trong không gian ba chiều đã khó trực quan hóa, huống chi trên màn hình hai chiều.",
    "B81E0": "Nhưng tương tác 3D thì có thể.",
    "B82E0": 'Khi bạn có thể tận tay "mở" một nguyên tử, xem đám mây electron nhảy múa thế nào. Khi bạn có thể "kéo dài" không-thời gian, xem lực hấp dẫn bóp méo hình học thế nào. Khi bạn có thể "chỉnh sửa" trình tự gene, xem protein gấp cuộn thế nào.',
    "B83E0": "Khoảnh khắc đó, kiến thức trừu tượng trở thành trải nghiệm cụ thể.",
    "B84E0": "Đây mới là giáo dục đúng nghĩa.",
    "B85E0": "Viết ở cuối",
    "B86E0": "Dự án này hôm nay mới ra đời.",
    "B87E0": 'Nhà phát triển nói, làm đến nửa chừng, bản thân anh ấy cũng bị sốc. Anh không ngờ AI bây giờ lại thông minh đến vậy, thông minh đến mức có thể biến một ý tưởng mơ hồ "tôi muốn làm một trang giảng dạy tương tác về xxx" thành sản phẩm hoàn chỉnh có thể sử dụng được.',
    "B88E0": "Khả năng tạo code (code generation) của Gemini 3.1 là chìa khóa cho bước đột phá lần này.",
    "B89E0": 'Có lẽ trong tương lai không xa, chúng ta sẽ không cần hành động "phát triển" nữa. Chỉ cần "mô tả" nhu cầu, AI sẽ biến nó thành hiện thực.',
    "B90E0": 'Nhà giáo dục có thể tập trung vào "dạy gì", thay vì "làm trang web thế nào".',
    "B91E0": 'Học sinh có thể tập trung vào "hiểu", thay vì "hiểu slide của thầy cô".',
    "B92E0": "Đây có lẽ chính là điều AI nên làm.",
    "B93E0": "Địa chỉ: https://github.com/andyhuo520/aetherviz-master/tree/master",
    "B94E0": "AetherViz Master v5.0, một công cụ trực quan hóa giáo dục vừa ra đời hôm nay. Lấy cảm hứng từ Gemini 3.1, biến mọi ý tưởng thành trang web tương tác.",
    "B3E1": "5 nhân viên số AI độc lập, trực tiếp tiếp quản nghiên cứu chọn sản phẩm thương mại điện tử xuyên biên giới, tạo video UGC TikTok, thu hút traffic qua Reddit và vận hành Amazon.",
    "B9E1": ": Giao diện duy nhất kết nối với người dùng trên Lark, chịu trách nhiệm phân tích yêu cầu, gọi sessions_send để phân phối tác vụ xuyên node.",
    "B11E1": ": Chịu trách nhiệm viết nội dung cho Amazon và website độc lập.",
    "B12E1": ": Chịu trách nhiệm thực hiện SOP nuôi tài khoản nghiêm ngặt trong 5 tuần. Lướt và tương tác trong các subreddit chính xác như r/BuyItForLife, r/SkincareAddiction.",
    "B13E1": ": Chịu trách nhiệm phân tích logic video viral trên TikTok.",
    "B19E1": ': Trong nhóm Lark @Tổng quản: "Phân tích thị trường giường gấp cắm trại, và triển khai nội dung đa kênh."',
    "B20E1": ': Tổng quản gửi chỉ thị cho voc-analyst. Nó tự động thu thập đánh giá tiêu cực của đối thủ trên Amazon, rút ra kết luận: "Điểm đau của người dùng là sức chịu tải không đủ và gấp gọn bất tiện."',
    "B21E1": ": Dữ liệu được đồng bộ cho geo-optimizer. Nó viết blog cho website sản phẩm độc lập, để phù hợp với các công cụ tìm kiếm AI như ChatGPT, bổ sung dữ liệu định lượng cụ thể như \"chịu tải 450 pound\" trong bài viết, đồng thời trích dẫn rõ ràng nguồn đánh giá từ các trang web outdoor uy tín.",
    "B22E1": ": Tổng quản đồng thời kích hoạt reddit-spec. Nó tìm kiếm bài viết cũ trên Google, tìm các bài thảo luận liên quan có thứ hạng cao. Bình luận chân thành dưới bài viết cũ, giới thiệu sản phẩm mới của chúng ta, nhấn mạnh rằng nó đã giải quyết các điểm đau của phiên bản cũ, thành công chiếm lấy traffic dài hạn.",
    "B23E1": ": Tổng quản gọi tiktok-director. Nó trực tiếp đọc các điểm đau VOC, sử dụng Seed 2.0 tạo bảng phân cảnh 25 ô. Nó thiết kế chính xác 2 giây đầu tiên với góc quay thở góc nhìn thứ nhất cầm tay. Nó còn thiết kế cận cảnh ấn đệm ở giây thứ 4, thể hiện rõ độ đàn hồi và lực đỡ.",
    "B29E1": ": Mỗi Agent phải có Workspace riêng biệt. Báo cáo nghiên cứu thị trường của voc-analyst tuyệt đối không được trộn lẫn với hồ sơ nuôi tài khoản của reddit-spec trong cùng một thư mục.",
    "B30E1": ": Tạo 5 ứng dụng độc lập trên nền tảng mở Lark, kết nối dài WebSocket. Thông qua mảng bindings trong openclaw.json, định tuyến chính xác accountId của Lark đến Agent cục bộ tương ứng.",
    "B31E1": ': Phải bật whitelist trong tools.agentToAgent, đây là "bus dữ liệu duy nhất" cho phép Tổng quản ra lệnh ở hậu trường.',
    "B37E1": "Cấu hình Lark trong bài viết trước ",
    "B37E2": ", bạn cần bao nhiêu agent thì tạo bấy nhiêu ứng dụng mới, ở đây rất đơn giản chỉ là xử lý lặp lại.",
    "B50E1": ", có bạn đề cập đến thắc mắc về multi-Agent, vừa hay bài viết hôm nay có thể trả lời một số câu hỏi.",
    "B54E1": 'Một "Giám đốc chiến lược nội dung" chịu trách nhiệm output toàn cục, sau đó phân phối tác vụ cho "phân thân Xiaohongshu" hoặc "phân thân TikTok" để thích ứng định dạng.',
    "B56E1": "Xem xét mô hình Squad, thực hiện trách nhiệm kinh doanh đầu-cuối.",
    "B59E1": "Phải dùng mô hình hàng đầu (như Claude 4.6), xử lý điều phối xuyên Agent phức tạp và độ sâu chọn đề tài.",
    "B60E1": "Dùng mô hình hiệu quả chi phí cao (như Gemini 3 Flash, Kimi K2.5), xử lý thu thập trang web, làm sạch dữ liệu và điền Emoji, chi phí có thể giảm 90%.",
    "B64E1": "Tạo phiên bản mới và đăng ký phát hành, thay đổi mới có hiệu lực.",
    "B66E2": "(chống vòng lặp chết robot) cơ chế, Agent A @Agent B trong nhóm, hậu trường Agent B sẽ không nhận được thông báo.",
    "B70E1": ": Phải đặt ở ~/.openclaw/skills/, đảm bảo gọi xuyên Agent không mất gói.",
    "B71E1": ": Đặt ở thư mục con skills riêng của Agent, có thể ngăn hiệu quả Agent tạo ảo giác công cụ, gọi nhầm API key của agent khác.",
    "B72E0": "Về cách chơi multi-Agent của OpenClaw, mọi người còn câu hỏi gì không? Hoan nghênh tiếp tục để lại bình luận.",
    "B73E0": "Mảng thương mại điện tử xuyên biên giới, cạnh tranh là ai có kiến trúc Agent ổn định hơn, chi phí thấp hơn. ",
    "B74E0": "Về cách dùng AI để trao quyền cho TikTok, Amazon, thậm chí là làm GEO qua Reddit, chúng tôi sẽ chia sẻ thực chiến tại ",
    "B74E1": "Đại hội Thương mại điện tử xuyên biên giới NGS AI lần thứ nhất ngày 14/3 ",
    "B74E2": "sẽ chia sẻ thực chiến.",
    "B75E1": "2026, logic content marketing xuyên biên giới đã thay đổi hoàn toàn"
}

# Apply translations
stats = {"total_blocks": len(data["blocks"]), "translated": 0, "kept": 0, "total_text": 0, "errors": []}

for i, block in enumerate(data["blocks"]):
    for j, elem in enumerate(block.get("elements", [])):
        content = elem.get("content", "")
        if not content.strip():
            continue
        stats["total_text"] += 1
        key = f"B{i}E{j}"
        if key in translations:
            elem["content"] = translations[key]
            stats["translated"] += 1
        elif not has_chinese(content):
            stats["kept"] += 1
        else:
            stats["errors"].append(key)

with open("art1_translated.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Stats: {json.dumps(stats, ensure_ascii=False)}")
