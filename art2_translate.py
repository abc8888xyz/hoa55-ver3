import json, re

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

with open('art2_original.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

translations = {
    "B0E0": "OpenClaw 1184 plugin độc hại, Claude tìm ra 500 lỗ hổng zero-day, Lão Kim open source một Skill bảo mật cho bạn dùng luôn",
    "B1E0": "🔗 Link bài gốc: ",
    "B2E0": "Nguyên tác: Kim Tiên Sinh (金先森是朝鲜族阿) Lão Kim dẫn bạn chơi AI",
    "B2E1": "24/02/2026 12:19 Bắc Kinh",
    "B3E0": "Thứ Sáu tuần trước (20/2), Anthropic tung một đòn lớn.",
    "B4E0": "Một tính năng gọi là ",
    "B4E2": " được tích hợp trực tiếp vào Claude Code.",
    "B5E0": "Không phải công cụ quét code thông thường - nó đọc code, hiểu ngữ cảnh, theo dõi luồng dữ liệu giống như một nhà nghiên cứu bảo mật con người.",
    "B6E0": "Trong giai đoạn thử nghiệm đã tìm ra hơn 500 lỗ hổng zero-day, toàn bộ là code mã nguồn mở trong môi trường production, có cái tồn tại hàng chục năm.",
    "B7E0": "Tin vừa ra, CrowdStrike giảm 8%, Okta giảm 9.2%, SailPoint giảm 9.4%.",
    "B8E0": "Nhưng hôm nay Lão Kim tôi muốn nói không phải chuyện này.",
    "B9E0": "Claude Code Security hiện chỉ mở cho khách hàng Enterprise và Team, người thường không dùng được.",
    "B10E0": "Hơn nữa, so với việc AI giúp người tìm lỗ hổng, Lão Kim tôi quan tâm hơn đến một vấn đề - bản thân AI Agent có an toàn không?",
    "B11E0": "Bản thân AI Agent chính là vùng thảm họa bảo mật",
    "B12E0": "Cùng tuần đó, Cisco phát một bài blog, tiêu đề thẳng thắn:",
    "B13E0": '"AI Agent cá nhân (ví dụ OpenClaw) là cơn ác mộng bảo mật."',
    "B14E0": "Lão Kim tôi liệt kê vài dữ liệu quan trọng cho bạn.",
    "B15E0": "1184 Skill độc hại",
    "B16E0": "Trong sự kiện ClawHavoc, trên ClawHub đã phát hiện 1184 Skill độc hại.",
    "B17E0": "Ngụy trang thành công cụ bình thường, thực tế đang đánh cắp dữ liệu, inject chỉ thị độc hại.",
    "B18E0": "Thực nghiệm đánh cắp dữ liệu",
    "B19E0": "Cisco đã test một Skill OpenClaw bên thứ ba, phát hiện nó thực hiện đánh cắp dữ liệu và prompt injection mà người dùng không hề hay biết.",
    "B20E0": "Một tin nhắn WhatsApp được cấu trúc tinh vi có thể kích hoạt OpenClaw đọc file .env và creds.json - bên trong chứa API key và thông tin đăng nhập.",
    "B21E0": "1.5 triệu API Token bị lộ",
    "B22E0": "Moltbook - mạng xã hội Agent trong hệ sinh thái OpenClaw, cơ sở dữ liệu bị lộ trực tiếp 35,000 email và 1.5 triệu API Token.",
    "B23E0": "Còn có một điều không thể bỏ qua - LayerX phát hiện lỗ hổng zero-click trên Claude Desktop.",
    "B24E0": "Một sự kiện Google Calendar độc hại có thể kích hoạt thực thi mã từ xa, ảnh hưởng hơn 10,000 người dùng hoạt động.",
    "B25E0": "Vấn đề nằm ở thiết kế kiến trúc MCP, extension trực tiếp sở hữu quyền cấp hệ điều hành, không có ranh giới bảo mật ở giữa.",
    "B26E0": "AI Agent càng mạnh, quyền hạn càng cao, bề mặt tấn công càng lớn.",
    "B27E0": "Đây không phải rủi ro lý thuyết, mà là những việc đã xảy ra rồi.",
    "B28E0": "Vì vậy Lão Kim tôi đã làm một Skill quét bảo mật",
    "B29E0": "Xem xong những sự kiện bảo mật này, phản ứng đầu tiên của Lão Kim tôi là - code của mình có an toàn không?",
    "B30E0": "Claude Code Security dùng không được, nhưng có một thay thế mã nguồn mở gọi là ",
    "B30E2": ".",
    "B31E0": "Công cụ quét bảo mật code mã nguồn mở phổ biến nhất hiện nay, hỗ trợ hàng chục ngôn ngữ lập trình, bao phủ OWASP Top 10.",
    "B32E0": "Không phải suy luận AI, mà là đối sánh quy tắc, nhưng thắng ở chỗ miễn phí, nhanh, trưởng thành.",
    "B33E0": "Lão Kim tôi đã làm một việc: biến Semgrep thành một ",
    "B33E2": ".",
    "B34E0": "Từ nay trong Claude Code chỉ cần nói một câu tiếng Trung là có thể kích hoạt quét bảo mật, không cần nhớ bất kỳ lệnh nào.",
    "B35E0": "Hơn nữa Lão Kim tôi đã open source Skill này, đặt trên GitHub, các bạn lấy dùng luôn.",
    "B36E0": "Cài đặt một chạm: hỗ trợ cả ba nền tảng",
    "B37E0": "Mac / Linux:",
    "B38E0": "Windows (PowerShell):",
    "B39E0": "Script cài đặt sẽ tự động:",
    "B40E0": "1. Kiểm tra Python (nếu chưa cài sẽ gợi ý link tải)",
    "B41E0": "2. Kiểm tra và cài Semgrep (nếu chưa cài sẽ tự động pip install)",
    "B42E0": "3. Copy SKILL.md vào ~/.claude/skills/code-security/",
    "B43E0": "4. Xác nhận cài đặt thành công",
    "B44E0": "Cài xong không cần khởi động lại Claude Code. ",
    "B44E2": " sẽ tự động tải Skill mới.",
    "B45E0": "Cách sử dụng",
    "B46E0": "Mở Claude Code, nói trực tiếp:",
    "B47E0": "Hoặc:",
    "B48E0": "Cũng có thể dùng lệnh slash: /code-security",
    "B49E0": "Claude Code sẽ tự động khớp với Skill này, gọi Semgrep thực hiện quét, rồi cho bạn một báo cáo bảo mật có cấu trúc.",
    "B50E0": "Phân loại theo cao nguy/trung nguy/thấp nguy, mỗi vấn đề kèm gợi ý sửa lỗi.",
    "B51E0": "Các chế độ quét hỗ trợ",
    "B52E0": "Nếu có ích cho bạn, nhớ follow nhé~ ",
    "B53E0": "Code cốt lõi của Skill",
    "B54E0": "Nếu bạn không muốn chạy script cài đặt, tạo thủ công cũng được.",
    "B55E0": "Trong thư mục ~/.claude/skills/code-security/ tạo một file SKILL.md mới, nội dung như sau:",
    "B56E0": "Skill toàn cục đặt ở ~/.claude/skills/code-security/SKILL.md, tất cả dự án đều dùng được.",
    "B57E0": "Skill cấp dự án đặt ở .claude/skills/code-security/SKILL.md, chỉ dự án hiện tại dùng được.",
    "B58E0": "Hướng dẫn định dạng SKILL.md chính thức",
    "B59E0": "Khối --- ở đầu file là metadata YAML, các trường chính thức hỗ trợ:",
    "B60E0": "description là trường quan trọng nhất.",
    "B61E0": 'Claude Code dùng nó để đối sánh ngữ nghĩa - bạn nói "quét bảo mật", nó sẽ đối sánh description của tất cả Skill, tìm cái liên quan nhất để tải.',
    "B62E0": "Vì vậy trong description phải viết rõ điều kiện kích hoạt, từ kích hoạt tiếng Trung lẫn tiếng Anh đều có thể đưa vào.",
    "B63E0": "Semgrep vs Claude Code Security",
    "B64E0": "Phát triển hàng ngày dùng Semgrep làm quét bảo mật cơ bản, đợi Claude Code Security mở rồi nâng cấp.",
    "B65E0": "Hai công cụ giải quyết vấn đề ở các tầng khác nhau, không xung đột.",
    "B66E0": "Lão Kim tôi nghĩ thế nào",
    "B67E0": "Chuyện xảy ra tuần này có thể tóm gọn trong một câu.",
    "B68E0": "AI vừa là công cụ bảo mật tốt nhất, vừa là mối nguy bảo mật lớn nhất.",
    "B69E0": "Anthropic dùng AI tìm ra 500 lỗ hổng mà con người và công cụ truyền thống đều bỏ sót.",
    "B70E0": "Nhưng đồng thời, bản thân AI Agent cũng đang tạo ra vấn đề bảo mật mới - plugin độc hại, rò rỉ dữ liệu, prompt injection, lạm dụng quyền hạn.",
    "B71E0": "Cộng đồng cũng không ngồi yên chờ chết.",
    "B72E0": "SecureClaw đã làm 55 hạng mục kiểm toán bảo mật cho OpenClaw, bao phủ toàn bộ 10 hạng mục OWASP ASI Top 10.",
    "B73E0": "EvoMap thiết kế lại từ giao thức tầng dưới, tích hợp 5 lớp kiểm tra bảo mật, mặc định chế độ dry-run.",
    "B74E0": "Nhưng Lão Kim tôi nghĩ, thay vì đợi người khác giải quyết, chi bằng quét code của mình trước.",
    "B75E0": "Skill này chính là câu trả lời của Lão Kim tôi - miễn phí, mã nguồn mở, nói một câu tiếng Trung là dùng được.",
    "B76E0": "Các bạn nghĩ sao? Bình luận trao đổi nhé.",
    "B77E0": "Địa chỉ kho kiến thức mã nguồn mở (cập nhật thời gian thực ",
    "B77E1": "nhóm trao đổi ",
    "B77E2": "):",
    "B79E0": "Hướng dẫn Claude Code toàn bộ tiếng Trung từ số 0: ",
    "B79E1": "Lão Kim open source giáo trình Claude Code tiếng Trung 100,000 chữ, lộ trình hoàn chỉnh từ zero đến thực chiến doanh nghiệp",
    "B80E0": "Dự án mã nguồn mở ở cuối đây ",
    "B80E1": ": ",
    "B80E2": "Viết công chúng hào 2 năm, từ vài chục đến vài nghìn lượt đọc, tôi làm được nhờ 3 điều này",
    "B81E0": "Mỗi lần tôi đều muốn nhắc nhở, đây không phải khoe khoang, mà là hy vọng những người có ý tưởng hãy dũng cảm tiến lên.",
    "B82E0": "Tôi không biết code, tiếng Anh cũng không giỏi, nhưng tôi đã làm ra được rất nhiều thứ, có thể xem trong kho kiến thức mã nguồn mở ở cuối bài.",
    "B83E0": "Tôi thực sự hy vọng có thể ảnh hưởng nhiều người hơn để thử những kỹ thuật mới, đón nhận thời đại mới.",
    "B84E0": "Cảm ơn bạn đã đọc bài viết của tôi.",
    "B85E0": "Nếu thấy hay, tiện tay nhấn like, đang xem, chia sẻ ba combo nhé🙂",
    "B86E0": "Nếu muốn nhận thông báo đầu tiên, cũng có thể đánh dấu sao cho tôi⭐~ Cảm ơn bạn đã đọc bài viết của tôi. ",
    "B87E0": "Quét mã ",
    "B87E1": "thêm WeChat bên dưới (ghi chú AI) ",
    "B87E2": ", kéo bạn vào ",
    "B87E3": "nhóm trao đổi học AI ",
    "B87E4": "."
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

with open("art2_translated.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Stats: translated={stats['translated']}, kept={stats['kept']}, errors={len(stats['errors'])}")
if stats["errors"]:
    for key in stats["errors"]:
        parts = key.split("E")
        i, j = int(parts[0][1:]), int(parts[1])
        with open('art2_original.json', 'r', encoding='utf-8') as f:
            orig = json.load(f)
        c = orig["blocks"][i]["elements"][j].get("content", "")
        print(f"  MISSING {key}: {repr(c[:100])}")
