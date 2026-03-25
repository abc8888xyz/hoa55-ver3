# -*- coding: utf-8 -*-
import json, sys, copy
sys.stdout.reconfigure(encoding='utf-8')

with open('_art20_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

trans = copy.deepcopy(data)

# Translation map: (block_index, element_index) -> Vietnamese translation
T = {}

# Block 0: page title
T[(0, 0)] = "Tổng hợp livestream | Phân tích kiến trúc kỹ thuật OpenClaw, hướng dẫn bạn tự tay xây dựng một con Tôm Hùm nhỏ nhất"
# Block 1
T[(1, 0)] = "Tối ngày 24 tháng 2, chúng tôi đã mời Lai Tân Lộc từ Share AI cùng phân tích kiến trúc kỹ thuật của OpenClaw, và hướng dẫn mọi người tự tay xây dựng một con Tôm Hùm nhỏ nhất."
# Block 2
T[(2, 0)] = "Buổi livestream lần này có một hiệu ứng rất kịch tính, giữa chừng Lai Tân Lộc tiện tay cho Tôm Hùm gọi một cuộc FaceTime cho khán giả trong phòng livestream, sau một hồi xoay xở thì thực sự đã kết nối được, đối phương được kéo thẳng vào làm một cuộc kết nối ngẫu hứng."
# Block 3
T[(3, 0)] = 'Một điều nữa là gần cuối buổi livestream, anh ấy cho Tôm Hùm "thoát khỏi ứng dụng Feishu", kết quả là buổi livestream cứ thế bị Tôm Hùm tự tay tắt, hiệu ứng chương trình đạt đỉnh.'
# Block 4
T[(4, 0)] = "Lai Tân Lộc là một bạn sinh năm 2000, trước đó tự làm Kode agent, đã phân tích Claude Code. Lần này anh ấy mang theo một kho mã nguồn mở dạy học chuẩn bị riêng cho buổi livestream là Claw 0, bóc từng lớp kiến trúc kỹ thuật của Tôm Hùm cho mọi người xem."
# Block 5 - 2 elements
T[(5, 0)] = "Kết luận rất đơn giản: "
T[(5, 1)] = "Tôm Hùm = Claude Code + Bộ hẹn giờ + Tự tìm việc cho mình khi rảnh."
# Block 6 - 3 elements
T[(6, 0)] = "Chỉ với hai cơ chế này, nó đã biến từ một công cụ thụ động thành một "
T[(6, 1)] = "trợ lý AI cá nhân hoạt động chủ động"
T[(6, 2)] = "."
# Block 7
T[(7, 0)] = "1. OpenClaw thực chất là gì"
# Block 8
T[(8, 0)] = "Trước tiên nói về bối cảnh."
# Block 9
T[(9, 0)] = "Tháng 2 năm ngoái Claude Code ra mắt, tháng 3 Manus xuất hiện, đến tháng 11 năm ngoái bắt đầu có lượng lớn người dùng không phải lập trình viên tràn vào. Trong khoảng thời gian này, cộng đồng mã nguồn mở bùng nổ theo, xuất hiện hàng loạt dự án agent, OpenClaw là một trong những dự án chạy nhanh nhất."
# Block 10
T[(10, 0)] = 'Ban đầu nó tên là Clawdbot, sau đó vì nhận được thư luật sư của Anthropic nên đổi thành Moltbot, cuối cùng định tên là OpenClaw, cũng chính là "Tôm Hùm" mà mọi người vẫn nói.'
# Block 11 - 2 elements
T[(11, 0)] = "Tính đến tối livestream, dự án này đã có hơn 200.000 star trên GitHub, "
T[(11, 1)] = "là một trong những dự án mã nguồn mở tăng trưởng nhanh nhất trong lịch sử GitHub."
# Block 12
T[(12, 0)] = "Phần agent cốt lõi của OpenClaw sử dụng một framework gọi là Pi agent. Framework này về bản chất cực kỳ tối giản: chưa đến 150 dòng code, định nghĩa các công cụ như bash, read, write, edit, là có thể chạy được một agent hoạt động bình thường."
# Block 13
T[(13, 0)] = "Điều thực sự làm OpenClaw khác biệt không phải là bản thân agent, mà là những cơ chế bao bên ngoài agent."
# Block 14
T[(14, 0)] = "Ps: Hình trên là AJ dùng Tôm Hùm + Skill chạy ra, sau này cũng sẽ chia sẻ bộ prompt này, các bạn quan tâm có thể theo dõi nhé~"
# Block 15
T[(15, 0)] = "2. Phân tích ba cơ chế cốt lõi"
# Block 16
T[(16, 0)] = "Tác vụ định kỳ (Cron)"
# Block 17
T[(17, 0)] = "Cơ chế này cho phép agent tự sắp xếp các tác vụ định kỳ cho chính mình."
# Block 18 - 2 elements
T[(18, 0)] = "Hỗ trợ ba chế độ: "
T[(18, 1)] = "Thực hiện một lần (ví dụ ngày mai lúc 3 giờ chiều nhắc tôi bật livestream), thực hiện định kỳ (ví dụ mỗi ngày lúc 10 giờ sáng tặng tôi một bất ngờ), và biểu thức Cron tiêu chuẩn."
# Block 19
T[(19, 0)] = "Điểm mấu chốt là, những tác vụ này không chỉ người dùng có thể thiết lập, agent cũng có thể tự chủ động thêm vào."
# Block 20
T[(20, 0)] = "Ví dụ agent có thể tự sắp xếp mỗi tối lúc 12 giờ đêm quét qua một lượt issues của một kho mã nguồn mở nào đó, rồi ngày hôm sau khi có người hỏi, nó đã chuẩn bị sẵn tài liệu trước rồi."
# Block 21
T[(21, 0)] = "Nhịp tim (Heartbeat)"
# Block 22
T[(22, 0)] = 'Đây là cơ chế thú vị nhất, cũng là nguyên nhân khiến Tôm Hùm trông có vẻ "có sự sống".'
# Block 23 - 2 elements
T[(23, 0)] = "Giải thích bằng một câu: "
T[(23, 1)] = "Cứ mỗi 30 giây, hệ thống tự động gửi một tin nhắn cho agent, để nó kiểm tra xem có việc gì có thể làm không."
# Block 24
T[(24, 0)] = "Nội dung tin nhắn đến từ một file heartbeat.md, trong đó ghi các nhiệm vụ cần làm và nhắc nhở định kỳ. Agent đọc xong, có việc thì làm, không có việc thì trả về một từ khóa cụ thể, hệ thống nhận được thì sẽ không làm phiền bạn."
# Block 25
T[(25, 0)] = "Sự khác biệt bản chất với Claude Code nằm ở đây, Claude Code là đá một cái mới động một cái, OpenClaw là tự tỉnh dậy mỗi 30 giây, xem có việc gì để làm không."
# Block 26
T[(26, 0)] = "Soul (Linh hồn)"
# Block 27
T[(27, 0)] = 'Mọi người nói Tôm Hùm "có linh hồn", khái niệm này nghe có vẻ rất huyền bí.'
# Block 28
T[(28, 0)] = 'Nhưng thực tế, cái gọi là linh hồn, chỉ là trích phần nội dung về "agent là ai, phong cách hành vi là gì" trong system prompt ra, lưu thành một file soul.md riêng.'
# Block 29 - 2 elements
T[(29, 0)] = "Logic giống hệt với skill. Trước đây mỗi lần phải dán thủ công một đoạn prompt dài để bảo AI làm việc thế nào, bây giờ cố định thành file .md, agent tự động đọc khi khởi động. "
T[(29, 1)] = "Soul chính là phiên bản áp dụng tư tưởng này vào việc thiết lập nhân cách."
# Block 30
T[(30, 0)] = 'Vì vậy bạn có thể chia sẻ file soul.md của mình trên cộng đồng, người khác tải về, agent sẽ có phong cách mà bạn đã tinh chỉnh. "Truyền bá linh hồn" nói đến chính là việc này.'
# Block 31
T[(31, 0)] = "3. Những gì đã xảy ra tại hiện trường livestream"
# Block 32
T[(32, 0)] = "Agent âm thầm hoàn thành nhiệm vụ dịch thuật trong buổi livestream"
# Block 33
T[(33, 0)] = "Buổi livestream diễn ra được khoảng 20 phút, Lai Tân Lộc kéo trang GitHub của kho mã dạy học Claw 0 mà anh ấy đã chuẩn bị hôm nay ra cho mọi người xem."
# Block 34 - 2 elements
T[(34, 0)] = "Rồi phát hiện rằng, một nhiệm vụ mà anh ấy giao cho agent trước khi bắt đầu livestream đã hoàn thành: "
T[(34, 1)] = "dịch tài liệu dạy học sang tiếng Anh và tiếng Nhật, rồi đẩy lên kho mã."
# Block 35
T[(35, 0)] = "Trước khi livestream bắt đầu, kho mã chỉ có thư mục phiên bản tiếng Trung. Sau hơn 20 phút, làm mới trang, hai thư mục phiên bản tiếng Anh và tiếng Nhật đã lặng lẽ xuất hiện ở đó."
# Block 36
T[(36, 0)] = '"Tôi còn không để ý, nó tự làm xong ở nền, trực tiếp commit luôn."'
# Block 37
T[(37, 0)] = "Cộng đồng WaytoAGI có rất nhiều bạn bè ở Nhật Bản, Singapore. Việc Tôm Hùm tiện tay xử lý xong phiên bản đa ngôn ngữ này, là minh chứng trực quan nhất cho giá trị của việc triển khai tại máy local."
# Block 38
T[(38, 0)] = "Một tuần 5000 commit"
# Block 39 - 2 elements
T[(39, 0)] = "Lai Tân Lộc pull code mới nhất của OpenClaw, "
T[(39, 1)] = "so với một tuần trước, đã tăng thêm gần 5000 commit."
# Block 40
T[(40, 0)] = "Tính ra: một kỹ sư của một công ty, trung bình mỗi ngày commit mười mấy đến hai mươi cái, làm liên tục một năm mới tích lũy được 5000, còn dự án này một tuần đã đạt đến."
# Block 41
T[(41, 0)] = '"Dự án này 99% là do phi-con-người đang cập nhật."'
# Block 42
T[(42, 0)] = "Tác giả dự án Kidd chắc chắn review không xuể, nhiều khả năng là cho agent lướt qua một cái rồi merge. Điều này cũng giải thích vì sao gần đây nhiều người dùng gặp những bug khó hiểu, cứ một hai tuần cập nhật một lần là thường sẽ hết."
# Block 43
T[(43, 0)] = "Dùng Tôm Hùm gọi FaceTime kết nối với khán giả"
# Block 44
T[(44, 0)] = "Đây là phần có hiệu ứng chương trình nhất trong buổi tối đó."
# Block 45
T[(45, 0)] = "Lai Tân Lộc muốn thử nghiệm xem Tôm Hùm có thể điều khiển máy tính gọi điện thoại không. Anh ấy cho agent gọi FaceTime cho một khán giả trong phòng livestream, gửi một tin nhắn, rồi nhìn màn hình, cửa sổ ứng dụng FaceTime hiện lên, tự động điền số của đối phương, cuộc gọi thực sự được thực hiện!"
# Block 46
T[(46, 0)] = "Khán giả Lục Mộng nghe máy, được kéo vào buổi livestream làm một cuộc kết nối ngẫu hứng, ngay tại chỗ chúc mọi người đầu xuân, AJ nói lần sau có thể dùng cách này để kết nối."
# Block 47 - 2 elements
T[(47, 0)] = "Bản thân Lai Tân Lộc cũng không ngờ là thực sự thành công. "
T[(47, 1)] = "Việc gọi điện thoại này, agent thực hiện bằng cách sử dụng trực tiếp tham số dòng lệnh của FaceTime, được điều khiển bởi mô hình GLM của Zhipu, không cấu hình bất kỳ browser MCP nào."
# Block 48
T[(48, 0)] = "4. Một số nhận định đáng ghi nhớ"
# Block 49
T[(49, 0)] = "Triển khai tại máy local vs. triển khai trên cloud, chênh lệch rất lớn."
# Block 50
T[(50, 0)] = "Hai tuần trước, Lai Tân Lộc đã triển khai một phiên bản Tôm Hùm trên máy chủ cloud, dùng một thời gian rồi bỏ."
# Block 51
T[(51, 0)] = "Triển khai trên máy chủ cloud, về cơ bản không khác gì dùng Manus. Trên đó không có dữ liệu local của bạn, không có file của bạn, những gì có thể làm là rất hạn chế."
# Block 52
T[(52, 0)] = "Triển khai trên máy tính local lại là chuyện khác hẳn."
# Block 53
T[(53, 0)] = "Nó có thể đọc tất cả file trên desktop của bạn, giúp bạn dọn dẹp ổ đĩa, điều chỉnh chính sách pin, tìm một file gửi cho bạn, những thứ này là cloud không thể làm được."
# Block 54
T[(54, 0)] = "Tất nhiên, quyền hạn càng lớn, rủi ro càng lớn."
# Block 55
T[(55, 0)] = 'Có lần cho agent "tiếp tục làm tất cả những gì bạn có thể làm", kết quả là khi dọn dẹp ổ đĩa, nó suýt xóa luôn cả dữ liệu tài liệu dùng cho khách hàng bên A.'
# Block 56
T[(56, 0)] = '"Bạn làm bảo mật càng tốt, Tôm Hùm càng ít việc có thể làm; bạn làm bảo mật càng lỏng lẻo, bạn không biết mô hình có làm điều gì bất ngờ không."'
# Block 57
T[(57, 0)] = "Về việc dùng mô hình nào để chạy Tôm Hùm."
# Block 58
T[(58, 0)] = "Khuyến nghị của Lai Tân Lộc là nên dùng Claude càng nhiều càng tốt, để điều khiển agent làm các nhiệm vụ phức tạp, sự chênh lệch về năng lực mô hình là rất rõ ràng."
# Block 59
T[(59, 0)] = "Mô hình nội địa cũng chạy được, nhưng anh ấy dùng một mô hình nội địa nào đó để dọn dẹp ổ đĩa, agent rõ ràng đã ghi lại mỗi mục dọn được bao nhiêu dung lượng, nhưng khi báo cáo dung lượng khả dụng cuối cùng lại tính sai, từ 25G ban đầu càng tính càng nhỏ, thành 21G."
# Block 60
T[(60, 0)] = "Tuy nhiên nếu chỉ dùng để chạy thông quy trình, làm quen với cơ chế, thì coding plan của mô hình nội địa là đủ dùng."
# Block 61
T[(61, 0)] = "Hơn nữa hiện nay nhiều người đã có gói đăng ký Claude Code, có thể thay thế phần agent core bằng Claude Code CLI, tái sử dụng gói đăng ký thay vì trả phí API, chi phí thấp hơn."
# Block 62
T[(62, 0)] = "Xem xong buổi này, bạn sẽ thấy Tôm Hùm không bí ẩn đến thế, nhưng cũng không phải cứ để nó làm là sẽ làm tốt."
# Block 63 - 2 elements
T[(63, 0)] = "Giới hạn năng lực của nó, "
T[(63, 1)] = "phụ thuộc rất nhiều vào bạn cấu hình những công cụ gì, dùng mô hình nào, triển khai ở đâu."
# Block 64
T[(64, 0)] = "Tư thế phù hợp nhất hiện tại, có lẽ là trước tiên triển khai nó trên máy tính của mình, coi nó như một đồng đội luôn chạy nền giúp bạn theo dõi công việc, không có gì làm thì tự tìm việc, rồi dần dần thêm các mở rộng."

# Apply translations
translated_count = 0
total_text = 0
kept_count = 0

for bi, block in enumerate(trans['blocks']):
    for ei, el in enumerate(block['elements']):
        if el['type'] == 'text_run' and el['content'].strip():
            total_text += 1
            key = (bi, ei)
            if key in T:
                el['content'] = T[key]
                translated_count += 1
            else:
                kept_count += 1
                print(f'WARNING: Missing translation for block {bi} element {ei}: {el["content"][:60]}')

print(f'Total text: {total_text}, Translated: {translated_count}, Kept: {kept_count}')

with open('_art20_trans.json', 'w', encoding='utf-8') as f:
    json.dump(trans, f, ensure_ascii=False, indent=2)
print('Saved _art20_trans.json')
