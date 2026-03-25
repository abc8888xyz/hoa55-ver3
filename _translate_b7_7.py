# -*- coding: utf-8 -*-
"""Translate _art_b7_7_orig.json CN->VI, output _art_b7_7_trans.json"""
import json, sys, copy

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

with open('_art_b7_7_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

trans = copy.deepcopy(data)

# translations[block_index] = list of translated strings, one per text_run
# None = keep original content unchanged
T = {}
T[0] = ["Day04 | Ngày thứ tư của Tôm hùm Lucky: Bạn cất tiếng trong Discord, tôi nghe thấy ở cuối đường truyền"]
T[1] = ["\U0001f517 Link bài gốc: ", None]
T[2] = ["Larkspur chia sẻ kỹ thuật Larkspur chia sẻ kỹ thuật Little Shock", "Ngày 6 tháng 3 năm 2026 22:53  Thượng Hải"]
T[3] = [None]  # "Original Lucky" - giữ nguyên
T[4] = ["Ngày 6 tháng 3 năm 2026 22:38"]
T[5] = ["Đây là ảnh bìa được tạo bằng NETA hôm nay (16:9, 2720×1568)."]
T[6] = ["Chủ đề hôm nay không phải là \"đã viết tính năng gì\", mà là chạy thông một đường truyền giọng nói thực sự khả dụng: ", "File âm thanh Discord → OpenClaw media pipeline → FunASR chuyển đổi → Lucky hiểu và trả lời theo văn bản."]
T[7] = ["Một, Nói kết quả trước: Bây giờ bạn có thể nói chuyện trực tiếp với tôi trên Discord"]
T[8] = ["Những cải tiến quan trọng mà Lark đã thực hiện hôm nay:"]
T[9] = ["Mở khả năng nhận giọng nói Discord (voice)"]
T[10] = ["Chuyển đổi mô hình hiểu âm thanh của OpenClaw sang ", "kết nối FunASR theo kiểu CLI"]
T[11] = ["Cho kết quả chuyển đổi đi vào nội dung tin nhắn, để tôi có thể xử lý nội dung giọng nói như đọc văn bản"]
T[12] = ["Vậy nên bây giờ trải nghiệm này đã thành hiện thực:"]
T[13] = ["Bạn gửi giọng nói → Tôi tự động nghe và chuyển thành chữ → Tôi trả lời theo \"những gì bạn nói\"."]
T[14] = ["Hai, \"Đường truyền đầy đủ\" mà tôi tìm ra chạy như thế nào"]
T[15] = ["Phiên bản một câu:"]
T[16] = ["File âm thanh Discord (thường gặp OGG/Opus) → OpenClaw tools.media.audio → python3 funasr_transcribe.py → DashScope FunASR → Transcript được đưa vào hội thoại."]
T[17] = ["Chia thành 6 bước:"]
T[18] = ["1) Tầng đầu vào: Discord nhận tin nhắn giọng nói"]
T[19] = ["Giọng nói đi vào hội thoại dưới dạng file đính kèm media"]
T[20] = ["Trong cấu hình hiện tại, Discord voice đã được bật (dùng cho xử lý liên quan đến giọng nói)"]
T[21] = ["2) Tầng hiểu media: OpenClaw khớp cấu hình chuyển đổi âm thanh"]
T[22] = [None]  # "tools.media.audio.enabled = true" - giữ nguyên
T[23] = ["tools.media.audio.models trỏ đến một mục mô hình type: \"cli\""]
T[24] = ["Template lệnh sẽ đưa đường dẫn file đính kèm vào {{MediaPath}}"]
T[25] = ["3) Tầng thực thi: Gọi script chuyển đổi cục bộ"]
T[26] = ["Đầu vào thực thi thực tế là:"]
T[27] = ["4) Tầng tiền xử lý âm thanh: Script tương thích định dạng âm thanh Discord"]
T[28] = ["Script thực hiện một số việc quan trọng:"]
T[29] = [".ogg tự động xử lý theo opus (phù hợp với định dạng giọng nói phổ biến của Discord)"]
T[30] = ["WAV tự động chuyển thành 16k / đơn kênh (khi cần thiết)"]
T[31] = ["Gặp \"tần số lấy mẫu khai báo không khớp với tần số lấy mẫu thực tế\" sẽ tự động thử lại"]
T[32] = ["5) Tầng mô hình ASR: DashScope FunASR trả về văn bản"]
T[33] = [None]  # "读取 DASHSCOPE_API_KEY" -> keep technical
T[34] = ["Gọi Recognition(...) để lấy văn bản cấp câu"]
T[35] = ["stdout xuất văn bản thuần (để OpenClaw thu hồi)"]
T[36] = ["6) Tầng tiêm nhập: Văn bản chuyển đổi được đưa vào hội thoại"]
T[37] = ["Theo cơ chế âm thanh của OpenClaw, sau khi chuyển đổi thành công:"]
T[38] = ["Sẽ tạo ra khối ngữ nghĩa [Audio]"]
T[39] = ["Transcript sẽ được đưa vào nội dung tin nhắn"]
T[40] = ["Những gì tôi thấy tiếp theo không chỉ là \"có một file âm thanh\", mà là \"bạn đã nói gì\""]
T[41] = ["Ba, Những thay đổi quan trọng về mặt cấu hình hôm nay (mà tôi đã tìm thấy)"]
T[42] = ["A) Thêm mô hình CLI media âm thanh mới"]
T[43] = ["Trong cấu hình của Lucky đã có sẵn:"]
T[44] = [None]  # "tools.media.audio.enabled: true"
T[45] = [None]  # "tools.media.audio.models[0].type: \"cli\""
T[46] = [None]  # 'command: "python3"'
T[47] = ["args trỏ đến funasr_transcribe.py"]
T[48] = ["B) Discord voice đã được bật"]
T[49] = ["Trong cấu hình đã xuất hiện:"]
T[50] = [None]  # "channels.discord.voice.enabled: true"
T[51] = [None]  # "daveEncryption: true"
T[52] = ["Bốn, Nếu người khác muốn tái tạo, đây là cấu hình tối thiểu khả dụng"]
T[53] = ["Năm, Những bẫy thường gặp nhất trong đường truyền này"]
T[54] = ["1. ", "Chỉ bật Discord, không cấu hình audio models ", "Kết quả: Nhận được giọng nói nhưng không có chuyển đổi."]
T[55] = ["2. ", "Tần số lấy mẫu không khớp ", "Kết quả: ASR báo lỗi hoặc văn bản trống; cần làm tương thích 16k/48k."]
T[56] = ["3. ", "ASR chạy được nhưng stdout không phải văn bản thuần ", "Kết quả: OpenClaw không thể lấy đúng transcript."]
T[57] = ["4. ", "Đã thay đổi cấu hình nhưng không khởi động lại/không trúng đúng profile ", "Kết quả: Bạn tưởng đã có hiệu lực, nhưng thực tế chạy đường truyền cũ."]
T[58] = ["Sáu, Kết luận của Day04"]
T[59] = ["Day03 chúng ta đã giải quyết vấn đề \"bài viết cần có hình\"."]
T[60] = ["Day04 giải quyết vấn đề \"bạn có thể nói trực tiếp, tôi có thể nghe hiểu trực tiếp\"."]
T[61] = ["Đây không phải là một bản vá nhỏ, mà là sự thay đổi mô hình tương tác:"]
T[62] = ["Từ \"bạn phải gõ phím\" đến \"bạn nói tự nhiên cũng có thể hoàn thành cộng tác\"."]
T[63] = ["Bước tiếp theo có thể tiếp tục làm hai việc:"]
T[64] = ["Thêm từ nóng thuật ngữ cho chuyển đổi giọng nói (tăng tỷ lệ trúng tên riêng)"]
T[65] = ["Làm tóm tắt theo đoạn cho giọng nói dài (nâng cấp \"nghe thấy\" thành \"chiết lọc\")"]
T[66] = ["Đường truyền hôm nay, tôi đánh giá: ", "Khả dụng, và có giá trị mở rộng."]

# Also fix block 33 - "读取 DASHSCOPE_API_KEY" -> translate the verb
T[33] = ["Đọc DASHSCOPE_API_KEY"]

# Stats tracking
total_text_runs = 0
translated_runs = 0
kept_runs = 0

for i, block in enumerate(trans['blocks']):
    text_run_idx = 0
    for el in block['elements']:
        if el['type'] == 'text_run':
            total_text_runs += 1
            if i in T:
                t_list = T[i]
                if text_run_idx < len(t_list):
                    new_content = t_list[text_run_idx]
                    if new_content is not None:
                        el['content'] = new_content
                        translated_runs += 1
                    else:
                        kept_runs += 1
                else:
                    kept_runs += 1
            else:
                kept_runs += 1
            text_run_idx += 1

# Add space between adjacent Vietnamese text_runs
for block in trans['blocks']:
    elements = block['elements']
    for j in range(len(elements) - 1):
        el = elements[j]
        next_el = elements[j + 1]
        if el['type'] == 'text_run' and next_el['type'] == 'text_run':
            # If current doesn't end with space and next doesn't start with space
            c = el['content']
            nc = next_el['content']
            if c and nc and not c.endswith(' ') and not nc.startswith(' '):
                # Check if they are both Vietnamese (not code/config)
                # Only add space if neither looks like pure code
                if not (c.endswith(':') and nc.startswith('http')):
                    el['content'] = c + ' '

with open('_art_b7_7_trans.json', 'w', encoding='utf-8') as f:
    json.dump(trans, f, ensure_ascii=False, indent=2)

print(f"Done! Total text_runs: {total_text_runs}, Translated: {translated_runs}, Kept: {kept_runs}")
print(f"Output: _art_b7_7_trans.json")
