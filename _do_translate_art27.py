# -*- coding: utf-8 -*-
"""Translate art27 - CN to VI using JSON mapping"""
import json, sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('_art27_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def has_chinese(s):
    return bool(re.search(r'[\u4e00-\u9fff]', s))

# Build translation map as a JSON string to avoid encoding issues
trans_json = r"""
{
  "\u5f00\u6e90AI\u52a9\u624b ClawdBot \u706b\u7206\u5168\u7f51\uff0c\u5df2\u72c2\u98d950K Star\uff01\u9644\u5582\u996d\u7ea7\u5b89\u88c5\u4f7f\u7528\u6559\u7a0b": "Tr\u1ee3 l\u00fd AI m\u00e3 ngu\u1ed3n m\u1edf ClawdBot b\u00f9ng n\u1ed5 to\u00e0n m\u1ea1ng, \u0111\u00e3 v\u01b0\u1ee3t m\u1ed1c 50K Star! K\u00e8m h\u01b0\u1edbng d\u1eabn c\u00e0i \u0111\u1eb7t v\u00e0 s\u1eed d\u1ee5ng chi ti\u1ebft t\u1eebng b\u01b0\u1edbc"
}
"""

# Instead of a huge JSON, let's do block-by-block translation with index
translations = [None] * len(data['blocks'])

# Block 0: page title
translations[0] = ["Trợ lý AI mã nguồn mở ClawdBot bùng nổ toàn mạng, đã vượt mốc 50K Star! Kèm hướng dẫn cài đặt và sử dụng chi tiết từng bước"]

# Block 1: quote - link
translations[1] = ["🔗 Link bài gốc: ", None]  # None = keep as-is

# Block 2: author info
translations[2] = ["Nguyên tác Đại Thử Đế Đại Thử Đế Quán trọ AI Đại Thử Đế", "Ngày 27 tháng 1 năm 2026 12:33 Vân Nam"]

# Block 3: multi-element
translations[3] = ["Các bạn có thể triển khai thông qua Alibaba Cloud Bailian", None, " để triển khai", ":"]

# Block 4
translations[4] = ["Mua lần đầu chỉ từ 7,9 tệ, gia hạn giảm từ 50%, hỗ trợ các mô hình Qwen3.5, Qwen3-max, Qwen3-coder, GLM-5, GLM-4.7, Kimi-k2.5 v.v."]

# Block 5
translations[5] = ["👉 Nhấn link truy cập trực tiếp:", None]

# Block 6
translations[6] = ["👉 Xem hướng dẫn triển khai chi tiết:", None]

# Block 7
translations[7] = ["Chỉ tối đa ba bước, bạn sẽ có trợ lý AI trực tuyến 7x24 giờ, phản hồi mọi lúc"]

# Block 8
translations[8] = ["Xin chào mọi người, tôi là Đại Thử Đế."]

# Block 9
translations[9] = ["Sáng hôm qua tôi lờ đờ bò dậy, theo thói quen mở X lướt tweet, kết quả cả người tỉnh táo hẳn."]

# Block 10
translations[10] = ["Một dự án mã nguồn mở tên clawdbot, giống như bất ngờ mọc lên từ dưới đất, chỉ sau một đêm đã bùng nổ khắp mạng!"]

# Block 11
translations[11] = ["Mọi người đều phát cuồng:"]

# Block 12 - URL, keep as-is
translations[12] = [None]

# Block 13
translations[13] = ["Tôi kiểm tra dữ liệu GitHub của nó, thật sự đáng sợ, chỉ trong vòng 20 ngày ngắn ngủi, số Star từ vài trăm tăng vọt lên hơn 40K, riêng hôm qua đã tăng mạnh 30K."]

# Block 14
translations[14] = ["Đây chắc chắn là dự án mã nguồn mở cấp hiện tượng."]

# Block 15
translations[15] = ["Điều vô lý hơn nữa là nghe nói vì dự án này mà doanh số Mac Mini cũng tăng theo một đợt."]

# Block 16
translations[16] = ["Phải biết rằng một chiếc Mac Mini cấu hình tốt không hề rẻ, mấy vạn tệ, vậy mà lại được một phần mềm mã nguồn mở kéo doanh số? Nhưng thực tế rào cản sử dụng thứ này không cao lắm, hơi khó hiểu 🤔"]

# Block 17
translations[17] = ["Xem ra mọi người đã khao khát có một trợ lý AI thực sự thuộc về mình quá lâu rồi."]

# Block 18: multi-element
translations[18] = ["Hôm qua tôi vừa giới thiệu cho mọi người ", "CodeBuddy Code của Tencent ", ", nó cũng là Agent chạy cục bộ, tương tự có thể triển khai lên cloud làm trợ lý cá nhân."]

# Block 19
translations[19] = ["Tiện thể nói thêm, tối qua họ lại ra một bản cập nhật thú vị, bây giờ codebuddy code đã trở thành công cụ CLI đầu tiên trên thế giới hỗ trợ tạo ảnh. Vậy nếu tôi tích hợp x-skills mã nguồn mở trước đó vào, việc sản xuất tweet dạng hình ảnh + văn bản chẳng phải cất cánh sao? "]

# Block 20
translations[20] = ["Hôm qua nhận được tin nhắn, phát hiện codebuddy gần đây có hoạt động năm mới, bạn nào quan tâm có thể xem thử:"]

# Block 21 - URL
translations[21] = [None]

# Block 22
translations[22] = ["Bài này cũng cùng xem nhé, Clawdbot rốt cuộc khác gì so với CodeBuddy Code, Claude Code và các công cụ CLI khác? "]

# Block 23
translations[23] = ["Công cụ khiến các geek toàn cầu phát cuồng này, rốt cuộc là thần thánh phương nào?"]

# Block 24
translations[24] = ["Rốt cuộc nó có sức hút gì mà khiến mọi người đặt mua server và Mac Mini xuyên đêm? Rào cản cài đặt có cao không?"]

# Block 25
translations[25] = ["Rốt cuộc chuyện gì, xuất phát thôi!"]

# Block 26 - heading2
translations[26] = ["Một, Clawdbot rốt cuộc là gì? "]

# Block 27
translations[27] = ["Nói đơn giản, Clawdbot chính là một trợ lý AI sống trong phần mềm chat của bạn (ví dụ WhatsApp, Telegram, iMessage)."]

# Block 28
translations[28] = ["Trước đây chúng ta dùng ChatGPT hoặc Claude, logic là: tôi có câu hỏi -> mở trang web/App -> đặt câu hỏi -> AI trả lời, đây là \"người tìm AI\"."]

# Block 29
translations[29] = ["Nhưng logic của Clawdbot thay đổi hoàn toàn, nó là \"AI tìm người\"."]

# Block 30
translations[30] = ["Clawdbot là một chương trình chạy 7x24 giờ trên server (hoặc máy tính rảnh rỗi trong nhà bạn)."]

# Block 31
translations[31] = ["Nó kết nối với phần mềm chat của bạn, bạn có thể nhắn tin cho nó như nhắn tin cho bạn bè qua WeChat."]

# Block 32
translations[32] = ["Điều quan trọng nhất là, nó không chỉ trò chuyện, nó còn làm việc được."]

# Block 33
translations[33] = ["Nó còn có thể kết nối GitHub, Google Drive, Gmail, lịch của bạn, thậm chí giúp bạn theo dõi cổ phiếu, lướt Twitter."]

# Block 34
translations[34] = ["Có một anh bạn chia sẻ trên X, anh ấy kết nối Clawdbot với tất cả các công cụ, rồi gửi một tin nhắn thoại: \"Phân tích dữ liệu website của tôi, viết một bài blog, cập nhật metadata, rồi đăng bài lên LinkedIn.\""]

# Block 35
translations[35] = ["Sau đó anh ấy đi ngủ, sáng hôm sau thức dậy, Clawdbot đã hoàn thành tất cả công việc, còn tiện thể gửi cho anh ấy một bản báo cáo ngày!"]

# Block 36
translations[36] = ["Còn có một trường hợp tuyệt vời hơn. Có người dùng để Clawdbot giám sát một cổ phiếu, một khi giảm xuống dưới một mức giá nhất định thì thông báo cho anh ấy."]

# Block 37
translations[37] = ["Kết quả hôm đó anh ấy đang lái xe, Clawdbot trực tiếp gửi cho anh ấy tin nhắn Telegram: \"Sếp ơi, cổ phiếu giảm rồi, đề nghị mua thêm.\""]

# Block 38
translations[38] = ["Đây chính là lý do tại sao mọi người phát cuồng đến vậy."]

# Block 39
translations[39] = ["Phần lớn công cụ AI chỉ là máy hỏi đáp, còn Clawdbot là một nhân viên số thực sự có thể làm việc, có trí nhớ, có thể chủ động tìm bạn."]

# Block 40
translations[40] = ["Nói thật, \"AI làm việc thật\" đã nói mệt rồi, trên thị trường hầu như mọi Agent đều nói mình là AI làm việc thật, nhưng mà, vẫn còn nhiều việc không làm được, không thể thực sự giải quyết vấn đề của đa số người dùng, kỳ vọng của người dùng cũng ngày càng cao."]

# Block 41
translations[41] = ["Hơn nữa, điều quan trọng nhất là clawdbot là mã nguồn mở! Bạn có thể tùy ý tùy chỉnh, DIY trợ lý AI chuyên dụng của riêng mình, đây mới là điểm thú vị và thực dụng nhất."]

# Block 42
translations[42] = ["Tại sao mọi người nghĩ nó cần Mac Mini?"]

# Block 43
translations[43] = ["Thực ra đây là một hiểu lầm, vì Clawdbot chạy cục bộ nên nhiều người nghĩ phải có máy tính hiệu năng cao mới được. Thực tế, yêu cầu cấu hình của nó cực thấp."]

# Block 44
translations[44] = ["Bạn hoàn toàn không cần mua Mac Mini, một cloud server vài chục tệ một tháng, thậm chí một chiếc laptop cũ trong nhà, đều có thể chạy mượt mà."]

# Block 45
translations[45] = ["Nó có ba ưu điểm cốt lõi:"]

# Block 46
translations[46] = ["1. Nó \"sống\": nó có trí nhớ, hôm qua bạn nói với nó bạn không ăn rau mùi, có thể tuần sau khi nhờ nó đặt đồ ăn nó vẫn nhớ. Không như Siri, mãi mãi như một bệnh nhân mất trí nhớ."]

# Block 47
translations[47] = ["2. Nó rất chủ động: nó không ngồi chờ bạn hỏi. Nếu bạn cấp quyền, nó sẽ chủ động nói với bạn: \"Sếp ơi, ngày mai sẽ mưa, chuyến bay của bạn có thể bị trễ, đề nghị đổi vé.\" Điều này rất quan trọng, vì AI hiện tại hầu như không có tính chủ động..."]

# Block 48
translations[48] = ["3. Nó là của bạn: dữ liệu đều nằm trên server của chính bạn, không giống một số AI đám mây, quyền riêng tư của bạn có khả năng nhỏ bị lấy đi để huấn luyện mô hình."]

# Block 49 - heading2
translations[49] = ["Hai, Hướng dẫn cài đặt siêu tốc trong 30 phút "]

# Block 50
translations[50] = ["Nhiều người vừa nghe đến triển khai server, lệnh terminal, lập tức bỏ cuộc, nghĩ rằng đây là việc chỉ lập trình viên mới làm được."]

# Block 51
translations[51] = ["Thực ra không phải vậy.."]

# Block 52
translations[52] = ["Quy trình cài đặt Clawdbot đơn giản đến mức khó tin, cơ bản chỉ là việc copy paste vài dòng code."]

# Block 53
translations[53] = ["Tôi đã soạn cho mọi người một hướng dẫn cầm tay chỉ việc, chỉ cần bạn biết đọc chữ là làm được."]

# Block 54 - heading3
translations[54] = ["Bước một: Kiếm một server miễn phí/giá rẻ (5 phút) "]

# Block 55
translations[55] = ["Clawdbot cần một nơi chạy 7x24 giờ không tắt máy."]

# Block 56
translations[56] = ["Phương án A (bản đại gia): Mua một chiếc Mac Mini hoặc dùng máy tính ở nhà bật liên tục."]

# Block 57
translations[57] = ["Phương án B (bản khuyên dùng): Thuê một cloud server."]

# Block 58
translations[58] = ["Ở đây khuyến nghị dùng VPS nước ngoài, ví dụ Evoxt hoặc gói miễn phí của AWS."]

# Block 59
translations[59] = ["Chọn một node gần bạn (ví dụ Hong Kong hoặc Singapore), hệ điều hành chọn Ubuntu, cấu hình chọn 2 nhân 4G hoặc 8G RAM là đủ."]

# Block 60
translations[60] = ["Sau khi mua xong, bạn sẽ nhận được một địa chỉ IP và mật khẩu."]

# Block 61
translations[61] = ["Cũng có thể dùng Qiniu Cloud, họ có server nước ngoài, chủ yếu là Tokyo và Đông Nam Á"]

# Block 62 - URL
translations[62] = [None]

# Block 63
translations[63] = ["Giá cũng không đắt, tôi xem thì chỉ khoảng 20 tệ một tháng"]

# Block 64
translations[64] = ["Rồi họ hành động thật nhanh, đã tung ra image tích hợp sẵn clawdbot rồi..."]

# Block 65
translations[65] = ["Rồi họ tặng một số phúc lợi, có 100 coupon 100 tệ không điều kiện, like-share-comment bài viết này, rồi bạn nào cần có thể thêm WeChat: ai-kangarooking, nhắn riêng tôi để nhận"]

# Block 66
translations[66] = ["Nếu mọi người còn có lựa chọn giá hời hơn, hoan nghênh chia sẻ ở phần bình luận nhé"]

# Block 67 - heading3
translations[67] = ["Bước hai: Cài đặt một click (2 phút) "]

# Block 68
translations[68] = ["Kết nối đến server của bạn thông qua công cụ SSH (ví dụ Termius hoặc terminal có sẵn trong hệ thống)."]

# Block 69
translations[69] = ["Copy dòng lệnh thần kỳ bên dưới, dán vào, nhấn Enter:"]

# Block 70
translations[70] = ["Sau đó bạn có thể đi pha một ly cà phê. Script sẽ tự động giúp bạn cài đặt toàn bộ môi trường và dependency."]

# Block 71
translations[71] = ["Cuối cùng cũng đợi khá lâu mới cài xong, vì giữa chừng đi làm việc khác nên cụ thể bao lâu thì không rõ"]

# Block 72 - heading3
translations[72] = ["Bước ba: Trình hướng dẫn cấu hình dễ như chơi (10 phút) "]

# Block 73
translations[73] = ["Sau khi script cài đặt chạy xong, sẽ tự động hiện ra một trình hướng dẫn cấu hình."]

# Block 74
translations[74] = ["Chọn \"Quick Start\"."]

# Block 75
translations[75] = ["Cấu hình mô hình: ở đây cần dùng API Key (còn hỗ trợ khá nhiều nhà cung cấp)."]

# Block 76
translations[76] = ["Bạn có thể vào MiniMax hoặc GLM tạo một API Key, rồi dán Key vào."]

# Block 77
translations[77] = ["Tôi vừa hay mua bản coding plan max của GLM"]

# Block 78
translations[78] = ["Nên tôi dùng luôn API Key của Zhipu"]

# Block 79
translations[79] = ["Chọn kênh chat: khuyến nghị chọn Telegram Bot, ổn định và tiện lợi."]

# Block 80
translations[80] = ["Giá mà hỗ trợ được WeChat trong nước thì tốt quá, tôi định nghiên cứu thử 🤔"]

# Block 81 - heading3
translations[81] = ["Bước bốn: Tạo bot Telegram của bạn (3 phút) "]

# Block 82
translations[82] = ["Mở Telegram, tìm kiếm @BotFather."]

# Block 83
translations[83] = ["Gửi lệnh /newbot."]

# Block 84
translations[84] = ["Sau đó đặt tên cho bot của bạn (ví dụ \"Tay sai của Đại Thử Đế\")."]

# Block 85
translations[85] = ["Tuy nhiên chưa dùng được tiếng Trung, cuối cùng tôi dùng kangarooking_bot"]

# Block 86
translations[86] = ["BotFather sẽ cho bạn một chuỗi Token, hãy copy nó."]

# Block 87
translations[87] = ["Quay lại trình hướng dẫn cấu hình trên server, dán Token vào."]

# Block 88
translations[88] = ["Để đảm bảo an toàn, có thể còn cần lấy User ID của bạn, đảm bảo chỉ mình bạn có thể điều khiển nó."]

# Block 89
translations[89] = ["Tìm kiếm @userinfobot trên Telegram, lấy ID của bạn, điền vào clawdbot."]

# Block 90
translations[90] = ["PS: Tuy nhiên bước này tôi không gặp"]

# Block 91
translations[91] = ["Còn có thể cài đặt rất nhiều công cụ"]

# Block 92
translations[92] = ["Có thể tích hợp NanoBanana Pro"]

# Block 93
translations[93] = ["Còn có thể chọn cách khởi động bot (terminal TUI, giao diện web UI)"]

# Block 94
translations[94] = ["Tóm lại, chỉ là một loạt lựa chọn đa chọn hoặc đơn chọn, đa chọn thì phím lên xuống + phím cách để chọn nhiều, Enter là gửi, tuy nhiên toàn tiếng Anh, có thể chụp màn hình đưa cho Doubao dịch hộ"]

# Block 95
translations[95] = ["Có một vấn đề, nếu cài trên server trong nước, clawdbot khởi động sẽ do vấn đề mạng mà không thể kết nối được với Telegram, nên nếu trước đó đã cấu hình Telegram thì phải tắt đi, nếu không khởi động sẽ báo lỗi"]

# Block 96
translations[96] = ["Địa chỉ file cấu hình ở /root/.clawdbot/clawdbot.json"]

# Block 97
translations[97] = ["Tìm phần telegram, đổi giá trị enable thành false là xong"]

# Block 98
translations[98] = ["Sau đó nhập clawdbot gateway để mở gateway"]

# Block 99
translations[99] = ["Sau đó nhập clawdbot tui để khởi động và vào clawdbot"]

# Block 100 - heading3
translations[100] = ["Bước năm: Trao linh hồn (1 phút) "]

# Block 101
translations[101] = ["Sau khi cấu hình xong, Clawdbot sẽ chủ động nhắn tin cho bạn trên Telegram."]

# Block 102
translations[102] = ["Lúc này, bạn có thể thiết lập nhân vật cho nó. Ví dụ: \"Bạn tên là Jarvis, nhiệm vụ của bạn là giúp tôi quản lý lịch trình và sắp xếp thông tin.\""]

# Block 103
translations[103] = ["Vì lần này tôi dùng server trong nước, do vấn đề mạng không thể kết nối Telegram, nên tôi chỉ có thể khởi động thử nghiệm cục bộ trên server bằng TUI trước"]

# Block 104
translations[104] = ["Trí nhớ của nó thật sự tốt, thứ này nếu kết nối được WeChat thì chắc chắn làm được rất nhiều việc."]

# Block 105 - emoji only, keep
translations[105] = [None]

# Block 106
translations[106] = ["Đến đây, một trợ lý AI chuyên dụng của riêng bạn đã ra đời."]

# Block 107
translations[107] = ["Bài tiếp theo về clawdbot, sẽ hướng dẫn mọi người cách kết nối API tùy chỉnh, cũng như cách kết nối mô hình Claude"]

# Block 108 - heading2
translations[108] = ["Ba, Thực nghiệm "]

# Block 109
translations[109] = ["Để kiểm chứng khả năng của nó, tôi chạy thử một tác vụ đơn giản: tạo bản tin sáng"]

# Block 110
translations[110] = ["Ôi trời, cảm giác thật sự rất 🐂🍺, xem quá trình nó thật sự crawl rất nhiều thứ để sàng lọc."]

# Block 111
translations[111] = ["Vì giới hạn bài viết, tôi sẽ không thử những tác vụ quá phức tạp trước, nếu muốn liên kết các ứng dụng khác nhau cần cấu hình, phần này sẽ chia sẻ sau"]

# Block 112
translations[112] = ["Đánh giá sử dụng"]

# Block 113
translations[113] = ["Ưu điểm:"]

# Block 114 - quote with multiple elements
translations[114] = ["Tương tác tự nhiên: ", " Giống như trò chuyện với người thật, không có cảm giác rời rạc khi dùng phần mềm, thân thiện hơn. ", "\n", " Năng lực mạnh mẽ: ", " Chỉ cần cấp quyền, nó có thể điều khiển gần như mọi công cụ."]

# Block 115 - quote
translations[115] = ["Quyền riêng tư an toàn: ", " Dữ liệu đều nằm trên server của mình, yên tâm hơn."]

# Block 116 - quote
translations[116] = ["Mức độ kỹ thuật hóa cao: ", " Tôi cảm thấy, so với các Agent cục bộ cần tùy chỉnh như Claude Code, mức độ kỹ thuật hóa của clawdbot cao hơn, bản thân nó đã hướng đến mục tiêu làm trợ lý AI cá nhân."]

# Block 117 - quote
translations[117] = ["Chi phí thấp: ", " Ngoài chi phí server và chi phí API, bản thân phần mềm là miễn phí mã nguồn mở."]

# Block 118
translations[118] = ["Nhược điểm:"]

# Block 119 - quote with multiple elements
translations[119] = ["Vẫn có rào cản nhất định về thực hành: ", " Mặc dù đã rất đơn giản, nhưng với người mới hoàn toàn, mua server, cấu hình API Key vẫn hơi phức tạp, cần bỏ chút thời gian, tuy nhiên bây giờ có AI rồi, những thứ này đều có thể hỏi. ", "\n", " Độ ổn định phụ thuộc API mô hình: ", " Nếu API không ổn định, thì bộ não của nó cũng sập"]

# Block 120 - quote
translations[120] = ["Tác vụ phức tạp cần điều chỉnh: ", " Muốn nó thực hiện hoàn hảo các workflow phức tạp, giai đoạn đầu cần bỏ chút thời gian chạy rà."]

# Block 121 - heading2
translations[121] = ["Điểm dừng tiếp theo của AI "]

# Block 122
translations[122] = ["Sự bùng nổ của Clawdbot thực ra đã phát đi một tín hiệu mạnh mẽ: năm 2026, AI sẽ chuyển từ \"bị động\" sang \"chủ động\"."]

# Block 123
translations[123] = ["Vài năm qua, chúng ta đã quen coi AI như một chatbot, hoặc là công cụ tạo nội dung. Nhưng tương lai thực sự, là AI trở thành trợ lý trong cuộc sống và công việc của chúng ta."]

# Block 124
translations[124] = ["Mọi người ngày càng không cần một bộ bách khoa toàn thư chỉ biết trả lời câu hỏi, cần hơn là một trợ lý AI có thể giúp đặt vé, giúp trả email, giúp theo dõi công việc, có thể chủ động làm việc."]

# Block 125
translations[125] = ["Clawdbot chỉ là một khởi đầu, trong tương lai, điện thoại, máy tính, thậm chí tủ lạnh trong nhà bạn, đều sẽ kết nối với Agent như vậy."]

# Block 126
translations[126] = ["Khoảng cách hiệu suất giữa người có trợ lý AI 7x24 giờ và người không có sẽ ngày càng lớn."]

# Block 127
translations[127] = ["Hãy xây dựng một trợ lý AI của riêng bạn, ngay hôm nay, bắt tay vào hành động thôi~"]

# Block 128
translations[128] = ["Tôi là Đại Thử Đế, một blogger dẫn bạn khám phá AI."]

# Block 129
translations[129] = ["Nếu bạn còn thắc mắc về quá trình cài đặt, hoan nghênh để lại bình luận."]

# Block 130
translations[130] = ["Tôi là Đại Thử Đế, một du mục kỹ thuật số trong thời đại AI, liên tục chia sẻ kinh nghiệm thực chiến AI, đồng hành cùng bạn tiến hóa."]

# Block 131
translations[131] = ["Nhấn theo dõi tài khoản bên dưới, bạn sẽ cảm nhận được một linh hồn punk."]

# Block 132
translations[132] = ["Ai đọc được đến đây đều là những người hiếm hoi!"]

# Block 133
translations[133] = ["Nếu thấy hay, tiện tay nhấn like, xem, chia sẻ ba liên hoàn nhé~"]

# Block 134
translations[134] = ["Nếu muốn nhận thông báo đầu tiên, cũng có thể đánh dấu sao cho tôi ⭐"]

# Block 135
translations[135] = ["Cảm ơn bạn đã kiên nhẫn đọc hết bài viết của tôi~"]


# Apply translations
translated_count = 0
kept_count = 0
total_text = 0

for i, block in enumerate(data['blocks']):
    if translations[i] is None:
        # No translation defined - count elements
        for el in block['elements']:
            if el['type'] == 'text_run':
                total_text += 1
                kept_count += 1
        continue

    text_idx = 0
    for el in block['elements']:
        if el['type'] == 'text_run':
            total_text += 1
            if text_idx < len(translations[i]):
                new_val = translations[i][text_idx]
                if new_val is not None:
                    old_content = el['content']
                    el['content'] = new_val
                    if has_chinese(old_content):
                        translated_count += 1
                    else:
                        kept_count += 1
                else:
                    kept_count += 1
            else:
                kept_count += 1
            text_idx += 1
        # non-text_run elements are skipped in counting

# Save
with open('_art27_trans.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total text elements: {total_text}")
print(f"Translated: {translated_count}")
print(f"Kept as-is: {kept_count}")
print("Saved to _art27_trans.json")
