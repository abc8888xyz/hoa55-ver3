# -*- coding: utf-8 -*-
import json, sys, re
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff\u3400-\u4dbf]', text))

with open('original_blocks_4.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract exact Chinese segments
segments = []
for bi, block in enumerate(data['blocks']):
    for ei, elem in enumerate(block.get('elements', [])):
        content = elem.get('content', '')
        if content.strip() and has_chinese(content):
            segments.append(content)

translations = [
    "laughing哥: OpenClaw Chia sẻ thực hành: Khám phá cộng tác đa agent",
    "🔗 Link bài gốc: ",
    "Nguyên bản: laughing哥 laughing哥 flashCoder",
    "Ngày 3 tháng 2 năm 2026 14:08  Mỹ",
    "Các bạn cũng có thể thông qua Alibaba Cloud Bailian",
    " để triển khai",
    "Mua lần đầu chỉ từ 7.9 tệ, gia hạn giảm 50%, hỗ trợ các model Qwen3.5, Qwen3-max, Qwen3-coder, GLM-5, GLM-4.7, Kimi-k2.5, v.v.",
    "👉Nhấn link truy cập trực tiếp:",
    "👉Xem hướng dẫn triển khai chi tiết:",
    "Chỉ cần tối đa ba bước, là có thể sở hữu trợ lý AI trực tuyến 7x24 giờ, phản hồi mọi lúc",
    "OpenClaw, tiền thân là Moltbot, trước đó là Clawdbot. Đúng vậy nó đã đổi tên 3 lần. Tính đến hôm nay nó tên là OpenClaw. Là dự án AI mã nguồn mở hot nhất hiện tại. Hot đến mức nào? Số star trên GitHub tăng vọt như tên lửa, hiện tại đã đạt 150k star\nĐịa chỉ dự án: ",
    "Nói đơn giản, nó rất gần với khái niệm nhân viên số theo cách hiểu truyền thống của chúng ta. Cho nó một máy tính, nó có thể hoàn toàn giúp bạn làm việc. Điều kiện là bạn cần triển khai nó trước. Thêm nguyên liệu tức là API key của model lớn, rồi nó có thể chat với bạn qua Telegram hoặc Lark, gửi email, làm nghiên cứu theo chỉ dẫn của bạn - đều là chuyện nhỏ.",
    "Nếu chỉ nói về khía cạnh này thì thực ra nó còn không bằng Doubao, vì API key model lớn không thể tạo hình ảnh, không thể gọi thoại. Vậy làm sao dùng tốt nó? Qua thời gian sử dụng cường độ cao, tôi đại khái tổng kết được 3 điểm. Bài viết này không phải tutorial, thuần túy là ghi chép quá trình thực hành OpenClaw, nếu có thể mang lại cảm hứng cho mọi người thì thật sự là tôi",
    "Cảnh báo nội dung nặng! Bài viết có độ dài hạn chế, phần giới thiệu cơ bản OpenClaw đã xong, toàn bộ nội dung tiếp theo đều cần hiểu trước các kiến thức cơ bản khác của OpenClaw. Khuyến nghị ít nhất đọc thêm 5 bài viết liên quan trước khi tiếp tục đọc",
    "1. Làm tác vụ định thời.",
    "Hãy xem OpenClaw có những khả năng gì, nó có một loạt file cấu hình cơ bản. Tôi để Tiểu Vương chăm chỉ giới thiệu cho bạn. Ví dụ tôi hỏi Tiểu Vương chăm chỉ: Còn bao nhiêu file cấp hệ thống như Agents.md? Giải thích chi tiết chức năng của chúng",
    "Tiểu Vương chăm chỉ chẳng khách sáo cũng chẳng gọi sếp. Trực tiếp làm luôn, tuôn ra hết không giữ lại gì. Đây là phản hồi của nó:",
    "Nhìn chức năng khá nhiều, thực tế cũng đúng là không ít. Ở đây tôi chủ yếu muốn nói về heartbeat - danh sách tác vụ định thời.",
    "Cuối tuần tôi đang dùng bot, lúc đó chưa có Tiểu Vương, anh họ nó ",
    "Cỗ máy đốt token vô tình",
    " làm việc không ít, mỗi giờ gửi một lần báo cáo tiến độ tác vụ định thời. Đây là tin nhắn nó gửi cho tôi, hơn 3 giờ sáng cũng biết dậy làm việc. ",
    "Nghĩa là nó thực sự có thể chạy dữ liệu theo giờ theo điểm, biên đạo theo chỉ dẫn và kế hoạch tác vụ của bạn, máy tính bạn bật 24 giờ thì nó có thể làm việc 24 giờ. Lúc đó tôi dùng khá loạn vì mới tiếp xúc thứ mới cần thời gian làm quen. Giao không ít việc linh tinh, nó đều chạy hết cho tôi.",
    "Skill dịch thẳng nghĩa là gói kỹ năng. Cụ thể nghĩa là gì? DeepSeek cũng vậy, ChatGPT cũng thế, đều là rồng phượng trong người, đều là học bá, tiến sĩ còn kèm hậu tố. Anh em mình so sao cũng không bằng. Nhưng đó là trước đây, bây giờ chúng ta có Skill rồi, đám 9X ngày xưa hay nói câu gì nhỉ",
    "Có thể nói bạn chỉ cách chơi tốt OpenClaw một gói kỹ năng thôi. Nếu bạn không biết dùng Skill nào? Hỏi trực tiếp nó là được",
    "3. Xử lý lỗi",
    "Trước hết đây là một dự án mã nguồn mở mới nổi, do khả năng mở rộng và tính linh hoạt cao nên tôi cho rằng rất có tiềm năng. Đồng thời thỉnh thoảng sẽ bị lỗi. Ví dụ không trả lời tin nhắn:",
    "Tiểu Vương kiểu này tôi cũng lười để ý. Vì tôi đã SSH tiếp quản Mac headless, và cài sẵn Claude bên trong, tôi trực tiếp kết nối máy chủ của nó, để Claude xem có chuyện gì giúp tôi sửa. Ví dụ thế này, tôi nói với Claude xem nó lại không trả lời tôi rồi",
    "Rồi Claude trực tiếp sửa xong cho tôi",
    "Chỉ cần nó đang typing là đang làm việc ",
    "Bạn thấy đấy, chúng ta có đầy đủ phương án dự phòng, Tiểu Vương chăm chỉ lại hì hục làm việc.",
    "Ngoài ra nó cũng có thể tự sửa chính mình. ",
    "Tối qua tôi cần mở thêm một bot cho vợ, OpenClaw có nhiều chế độ chạy đa phiên, ví dụ tạo mới một profile là một cách. Điều này sẽ mở một cổng mới chạy một bộ dịch vụ mới. Bạn tự cấu hình Telegram, người khác không có Telegram thì cấu hình Lark, tài khoản độc lập với nhau.",
    "Hôm qua tôi thử cấu hình nhưng có vấn đề, bot Lark mới cấu hình long connection cứ không kết nối được, dịch vụ cổng mới không chạy được. Rồi tôi nói với bot của profile mình về vấn đề này, nó cũng có thể tìm nguyên nhân giải quyết vấn đề, vì chúng cùng trên một máy nên nó có thể sửa các file này. Nó lần lượt làm những điều sau:",
    "Mở rộng",
    "Bình thường một bài viết đến đây có thể kết thúc rồi, dù gì cũng đã 1.500 từ. Nhưng vì người viết bài là tôi, nên tôi mở rộng thêm một chút. Hiện tại tôi đã tạo ba bot: Cỗ máy đốt token vô tình, Tiểu Vương chăm chỉ và Yoyo dễ thương. Tôi kéo cả ba vào một nhóm. Ngoài tôi ra đều là bot",
    "Tiểu Vương chăm chỉ và Yoyo dễ thương là cặp song sinh nam nữ anh em ruột, cả hai đều ở trong Mac headless của tôi, cùng trong một profile, khác biệt là hai agents khác nhau.",
    "Một cái khác chạy trên server, Cỗ máy đốt token vô tình, trước đó chat khá nhiều, context bị ô nhiễm một chút, lúc nào đó sẽ xóa sạch. Như vậy tôi có 3 agent, lý thuyết là 3 người có thể làm việc riêng rồi giao tiếp công việc trong một nhóm. Điểm quan trọng là có thể làm việc 24 giờ không ăn không uống không ngủ. Chi phí duy nhất có thể là token. Nhưng vì",
    "Vừa xem mức dùng, mới tiêu hơn 30 triệu, nửa đêm không có AI nào đang làm việc, sao được? Thôi không nói nữa tôi phải sắp xếp lên thôi",
]

mapping = {}
for orig, trans in zip(segments, translations):
    mapping[orig] = trans

with open('mapping_4.json', 'w', encoding='utf-8') as f:
    json.dump(mapping, f, ensure_ascii=False, indent=2)
print(f"Saved {len(mapping)} translations for {len(segments)} segments")
