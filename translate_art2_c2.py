#!/usr/bin/env python3
"""Translate article 2 for batch chunk 2"""
import json, sys, re, copy

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

def has_chinese(t):
    return bool(re.search(r'[\u4e00-\u9fff\u3400-\u4dbf]', t))

d = json.load(open('art2_orig_c2.json', 'r', encoding='utf-8'))

vn = [
    "芋头小宝: OpenClaw kết nối Feishu và DingTalk rốt cuộc có thể chơi gì? Sau một ngày đào bới use case cuối cùng cũng hiểu rồi...",
    "🔗 Link bài gốc: ",
    "Bài gốc Yutou Xiaobao Yutou Xiaobao GenAI Cộng sinh nhân",
    "Ngày 3 tháng 2 năm 2026 07:55  Thượng Hải",
    "Các bạn cũng có thể thông qua Alibaba Cloud Bailian",
    "để triển khai",
    "Mua lần đầu chỉ từ 7,9 tệ, gia hạn giảm từ 50%, hỗ trợ các mô hình Qwen3.5, Qwen3-max, Qwen3-coder, GLM-5, GLM-4.7, Kimi-k2.5",
    "👉Nhấn link truy cập trực tiếp:",
    "👉Xem hướng dẫn triển khai chi tiết:",
    "Chỉ cần tối đa ba bước, bạn sẽ có trợ lý AI trực tuyến 7x24 giờ, phản hồi mọi lúc",
    "Gần đây openclaw (tên cũ clawdbot) hot đến nổ trời.",
    "Tôi cũng dành cả cuối tuần để chơi thử một phen.",
    "Bài viết này chia sẻ với mọi người một số kinh nghiệm thực hành và use case của tôi.",
    "Lưu ý an toàn quan trọng trước khi bắt đầu",
    "Trước khi bắt đầu, phải nhấn mạnh lặp đi lặp lại: ",
    "OpenClaw là một trợ lý AI có quyền hạn cực cao ",
    ". Nó có thể mô phỏng chuột bàn phím của bạn, đọc file của bạn. Vì vậy, ",
    "tuyệt đối không ",
    "chạy trực tiếp trên máy chính có chứa dữ liệu bí mật quan trọng hoặc dữ liệu duy nhất.",
    "Môi trường chạy được khuyến nghị (xếp theo mức độ an toàn):",
    "Máy ảo / Docker ",
    "(ưu tiên hàng đầu, cách ly hoàn toàn, hỏng thì tạo lại)",
    "Máy tính dự phòng không sử dụng ",
    "(đảm bảo không có file quan trọng không thể khôi phục)",
    "Lưu ý: Nếu bạn cần nó hoạt động 24 giờ (ví dụ làm chatbot nhóm), nên triển khai trên cloud server và khuyến nghị dùng Docker để cài đặt. (Nhưng luôn chú ý mức tiêu thụ token)",
    "Sau khi cài đặt openclaw theo nhu cầu, hiện tại hai use case chính là: ",
    "Chuyển đổi model & Thêm channels nội địa",
    "Tiếp theo là chia sẻ thực hành hai use case này.",
    "Một, Cách chuyển đổi model:",
    "Cấu hình tương tác qua command line",
    "Nhập openclaw config trong terminal, thao tác lần lượt theo lựa chọn bên dưới",
    "Cuối cùng chọn model mới để thay thế, ví dụ ở đây tôi đổi sang kimi",
    "Cuối cùng trong giao diện model hiện ra, chọn model liên quan đến kimi-coding",
    "Sau khi đổi model, nhớ khởi động lại gateway: openclaw gateway restart",
    "Sửa file cấu hình",
    "Tất nhiên bạn có thể trực tiếp sửa models trong file cấu hình, dùng lệnh nano ~/.openclaw/openclaw.json để mở file cấu hình,",
    "Sau đó tìm phần models trong file cấu hình, tham khảo các model khác để sửa và cấu hình thông số.",
    "Hai, Phương pháp kết nối kênh nội địa",
    "Kết nối kênh, nước ngoài thì không nói, trong nước hiện tại chủ yếu hỗ trợ: Feishu, DingTalk, WeCom, QQ.",
    "Hôm nay giới thiệu ngắn gọn một cách cài đặt rất dễ và tiết kiệm công (nhưng sẽ hơi tốn token, bạn kỹ thuật có thể cài trực tiếp qua command line).",
    "Ý tưởng cốt lõi là phương pháp ba bước:",
    "Tìm tài nguyên trên github cài plugin",
    "Cấu hình thông tin chứng chỉ theo hướng dẫn",
    "Kiểm tra kết nối",
    "1. Kết nối Feishu",
    "Đầu tiên nhập thông tin sau trong giao diện WebUI hoặc TUI của bạn, để openclaw tự cài plugin",
    "Prompt:",
    "Lúc này bạn có thể đi làm việc khác.",
    "Sau khi cài xong, nó sẽ cho bạn biết tiếp theo cần bạn ",
    "đi đâu, lấy nội dung gì ",
    "cho nó.",
    "Tuy nhiên các bước thao tác khá nhiều, nếu bạn nào chưa quen có thể tham khảo tài liệu của @林月半子 để cấu hình https://mp.weixin.qq.com/s/qnDCqYtZr4xvGx1mgEDKVw",
    "Sau khi kết nối thành công, có thể trò chuyện trên Feishu rồi.",
    "2. Kết nối DingTalk",
    "Vì chúng ta vừa cài xong plugin Feishu, nên cũng có thể trò chuyện trực tiếp trong cửa sổ chat bot Feishu.",
    "Tìm bot tôm hùm bạn vừa tạo, nhập thông tin sau",
    "Prompt:",
    "Sau khi cài xong, nó sẽ thông báo loại chứng chỉ bạn cần cung cấp và lấy ở đâu.",
    "Tiếp theo theo hướng dẫn của nó, truy cập DingTalk Developer Console: https://open-dev.dingtalk.com/",
    "Chọn Phát triển ứng dụng, tạo ứng dụng.",
    "Điền thông tin liên quan của bot, nhấn lưu.",
    "Cấu hình bot trong trang chuyển hướng",
    "Điền các mục bắt buộc trong trang cấu hình (tuân thủ yêu cầu, tùy chỉnh cá nhân đều được), ở phần chế độ nhận tin nhắn cuối cùng chọn \"stream mode\")",
    "Cuối cùng tạo phiên bản và phát hành ở phần Quản lý phiên bản & Phát hành.",
    "Sau khi phát hành xong, có thể tìm thông tin chứng chỉ cần thiết trong \"Chứng chỉ & Thông tin cơ bản\"",
    "Robot Code (giống với Client ID)",
    "Corp ID (ID doanh nghiệp)",
    "Agent ID (ID ứng dụng)",
    "Trong đó corp ID lấy bằng cách nhấn vào avatar của bạn trên trang hiện tại.",
    "Sau đó gửi thông tin chứng chỉ đã lấy cho openclaw của bạn, để nó giúp bạn cấu hình.",
    "Prompt:",
    "Đợi một lát, sau khi nó phản hồi đã cấu hình thành công.",
    "Mở ứng dụng DingTalk trên điện thoại, tạo một nhóm chat (bạn là admin), thêm bot bạn vừa tạo trong cài đặt nhóm.",
    "Sau đó bạn có thể vui vẻ @nó để chat trong nhóm rồi",
    "Tất nhiên, nếu không tạo nhóm chat, bạn tự chat riêng với bot cũng không vấn đề gì.",
    "Lưu ý:",
    "Tổ chức tạo bot phải cùng tổ chức bạn đang sử dụng, nếu bạn tạo bot ở ",
    "Tổ chức A ",
    "nhưng kéo nhóm sử dụng ở ",
    "Tổ chức B ",
    "thì chắc chắn không tìm thấy.",
    "Khi tạo nhóm chat, tất cả thành viên phải được thêm vào cùng một tổ chức trước, nếu không bot cũng sẽ không thêm thành công.",
    "3. Kết nối WeCom",
    "Phương pháp kết nối WeCom tương tự như trên, cũng phải cài plugin trước (https://github.com/sunnoy/openclaw-plugin-wecom), sau đó cấu hình thông tin chứng chỉ bot WeCom, cuối cùng kiểm tra hiệu quả.",
    "Ở đây có một lưu ý, khác với DingTalk và Feishu, callback URL của WeCom cần được cấu hình thành địa chỉ công cộng có thể truy cập, nếu openclaw của bạn chạy trong môi trường local thì cần dùng công cụ xuyên hầm mạng nội bộ (như ngrok), hoặc chuyển lên cloud server mới có thể tạo thành công.",
    "(Đúng rồi, cái này tôi không kết nối, chủ yếu thật sự hoàn toàn không có use case)",
    "Ba, Khám phá và chia sẻ cách chơi",
    "Trước khi chơi, hãy tìm hiểu ranh giới khả năng của bot này.",
    "Ưu điểm:",
    "Giống như một AI IDE, có thể thao tác file, chạy skills, viết code cài plugin, làm những thứ mà phần mềm chat AI thuần túy không làm được, tính linh hoạt và không gian tưởng tượng rất lớn.",
    "Có thể tích hợp với các IM khác nhau, thông qua điện thoại mọi lúc mọi nơi điều khiển bot giúp bạn làm việc.",
    "Nhược điểm:",
    "Tốn token.",
    "Phản hồi chậm, thỉnh thoảng phải reconnect.",
    "(Nếu không có use case mang lại phản hồi tích cực, khuyên bạn nên chơi Yuanbao hoặc Doubao miễn phí còn hơn)",
    "Còn có quyền hạn lớn, đây vừa là ưu điểm vừa có thể là nhược điểm, tôi không bình luận thêm.",
    "Rốt cuộc có thể làm gì?",
    "Sau khi biết đến bot này tuần trước, tôi đã liên tục suy nghĩ nó có use case gì.",
    "Cái gọi là 7x24, thực ra cũng chỉ là chạy một số tác vụ định kỳ, những thứ này tôi dùng n8n để chạy, ổn định và tiết kiệm.",
    "Triệu hồi làm việc mọi lúc mọi nơi, thì đúng là phải có use case thực tế, cần nó có thể túc trực khi tôi rời máy tính, một tin nhắn là lập tức giúp tôi làm việc (nếu không có thì không cần thử, cái này thật sự đốt token).",
    "Nhưng sau khi kết nối bot các kênh, tôi lại phát hiện một use case thú vị:",
    "Tôi tạo \"Đặc vụ tôm hùm số 1\" trên Feishu, cho nó một tài liệu; quay sang hỏi \"Đặc vụ tôm hùm số 2\" trên DingTalk, nó cũng có thể gọi liền mạch thông tin từ tài liệu đó cho tôi.",
    "Cái này hơi giống khái niệm trong Naruto ",
    "Lục đạo Pein - chia sẻ thị giác ",
    ". Còn các bot này thì chia sẻ ngữ cảnh, sau đó truyền và chia sẻ dữ liệu trong các IM khác nhau.",
    "Tuy nhiên cũng chỉ là chơi vui thôi, use case thực tế tôi vẫn chưa có.",
    "Openclaw có thể là hình mẫu ban đầu của một hướng ứng dụng AGI di động trong tương lai, trong tương lai mọi người đều có thể là OPC, mọi người đều nuôi một nhóm nhân viên AI, và năng lực của nhóm nhân viên này có thể quyết định sự nghiệp của bạn.",
    "Haha nói vậy thì có cảm giác như game nuôi nhân vật rồi, chúng hiện tại đều là bạn nhỏ của bạn, sẽ dựa trên \"phương pháp giáo dục\" của bạn mà tương lai thành tài hoặc đi chệch hướng.",
    "Thôi không nói nữa, tôi phải đi dạy quy tắc cho mấy đặc vụ tôm hùm của tôi rồi~",
]

translated = copy.deepcopy(d)
total_seg = 0
trans_count = 0
kept_count = 0
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

with open('art2_translated_c2.json', 'w', encoding='utf-8') as f:
    json.dump(translated, f, ensure_ascii=False, indent=2)

print(f'Total segments: {total_seg}, Translated: {trans_count}, Kept: {kept_count}')
print(f'Chinese segments found: {cn_idx}, Vietnamese translations: {len(vn)}')
print(f'Total blocks: {len(translated["blocks"])}')
