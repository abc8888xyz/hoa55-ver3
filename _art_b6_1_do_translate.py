"""Translate _art_b6_1_orig.json CN->VI, preserving all styles/URLs/code/emoji"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import json, copy

with open('_art_b6_1_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Build translation map: block_index -> {element_index: new_content}
# Preserve URLs, code identifiers, technical terms, emoji as-is

trans = {}

# Block 0 - page title
trans[0] = {0: " Lộc Đạo: OpenClaw không dễ dùng? Đó là bạn chưa dùng Cursor \"độ\" lại Tôm Hùm Lớn \"Tà Phái Đại Pháp Tập 2\""}

# Block 1
trans[1] = {0: "Các bạn cũng có thể deploy qua Alibaba Cloud Bách Luyện "}
trans[1][2] = "để deploy"
trans[1][3] = ": "

# Block 2
trans[2] = {0: "Mua lần đầu chỉ từ 7.9 NDT, gia hạn giảm 50%, hỗ trợ Qwen3.5, Qwen3-max, Qwen3-coder, GLM-5, GLM-4.7, Kimi-k2.5 và các model khác"}

# Block 3
trans[3] = {0: "👉 Bấm link truy cập trực tiếp: "}

# Block 4
trans[4] = {0: "👉 Xem hướng dẫn deploy chi tiết: "}

# Block 5
trans[5] = {0: "Chỉ cần tối đa 3 bước, bạn sẽ có trợ lý AI online 24/7, phản hồi bất cứ lúc nào"}

# Block 6
trans[6] = {0: "Chuỗi hướng dẫn | Không cần code | Phù hợp cho tất cả những ai muốn dùng tốt OpenClaw"}

# Block 7
trans[7] = {
    0: "Điều kiện tiên quyết",
    1: ": Đã cài đặt OpenClaw và đã cập nhật lên phiên bản ",
    3: ", và hoàn thành onboard, nếu chưa hoàn thành hãy xem ",
    4: "hướng dẫn"
}

# Block 8 - heading1
trans[8] = {
    0: "Tập 2: ",
    1: "OpenClaw + Claude Code Hooks - Hướng dẫn phát triển Zero-Polling"
}

# Block 9 - heading2
trans[9] = {0: "🛑 Cách dùng OpenClaw của bạn có thể đã sai từ đầu"}

# Block 10
trans[10] = {0: "Nhiều người khi nhận được OpenClaw (Tôm Hùm Lớn), phản ứng đầu tiên là coi nó như một model lập trình mạnh khác."}

# Block 11
trans[11] = {
    0: "Phần lớn mọi người chỉ bảo nó: ",
    1: "\"Ghi lại cái xxxx giúp tôi\"",
    2: ", ",
    3: "\"Chat với tôi đi\"",
    4: ", ",
    5: "\"Viết cho tôi một game Rắn Săn Mồi bằng Python.\"",
    6: " Rồi Tôm Hùm Lớn bắt đầu hì hục tạo code block, tạo một file, rồi tạo file tiếp theo."
}

# Block 12
trans[12] = {0: "Nói thật, nếu chỉ để viết code, bạn hoàn toàn có thể dùng Claude Code, Code x, hoặc Cursor, Trae và những sản phẩm trưởng thành hơn. Vậy tại sao chúng ta phải \"vật vã\" với OpenClaw?"}

# Block 13
trans[13] = {
    0: "Tôi cho rằng điểm quyến rũ thực sự của OpenClaw nằm ở chỗ nó mở khóa khả năng ",
    1: "\"Agent Team mã nguồn mở\"",
    2: "."
}

# Block 14
trans[14] = {0: "Các sản phẩm AI trước đây giống như cắm cọc xuống biển. Hôm nay AutoGPT nổi, mọi người đổ xô đi cắm một cái cọc; ngày mai BabyAGI nổi, lại đi cắm thêm cọc. Kết quả? Có thể chỉ một vòng nâng cấp model lớn, giống như thủy triều dâng lên, những cái cọc này nhanh chóng bị một con sóng đánh sập hết trên bãi cát."}

# Block 15
trans[15] = {0: "Nhưng OpenClaw bạn có thể hiểu nó là một con tàu."}

# Block 16
trans[16] = {
    0: "Nó không ràng buộc với bất kỳ model nào, nó là một ",
    1: "container",
    2: ". Dù mới ra mắt là GLM-5, hay Claude Opus 4.6, hoặc là một model công nghệ đen nào đó chưa từng nghe, con tàu này đều có thể nạp chúng vào, biến chúng thành \"thủy thủ\" trên tàu. ",
    3: "Mực nước (năng lực model) càng cao, con tàu OpenClaw càng nổi cao."
}

# Block 17
trans[17] = {
    0: "Vì vậy, trong thời đại các \"thần tiên đánh nhau\" này, chúng ta không nên để OpenClaw trực tiếp làm công việc nặng nhọc như \"viết code\". Bạn nên tự mình làm thuyền trưởng, còn nó là phó thuyền trưởng của bạn, chỉ huy đội ngũ thủy thủ",
    1: ".",
    2: " Nhiệm vụ của nó là điều phối một Agent Team, điều phối những thủy thủ giỏi nhất trên thị trường, làm việc cho chúng ta."
}

# Block 18 - heading2
trans[18] = {0: "💡 Tư thế đúng: Nhà thầu vs. Kỹ sư"}

# Block 19
trans[19] = {0: "Vậy những cao thủ thực sự chơi như thế nào?"}

# Block 20
trans[20] = {
    0: "Họ sẽ không để OpenClaw tự khiêng gạch. Họ sẽ trang bị cho OpenClaw một \"cao thủ thần cấp\" -- ",
    2: "."
}

# Block 21 - bullet
trans[21] = {
    0: "OpenClaw (Tôm Hùm Lớn)",
    1: " = ",
    2: "Quản lý dự án (PM)",
    3: ". Chịu trách nhiệm hiểu yêu cầu của bạn, phân tách nhiệm vụ, nghiệm thu kết quả."
}

# Block 22 - bullet
trans[22] = {
    1: " = ",
    2: "Kỹ sư cấp cao",
    3: ". Chuyên trách viết code, đọc file, chạy test. Nó chạy trong terminal, có quyền truy cập code cực cao và năng lực kỹ thuật cực mạnh."
}

# Block 23
trans[23] = {0: "Bây giờ logic trở thành: Bạn nói với OpenClaw: \"Tôi muốn game Rắn Săn Mồi.\" "}

# Block 24
trans[24] = {0: "OpenClaw quay sang nói với Claude Code: \"Đi viết game Rắn Săn Mồi cho sếp.\""}

# Block 25
trans[25] = {
    0: "Nhưng vẫn chưa hoàn hảo!",
    1: " Tại sao?"
}

# Block 26 - heading2
trans[26] = {0: "💸 Vấn đề mới: Nó đang \"chờ ngốc\""}

# Block 27
trans[27] = {0: "Tại sao khi bạn cho OpenClaw đi chỉ huy Claude Code làm việc, nó thường không phản hồi trong thời gian dài, nhìn vào backend thì token tăng vùn vụt?"}

# Block 28
trans[28] = {
    0: "Đó là vì logic gọi ",
    1: "Agent của Openclaw",
    2: " như thế này:"
}

# Block 29
trans[29] = {
    0: "Bạn: ",
    1: "Tôm Hùm Lớn, tôi muốn một game Rắn Săn Mồi"
}

# Block 30
trans[30] = {
    0: "Tôm Hùm Lớn: ",
    1: "OK sếp, tôi sắp xếp ngay!"
}

# Block 31
trans[31] = {
    0: "Tôm Hùm Lớn: ",
    1: "Claude, đi viết game Rắn Săn Mồi giúp tôi."
}

# Block 32
trans[32] = {
    0: "Claude: ",
    1: "OK.",
    2: " (Bắt đầu viết)"
}

# Block 33
trans[33] = {
    0: "Tôm Hùm Lớn (polling sau 5 giây): ",
    1: "Viết xong chưa?",
    2: " (Tiêu hao Token)"
}

# Block 34
trans[34] = {
    0: "Tôm Hùm Lớn (polling sau 10 giây): ",
    1: "Viết xong chưa?",
    2: " (Tiêu hao Token)"
}

# Block 35 - "..." keep as is

# Block 36
trans[36] = {0: "(Lược bỏ N lần 5 giây)"}

# Block 37 - "..." keep as is

# Block 38
trans[38] = {
    0: "Tôm Hùm Lớn (polling sau 30 phút): ",
    1: "Viết xong chưa?",
    2: " (Tiêu hao Token)"
}

# Block 39
trans[39] = {0: "Giống như bạn đứng trong bếp cứ 5 giây nhìn lò nướng một lần -- lãng phí thời gian và công sức."}

# Block 40
trans[40] = {0: "Hướng dẫn này dạy bạn cách dùng Cursor để \"phẫu thuật\" Tôm Hùm Lớn, đừng để nó trở thành cái lãnh đạo phiền phức cứ giục giục giục, phiền chết đi, làm xong rồi tôi nói bạn không được sao!"}

# Block 41
trans[41] = {0: "Được, trong tương tác của agent, chúng ta có thể thực hiện hiệu ứng này thông qua hooks."}

# Block 42 - heading2
trans[42] = {0: "Hooks là gì? Tại sao nó là \"thuốc giải\" duy nhất?"}

# Block 43
trans[43] = {
    0: "Trước khi bắt đầu \"phẫu thuật\", chúng ta cần nói về nhân vật chính hôm nay -- ",
    1: "Hooks (móc)",
    2: "."
}

# Block 44
trans[44] = {0: "Hãy tưởng tượng bạn đi quán trà sữa đặt món."}

# Block 45 - bullet
trans[45] = {
    0: "Polling (Vòng lặp hỏi)",
    1: ": Bạn đặt món xong, đứng trước quầy không đi, cứ 3 giây hỏi nhân viên một lần: \"Xong chưa?\" \"Xong chưa?\" \"Xong chưa?\""
}

# Block 46 - bullet
trans[46] = {
    0: "Hậu quả",
    1: ": Nhân viên phiền chết (API áp lực lớn), bạn cũng mệt chết (không thể đi shopping), và nếu hỏi một lần lại tính phí (Token), cốc trà sữa của bạn có thể tốn vài nghìn đồng."
}

# Block 47 - bullet
trans[47] = {
    0: "Hook (Móc)",
    1: ": Bạn đặt món xong, lấy một cái ",
    2: "máy báo nhận món",
    3: " (đây chính là Hook), rồi quay sang cửa hàng bên cạnh mua giày, xem phim."
}

# Block 48 - bullet
trans[48] = {
    0: "Hậu quả",
    1: ": Ngay khi trà sữa làm xong, máy báo \"tít tít\" kêu (callback kích hoạt), bạn qua lấy."
}

# Block 49 - bullet
trans[49] = {
    0: "Ưu điểm",
    1: ": Trong 30 phút chờ đợi, bạn được tự do, và miễn phí."
}

# Block 50
trans[50] = {
    0: "Trong thế giới của OpenClaw, ",
    1: "Hooks chính là cái \"máy báo nhận món\" đó",
    2: ". Nó cho phép chúng ta sau khi Claude Code đã giao nhiệm vụ thì không cần quan tâm nữa, chờ đến thời khắc nhiệm vụ hoàn thành, ",
    3: "từ tầng hệ thống đá ngược một cú vào OpenClaw",
    4: ", nói với nó: ",
    5: "\"Tỉnh dậy, việc xong rồi.\""
}

# Block 51 - heading2
trans[51] = {0: "OpenClaw + Claude Code Hooks - Phẫu thuật Zero-Polling"}

# Block 52 - heading3
trans[52] = {0: "Bước 0: Dùng Cursor mở thư mục OpenClaw của bạn"}

# Block 53
trans[53] = {0: "File cấu hình của OpenClaw nằm trong một thư mục ẩn. Nhiều người không tìm thấy nó vì macOS mặc định không hiển thị thư mục bắt đầu bằng `.`."}

# Block 54
trans[54] = {0: "Cách 1: Mở trực tiếp từ Terminal"}

# Block 55
trans[55] = {0: "Mở Terminal, nhập:"}

# Block 56
trans[56] = {0: "Cách 2: Tìm thủ công bằng Finder"}

# Block 57
trans[57] = {0: "1. Mở Finder"}

# Block 58
trans[58] = {0: "2. Nhấn `Cmd + Shift + G` (Đi tới thư mục)"}

# Block 59
trans[59] = {0: "3. Nhập `~/.openclaw` và nhấn Enter"}

# Block 60
trans[60] = {0: "4. Kéo thư mục này vào icon Cursor để mở"}

# Block 61
trans[61] = {0: "Cách 3: Mở trực tiếp trong Cursor"}

# Block 62
trans[62] = {0: "1. Mở Cursor"}

# Block 63
trans[63] = {0: "2. `Cmd + O` (Mở thư mục)"}

# Block 64
trans[64] = {0: "3. Nhấn `Cmd + Shift + .` (Hiển thị file ẩn)"}

# Block 65
trans[65] = {0: "4. Tìm thư mục `.openclaw` trong thư mục user của bạn, mở ra"}

# Block 66
trans[66] = {0: "Sau khi mở bạn sẽ thấy cấu trúc thư mục như thế này:"}

# Block 67 - heading3
trans[67] = {0: "Bước 1: Tải file script"}

# Block 68
trans[68] = {0: "Tôi đã đóng gói tất cả script lên GitHub Gist, bạn chỉ cần chạy 3 lệnh trong terminal:"}

# Block 69
trans[69] = {0: "Địa chỉ Gist đầy đủ: https://gist.github.com/alextangson/7f42bf0a078b4266f098a4ad61732ae3"}

# Block 70
trans[70] = {0: "Logic cốt lõi của hai script lần lượt là:"}

# Block 71
trans[71] = {1: " -- Giao việc đi:"}

# Block 72
trans[72] = {1: " -- Việc xong rồi thông báo:"}

# Block 73
trans[73] = {0: "Muốn xem code đầy đủ? Trực tiếp mở link Gist, hoặc mở file đã tải trong Cursor."}

# Block 74 - heading3
trans[74] = {0: "Bước 2: Cấu hình Hook của Claude Code (Bước quan trọng nhất!)"}

# Block 75
trans[75] = {
    0: "Script đã tải xong, nhưng làm sao Claude Code biết sau khi làm xong phải gọi ",
    2: "?"
}

# Block 76
trans[76] = {
    0: "Câu trả lời là: ",
    1: "Đăng ký Hook trong file cấu hình của Claude Code."
}

# Block 77
trans[77] = {0: "Cũng tải template cấu hình từ Gist:"}

# Block 78
trans[78] = {0: "Bạn sẽ thấy JSON như thế này:"}

# Block 79
trans[79] = {0: "Bây giờ cần thao tác thủ công:"}

# Block 80 - ordered
trans[80] = {
    0: "Dùng Cursor mở ",
    2: " (nếu chưa có thì tạo mới)"
}

# Block 81 - ordered
trans[81] = {
    0: "Sao chép phần ",
    2: " của ",
    4: " từ Gist vào"
}

# Block 82 - ordered
trans[82] = {
    0: "Thay ",
    2: " trong đường dẫn bằng đường dẫn thực tế của bạn",
    3: " (nhập ",
    5: " trong terminal để xem)"
}

# Block 83
trans[83] = {
    0: "⚠️ Bước này không thể tự động hóa, vì tên người dùng mỗi người khác nhau, và bạn có thể đã có nội dung ",
    2: " cần hợp nhất."
}

# Block 84
trans[84] = {0: "Đây đăng ký hai sự kiện Hook:"}

# Block 85 - bullet
trans[85] = {1: ": Kích hoạt khi Claude Code hoàn thành nhiệm vụ bình thường"}

# Block 86 - bullet
trans[86] = {1: ": Kích hoạt khi phiên Claude Code kết thúc (dự phòng)"}

# Block 87
trans[87] = {0: "Cả hai đều trỏ đến cùng một script callback, bên trong script có cơ chế chống lặp, không lo kích hoạt hai lần."}

# Block 88 - heading3
trans[88] = {0: "Bước 3: Dạy Tôm Hùm Lớn cách dùng kỹ năng mới"}

# Block 89
trans[89] = {0: "Script và Hook đã cấu hình xong, nhưng Tôm Hùm Lớn chưa biết mình có kỹ năng mới. Chúng ta cần nói cho nó."}

# Block 90
trans[90] = {
    0: "Trong Cursor, tại ",
    2: " tạo thư mục ",
    4: ", rồi tạo ",
    6: " bên trong:"
}

# Block 91
trans[91] = {0: "Nội dung (dạy Tôm Hùm Lớn cách dùng kỹ năng này):"}

# Block 92 - heading3
trans[92] = {0: "Bước 4: Kiểm tra!"}

# Block 93
trans[93] = {0: "Mọi cấu hình đã hoàn tất. Bây giờ kiểm tra toàn bộ luồng."}

# Block 94
trans[94] = {0: "Chạy trong terminal:"}

# Block 95
trans[95] = {0: "Bạn sẽ thấy:"}

# Block 96
trans[96] = {0: "Sau đó chờ Claude Code hoàn thành (thường vài chục giây đến vài phút), kiểm tra kết quả:"}

# Block 97
trans[97] = {
    0: "Nếu thấy ",
    2: ", chúc mừng bạn, phẫu thuật thành công!"
}

# Block 98 - heading2
trans[98] = {0: "📊 So sánh hiệu quả"}

# Block 99
trans[99] = {0: "Chỉ số"}

# Block 100
trans[100] = {0: "Trước cải tiến (Polling)"}

# Block 101
trans[101] = {0: "Sau cải tiến (Hooks)"}

# Block 102
trans[102] = {0: "Token tiêu hao mỗi nhiệm vụ"}

# Block 103 - keep "5,000 - 50,000+"

# Block 104
trans[104] = {0: "~700 (cố định)"}

# Block 105
trans[105] = {0: "Trong lúc chờ, bạn có thể làm việc khác không"}

# Block 106
trans[106] = {0: "Không, Tôm Hùm Lớn bị chiếm dụng"}

# Block 107
trans[107] = {0: "Có, Tôm Hùm Lớn hoàn toàn rảnh"}

# Block 108
trans[108] = {0: "Chi phí nhiệm vụ mất 30 phút"}

# Block 109
trans[109] = {0: "Có thể $5-10"}

# Block 110 - keep "$0.01"

# Block 111
trans[111] = {0: "Thất bại có tự động thông báo được không"}

# Block 112
trans[112] = {0: "Không"}

# Block 113
trans[113] = {0: "Có (Hook dự phòng)"}

# Block 114 - heading2
trans[114] = {0: "🧠 Tóm tắt nguyên lý"}

# Block 115
trans[115] = {0: "Cốt lõi chỉ 3 file:"}

# Block 116 - ordered
trans[116] = {1: " -- Script phân phối (giao việc đi)"}

# Block 117 - ordered
trans[117] = {1: " -- Script callback (việc xong thông báo)"}

# Block 118 - ordered
trans[118] = {1: " -- Đăng ký Hook (nói cho Claude Code biết xong việc phải báo ai)"}

# Block 119 - heading2
trans[119] = {0: "🔜 Xem trước tập tiếp theo"}

# Block 120
trans[120] = {
    0: "Tập 3 chúng ta sẽ mở rộng chế độ zero-polling này sang ",
    2: " (Code Agent của OpenAI), và xây dựng một ",
    3: "hệ thống kiểm toán tự động dựa trên sự kiện Git",
    4: ": Bạn viết code trên MacBook và push lên GitHub, Agent Team trên Mac Mini tự động kiểm toán code của bạn và tạo PR."
}

# Block 121
trans[121] = {0: "Từ tác chiến đơn độc, đến Agent Team phối hợp -- đây mới là hướng đi thực sự của con tàu OpenClaw."}

# Block 122
trans[122] = {0: "Lưu ý: Tất cả script trong hướng dẫn này đều có thể copy-paste trực tiếp sử dụng, không cần kiến thức lập trình. Nếu gặp vấn đề, nhiều khả năng là đường dẫn chưa sửa đúng -- kiểm tra xem `$HOME` và đường dẫn trong script có khớp không."}

# Block 123
trans[123] = {0: "Liên hệ Lộc Đạo vui lòng thêm: "}

# ─── Apply translations ───
result = copy.deepcopy(data)

translated_count = 0
kept_count = 0

for block_idx, block in enumerate(result['blocks']):
    if block_idx in trans:
        for el_idx, el in enumerate(block['elements']):
            if el['type'] == 'text_run' and el_idx in trans[block_idx]:
                el['content'] = trans[block_idx][el_idx]
                translated_count += 1
            elif el['type'] == 'text_run':
                kept_count += 1
    else:
        for el in block['elements']:
            if el['type'] == 'text_run':
                kept_count += 1

# Add spaces between adjacent Vietnamese text_runs where needed
for block in result['blocks']:
    elements = block['elements']
    for i in range(len(elements) - 1):
        el = elements[i]
        next_el = elements[i + 1]
        if el['type'] == 'text_run' and next_el['type'] == 'text_run':
            curr = el['content']
            nxt = next_el['content']
            if curr and nxt:
                if not curr[-1] in ' \t\n:,;.!?\"\'\u2018\u2019\u201c\u201d()[]{}' and not nxt[0] in ' \t\n:,;.!?\"\'\u2018\u2019\u201c\u201d()[]{}':
                    curr_style = el.get('style', {})
                    next_style = next_el.get('style', {})
                    curr_is_code = curr_style.get('inline_code', False)
                    next_is_code = next_style.get('inline_code', False)
                    if not curr_is_code and not next_is_code:
                        el['content'] = curr + ' '

# Save
with open('_art_b6_1_trans.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"Translated: {translated_count} text_run elements")
print(f"Kept original: {kept_count} text_run elements")
print(f"Total blocks: {len(result['blocks'])}")
print(f"Saved to _art_b6_1_trans.json")
