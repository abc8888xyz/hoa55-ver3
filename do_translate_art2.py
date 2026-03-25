# -*- coding: utf-8 -*-
import sys, json, copy
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

with open('art2_original.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

translated = copy.deepcopy(data)

T = {}
T[(0,0)] = 'Con "tôm hùm" này giúp bạn tự động kiếm tiền! Hướng dẫn toàn diện tạo video OpenClaw Seedance 2.0'
T[(1,0)] = "Link bài gốc: https://x.com/LufzzLiz/status/2028460767444689392"
T[(2,0)] = "Cuối cùng cũng hoàn thành, xong rồi hướng dẫn tạo video seedance 2.0 một chạm bằng tôm hùm (OpenClaw)"
T[(3,0)] = "Bài viết này sẽ kết hợp các case study thực tế, giới thiệu phương pháp sử dụng đầy đủ và hành trình trải nghiệm, để mọi người cảm nhận sức mạnh của tôm hùm"
T[(4,0)] = "Áp dụng cho VPS, máy tính cá nhân. Agent áp dụng: openclaw, claude code "
T[(5,0)] = "Một, Khởi nguồn"
T[(6,0)] = "Câu chuyện bắt nguồn từ một bài đăng của một đại ca trên X, sau khi đọc xong, tôi thấy có thể mở riêng một topic để nghiên cứu nó"
T[(7,0)] = "Rất xin lỗi vì lúc đó copy quá nhanh, không nhớ là đại ca nào đăng... Nếu bài viết may mắn được vị đại ca đó nhìn thấy, có thể nhắn riêng cho tôi, để tôi cảm ơn đích danh 😊"
T[(8,0)] = "Kết quả tôm hùm ngoài mong đợi, đã tải xuống video hot thành công, còn hiển thị video trực tiếp cho tôi xem, quá trình này tôi hầu như không cần dạy nó"
T[(9,0)] = "Rồi vài ngày sau, tôi bắt đầu bước thứ hai - xác minh việc tạo video bằng seedance 2.0. Tôi nghĩ sau này khi thấy một video hay, hoặc có ý tưởng, hoặc tự động giúp tôi tiêu hết quota seedance hàng ngày, thì sướng biết mấy. Vì vậy tôi nghĩ đến việc tiếp tục dùng tôm hùm để hoàn thành nhiệm vụ này."
T[(10,0)] = "Đến ngày 28 tôi đã chạy thông toàn bộ quy trình, dưới đây là video đầu tiên tôi tạo ra"
T[(11,0)] = "Video như sau:"
T[(12,0)] = "Nhưng cũng phát hiện vấn đề, tính năng tạo video từ ảnh mà tôm hùm phát triển (ảnh cũng do tôm hùm gọi gemini tạo ra). Tạo video tham chiếu từ video vẫn chưa chạy được, chủ yếu là nền tảng tiểu vân tước có lỗi, ở đây không đi vào chi tiết"
T[(13,0)] = "Tóm lại sau khi Lan Thúc điều chỉnh, đã hoàn thành thành công tạo video từ text, tạo video từ ảnh, tạo video tham chiếu từ video dựa trên seedance 2.0, đồng thời tự động gửi video đến cửa sổ chat của bạn"
T[(14,0)] = "Hai, Thực chiến"
T[(15,0)] = "Công việc chuẩn bị:"
T[(16,0)] = "Tải xuống và cài đặt code do Lan Thúc phát triển:"
# 17 = URL - keep
T[(18,0)] = " (xin star~ 🙏)"
T[(19,0)] = "Cũng có thể trực tiếp nói với agent (ví dụ tôm hùm):"
T[(20,0)] = "Như hình, chúng ta mở một cuộc hội thoại topic mới, nói cho nó cài đặt, có thể thấy tôm hùm trong cuộc hội thoại mới cũng nhớ quy ước của Lan Thúc, cài đặt thành công theo thói quen của chúng ta"
T[(21,0)] = "Nếu tôm hùm của bạn đủ thông minh, sẽ bảo bạn đi cấu hình cookie. Cookie này có thể cần bạn tự cấu hình, trước đó tôi test tôm hùm yêu cầu tôi cho số điện thoại và mã xác minh, nhưng không qua được 😂, sau đó tôi đành copy cookie từ trình duyệt cho nó, thế là thành công."
T[(22,0)] = "Copy cookie trình duyệt có thể tham khảo hướng dẫn trong file readme của Lan Thúc -- đây là điều duy nhất bạn cần rời trang tôm hùm để làm"
T[(23,0)] = "1. Tạo video từ text"
T[(24,0)] = "Sau khi hoàn thành công việc chuẩn bị, bắt đầu thực hành"
T[(25,0)] = "Như hình, cứ nói trực tiếp thôi:"
T[(26,0)] = "Video xem tại:"
T[(27,0)] = "Nhưng trong quá trình gặp vấn đề, như ảnh chụp, bị timeout, chỗ này khuyến nghị cấu hình một chút:"
T[(28,0)] = "Đoạn code sau khi sửa trông đại khái như thế này, có thể nói tôm hùm tham khảo và backup trước rồi cấu hình:"
T[(29,0)] = "Kiểm tra OK rồi, restart lại"
T[(30,0)] = "Sau đó tiếp tục, như ảnh chụp, nói tôm hùm retry là được"
T[(31,0)] = "Rồi video đã được tạo. Vậy có phải tạo một lần là xong không? Chúng ta vào tiểu vân tước xác minh một chút:"
T[(32,0)] = "Chúng ta phát hiện tổng cộng tạo ba lần, lần đầu vì chúng ta bị timeout. Lần thứ hai chúng ta vào xem, là lỗi của nền tảng tiểu vân tước, bị lạc đường..."
T[(33,0)] = "Nhưng mà! Điểm mấu chốt đây, cuộc hội thoại của chúng ta chỉ hai lần là thành công, điều này chứng tỏ code của chúng ta robust và tôm hùm mạnh mẽ, nó tự retry! Quá cool!"
T[(34,0)] = "2. Tạo video tham chiếu"
T[(35,0)] = "Chúng ta để tôm hùm tìm video hot trước"
T[(36,0)] = "Sau đó Lan Thúc chọn một cái, để nó tải xuống cho tôi xem"
T[(37,0)] = "Cũng được (ps: nếu quá 15s, còn có thể để tôm hùm dùng ffmpeg xử lý cắt một chút, chỉ một câu nói thôi~)"
T[(38,0)] = "Video đã tạo (lần này qua một phát, tiểu vân tước không lỗi):"
T[(39,0)] = "Thế nào, đã chạy thông hết rồi phải không, phải không đã có thể đăng lên YouTube, video Alipay, Douyin, Video Channel và các nền tảng video lớn để kiếm tiền rồi 😂"
T[(40,0)] = "Ném gạch dẫn ngọc, tôi hát xong rồi, sân khấu đã dựng sẵn cho bạn, hy vọng hữu ích cho bạn, nếu thấy hữu ích xin hãy like-share-subscribe, gõ 666 ở phần bình luận, cảm ơn 💗"

# Apply translations
translated_count = 0
kept_count = 0
total_text = 0

for i, block in enumerate(translated['blocks']):
    for j, el in enumerate(block['elements']):
        if el['type'] == 'text_run':
            total_text += 1
            key = (i, j)
            if key in T:
                el['content'] = T[key]
                translated_count += 1
            else:
                kept_count += 1

with open('art2_translated.json', 'w', encoding='utf-8') as f:
    json.dump(translated, f, ensure_ascii=False, indent=2)

print(f"Total text segments: {total_text}")
print(f"Translated: {translated_count}")
print(f"Kept: {kept_count}")
