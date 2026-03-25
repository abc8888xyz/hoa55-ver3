# -*- coding: utf-8 -*-
import sys, json, copy
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

with open('art8_original.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
translated = copy.deepcopy(data)

T = {}
T[(0,0)] = "Không ngờ! Một con AI 'tôm hùm' Openclaw đã giải quyết bài toán nuôi con của tôi: Tự động quản lý thời gian xem TV, còn dạy tôi kỹ năng mới"
T[(1,0)] = "Bài gốc trên tài khoản công khai:"
T[(2,0)] = "Xin chào mọi người, hôm nay chia sẻ với mọi người một case sử dụng OpenClaw trong kịch bản thực tế"
T[(3,0)] = "\"Mẹ ơi, con xem thêm một tập nữa thôi!\" — câu này có quen tai không? Trẻ con nghiện TV, thời gian dùng màn hình mất kiểm soát, là pain point chung của vô số gia đình."
T[(4,0)] = "Bạn có từng trải qua tình huống này không, trẻ ở nhà cứ xem TV mãi, bảo tắt không tắt; hoặc nói là dùng điện thoại học bài nhưng thực ra đang chơi game"
T[(5,0)] = "Hôm nay, chia sẻ một case thực tế: Cách dùng OpenClaw (tôm hùm) đang cực hot gần đây, để \"thuần hóa\" TV thông minh trong nhà, thực hiện quản lý tự động, Openclaw tự động tiếp quản TV trong nhà, "
T[(5,1)] = "làm phụ huynh không làm mất hứng (việc bẩn openclaw làm ngầm giúp bạn)"
T[(6,0)] = "Mục lục"
T[(7,0)] = "1) Chuẩn bị trước"
T[(8,0)] = "2) Điều chỉnh thiết bị (bài viết lấy TV thông minh làm ví dụ)"
T[(9,0)] = "3) Hướng dẫn sử dụng"
T[(10,0)] = "4) Đóng gói kỹ năng"
T[(11,0)] = "Một, Chuẩn bị trước"
T[(12,0)] = "Trước hết nhất định phải có một con tôm hùm của riêng mình (OpenClaw, Copaw và các bản phái sinh trong nước đều được)"
T[(12,1)] = "Tôi có một bài hướng dẫn trước đây về cách triển khai Copaw trên máy tính Windows, nếu bạn chưa \"nuôi tôm\" có thể tự triển khai trước, nếu không biết triển khai cũng có thể bình luận"
T[(12,2)] = "Hướng dẫn chi tiết cài đặt Copaw trên Windows, xây dựng tôm hùm phù hợp thể chất người Việt, tất cả các hố đã được"
T[(13,0)] = "Để tôm hùm quản lý được TV thông minh, máy tính triển khai tôm hùm nhất định phải cùng môi trường mạng với TV thông minh, tức là dùng cùng WiFi"
T[(14,0)] = "Còn một điều nữa là tôm hùm của bạn phải đã kết nối Lark, DingTalk hoặc công cụ chat khác, tất nhiên nếu chưa kết nối cũng có thể dùng tính năng chat tích hợp của Openclaw để thực hiện các thao tác tiếp theo"
T[(15,0)] = "Hai, Điều chỉnh thiết bị"
T[(16,0)] = "Bài viết sử dụng TV thông minh làm demo, điện thoại Android tương tự"
T[(17,0)] = "Bật chức năng ADB của TV"
T[(18,0)] = "TV demo trong bài là Xiaomi, nếu bạn dùng thương hiệu TV khác cách làm tương tự. Tôi cũng đã tổng hợp một tài liệu bao gồm cách bật adb trên các TV phổ biến trên thị trường, "
T[(18,1)] = "theo dõi tài khoản công khai, trả lời \"adb教程\" để nhận link tải"
T[(19,0)] = "Cài đặt → Giới thiệu → Tìm mã sản phẩm, dùng remote bấm 7 lần vào mã sản phẩm, sẽ thấy thông báo (Chế độ nhà phát triển đã bật) → Quay lại, tìm Tài khoản và Bảo mật, bên trong sẽ thấy nội dung như hình dưới"
T[(20,0)] = "Chuyển ADB debug từ Từ chối sang Bật"
T[(21,0)] = "Tiếp theo tải công cụ adb trên máy tính, đây là công cụ bắt buộc cho phát triển Android, nếu máy tính bạn trước đó đã cài Android Studio hoặc công cụ tương tự thì có thể bỏ qua bước này"
T[(22,0)] = "(Bước này có thể nhờ tôm hùm giúp cài: \"Giúp tôi cài công cụ adb\")"
T[(23,0)] = "Địa chỉ tải chính thức"
T[(25,0)] = "Công cụ này không cần cài đặt, tải về giải nén để đó là được, nhớ đường dẫn giải nén nhé"
T[(26,0)] = "Có thể thêm adb.exe vào biến môi trường máy tính, như vậy ở đâu cũng có thể gõ lệnh adb, nếu không muốn cấu hình cũng có thể vào thẳng đường dẫn giải nén để sử dụng"
T[(27,0)] = "Tìm Path trong biến hệ thống, nhấp đúp mở"
T[(28,0)] = "Thêm đường dẫn adb vào dòng cuối cùng"
T[(29,0)] = "Nhấn Đồng ý tất cả là xong"
T[(30,0)] = "Bấm phím win+r trên bàn phím, gõ cmd trong cửa sổ mở ra, sẽ bật lên cửa sổ command line, gõ adb vào, hiện ra như hình dưới nghĩa là cài thành công."
T[(31,0)] = "Tiếp theo tìm địa chỉ IP của TV, cũng trong Cài đặt, nhấp vào Mạng không dây là thấy (để tiện sử dụng sau này khuyến nghị bật Cài đặt thủ công, nhập lại IP, lợi ích là sau này dù bật tắt TV thế nào, IP của nó đều không đổi)"
T[(32,0)] = "Ba, Hướng dẫn sử dụng"
T[(33,0)] = "Hoàn thành chuẩn bị trên, tiếp theo là dùng Openclaw để thao tác"
T[(34,0)] = "Tiếp theo nói trực tiếp với tôm hùm:"
T[(35,0)] = "1. Giúp tôi kết nối thiết bị Android 192.168.1.12 -- nếu bước trước bạn chưa thêm adb vào biến môi trường, ở đây phải cho tôm hùm biết đường dẫn cài adb.exe"
T[(36,0)] = "Lần đầu sử dụng cần cho nó biết địa chỉ IP của TV, sau này không cần nữa."
T[(37,0)] = "2. \"Giúp tôi xem thời gian thiết bị đã chạy\" -- lúc này tôm hùm sẽ bắt đầu gửi lệnh đến TV, trả về thời gian TV đã bật (yên tâm sử dụng, các lệnh này đều được thiết bị Android hỗ trợ sẵn, không ảnh hưởng gì đến thiết bị)"
T[(38,0)] = "3. \"Chụp màn hình thiết bị hiện tại, trả về cho tôi dưới dạng file đính kèm\" -- nếu bạn gửi lệnh trên Lark, lát nữa sẽ thấy một hình ảnh, chính là nội dung màn hình TV hiện tại"
T[(39,0)] = "4. \"Xem thiết bị này đã mở những app nào, thời gian sử dụng mỗi app\"."
T[(40,0)] = "Còn nhiều tính năng tương tự, cũng có thể nhờ tôm hùm giúp click trên TV v.v., giống như remote vậy"
T[(41,0)] = "Bốn, Tạo kỹ năng"
T[(42,0)] = "Có thể tạo một kỹ năng cho tôm hùm, sau này mỗi lần truy vấn hoặc để tôm hùm tự động truy vấn thời gian chạy thiết bị sẽ tiện hơn nhiều"
T[(43,0)] = "Giúp tôi tạo một kỹ năng, bao gồm từ lấy thiết bị Android có thể kết nối, đến kết nối thiết bị rồi lấy thời gian chạy thiết bị. (Hãy đảm bảo bạn đã cài skill-creater là kỹ năng chính thức)"
T[(44,0)] = "Tiếp theo có thể tạo task định kỳ, ví dụ mỗi 10 phút để tôm hùm kiểm tra thời gian chạy thiết bị, nếu vượt quá bao lâu thì thực thi lệnh tắt máy."
T[(45,0)] = "Trên đây chỉ là ví dụ đơn giản, hiểu cách cấu hình rồi, còn lại chơi thế nào, các bạn tự suy nghĩ nhé."
T[(46,0)] = "Quy trình trên cũng áp dụng cho điện thoại Android, xem video dưới đây"
T[(47,0)] = "Tại sao tôi không dùng điện thoại làm ví dụ, vì tôi sợ liên quan đến vấn đề riêng tư, lỡ bị dùng để \"giám sát\" phá hoại hạnh phúc gia đình thì có tội."
T[(48,0)] = "Về lý thuyết, bất kỳ thiết bị thông minh Android nào hỗ trợ ADB hoặc giao diện debug mạng (như một số máy chiếu, hệ thống xe hơi) đều có thể trở thành đối tượng quản lý của OpenClaw."
T[(49,0)] = "Lời kết: AI quản gia của bạn, bắt đầu từ việc động tay"
T[(50,0)] = "Case này cho thấy công nghệ AI đã tiến hóa từ \"đồ chơi chat\" thành \"công cụ sống\" như thế nào. Giá trị cốt lõi của OpenClaw không nằm ở bản thân nó là gì, mà ở cách bạn hướng dẫn nó, dạy nó, và cuối cùng để nó phục vụ bạn."
T[(51,0)] = "Từ \"gợi ý bằng miệng\" đến \"thực thi bằng tay\", từ \"một cuộc hội thoại\" đến \"kỹ năng vĩnh viễn\", đây chính là sự thay đổi paradigm mà AI agent mang lại. Quản gia số của bạn, có lẽ bắt đầu từ việc quản lý một chiếc TV hôm nay."
T[(52,0)] = "Tuyên bố miễn trừ trách nhiệm: Công nghệ, phương pháp và công cụ mô tả trong bài viết chỉ dùng cho mục đích giáo dục và nghiên cứu kỹ thuật hợp pháp, nhằm giúp người dùng quản lý và tối ưu trải nghiệm thiết bị thông minh cá nhân tốt hơn. Nghiêm cấm sử dụng nội dung bài viết cho bất kỳ hoạt động bất hợp pháp nào, mọi tổn thất trực tiếp hoặc gián tiếp, trách nhiệm pháp lý hoặc hậu quả khác do sử dụng hoặc lạm dụng nội dung bài viết, đều do người sử dụng tự chịu trách nhiệm, không liên quan đến tác giả và nền tảng phát hành."

translated_count = 0
kept_count = 0
total_text = 0
for i, block in enumerate(translated['blocks']):
    for j, el in enumerate(block['elements']):
        if el['type'] == 'text_run':
            total_text += 1
            if (i,j) in T:
                el['content'] = T[(i,j)]
                translated_count += 1
            else:
                kept_count += 1

with open('art8_translated.json', 'w', encoding='utf-8') as f:
    json.dump(translated, f, ensure_ascii=False, indent=2)
print(f"Total: {total_text}, Translated: {translated_count}, Kept: {kept_count}")
