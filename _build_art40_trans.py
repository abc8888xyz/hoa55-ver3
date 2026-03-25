# -*- coding: utf-8 -*-
"""Build translated JSON for article 40"""
import json, sys, copy

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

with open('_art40_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

trans = copy.deepcopy(data)

# Translation map: block_index -> list of translated text_run contents (in order)
# URLs, commands, and English terms are kept as-is
translations = {
    0: ["Sim: Hướng dẫn moltbot cực chi tiết dành cho người mới (tên cũ clawdbot) -- phiên bản Discord"],
    1: ["Các bạn có thể triển khai thông qua Alibaba Cloud Bailian ", "Coding Plan ", "để triển khai", ":"],
    2: ["Mua lần đầu chỉ từ 7.9 tệ, gia hạn giảm từ 50%, hỗ trợ Qwen3.5, Qwen3-max, Qwen3-coder, GLM-5, GLM-4.7, Kimi-k2.5 và các mô hình khác"],
    3: ["👉 Nhấn vào link truy cập ngay: ", "https://t.aliyun.com/U/0iiOuy"],
    4: ["👉 Xem hướng dẫn triển khai chi tiết: ", "https://t.aliyun.com/U/MNkA9b"],
    5: ["Chỉ cần tối đa ba bước, bạn sẽ có trợ lý AI hoạt động 7x24 giờ, phản hồi bất cứ lúc nào"],
    6: ["Vừa test xong skills, đã thấy mọi người đang bàn tán rần rần về 🦞 clawdbot (giờ đổi tên thành moltbot)"],
    7: ["Các kiểu như moltbot là nhân viên AI đầu tiên của bạn, phân thân kỹ thuật số..."],
    8: ["Thậm chí mọi người còn đặc biệt đi mua Mac mini chỉ để chạy moltbot"],
    9: ["Đến mức Mac mini hết hàng luôn"],
    10: ["Hơn nữa trên GitHub đã có 93 nghìn star, vì quá hot nên cũng bị Anthropic kiện, đổi tên thành: moltbot"],
    11: ["Lý do là vì tên cũ clawdbot khiến người ta nhầm tưởng là sản phẩm khác của Claude Code"],
    12: ["「Nói về bối cảnh trước」Moltbot là gì"],
    13: ["Địa chỉ GitHub chính thức: ", "https://github.com/moltbot/moltbot"],
    14: ["Theo lời giới thiệu chính thức: moltbot là một trợ lý AI cá nhân chạy trên thiết bị của chính bạn"],
    15: ["Theo mình, nó là một Agent cục bộ có quyền hạn cực cao, có thể được kích hoạt trên các phần mềm chat khác nhau."],
    16: ["Quyền hạn cực cao nghĩa là nó có thể dễ dàng đọc các file trên máy tính cục bộ của bạn, thậm chí chỉnh sửa chúng"],
    17: ["Đó là lý do mọi người đều đi mua Mac mini, vẫn không yên tâm giao máy chính cho AI"],
    18: ["Nhưng để thử nghiệm, chẳng lẽ đi mua một cái mini, lỡ chơi xong hết hứng thú, bỏ ra 3-4 nghìn tệ để bám bụi thì không đáng lắm."],
    19: ["Vì vậy chúng ta chuyển sang dùng máy chủ đám mây, chỉ 20-30 tệ một tháng, còn có thể chạy 24 giờ, tiền điện cũng chẳng đáng lo."],
    20: ["Hiện tại Tencent Cloud và Alibaba Cloud đều đã hỗ trợ"],
    21: ["Hướng dẫn sẽ sử dụng Tencent Cloud để làm ví dụ, có triển khai một cú nhấp, không cần cấu hình môi trường phức tạp."],
    22: ["「Cách cài đặt moltbot」"],
    23: ["Mở máy chủ đám mây"],
    24: ["Trước tiên vào Tencent Cloud: ", "https://cloud.tencent.com/act/pro/double12-2025?fromSource=gwzcw.10342314.10342314.10342314&utm_medium=cpc&utm_id=gwzcw.10342314.10342314.10342314#MS"],
    25: ["Tìm Lightweight Application Server, cấu hình tối thiểu chọn 2 nhân 2G trở lên, ", "khuyến nghị chọn khu vực Singapore/Hong Kong", ", đừng mua server đại lục, có vấn đề về mạng, mở mua một máy, nếu chưa xác thực danh tính thì hãy đi xác thực nhé."],
    26: ["Nhớ chọn ", "image moltbot"],
    27: ["Sau đó vào góc trên bên phải trang web tìm Console để vào, tìm Lightweight Application Server"],
    28: ["Đăng nhập máy chủ đám mây"],
    29: ["Quét mã đăng nhập"],
    30: ["Cấu hình moltbot"],
    31: ["Nhập lệnh: clawdbot onboard, nhấn Enter"],
    32: ["Chạy ", "clawdbot onboard xong, cần dùng bàn phím để hoàn thành ", "các thao tác cấu hình tiếp theo, thao tác chính: phím mũi tên điều khiển lựa chọn, Enter để chọn và xác nhận."],
    33: ["Đây là tuyên bố miễn trừ trách nhiệm chính thức, ý nghĩa là: Tôi hiểu rằng nó rất mạnh mẽ và có rủi ro lớn"],
    34: ["Đó là lý do mình khuyên cái này không nên cài trên máy chính, hãy tách biệt môi trường"],
    35: ["Chọn ", "Yes", " là được."],
    36: ["Chọn cái đầu tiên: QuickStart (khởi động nhanh), thực hiện một số cấu hình"],
    37: ["Ở đây mình chọn Z.AI (Zhipu), trước đó đã chia sẻ skills với glm4.7 nên ở đây tiếp tục sử dụng"],
    38: ["Bạn nào không biết cách cấu hình, có thể vào: ", "https://mp.weixin.qq.com/s/ee4iIdFLYKtr4VKVoz2Ynw", " xem bài viết trước của mình"],
    39: ["Nhập API key của Zhipu"],
    40: ["Sẽ yêu cầu bạn chọn lại model một lần nữa, chọn cái đầu tiên keep current (zai/glm-4.7) giữ nguyên lựa chọn là được, nếu muốn đổi model khác thì nhấn phím để chuyển"],
    41: ["Cấu hình model xong rồi, bây giờ cần bạn liên kết phần mềm chat, nếu chọn Discord thì ở đây chọn Discord"],
    42: ["Cấu hình Discord với moltbot"],
    43: ["Bây giờ chúng ta cần vào Discord để lấy token và tạo bot."],
    44: ["Vào trang quản trị dành cho nhà phát triển Discord: ", "https://discord.com/developers/applications"],
    45: ["Nhấn Applications, ở góc trên bên phải tạo một Applications mới"],
    46: ["Tìm mục Bot, kéo xuống cuối cùng"],
    47: ["Nhấn reset token để đặt lại token, sau đó copy token này lại"],
    48: ["Quay lại Tencent Cloud, dán token Discord vào"],
    49: ["Sau đó quay lại nền tảng phát triển Discord"],
    50: ["Tìm Message Content Intent (ý định nội dung tin nhắn), bật tùy chọn này lên"],
    51: ["Nhớ ở phía dưới cùng có nút lưu"],
    52: ["Sau đó tìm OAuth2"],
    53: ["Bật bot trong Scopes, bật manage messages và read messages history trong bot permissions (quyền bot)"],
    54: ["Sau đó ở phía dưới cùng copy địa chỉ này, ", "đây là link mời bot"],
    55: ["Đăng nhập Discord"],
    56: ["Nhấn dấu + bên trái, tạo một server"],
    57: ["Sau đó dán và truy cập link mời bot đã copy từ Discord vào trình duyệt, thêm bot vào server vừa tạo"],
    58: ["Quay lại Tencent Cloud, chúng ta tiếp tục cấu hình moltbot"],
    59: ["Cấu hình kênh Discord chọn yes"],
    60: ["Quyền kênh Discord chọn cái thứ hai, cái thứ nhất nếu cấu hình không tốt thì chat nhóm dễ bị hạn chế"],
    61: ["Bây giờ nó thiếu skills (kỹ năng), ở đây cho nó cài đặt là được, chọn yes"],
    62: ["Cần hiển thị lệnh cài đặt homebrew, chọn yes"],
    63: ["Skills thì dùng npm để cài đặt"],
    64: ["Bây giờ yêu cầu bạn cài đặt các skills còn thiếu, nếu thấy phiền có thể chọn cái đầu tiên Skip for now (tạm thời bỏ qua), sau này cũng có thể cài"],
    65: ["Nếu nhấn Enter trực tiếp, nó sẽ yêu cầu bạn nhấn Space để chọn/bỏ chọn, Enter là bước tiếp theo"],
    66: ["Mình đã liệt kê hết tác dụng của các skills này, ai cần thì cũng có thể chọn cài đặt"],
    67: ["Hiện ra mấy cái này, ai có API thì điền, nếu không có thì chọn No hết"],
    68: ["Lúc này sẽ hỏi bạn có muốn cài hooks không"],
    69: ["Tổng cộng có ba plugin:"],
    70: ["🚀 boot-md (đưa các sở thích thường dùng, thông tin cơ bản của bạn cho AI)"],
    71: ["📝 command-logger (mọi thao tác của moltbot đều được ghi lại)"],
    72: ["💾 session-memory (lưu lại bộ nhớ hội thoại giữa bạn và AI)"],
    73: ["Đều khuyến nghị cài"],
    74: ["Sau đó đợi một lát, bạn sẽ thấy nó chuyển thành root@VM-0-XX-ubuntu:~# "],
    75: ["Khởi động moltbot"],
    76: ["Nhập lệnh: clawdbot gateway --port 18789 --verbose"],
    77: ["Vậy là nó đã khởi động, nhưng bạn không được đóng cửa sổ hoặc trang trình duyệt, nếu không nó sẽ tự thoát, vì đây là khởi động tạm thời"],
    78: ["Nếu muốn khởi động lâu dài, các bạn có thể dùng lệnh này (tắt máy cần khởi động lại): nohup clawdbot gateway --port 18789 --verbose > /tmp/clawdbot-gateway.out 2>&1 & disown"],
    79: ["Nếu gặp vấn đề có thể nói với AI: Tôi đang cài đặt moltbot, dùng lệnh clawdbot gateway --port 18789 --verbose để khởi động, bây giờ tôi cần nó chạy lâu dài, hãy hướng dẫn tôi"],
    80: ["Cấu hình cuối cùng để Discord kết nối hoàn toàn"],
    81: ["Vào Discord bên trái tìm server đã tạo trước đó, trong hộp chat @ bot đã tạo, gửi tin nhắn, sau đó nhấn vào tên bot, nhắn tin riêng cho nó"],
    82: ["Sau đó trong cửa sổ tin nhắn riêng, nói bất kỳ câu gì với nó, nó sẽ trả về một tin nhắn"],
    83: ["Quay lại server, dùng Ctrl+C để dừng Gateway, thực hiện lệnh sau để ghép nối. Trong đó, ", "<code>", " là mã ghép nối của bạn. Lệnh: clawdbot pairing approve discord <code>"],
    84: ["Sau khi ghép nối xong, thực hiện lệnh sau để chạy, quay lại Discord trò chuyện với bot đã tạo trên server, nếu phản hồi bình thường thì triển khai thành công. Lệnh: clawdbot gateway --port 18789 --verbose"],
    85: ["🎉 Chúc mừng bạn đã hoàn thành kết nối moltbot với Discord, tuyệt vời 👍"],
}

# Track stats
total_text = 0
translated_text = 0
kept_text = 0

for i, block in enumerate(trans['blocks']):
    if i in translations:
        t = translations[i]
        text_idx = 0
        for j, el in enumerate(block['elements']):
            if el['type'] == 'text_run':
                total_text += 1
                if text_idx < len(t):
                    old = el['content']
                    new = t[text_idx]
                    if old != new:
                        el['content'] = new
                        translated_text += 1
                    else:
                        kept_text += 1
                    text_idx += 1
                else:
                    kept_text += 1
            else:
                pass  # non-text elements kept as-is

print(f"Total text elements: {total_text}")
print(f"Translated: {translated_text}")
print(f"Kept (URLs/code/same): {kept_text}")

with open('_art40_trans.json', 'w', encoding='utf-8') as f:
    json.dump(trans, f, ensure_ascii=False, indent=2)

print("Saved _art40_trans.json")
