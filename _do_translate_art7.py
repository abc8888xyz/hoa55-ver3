import json, sys, re, copy
sys.stdout.reconfigure(encoding='utf-8')

with open("C:/Users/ADMIN/hoa55_ ver3/_art7_orig.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Build a mapping from original content to translations
# We'll iterate block by block and element by element to ensure exact matching
def translate_content(content):
    """Translate Chinese content to Vietnamese"""
    cn_pattern = re.compile(r'[\u4e00-\u9fff]')
    if not cn_pattern.search(content):
        return content  # No Chinese, return as-is

    # Direct mapping table
    mapping = [
        # Title
        ('\u622a\u81f33.25\uff5c\u603b\u4ef7\u503c50\u4e07\u5956\u52b1\uff0c\u5bfb\u627e\u884c\u4e1a\u7ea7\u201c\u9f99\u867e\u201d\uff01',
         'H\u1ea1n ch\u00f3t 25/3 | T\u1ed5ng gi\u1ea3i th\u01b0\u1edfng tr\u1ecb gi\u00e1 500.000 NDT, t\u00ecm ki\u1ebfm "T\u00f4m h\u00f9m" c\u1ea5p ng\u00e0nh!'),
    ]
    for cn, vi in mapping:
        if content == cn:
            return vi
    return content

# Instead of character-level mapping, let's use a comprehensive approach
# Build translations by reading every text_run and providing Vietnamese version

translations_by_block = {}

# Block 0: Title
translations_by_block[0] = {0: 'H\u1ea1n ch\u00f3t 25/3 | T\u1ed5ng gi\u1ea3i th\u01b0\u1edfng tr\u1ecb gi\u00e1 500.000 NDT, t\u00ecm ki\u1ebfm "T\u00f4m h\u00f9m" c\u1ea5p ng\u00e0nh!'}

# Block 1: quote link
translations_by_block[1] = {0: '\U0001f517 Link b\u00e0i g\u1ed1c: '}

# Block 2: author info
translations_by_block[2] = {0: 'B\u00e0i g\u1ed1c: Linh Ti\u1ec3u H\u1ea1ch - Linh H\u1ea1ch S\u1ed1 Tr\u00ed', 1: '16/03/2026 17:32  Chi\u1ebft Giang'}

# Block 3: paragraph
translations_by_block[3] = {0: 'Trong n\u0103m qua, c\u00e1c nh\u00e0 ph\u00e1t tri\u1ec3n to\u00e0n c\u1ea7u \u0111ang \u0111i\u00ean cu\u1ed3ng kh\u00e1m ph\u00e1 c\u00e1c kh\u1ea3 n\u0103ng c\u1ee7a Agent: nghi\u00ean c\u1ee9u t\u1ef1 \u0111\u1ed9ng, giao d\u1ecbch t\u1ef1 \u0111\u1ed9ng, v\u1eadn h\u00e0nh t\u1ef1 \u0111\u1ed9ng, ch\u0103m s\u00f3c kh\u00e1ch h\u00e0ng t\u1ef1 \u0111\u1ed9ng, ph\u00e1t tri\u1ec3n t\u1ef1 \u0111\u1ed9ng, ra quy\u1ebft \u0111\u1ecbnh t\u1ef1 \u0111\u1ed9ng... nh\u01b0ng c\u00e1c Agent th\u1ef1c s\u1ef1 c\u00f3 th\u1ec3 \u1ee9ng d\u1ee5ng v\u00e0o ng\u00e0nh v\u1eabn r\u1ea5t \u00edt. Ph\u1ea7n l\u1edbn Agent v\u1eabn d\u1eebng l\u1ea1i \u1edf giai \u0111o\u1ea1n chatbot ho\u1eb7c \u1ee9ng d\u1ee5ng gi\u1ea3i tr\u00ed.'}

# Block 4
translations_by_block[4] = {0: 'L\u00e0n s\u00f3ng kh\u1edfi nghi\u1ec7p AI ti\u1ebfp theo s\u1ebd sinh ra m\u1ed9t h\u00ecnh th\u00e1i s\u1ea3n ph\u1ea9m ho\u00e0n to\u00e0n m\u1edbi: Agent c\u1ea5p ng\u00e0nh. Ch\u00fang s\u1ebd \u0111i s\u00e2u v\u00e0o y t\u1ebf, t\u00e0i ch\u00ednh, s\u1ea3n xu\u1ea5t, gi\u00e1o d\u1ee5c, ph\u00e1p lu\u1eadt, d\u1ecbch v\u1ee5 doanh nghi\u1ec7p v\u00e0 nhi\u1ec1u k\u1ecbch b\u1ea3n th\u1ef1c t\u1ebf kh\u00e1c, tr\u1edf th\u00e0nh c\u00e1c t\u00e1c t\u1eed th\u00f4ng minh c\u00f3 kh\u1ea3 n\u0103ng gi\u1ea3i quy\u1ebft v\u1ea5n \u0111\u1ec1 th\u1ef1c, t\u1ea1o ra gi\u00e1 tr\u1ecb th\u1ef1c, mang l\u1ea1i c\u01a1 h\u1ed9i kinh doanh th\u1ef1c, chuy\u1ec3n t\u1eeb "\u1ee9ng d\u1ee5ng \u0111\u1ed3 ch\u01a1i" th\u00e0nh c\u00f4ng c\u1ee5 n\u0103ng su\u1ea5t c\u1ea5p c\u00f4ng nghi\u1ec7p th\u1ef1c s\u1ef1.'}

# Block 5
translations_by_block[5] = {
    0: 'V\u00ec v\u1eady, Linh H\u1ea1ch S\u1ed1 Tr\u00ed ph\u1ed1i h\u1ee3p c\u00f9ng ',
    1: 'Thi\u00ean T\u1ebf Khoa K\u1ef9 \u0110\u1ea7u T\u01b0, Vi Li\u00ean, Phi Ph\u00e0m S\u1ea3n Nghi\u00ean ',
    2: ', Qianwen v\u00e0 c\u00e1c doanh nghi\u1ec7p, t\u1ed5 ch\u1ee9c kh\u00e1c ph\u00e1t \u0111\u1ed9ng s\u1ef1 ki\u1ec7n l\u1edbn n\u00e0y \u2014\u2014 ',
    3: 'AI Hackathon T\u00f4m H\u00f9m \u00b7 Cu\u1ed9c thi B\u00ecnh ch\u1ecdn Agent c\u1ea5p ng\u00e0nh ',
    4: ', hy v\u1ecdng t\u00ecm ra: th\u1ebf h\u1ec7 Agent ti\u1ebfp theo thay \u0111\u1ed5i t\u01b0\u01a1ng lai ng\u00e0nh.'
}

# Block 6
translations_by_block[6] = {0: 'Cu\u1ed9c thi l\u1ea7n n\u00e0y h\u01b0\u1edbng t\u1edbi c\u00e1c nh\u00e0 ph\u00e1t tri\u1ec3n to\u00e0n c\u1ea7u v\u00e0 \u0111\u1ed9i ng\u0169 kh\u1edfi nghi\u1ec7p AI \u0111\u1ec3 tuy\u1ec3n ch\u1ecdn d\u1ef1 \u00e1n. N\u1ebfu b\u1ea1n \u0111ang ph\u00e1t tri\u1ec3n Agent, n\u1ebfu b\u1ea1n c\u00f3 m\u1ed9t \u00fd t\u01b0\u1edfng \u0111i\u00ean r\u1ed3 nh\u01b0ng kh\u1ea3 thi, n\u1ebfu b\u1ea1n \u0111ang t\u00ecm ki\u1ebfm c\u01a1 h\u1ed9i kh\u1edfi nghi\u1ec7p... h\u00e3y tham gia s\u1ef1 ki\u1ec7n d\u00e0nh cho nh\u1eefng nh\u00e0 s\u00e1ng t\u1ea1o Agent c\u1ea5p ng\u00e0nh! H\u00e3y tr\u1edf th\u00e0nh ng\u01b0\u1eddi \u0111\u1ecbnh ngh\u0129a ng\u00e0nh ti\u1ebfp theo!'}

# Block 7
translations_by_block[7] = {0: 'Agent c\u1ea5p ng\u00e0nh l\u00e0 g\u00ec?'}

# Block 8
translations_by_block[8] = {0: 'V\u00ed d\u1ee5 \u0111\u01a1n gi\u1ea3n:'}

# Block 9
translations_by_block[9] = {0: 'N\u1ebfu ai \u0111\u00f3 t\u1ea1o ra m\u1ed9t "tr\u1ee3 l\u00fd qu\u1ea3n l\u00fd th\u1eddi gian h\u00ecnh t\u00f4m h\u00f9m", \u0111\u00f3 ch\u1ec9 l\u00e0 m\u1ed9t \u1ee9ng d\u1ee5ng AI th\u00fa v\u1ecb.'}

# Block 10
translations_by_block[10] = {0: 'Nh\u01b0ng n\u1ebfu tr\u00ean c\u01a1 s\u1edf \u0111\u00f3 n\u00e2ng c\u1ea5p th\u00e0nh:'}

# Block 11-13: bullets
translations_by_block[11] = {0: 'Tr\u1ee3 l\u00fd qu\u1ea3n l\u00fd s\u1ee9c kh\u1ecfe AI h\u01b0\u1edbng t\u1edbi ng\u00e0nh y t\u1ebf'}
translations_by_block[12] = {0: 'Agent qu\u1ea3n l\u00fd s\u1ee9c kh\u1ecfe nh\u00e2n vi\u00ean h\u01b0\u1edbng t\u1edbi doanh nghi\u1ec7p'}
translations_by_block[13] = {0: 'Agent theo d\u00f5i b\u1ec7nh nh\u00e2n h\u01b0\u1edbng t\u1edbi c\u01a1 s\u1edf y t\u1ebf'}

# Block 14
translations_by_block[14] = {0: 'Khi \u0111\u00f3, n\u00f3 chuy\u1ec3n t\u1eeb m\u1ed9t c\u00f4ng c\u1ee5 gi\u1ea3i tr\u00ed th\u00e0nh: m\u1ed9t Agent th\u1ef1c s\u1ef1 c\u00f3 th\u1ec3 \u0111i v\u00e0o ng\u00e0nh, t\u1ea1o ra gi\u00e1 tr\u1ecb th\u01b0\u01a1ng m\u1ea1i.'}

# Block 15
translations_by_block[15] = {0: 'Lo\u1ea1i s\u1ea3n ph\u1ea9m c\u00f3 th\u1ec3 ph\u1ee5c v\u1ee5 ng\u00e0nh, gi\u1ea3i quy\u1ebft v\u1ea5n \u0111\u1ec1 th\u1ef1c t\u1ebf, c\u00f3 ti\u1ec1m n\u0103ng th\u01b0\u01a1ng m\u1ea1i h\u00f3a \u2014 \u0111\u00f3 ch\u00ednh l\u00e0 Agent c\u1ea5p ng\u00e0nh m\u00e0 ch\u00fang t\u00f4i \u0111ang t\u00ecm ki\u1ebfm.'}

# Block 16
translations_by_block[16] = {0: 'Ai c\u00f3 th\u1ec3 tham gia?'}

# Block 17
translations_by_block[17] = {0: 'D\u00f9 l\u00e0 nh\u00e0 ph\u00e1t tri\u1ec3n c\u00e1 nh\u00e2n, \u0111\u1ed9i nh\u1ecf 2-5 ng\u01b0\u1eddi, hay d\u1ef1 \u00e1n AI \u0111ang kh\u1edfi nghi\u1ec7p, \u0111\u1ec1u c\u00f3 th\u1ec3 tham gia. Ch\u1ec9 c\u1ea7n b\u1ea1n \u0111ang l\u00e0m AI Agent, b\u1ea1n c\u00f3 th\u1ec3 \u0111\u0103ng k\u00fd.'}

# Block 18
translations_by_block[18] = {0: 'Ch\u00fang t\u00f4i ch\u00e0o \u0111\u00f3n:'}

# Block 19
translations_by_block[19] = {0: 'Nh\u00e0 ph\u00e1t tri\u1ec3n AI Agent ', 1: ', bao g\u1ed3m: nh\u00e0 ph\u00e1t tri\u1ec3n \u0111\u1ed9c l\u1eadp, geek c\u00f4ng ngh\u1ec7, ng\u01b0\u1eddi y\u00eau th\u00edch AI.'}

# Block 20
translations_by_block[20] = {0: '\u0110\u1ed9i ng\u0169 \u0111\u1ed5i m\u1edbi s\u00e1ng t\u1ea1o AI ', 1: ', bao g\u1ed3m: \u0111\u1ed9i kh\u1edfi nghi\u1ec7p AI, \u0111\u1ed9i k\u1ef9 thu\u1eadt, d\u1ef1 \u00e1n ph\u00f2ng th\u00ed nghi\u1ec7m.'}

# Block 21
translations_by_block[21] = {0: 'D\u1ef1 \u00e1n s\u1ea3n ph\u1ea9m Agent ', 1: ', bao g\u1ed3m: s\u1ea3n ph\u1ea9m \u0111\u00e3 ra m\u1eaft, d\u1ef1 \u00e1n Demo, s\u1ea3n ph\u1ea9m th\u1eed nghi\u1ec7m.'}

# Block 22
translations_by_block[22] = {0: 'C\u00f3 nh\u1eefng h\u1ea1ng m\u1ee5c thi n\u00e0o?'}

# Block 23
translations_by_block[23] = {0: 'S\u1ef1 ki\u1ec7n l\u1ea7n n\u00e0y t\u1eadp trung v\u00e0o c\u00e1c k\u1ecbch b\u1ea3n \u1ee9ng d\u1ee5ng th\u1ef1c t\u1ebf c\u1ee7a AI Agent c\u1ea5p ng\u00e0nh, h\u01b0\u1edbng tr\u1ecdng t\u00e2m v\u00e0o 4 h\u1ea1ng m\u1ee5c l\u1edbn: S\u1ea3n xu\u1ea5t th\u00f4ng minh, Logistics th\u00f4ng minh, Th\u01b0\u01a1ng m\u1ea1i \u0111i\u1ec7n t\u1eed s\u1ed1 tr\u00ed tu\u1ec7 v\u00e0 S\u1ee9c kh\u1ecfe sinh m\u1ec7nh.'}

# Block 24
translations_by_block[24] = {0: 'C\u00e1c l\u0129nh v\u1ef1c n\u00e0y \u0111ang \u1edf giai \u0111o\u1ea1n then ch\u1ed1t c\u1ee7a vi\u1ec7c n\u00e2ng c\u1ea5p s\u1ed1 h\u00f3a v\u00e0 tr\u00ed tu\u1ec7 h\u00f3a. Trong c\u00e1c kh\u00e2u nh\u01b0 qu\u1ea3n l\u00fd s\u1ea3n xu\u1ea5t, ph\u1ed1i h\u1ee3p chu\u1ed7i cung \u1ee9ng, v\u1eadn h\u00e0nh th\u01b0\u01a1ng m\u1ea1i \u0111i\u1ec7n t\u1eed v\u00e0 d\u1ecbch v\u1ee5 y t\u1ebf, nhu c\u1ea7u v\u1ec1 ra quy\u1ebft \u0111\u1ecbnh th\u00f4ng minh v\u00e0 h\u1ee3p t\u00e1c t\u1ef1 \u0111\u1ed9ng h\u00f3a kh\u00f4ng ng\u1eebng t\u0103ng. Ch\u00fang t\u00f4i hy v\u1ecdng ph\u00e1t hi\u1ec7n nh\u1eefng \u1ee9ng d\u1ee5ng AI Agent c\u1ea5p ng\u00e0nh th\u1ef1c s\u1ef1 c\u00f3 th\u1ec3 \u0111i v\u00e0o quy tr\u00ecnh c\u00f4ng nghi\u1ec7p, gi\u1ea3i quy\u1ebft v\u1ea5n \u0111\u1ec1 th\u1ef1c t\u1ebf v\u00e0 c\u00f3 ti\u1ec1m n\u0103ng th\u01b0\u01a1ng m\u1ea1i.'}

# Block 25
translations_by_block[25] = {0: 'H\u1ec7 th\u1ed1ng \u0111\u00e1nh gi\u00e1 cu\u1ed9c thi?'}

# Block 26
translations_by_block[26] = {0: '01', 1: 'T\u00ednh an to\u00e0n c\u1ee7a Agent l\u00e0 chi\u1ec1u \u0111\u00e1nh gi\u00e1 quan tr\u1ecdng'}

# Block 27
translations_by_block[27] = {0: 'Agent kh\u00f4ng ch\u1ec9 l\u00e0 m\u1ed9t c\u00f4ng c\u1ee5, n\u00f3 c\u00f3 th\u1ec3: g\u1ecdi h\u1ec7 th\u1ed1ng b\u00ean ngo\u00e0i, truy c\u1eadp d\u1eef li\u1ec7u, t\u1ef1 \u0111\u1ed9ng th\u1ef1c thi t\u00e1c v\u1ee5, \u1ea3nh h\u01b0\u1edfng \u0111\u1ebfn quy tr\u00ecnh kinh doanh th\u1ef1c t\u1ebf'}

# Block 28
translations_by_block[28] = {0: 'Do \u0111\u00f3, thi\u1ebft k\u1ebf an to\u00e0n l\u00e0 ti\u1ec1n \u0111\u1ec1 \u0111\u1ec3 Agent c\u00f3 th\u1ec3 \u0111i v\u00e0o ng\u00e0nh.'}

# Block 29
translations_by_block[29] = {0: 'Linh H\u1ea1ch S\u1ed1 Tr\u00ed khi \u0111\u00e1nh gi\u00e1 d\u1ef1 \u00e1n s\u1ebd \u0111\u1eb7c bi\u1ec7t ch\u00fa \u00fd:'}

# Blocks 30-34: bullets
translations_by_block[30] = {0: 'C\u00f3 tr\u00e1nh \u0111\u01b0\u1ee3c r\u1ee7i ro m\u00e3 \u0111\u1ed9c kh\u00f4ng'}
translations_by_block[31] = {0: 'C\u00f3 nh\u1eadn th\u1ee9c c\u01a1 b\u1ea3n v\u1ec1 b\u1ea3o m\u1eadt d\u1eef li\u1ec7u kh\u00f4ng'}
translations_by_block[32] = {0: 'C\u00f3 tr\u00e1nh \u0111\u01b0\u1ee3c r\u00f2 r\u1ec9 th\u00f4ng tin nh\u1ea1y c\u1ea3m kh\u00f4ng'}
translations_by_block[33] = {0: 'C\u00f3 ki\u1ec3m so\u00e1t quy\u1ec1n h\u1ec7 th\u1ed1ng h\u1ee3p l\u00fd kh\u00f4ng'}
translations_by_block[34] = {0: 'C\u00f3 tr\u00e1nh t\u1ea1o n\u1ed9i dung kh\u00f4ng ph\u00f9 h\u1ee3p ho\u1eb7c vi ph\u1ea1m kh\u00f4ng'}

# Block 35
translations_by_block[35] = {
    0: 'M\u1ed9t Agent th\u1ef1c s\u1ef1 c\u00f3 th\u1ec3 \u0111i v\u00e0o ng\u00e0nh kh\u00f4ng ch\u1ec9 c\u1ea7n th\u00f4ng minh, m\u00e0 c\u00f2n ph\u1ea3i an to\u00e0n, \u0111\u00e1ng tin c\u1eady, c\u00f3 th\u1ec3 ki\u1ec3m so\u00e1t. T\u1ea5t c\u1ea3 th\u00ed sinh vui l\u00f2ng t\u1ef1 ki\u1ec3m tra an to\u00e0n tr\u01b0\u1edbc khi n\u1ed9p d\u1ef1 \u00e1n. C\u00f3 th\u1ec3 tham kh\u1ea3o t\u00e0i li\u1ec7u g\u1ea7n \u0111\u00e2y do B\u1ed9 C\u00f4ng nghi\u1ec7p v\u00e0 C\u00f4ng ngh\u1ec7 Th\u00f4ng tin ph\u00e1t h\u00e0nh ',
    1: '\u300a6 \u0111i\u1ec1u n\u00ean v\u00e0 6 \u0111i\u1ec1u kh\u00f4ng n\u00ean khi s\u1eed d\u1ee5ng "T\u00f4m h\u00f9m"\u300b'
}

# Block 36
translations_by_block[36] = {0: '02', 1: 'Ti\u00eau chu\u1ea9n tham kh\u1ea3o ch\u1ea5m \u0111i\u1ec3m c\u1ee7a ban gi\u00e1m kh\u1ea3o'}

# Block 37
translations_by_block[37] = {0: 'Trong v\u00f2ng chung k\u1ebft, ban gi\u00e1m kh\u1ea3o s\u1ebd ch\u1ea5m \u0111i\u1ec3m theo 5 chi\u1ec1u sau:'}

# Block 38
translations_by_block[38] = {0: 'T\u00ednh an to\u00e0n: C\u00f3 thi\u1ebft k\u1ebf an to\u00e0n v\u00e0 tu\u00e2n th\u1ee7 c\u01a1 b\u1ea3n kh\u00f4ng'}

# Block 39
translations_by_block[39] = {0: 'M\u1ee9c \u0111\u1ed9 ho\u00e0n thi\u1ec7n: Ch\u1ee9c n\u0103ng c\u00f3 \u0111\u1ea7y \u0111\u1ee7 kh\u00f4ng, tr\u1ea3i nghi\u1ec7m ng\u01b0\u1eddi d\u00f9ng c\u00f3 m\u01b0\u1ee3t m\u00e0 kh\u00f4ng'}

# Block 40
translations_by_block[40] = {0: 'Gi\u00e1 tr\u1ecb \u1ee9ng d\u1ee5ng: C\u00f3 th\u1ef1c s\u1ef1 gi\u1ea3i quy\u1ebft v\u1ea5n \u0111\u1ec1 ng\u00e0nh kh\u00f4ng'}

# Block 41
translations_by_block[41] = {0: 'Ti\u1ec1m n\u0103ng th\u01b0\u01a1ng m\u1ea1i: C\u00f3 c\u01a1 h\u1ed9i c\u00f4ng nghi\u1ec7p h\u00f3a ho\u1eb7c th\u1ecb tr\u01b0\u1eddng kh\u00f4ng'}

# Block 42
translations_by_block[42] = {0: 'T\u00ednh \u0111\u1ed5i m\u1edbi: C\u00f4ng ngh\u1ec7 ho\u1eb7c m\u00f4 h\u00ecnh s\u1ea3n ph\u1ea9m c\u00f3 t\u00ednh \u0111\u1ed9t ph\u00e1 kh\u00f4ng'}

# Block 43
translations_by_block[43] = {0: 'Gi\u1ea3i th\u01b0\u1edfng tr\u1ecb gi\u00e1 ', 1: '500.000 NDT ', 2: '\u0111ang ch\u1edd b\u1ea1n nh\u1eadn!'}

# Block 44
translations_by_block[44] = {0: '01', 1: 'T\u1ed5ng gi\u1ea3i th\u01b0\u1edfng cu\u1ed9c thi l\u00ean t\u1edbi 140.000 NDT!'}

# Block 45
translations_by_block[45] = {0: 'Trong \u0111\u00f3:'}

# Block 46
translations_by_block[46] = {0: 'Gi\u1ea3i nh\u1ea5t 1 ng\u01b0\u1eddi \u2014 Th\u01b0\u1edfng 50.000 NDT'}

# Block 47
translations_by_block[47] = {0: 'Gi\u1ea3i nh\u00ec 2 ng\u01b0\u1eddi \u2014 Th\u01b0\u1edfng 30.000 NDT'}

# Block 48
translations_by_block[48] = {0: 'Gi\u1ea3i ba 3 ng\u01b0\u1eddi \u2014 Th\u01b0\u1edfng 10.000 NDT'}

# Block 49
translations_by_block[49] = {0: 'Gi\u1ea3i \u01afu t\u00fa nhi\u1ec1u su\u1ea5t, th\u01b0\u1edfng gi\u00e1 \u01b0u \u0111\u00e3i Token Qianwen, token mi\u1ec5n ph\u00ed n\u1ec1n t\u1ea3ng B\u00e1ch Luy\u1ec7n, d\u00f9ng th\u1eed mi\u1ec5n ph\u00ed server 1 th\u00e1ng! C\u00f2n r\u1ea5t nhi\u1ec1u ph\u00fac l\u1ee3i \u0111ang \u0111\u01b0\u1ee3c m\u1edf kh\u00f3a...'}

# Block 50
translations_by_block[50] = {0: '02', 1: 'Ch\u1ed7 ng\u1ed3i OPC, d\u1ecbch v\u1ee5 khoa h\u1ecdc s\u00e1ng t\u1ea1o v\u00e0 k\u1ebft n\u1ed1i ng\u00e0nh tr\u1ecdn g\u00f3i!'}

# Block 51
translations_by_block[51] = {0: 'C\u00e1c \u0111\u1ed9i \u0111o\u1ea1t gi\u1ea3i Nh\u1ea5t, Nh\u00ec, Ba s\u1ebd \u0111\u01b0\u1ee3c h\u01b0\u1edfng quy\u1ec1n l\u1ee3i nh\u1eadp tr\u00fa \u0111\u1ed9c quy\u1ec1n t\u1ea1i X\u01b0\u1edfng M\u01a1 B\u1eafc Cao Phong, H\u00e0ng Ch\u00e2u: cung c\u1ea5p mi\u1ec5n ph\u00ed ch\u1ed7 ng\u1ed3i v\u0103n ph\u00f2ng OPC s\u1eb5n s\u00e0ng s\u1eed d\u1ee5ng, m\u1edf kh\u00f3a ph\u00fac l\u1ee3i mi\u1ec5n ph\u00ed to\u00e0n b\u1ed9 ti\u1ec7n \u00edch c\u01a1 b\u1ea3n nh\u01b0 m\u1eb7t b\u1eb1ng, m\u1ea1ng, thi\u1ebft b\u1ecb v\u0103n ph\u00f2ng; d\u1ecbch v\u1ee5 khoa h\u1ecdc s\u00e1ng t\u1ea1o tr\u1ecdn g\u00f3i bao g\u1ed3m \u0111\u0103ng k\u00fd kinh doanh mi\u1ec5n ph\u00ed, k\u1ebft n\u1ed1i t\u00e0i nguy\u00ean chu\u1ed7i c\u00f4ng nghi\u1ec7p, k\u1ebft n\u1ed1i \u0111\u1ea7u t\u01b0 - t\u00e0i ch\u00ednh, h\u01b0\u1edbng d\u1eabn xin ch\u00ednh s\u00e1ch h\u1ed7 tr\u1ee3 to\u00e0n di\u1ec7n, gi\u00fap c\u00e1c d\u1ef1 \u00e1n AI Agent ch\u1ea5t l\u01b0\u1ee3ng nhanh ch\u00f3ng hi\u1ec7n th\u1ef1c h\u00f3a \u1ee9ng d\u1ee5ng c\u00f4ng ngh\u1ec7 v\u00e0 chuy\u1ec3n \u0111\u1ed5i th\u01b0\u01a1ng m\u1ea1i, \u0111\u1ec3 \u0111\u1ed9i kh\u1edfi nghi\u1ec7p nh\u1eb9 g\u00e1nh l\u00ean \u0111\u01b0\u1eddng, t\u0103ng t\u1ed1c ph\u00e1t tri\u1ec3n.'}

# Block 52
translations_by_block[52] = {0: '03', 1: 'Ngo\u00e0i ra, b\u1ea1n c\u00f2n c\u00f3 th\u1ec3:'}

# Block 53
translations_by_block[53] = {0: '\u0110\u1ed1i m\u1eb7t tr\u1ef1c ti\u1ebfp v\u1edbi c\u00e1c nh\u00e0 \u0111\u1ea7u t\u01b0 v\u00e0 doanh nh\u00e2n h\u00e0ng \u0111\u1ea7u, m\u1ea1nh d\u1ea1n tr\u00ecnh b\u00e0y \u00fd t\u01b0\u1edfng m\u1edbi, \u0111\u1ec3 nh\u1eefng ng\u01b0\u1eddi th\u1ef1c s\u1ef1 hi\u1ec3u AI l\u1eafng nghe \u00fd t\u01b0\u1edfng kh\u1edfi nghi\u1ec7p c\u1ee7a b\u1ea1n;'}

# Block 54
translations_by_block[54] = {0: 'K\u1ebft n\u1ed1i v\u1edbi \u0111\u1ed9i ng\u0169 d\u1ecbch v\u1ee5 c\u00f4ng nghi\u1ec7p m\u1ea1nh nh\u1ea5t H\u00e0ng Ch\u00e2u, bi\u1ebfn \u00fd t\u01b0\u1edfng th\u00e0nh d\u1ef1 \u00e1n, \u0111\u01b0a d\u1ef1 \u00e1n v\u00e0o ng\u00e0nh;'}

# Block 55
translations_by_block[55] = {0: 'Tham gia c\u1ed9ng \u0111\u1ed3ng nh\u00e0 ph\u00e1t tri\u1ec3n AI hot nh\u1ea5t hi\u1ec7n nay, giao l\u01b0u c\u00f9ng c\u00e1c cao th\u1ee7 c\u00f4ng ngh\u1ec7, nh\u00e0 kh\u1edfi nghi\u1ec7p, chuy\u00ean gia t\u00e0i nguy\u00ean, c\u00f9ng nhau ph\u00e1t tri\u1ec3n l\u1edbn m\u1ea1nh trong s\u1ef1 va ch\u1ea1m \u00fd t\u01b0\u1edfng.'}

# Block 56
translations_by_block[56] = {0: 'C\u00e1ch tham gia nh\u01b0 sau, nhanh ch\u00f3ng \u0111\u0103ng k\u00fd ngay!'}

# Block 57
translations_by_block[57] = {0: 'Th\u1eddi gian tuy\u1ec3n ch\u1ecdn d\u1ef1 \u00e1n'}

# Block 58
translations_by_block[58] = {0: 'T\u1eeb nay \u2014 25/03/2026 17:00'}

# Block 59
translations_by_block[59] = {0: 'N\u1ebfu b\u1ea1n \u0111\u00e3 c\u00f3 Demo d\u1ef1 \u00e1n Agent ho\u00e0n ch\u1ec9nh, h\u00e3y n\u1ed9p ngay qua m\u00e3 QR b\u00ean d\u01b0\u1edbi!'}

# Block 60
translations_by_block[60] = {0: '(C\u1ed5ng \u0111\u0103ng k\u00fd ho\u1ea1t \u0111\u1ed9ng ch\u00ednh th\u1ee9c v\u00e0 tuy\u1ec3n ch\u1ecdn d\u1ef1 \u00e1n)'}

# Block 61
translations_by_block[61] = {0: 'N\u1ebfu b\u1ea1n ch\u01b0a c\u00f3 Demo ho\u00e0n ch\u1ec9nh, c\u00f3 th\u1ec3 \u0111\u0103ng k\u00fd tr\u01b0\u1edbc qua m\u00e3 QR ph\u00eda tr\u00ean, sau \u0111\u00f3 tham gia nh\u00f3m trao \u0111\u1ed5i ho\u1ea1t \u0111\u1ed9ng \u0111\u1ec3 li\u00ean h\u1ec7 tr\u1ee3 l\u00fd s\u1ef1 ki\u1ec7n!'}

# Block 62
translations_by_block[62] = {0: '(Tham gia c\u1ed9ng \u0111\u1ed3ng trao \u0111\u1ed5i ho\u1ea1t \u0111\u1ed9ng ch\u00ednh th\u1ee9c tr\u00ean Feishu,'}

# Block 63
translations_by_block[63] = {0: 'theo d\u00f5i ti\u1ebfn tr\u00ecnh ho\u1ea1t \u0111\u1ed9ng, th\u00f4ng tin l\u1ecdt v\u00e0o v\u00f2ng trong v\u00e0 trao \u0111\u1ed5i h\u1ecdc h\u1ecfi)'}

# Block 64
translations_by_block[64] = {0: 'Th\u00f4ng tin n\u1ed9p d\u1ef1 \u00e1n'}

# Block 65
translations_by_block[65] = {0: 'Qu\u00e9t m\u00e3 QR \u0111\u0103ng k\u00fd ph\u00eda tr\u00ean \u0111\u1ec3 \u0111i\u1ec1n bi\u1ec3u m\u1eabu \u0111\u0103ng k\u00fd.'}

# Block 66
translations_by_block[66] = {0: 'Th\u00f4ng tin c\u1ea7n n\u1ed9p ch\u1ee7 y\u1ebfu bao g\u1ed3m:'}

# Block 67
translations_by_block[67] = {0: 'Th\u00f4ng tin c\u01a1 b\u1ea3n v\u00e0 gi\u1edbi thi\u1ec7u th\u00ed sinh/\u0111\u1ed9i thi'}

# Block 68
translations_by_block[68] = {0: 'T\u00ean d\u1ef1 \u00e1n v\u00e0 gi\u1edbi thi\u1ec7u t\u00f3m t\u1eaft d\u1ef1 \u00e1n'}

# Block 69
translations_by_block[69] = {0: '\u1ea2nh ch\u1ee5p m\u00e0n h\u00ecnh Demo d\u1ef1 \u00e1n ho\u1eb7c video tr\u00ecnh di\u1ec5n (L\u01b0u \u00fd: Demo c\u1ea7n l\u00e0 li\u00ean k\u1ebft c\u00f4ng khai c\u00f3 th\u1ec3 truy c\u1eadp, kh\u00f4ng \u0111\u01b0\u1ee3c ch\u1ee9a ch\u01b0\u01a1ng tr\u00ecnh \u0111\u1ed9c h\u1ea1i ho\u1eb7c n\u1ed9i dung vi ph\u1ea1m, n\u1ebfu kh\u00f4ng s\u1ebd b\u1ecb x\u00f3a th\u00f4ng tin \u0111\u0103ng k\u00fd, coi nh\u01b0 \u0111\u0103ng k\u00fd th\u1ea5t b\u1ea1i)'}

# Block 70
translations_by_block[70] = {0: 'L\u01b0u \u00fd: N\u1ebfu \u00fd t\u01b0\u1edfng c\u1ee7a b\u1ea1n ch\u01b0a th\u00e0nh Demo, h\u00e3y tranh th\u1ee7 th\u1eddi gian v\u00e0 v\u00e0o nh\u00f3m ho\u1ea1t \u0111\u1ed9ng li\u00ean h\u1ec7 tr\u1ee3 l\u00fd!'}

# Block 71
translations_by_block[71] = {0: 'Ban t\u1ed5 ch\u1ee9c ch\u00ednh th\u1ee9c s\u1ebd x\u00e9t duy\u1ec7t t\u1ea5t c\u1ea3 d\u1ef1 \u00e1n v\u00e0 \u0111\u01b0a v\u00e0o quy tr\u00ecnh b\u00ecnh ch\u1ecdn. N\u1ebfu d\u1ef1 \u00e1n c\u1ee7a b\u1ea1n l\u1ecdt v\u00e0o v\u00f2ng chung k\u1ebft offline, ch\u00fang t\u00f4i s\u1ebd li\u00ean h\u1ec7 b\u1ea1n tr\u01b0\u1edbc 3-5 ng\u00e0y. Vui l\u00f2ng \u0111i\u1ec1n s\u1ed1 \u0111i\u1ec7n tho\u1ea1i th\u1eadt v\u00e0 gi\u1eef \u0111i\u1ec7n tho\u1ea1i th\u00f4ng su\u1ed1t.'}

# Block 72
translations_by_block[72] = {0: 'Quy tr\u00ecnh b\u00ecnh ch\u1ecdn d\u1ef1 \u00e1n v\u00e0 v\u00f2ng chung k\u1ebft offline'}

# Block 73
translations_by_block[73] = {0: 'V\u00f2ng s\u01a1 tuy\u1ec3n d\u1ef1 \u00e1n tr\u1ef1c tuy\u1ebfn'}

# Block 74
translations_by_block[74] = {0: 'Th\u1eddi gian: 26/03/2026 \u2014 01/04/2026'}

# Block 75
translations_by_block[75] = {0: 'Ban \u0111\u00e1nh gi\u00e1 k\u1ef9 thu\u1eadt ch\u00ednh th\u1ee9c s\u1ebd s\u00e0ng l\u1ecdc 20 d\u1ef1 \u00e1n xu\u1ea5t s\u1eafc t\u1eeb t\u1ea5t c\u1ea3 d\u1ef1 \u00e1n \u0111\u1ec3 v\u00e0o v\u00f2ng chung k\u1ebft offline.'}

# Block 76
translations_by_block[76] = {0: 'Ti\u00eau chu\u1ea9n s\u00e0ng l\u1ecdc bao g\u1ed3m: an to\u00e0n v\u00e0 tu\u00e2n th\u1ee7, k\u1ecbch b\u1ea3n \u1ee9ng d\u1ee5ng c\u1ea5p ng\u00e0nh, \u0111\u1ed5i m\u1edbi c\u00f4ng ngh\u1ec7, ti\u1ec1m n\u0103ng th\u01b0\u01a1ng m\u1ea1i, m\u1ee9c \u0111\u1ed9 ho\u00e0n thi\u1ec7n th\u00f4ng tin \u0111\u0103ng k\u00fd, v.v.'}

# Block 77
translations_by_block[77] = {0: 'V\u00f2ng chung k\u1ebft tr\u00ecnh b\u00e0y offline'}

# Block 78
translations_by_block[78] = {0: 'Th\u1eddi gian: 02/04/2026 9:00\u201417:30'}

# Block 79
translations_by_block[79] = {0: '\u0110\u1ecba \u0111i\u1ec3m: T\u1ea7ng 24, T\u00f2a A, Qu\u1ea3ng tr\u01b0\u1eddng Th\u1eddi \u0111\u1ea1i Hoa Tinh, Qu\u1eadn T\u00e2y H\u1ed3, H\u00e0ng Ch\u00e2u, Trung Qu\u1ed1c (Ph\u00f2ng kh\u00e1ch Nh\u00e0 khoa h\u1ecdc B\u1eafc Cao Phong)'}

# Block 80
translations_by_block[80] = {0: '20 d\u1ef1 \u00e1n l\u1ecdt v\u00e0o v\u00f2ng trong s\u1ebd tr\u00ecnh di\u1ec5n Demo t\u1ea1i ch\u1ed7 (C\u00e1c b\u1ea1n mu\u1ed1n \u0111\u1ebfn xem thi tr\u1ef1c ti\u1ebfp h\u00e3y theo d\u00f5i b\u00e0i \u0111\u0103ng ti\u1ebfp theo tr\u00ean t\u00e0i kho\u1ea3n c\u00f4ng khai nh\u00e9! Ch\u00fang t\u00f4i s\u1ebd m\u1edf k\u00eanh \u0111\u0103ng k\u00fd cho kh\u00e1n gi\u1ea3).'}

# Block 81
translations_by_block[81] = {0: 'B\u1ea1n s\u1ebd \u0111\u1ed1i m\u1eb7t v\u1edbi ban gi\u00e1m kh\u1ea3o g\u1ed3m 5 v\u1ecb, bao g\u1ed3m: chuy\u00ean gia c\u00f4ng ngh\u1ec7 AI, doanh nh\u00e2n, nh\u00e0 \u0111\u1ea7u t\u01b0 h\u00e0ng \u0111\u1ea7u trong ng\u00e0nh'}

# Block 82
translations_by_block[82] = {0: 'M\u1ed7i \u0111\u1ed9i c\u1ea7n:'}

# Block 83
translations_by_block[83] = {0: 'Tr\u00ecnh di\u1ec5n Demo s\u1ea3n ph\u1ea9m t\u1ea1i ch\u1ed7 (th\u1eddi l\u01b0\u1ee3ng 10 ph\u00fat)'}

# Block 84
translations_by_block[84] = {0: 'Gi\u1edbi thi\u1ec7u logic v\u00e0 gi\u00e1 tr\u1ecb d\u1ef1 \u00e1n (th\u1eddi l\u01b0\u1ee3ng 5 ph\u00fat)'}

# Block 85
translations_by_block[85] = {0: 'Ban gi\u00e1m kh\u1ea3o s\u1ebd ch\u1ea5m \u0111i\u1ec3m theo quy t\u1eafc, cu\u1ed1i c\u00f9ng b\u00ecnh ch\u1ecdn ra: Gi\u1ea3i nh\u1ea5t 1, Gi\u1ea3i nh\u00ec 2, Gi\u1ea3i ba 3 v\u00e0 nhi\u1ec1u Gi\u1ea3i \u01afu t\u00fa.'}

# Block 86
translations_by_block[86] = {0: 'T\u1ea5t c\u1ea3 th\u00ed sinh chung k\u1ebft c\u00f3 m\u1eb7t t\u1ea1i hi\u1ec7n tr\u01b0\u1eddng c\u00f2n c\u00f3 c\u01a1 h\u1ed9i tham gia h\u1ed9i ngh\u1ecb k\u00edn do Linh H\u1ea1ch S\u1ed1 Tr\u00ed t\u1ed5 ch\u1ee9c sau \u0111\u00f3, g\u1eb7p m\u1eb7t tr\u1ef1c ti\u1ebfp nh\u00e0 \u0111\u1ea7u t\u01b0, t\u1ed5 ch\u1ee9c t\u00e0i ch\u00ednh, doanh nh\u00e2n, nh\u1eadn \u0111\u01b0\u1ee3c h\u1ed7 tr\u1ee3 \u0111\u1ea7u t\u01b0 m\u1ea1o hi\u1ec3m!'}

# Block 87
translations_by_block[87] = {0: '\u0110i\u1ec1u quan tr\u1ecdng nh\u1ea5t trong th\u1eddi \u0111\u1ea1i AI kh\u00f4ng ph\u1ea3i l\u00e0 m\u00f4 h\u00ecnh, m\u00e0 l\u00e0 ai c\u00f3 th\u1ec3 d\u00f9ng Agent t\u00e1i c\u1ea5u tr\u00fac ng\u00e0nh.'}

# Block 88
translations_by_block[88] = {0: 'N\u1ebfu b\u1ea1n \u0111ang ph\u00e1t tri\u1ec3n AI Agent, n\u1ebfu b\u1ea1n c\u00f3 \u00fd t\u01b0\u1edfng thay \u0111\u1ed5i ng\u00e0nh, n\u1ebfu b\u1ea1n \u0111ang t\u00ecm ki\u1ebfm c\u01a1 h\u1ed9i kh\u1edfi nghi\u1ec7p AI...'}

# Block 89
translations_by_block[89] = {0: 'H\u00e3y tham gia: AI Hackathon T\u00f4m H\u00f9m \u00b7 \u0110\u1ea1i h\u1ed9i B\u00ecnh ch\u1ecdn AI Agent c\u1ea5p ng\u00e0nh!'}

# Block 90
translations_by_block[90] = {0: 'B\u1ea1n, ch\u00ednh l\u00e0 ng\u01b0\u1eddi \u0111\u1ecbnh ngh\u0129a ng\u00e0nh ti\u1ebfp theo!'}

# Block 91
translations_by_block[91] = {0: '(C\u1ed5ng \u0111\u0103ng k\u00fd, qu\u00e9t m\u00e3 \u0111\u1ec3 \u0111i\u1ec1n Demo!)'}


# Apply translations
for block_idx, elem_map in translations_by_block.items():
    if block_idx < len(data["blocks"]):
        block = data["blocks"][block_idx]
        text_run_idx = 0
        for el in block["elements"]:
            if el["type"] == "text_run":
                if text_run_idx in elem_map:
                    el["content"] = elem_map[text_run_idx]
                text_run_idx += 1

# Update title
data["title"] = 'H\u1ea1n ch\u00f3t 25/3 | T\u1ed5ng gi\u1ea3i th\u01b0\u1edfng tr\u1ecb gi\u00e1 500.000 NDT, t\u00ecm ki\u1ebfm "T\u00f4m h\u00f9m" c\u1ea5p ng\u00e0nh!'

with open("C:/Users/ADMIN/hoa55_ ver3/_art7_trans.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Verify
cn_pattern = re.compile(r'[\u4e00-\u9fff]')
remaining = 0
for block in data["blocks"]:
    for el in block["elements"]:
        if el["type"] == "text_run" and cn_pattern.search(el["content"]):
            remaining += 1
            print(f'REMAINING: {el["content"][:60]}')

print(f"\nDone. Remaining Chinese blocks: {remaining}")
print(f"Total blocks: {len(data['blocks'])}")
