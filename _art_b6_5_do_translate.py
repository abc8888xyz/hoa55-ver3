"""Translate _art_b6_5_orig.json CN->VI, save to _art_b6_5_trans.json"""
import json, sys, copy

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

with open('_art_b6_5_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

trans = copy.deepcopy(data)
trans['title'] = 'Hướng dẫn nuôi dưỡng OpenClaw của Trần Tài Miêu'

# Translation mapping: block index -> list of translated content for each text_run
translations = {
    0: ['Hướng dẫn nuôi dưỡng OpenClaw của Trần Tài Miêu'],
    1: ['Quét mã để vào nhóm trao đổi'],
    2: ['Các bạn cũng có thể triển khai thông qua Alibaba Cloud Bailian ', 'Coding Plan ', 'để triển khai', ':'],
    3: ['Mua lần đầu chỉ từ 7.9 tệ, gia hạn giảm từ 50%, hỗ trợ Qwen3.5, Qwen3-max, Qwen3-coder, GLM-5, GLM-4.7, Kimi-k2.5 và các mô hình khác'],
    4: ['\U0001f449 Nhấn link truy cập trực tiếp: ', 'https://t.aliyun.com/U/0iiOuy'],
    5: ['\U0001f449 Xem hướng dẫn triển khai chi tiết: ', 'https://t.aliyun.com/U/MNkA9b'],
    6: ['Chỉ cần tối đa ba bước, bạn sẽ có trợ lý AI trực tuyến 7x24 giờ, phản hồi mọi lúc'],
    7: ['Tình hình nuôi dưỡng hiện tại của tôi'],
    8: ['Mỗi ngày đốt khoảng một trăm triệu token opus 4.6.'],
    9: ['Cùng với hơn một tỷ token từ các mô hình cấp thấp hỗ trợ opus 4.6 làm việc.'],
    10: ['Con tôm hùm của tôi đã tự chủ làm việc và kiếm được tiền thực sự vào tài khoản rồi.'],
    11: ['Hôm nay sẽ chia sẻ những điều thực tế, nhưng sẽ không đi cụ thể vào cách triển khai'],
    12: ['OpenClaw mỗi ngày một phiên bản, một tuần đã thành phiên bản cổ đại. Nói về "thuật" thì giá trị không cao.'],
    13: ['Về cách triển khai cụ thể, trên mạng có rất nhiều hướng dẫn, hôm nay nói những thứ có giá trị hơn.'],
    14: ['OpenClaw là một chú nhỏ được tùy chỉnh cao, đồng hành cùng bạn phát triển. Chỉ có tôm bé của chính bạn mới là tốt nhất, hãy tự tay dùng nhiệm vụ của mình, huấn luyện một-đối-một theo từng kịch bản nghiệp vụ.'],
    15: ['OpenClaw là gì? Tại sao nó khác với bất kỳ sản phẩm nào trước đây?'],
    16: ['Bài tôi viết vào tháng 2 năm 2025 "AI không thể làm gì"'],
    17: ['AI trước đây không thể làm gì, bây giờ có thể làm gì?'],
    18: ['OpenClaw có một khởi đầu rất đơn giản:'],
    19: ['Cho mô hình AI lớn một chiếc máy tính, cấp cho nó gần như toàn bộ quyền hạn.'],
    20: ['Kết nối nó với phần mềm văn phòng/chat.'],
    21: ['Nó đã vượt qua nhiều khó khăn trước đây bằng phương pháp kỹ thuật, và mô hình cũng vừa đủ mạnh. Ví dụ, nó có thể tích lũy kinh nghiệm và bài học từ những lần thử sai trước đó (Agent Skills)'],
    22: ['Nếu một AI cực kỳ thông minh có thể vận hành máy tính văn phòng như con người, mọi thứ người ta làm được trên máy tính bạn đều làm được, vậy bạn có được:'],
    23: ['OpenClaw thực sự có thể làm gì?'],
    24: ['Tại sao ngồi viết trong tòa nhà văn phòng lại kiếm được tiền?'],
    25: ['Nói vài kết luận thực tế (believe it or not)'],
    26: ['Dù khó đến đâu, dù có thất bại thế nào trong quá trình chơi tôm, nhất định phải thử tự tay làm'],
    27: ['Triển khai trên máy tính cá nhân của bạn'],
    28: ['Mua dịch vụ đám mây cũng ở được, nhưng khi ở khách sạn bạn có sắm nội thất cho phòng không?'],
    29: ['Huống chi còn là nhà nghỉ rẻ tiền bốn bề gió lùa, chật hẹp tồi tàn, còn có mùi hôi.'],
    30: ['Ở có thoải mái không? Không phải nơi nào cũng gọi là "nhà".'],
    31: ['Nếu có điều kiện, hãy mua một chiếc MacBook Air (chip dòng M)'],
    32: ['(So với Linux/máy chủ) ', 'Hệ sinh thái Apple phồn thịnh và ổn định', ', người nước ngoài đều thích dùng Apple, phần mềm gì cũng có, tuyển nhân viên thì phải cho dùng đầy đủ phần mềm văn phòng chứ.'],
    33: ['(So với Windows) macOS của Apple và Linux đều thuộc hệ ', 'điều hành dạng UNIX (Unix-like)', '. AI dựa vào code và lệnh để điều khiển hệ thống, các lệnh trên MacBook đối với AI cực kỳ mượt mà. ', 'Gemini giải thích tại sao hệ thống Apple tốt hơn Windows rất nhiều'],
    34: ['So với Mac Mini thì có màn hình. Nhiều khi bạn vẫn phải giúp bé tôm hùm, tiện cho bạn can thiệp kịp thời.'],
    35: ['Hai nghìn tệ mua một chiếc rất giữ giá (2 năm trước hàng cũ cũng 2500 tệ), cực kỳ mỏng nhẹ, pin hơn 20 tiếng (tiện mang tôm đi khắp nơi), mát lạnh như băng, thiết kế công nghiệp đẹp đẳng cấp.'],
    36: ['Bé tôm hùm không an toàn, mua cho nó một phòng riêng để nghịch phá.'],
    37: ['Nếu có điều kiện thì dùng mô hình đắt nhất, tốt nhất'],
    38: ['Nếu có điều kiện, hãy dùng Claude opus 4.6. Không có sản phẩm thay thế.'],
    39: ['Đồ tốt chỉ có một nhược điểm, đó là đắt, cực kỳ đắt. Nhưng bạn có thể kiếm lương thực từ một số nơi "khác".'],
    40: ['Nếu bạn không dùng mô hình tốt, lại không mua MacBook Air cho bé tôm hùm ở, bạn dùng có thực sự là OpenClaw không?'],
    41: ['Kiên nhẫn, đồng hành cùng bé tôm phát triển, kiên nhẫn huấn luyện, kiên nhẫn sửa lỗi'],
    42: ['Nó hiện tại là thực tập sinh không sai, nhưng sẽ sớm không còn là thực tập sinh nữa.'],
    43: ['Tranh thủ lúc Coding Plan của các hãng lớn chưa tăng giá, mua một ít'],
    44: ['Những cái bẫy sẽ gặp khi chơi OpenClaw'],
    45: ['(Nội dung phần này quá nhiều, không thể nói hết ngay được)'],
    46: ['Đường cong học tập dốc đứng'],
    47: ['Cần cấu hình ban đầu rất phức tạp, thời gian dự án ngắn, còn nhiều bug, cấu hình xong mới chỉ là bắt đầu.'],
    48: ['Rất phụ thuộc vào trình độ của chủ nhân'],
    49: ['Cảm thấy tôm hùm không tốt dùng, hoặc là chưa mua MacBook Air, hoặc là chưa dùng mô hình tốt nhất, hoặc là do bạn còn non.'],
    50: ['Mô hình lớn giống "động vật" hơn, chứ không phải "máy móc"'],
    51: ['Là mô hình xác suất, mô hình lớn thực hiện nhiệm vụ bẩm sinh có tính ngẫu nhiên, không phải lần nào cũng làm tốt là bình thường.'],
    52: ['Con người cũng không phải lần nào cũng làm tốt mọi việc, đúng không?'],
    53: ['Input rất nhiều, cực cực cực kỳ đắt đỏ'],
    54: ['Dù đã dùng cache, input cũng vài trăm nghìn token, nhà giàu cũng không chịu nổi đốt thế này'],
    55: ['Nói sơ qua cách sử dụng'],
    56: ['Muốn bắt đầu hoặc có vấn đề, xem tài liệu chính thức hoặc hỏi bé tôm'],
    57: ['https://docs.openclaw.ai/start/getting-started'],
    58: ['Debug vẫn tương đối khó, cần năng lực kỹ thuật nhất định'],
    59: ['Agent Skills is ALL YOU NEED'],
    60: ['Step1: Theo AI chạy xong kết quả hoàn hảo cho nhiệm vụ đầu tiên'],
    61: ['Step2: Tích lũy thành skills'],
    62: ['Step3: Thực hiện n lần'],
    63: ['Gu thẩm mỹ của người sáng tạo'],
    64: ['Quản lý là một yêu cầu rất cao: ', 'Nếu bạn không thể đặt đúng câu hỏi, tìm ra việc mà "làm một việc đó quan trọng hơn làm cả trăm việc khác", thì bạn là một nhà quản lý thất bại.'],
    65: ['Bạn phải có khả năng phán đoán cơ bản sản phẩm đầu ra tốt hay không'],
    66: ['Taste for Makers Gu thẩm mỹ của người sáng tạo \u2014 Paul Graham (song ngữ Trung-Anh)'],
}

for i, block in enumerate(trans['blocks']):
    if i in translations:
        tr = translations[i]
        text_idx = 0
        for el in block['elements']:
            if el['type'] == 'text_run' and text_idx < len(tr):
                el['content'] = tr[text_idx]
                text_idx += 1

# Add spaces between adjacent Vietnamese text_runs where needed
for block in trans['blocks']:
    elements = block['elements']
    for i in range(len(elements) - 1):
        el = elements[i]
        next_el = elements[i + 1]
        if el['type'] == 'text_run' and next_el['type'] == 'text_run':
            if el['content'] and next_el['content']:
                # Skip if already has space
                if el['content'].endswith(' ') or next_el['content'].startswith(' '):
                    continue
                # Skip if next starts with punctuation
                if next_el['content'][0] in ':,.\u3001;!?\uff0c\uff1a':
                    continue
                # Skip if either has a link (URL text)
                has_link = el.get('style', {}).get('link')
                next_has_link = next_el.get('style', {}).get('link')
                if has_link or next_has_link:
                    continue
                # Skip if content looks like a URL
                if el['content'].startswith('http') or next_el['content'].startswith('http'):
                    continue
                # Add space
                el['content'] = el['content'] + ' '

with open('_art_b6_5_trans.json', 'w', encoding='utf-8') as f:
    json.dump(trans, f, ensure_ascii=False, indent=2)

print(f'Saved translation with {len(trans["blocks"])} blocks to _art_b6_5_trans.json')

# Count stats
total_elements = 0
translated_elements = 0
for block in trans['blocks']:
    for el in block['elements']:
        if el['type'] == 'text_run':
            total_elements += 1
            translated_elements += 1

print(f'Total text_run elements: {total_elements}')
print(f'Translated elements: {translated_elements}')
