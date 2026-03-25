#!/usr/bin/env python3
"""Translate article 3 for batch chunk 2"""
import json, sys, re, copy

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

def has_chinese(t):
    return bool(re.search(r'[\u4e00-\u9fff\u3400-\u4dbf]', t))

d = json.load(open('art3_orig_c2.json', 'r', encoding='utf-8'))

vn = [
    "Phong Diệp: Nên lưu lại｜Hướng dẫn chi tiết từng bước kết nối Clawdbot với DingTalk và Feishu, chi phí chỉ vài đồng",
    "Các bạn cũng có thể thông qua Alibaba Cloud Bailian",
    "để triển khai",
    "Mua lần đầu chỉ từ 7,9 tệ, gia hạn giảm từ 50%, hỗ trợ các mô hình Qwen3.5, Qwen3-max, Qwen3-coder, GLM-5, GLM-4.7, Kimi-k2.5",
    "👉Nhấn link truy cập trực tiếp:",
    "👉Xem hướng dẫn triển khai chi tiết:",
    "Chỉ cần tối đa ba bước, bạn sẽ có trợ lý AI trực tuyến 7x24 giờ, phản hồi mọi lúc",
    "Hôm nay chia sẻ với mọi người một phương án triển khai Moltbot siêu đơn giản.",
    "Hướng dẫn này hỗ trợ triển khai Feishu + DingTalk.",
    "Moltbot chính là CLAWDBOT đang lan truyền chóng mặt trên mạng gần đây, vì tên quá giống Claude Code nên bị buộc phải đổi tên.",
    "Các bạn vào đây chắc gần đây đều bị Moltbot tràn ngập timeline rồi đúng không, đồng thời cũng biết ngưỡng sử dụng cao đến mức nào.",
    "Đầu tiên Mac mini đang lan truyền trên mạng khiến người ta khó mà xuống tay.",
    "Nhưng các nền tảng lớn trong nước hành động cũng rất nhanh, đây, đã có ngay phương án thay thế.",
    "Hôm nay dùng Service Marketplace của Alibaba Cloud để triển khai Moltbot, thật sự chỉ cần có tay là làm được (nhiều bẫy tôi đã giẫm hết rồi, cứ theo mà chép bài là xong).",
    "Mua server + Moltbot",
    "Đừng nghe đến server mà nghĩ là cao siêu gì, thực tế nó chỉ là một chiếc máy tính",
    "Đầu tiên đi đăng ký tài khoản Alibaba Cloud tại địa chỉ:",
    "Cách cài đặt triển khai Alibaba Cloud rất đơn giản, tôi giới thiệu hai cách: cách nhanh, trực tiếp mua Lightweight Application Server đã cài sẵn Moltbot. Sau khi đăng nhập truy cập địa chỉ này:",
    "Image ứng dụng này dựa trên hệ điều hành Alibaba Cloud Linux 3.2104 LTS 64bit, có nguồn từ ComputeNest của Alibaba Cloud.",
    "Tại",
    "Lightweight Application Server",
    "trang đã có sẵn tài nguyên, nếu muốn thay đổi cấu hình hãy tham khảo nội dung bên dưới. Giá thực ra khá hợp lý, tất nhiên nếu muốn dùng thử ngắn hạn có thể chuyển sang 1 tháng, 1 tháng là thời gian ngắn nhất, chỉ 56 xu. Ngoài ra còn có cách tốt hơn, tính phí theo thời gian thực, phù hợp cho trường hợp thử chơi vài ngày, không muốn dùng nữa thì giải phóng bất cứ lúc nào. Truy cập trực tiếp Service Marketplace của ComputeNest Alibaba Cloud sau khi đăng nhập tại địa chỉ: https://computenest.console.aliyun.com/service/market/cn-hangzhou",
    "Trực tiếp nhấn Bắt đầu triển khai, vào trang trông như thế này, cứ cấu hình theo hướng dẫn của tôi bên dưới:",
    "Tiếp theo là các cấu hình triển khai trực tiếp lên DingTalk. Chúng ta có thể cấu hình xong trước, rồi quay lại điền thông tin.",
    "Nếu không biết thao tác thế nào, trang này đều có link truy cập trực tiếp, thao tác cụ thể sau khi nhấn vào sẽ có phương pháp chi tiết ở phần sau bài viết. Chưa đăng ký DingTalk thì cứ theo hướng dẫn đăng ký. Tiếp theo là các bước lấy API-KEY và thông tin DingTalk liên quan.",
    "Cấu hình model Bailian, lấy API-Key",
    "Model Bailian có nhiều model có hạn mức miễn phí, rất phù hợp để dùng thử.",
    "Mọi người nhớ bật tính năng tự động dừng khi hết hạn mức miễn phí hàng loạt, tránh phát sinh chi phí thêm, ai không quan tâm tiền thì bỏ qua. Sau đó vào trang Quản lý khóa, ở phía dưới cùng menu bên trái trang, nhấn",
    "Tạo API-Key",
    "Sau khi tạo xong, quay lại trang server vừa rồi là có thể chọn sử dụng trực tiếp.",
    "Bây giờ chúng ta đã có tất cả thông tin bắt buộc, đặt hàng trực tiếp.",
    "Sau khi triển khai xong, chúng ta sẽ nhận được một địa chỉ Webhook, địa chỉ này chính là",
    "Ở đây có một bẫy rất lớn, đó là địa chỉ này, bạn truy cập trực tiếp sẽ không được. Địa chỉ này là sai. Cần thao tác thủ công, ghép nối địa chỉ, ví dụ:",
    "http://[IP của bạn]:18789?token=[đoạn cuối của địa chỉ]",
    "Hoặc bạn trực tiếp nhấn vào địa chỉ đó, rồi trên thanh địa chỉ xóa thủ công phần lệnh ở giữa là truy cập bình thường. Phần này chính là TOKEN của bạn, thông tin xác thực danh tính quan trọng. Nếu bị lộ thì:",
    "Bất kỳ ai có link này đều có thể vượt qua xác thực đăng nhập trực tiếp, có được quyền quản trị console Moltbot của bạn. Đây chính là bước đầu tiên sử dụng thành công",
    "Moltbot, đến bước này nếu không cần tích hợp DingTalk hoặc Feishu thì đã xong, đây chính là phiên bản sử dụng.",
    "Nếu muốn chuẩn bị tích hợp DingTalk và Feishu, chúng ta cần thực hiện thêm một số cài đặt ở đây:",
    "Bật truy cập ResponseAPI, sau này sẽ tạo AppFlow truy cập Moltbot qua API.",
    "Cấu hình DingTalk",
    "Tạo ứng dụng DingTalk",
    "Vì tạo ứng dụng DingTalk cần có quyền developer, nên tốt nhất là admin của tổ chức hoặc tài khoản có quyền khác. Nếu chưa có tổ chức có thể tự tạo một tổ chức, platform đều có hướng dẫn, cứ theo mà làm. Trong thanh navigation bên trái của Application Development, nhấn",
    "Ứng dụng DingTalk",
    ", tại",
    "Ứng dụng DingTalk",
    "nhấn góc trên bên phải",
    "Tạo ứng dụng",
    "Tại",
    "Tạo ứng dụng",
    "panel, điền",
    "Tên ứng dụng",
    "và",
    "Mô tả ứng dụng",
    ", tại",
    "Icon ứng dụng",
    "upload icon (không upload thì sẽ là icon mặc định như hình), xong nhấn",
    "Lưu",
    ". Sau đó nhấn vào ứng dụng vừa tạo, vào trang mới",
    "Lấy Client ID và Client Secret của ứng dụng",
    "Sau đó ở menu bên trái chọn",
    "Chứng chỉ & Thông tin cơ bản",
    ", copy",
    "và",
    ", dùng cho cấu hình server vừa rồi.",
    "2 Tạo thẻ tin nhắn",
    "Vì bot DingTalk hỗ trợ trả kết quả streaming qua tin nhắn thẻ, bạn cần tạo template thẻ để gửi tin nhắn. Truy cập Card Platform, nhấn",
    "Tạo template mới",
    "Tại ô input tạo template, điền thông tin template, nhấn",
    "Tạo",
    "Ở đây không dùng template có sẵn, thậm chí không cần thao tác thêm gì, tạo xong trực tiếp vào trang mới cũng không cần thao tác gì, trực tiếp",
    "Lưu",
    "và",
    "Phát hành",
    "template là xong. Sau đó nhấn",
    "Quay lại",
    "trang danh sách template.",
    "Sau khi quay lại, chọn copy Template ID, dùng để tạo flow kết nối DingTalk.",
    "Bây giờ đã có ứng dụng và thẻ, cần cấp quyền gửi tin nhắn thẻ cho ứng dụng",
    "Tìm ứng dụng vừa tạo, nhấn tên ứng dụng vào trang chi tiết. Ở menu bên trái chọn",
    "Cấu hình phát triển",
    "Quản lý quyền",
    ", ở ô tìm kiếm bên trái lần lượt nhập Card.Streaming.Write và Card.Instance.Write, rồi ở cột thao tác nhấn",
    "Xin cấp quyền",
    "Tạo AppFlow (phiên bản DingTalk)",
    "Tại trang ComputeNest, tìm nút này, nhấn vào",
    "Dùng template AppFlow tạo flow kết nối",
    "Ở đây đã có sẵn template, chúng ta không cần tự tạo, nhanh và ổn định. Feishu sau này cũng thao tác tương tự. Nhấn template, nhấn Sử dụng ngay để vào quy trình tạo",
    "Tại trang hướng dẫn ủy quyền tài khoản của flow kết nối, nhấn Thêm chứng chỉ mới. Nhập Token đã lấy khi cấu hình Moltbot",
    "[chính là chuỗi ghép nối phía sau địa chỉ vừa rồi].",
    "Tại trang hướng dẫn cấu hình",
    "Ủy quyền tài khoản",
    "của flow kết nối, nhấn",
    "Thêm chứng chỉ mới",
    ". Tại hộp thoại tạo chứng chỉ, điền Client ID và Client Secret của ứng dụng đã tạo trên DingTalk, quên thì kéo lên tìm lại, và đặt tên chứng chỉ tùy chỉnh.",
    "Tại",
    "Hành động thực thi",
    "trang hướng dẫn cấu hình, điền",
    "Tên model",
    "Địa chỉ công cộng",
    "và Template ID đã lấy từ template thẻ, xong nhấn",
    "Bước tiếp theo",
    "Tên model: Tham khảo các model Bailian hỗ trợ để điền.",
    "Ở đây nếu không biết tên model, có một cách đơn giản là trực tiếp hỏi BOT trên trang truy cập vừa rồi:",
    "Trực tiếp copy cái này là được. Còn địa chỉ công cộng là bẫy lớn, địa chỉ nhất định phải sạch, chỉ có IP và port:",
    "Chính là đoạn này của địa chỉ truy cập,",
    "Nhớ kỹ không được có http hoặc HTTPS!!!!!",
    "Tại",
    "Thông tin cơ bản",
    "trang hướng dẫn cấu hình, điền",
    "Tên flow kết nối",
    "và",
    "Mô tả flow kết nối",
    "(nên giữ mặc định), xong nhấn",
    "Bước tiếp theo",
    ". Giao diện thông báo cấu hình thành công, copy",
    ", nhấn",
    "Phát hành",
    "Đến đây, AppFlow kết nối DingTalk đã cấu hình thành công. Bây giờ chỉ còn bước cuối cùng, đó là biến ứng dụng thành bot DingTalk, phát hành lên client DingTalk để bắt đầu chat.",
    "Cấu hình bot DingTalk - Quay lại danh sách ứng dụng trên DingTalk Open Platform: Tìm ứng dụng vừa tạo, nhấn tên ứng dụng vào trang chi tiết. Tại trang Thêm khả năng ứng dụng, tìm thẻ Bot, nhấn Thêm. Các thông tin khác tự điền, không ảnh hưởng. Chỉ có một điểm: Chế độ nhận tin nhắn chọn HTTP mode, hiện tại AppFlow chỉ hỗ trợ HTTP mode, chọn Stream mode sẽ không trả được tin nhắn.",
    "Còn địa chỉ nhận tin nhắn này chính là cái mà chúng ta đã lấy từ AppFlow cấu hình ở trên",
    "Cài đặt xong, trực tiếp nhấn phát hành.",
    "Sau đó quay lại trang chi tiết ứng dụng, thực hiện phát hành phiên bản.",
    "Đến đây, tất cả cấu hình online đã thật sự hoàn thành.",
    "Vào client DingTalk, thêm bot vừa tạo: Nhấn Cài đặt nhóm:",
    "Rồi nhấn thêm bot:",
    "Xong! Con trâu cyber của bạn chính thức lên sóng! Bắt đầu chat! Bảo nó làm việc! Xem có thật sự lợi hại như trên mạng ca ngợi không.",
    "Feishu + CLAWDBOT",
    "Thực ra Feishu và DingTalk cũng không khác nhau mấy, quy trình đều giống nhau, chỉ khác là lấy thông tin cấu hình nào thôi.",
    "Nên tôi trực tiếp nói chi tiết quy trình:",
    "Đăng nhập Feishu Developer Console, địa chỉ: https://open.feishu.cn/app",
    "Nhấn",
    "Tạo ứng dụng doanh nghiệp tự xây",
    ", điền thông tin ứng dụng rồi nhấn Tạo.",
    "Ở thanh navigation bên trái nhấn",
    "Thêm khả năng ứng dụng",
    ", chọn",
    "Thêm theo khả năng",
    "tab, tìm",
    "Bot",
    "thẻ, nhấn",
    "Thêm",
    "Ở thanh navigation bên trái nhấn",
    "Quản lý quyền",
    ", nhấn Mở quyền, tìm và thêm các quyền API sau:",
    "Thu thập chứng chỉ cần thiết cho tích hợp. Khi cấu hình kết nối AppFlow sau này cần dùng những thông tin này.",
    "Tạo flow kết nối Feishu",
    "Tiếp tục quay lại trang tạo AppFlow flow vừa rồi, chọn template Feishu-Moltbot trong Trung tâm template, nhấn",
    "Sử dụng ngay, giống như DingTalk",
    "Nhấn thêm chứng chỉ xác thực Feishu, điền tên chứng chỉ, tham khảo hình dưới điền thông tin đã lấy ở bước ba. Điền xong nhấn OK và chọn chứng chỉ đã tạo trong dropdown.",
    "Tạo chứng chỉ xác thực Moltbot. Điền chứng chỉ lấy ở bước hai, điền xong nhấn OK và chọn chứng chỉ đã tạo trong dropdown.",
    "Nhấn bước tiếp theo, tiếp tục điền IP công cộng:port, port mặc định là 18789.",
    "Nhắc lại lần nữa không được có http hoặc https.",
    "Cấu hình xong nhấn phát hành, copy và lưu WebhookUrl.",
    "Cấu hình bot Feishu",
    "Quay lại Feishu Developer Console, ở thanh navigation bên trái nhấn",
    "Sự kiện & Callback",
    ", tại",
    "Cấu hình sự kiện",
    "tab, nhấn",
    "  nút cấu hình ",
    "Phương thức đăng ký",
    "chọn",
    "Gửi sự kiện đến server developer",
    ", điền WebhookUrl đã copy ở bước trước, nhấn",
    "Lưu",
    "Tại",
    "Cấu hình sự kiện",
    "tab phần",
    "Sự kiện đã thêm",
    "khu vực, nhấn",
    "Thêm sự kiện",
    ", tìm và thêm",
    "Nhận tin nhắn",
    "sự kiện.",
    "Điền xong, ở thanh navigation bên trái nhấn",
    "Quản lý phiên bản & Phát hành",
    ", tạo phiên bản hoặc nhấn phiên bản chỉnh sửa mới nhất, điền thông tin liên quan rồi lưu và gửi phê duyệt.",
    "Cấu hình xong, có thể thêm bot vừa tạo vào một nhóm nào đó, từ đó thực hiện tương tác giữa bot và thành viên trong nhóm.",
    "Hiện tại chỉ hỗ trợ thêm bot trên Feishu desktop. Nếu cần sử dụng bot trong nhóm ngoại bộ, có thể tham khảo tài liệu cấu hình bot hỗ trợ nhóm ngoại bộ và chat riêng với người dùng ngoại bộ.",
    "Thêm bot theo đường dẫn:",
    "Cài đặt",
    "Bot nhóm",
    "Thêm bot",
    "@bot gửi tin nhắn là có thể trò chuyện.",
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

with open('art3_translated_c2.json', 'w', encoding='utf-8') as f:
    json.dump(translated, f, ensure_ascii=False, indent=2)

print(f'Total segments: {total_seg}, Translated: {trans_count}, Kept: {kept_count}')
print(f'Chinese segments found: {cn_idx}, Vietnamese translations: {len(vn)}')
print(f'Total blocks: {len(translated["blocks"])}')
