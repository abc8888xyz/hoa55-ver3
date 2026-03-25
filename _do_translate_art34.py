"""Translate art34 Chinese -> Vietnamese"""
import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

with open('_art34_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Translation map: block_index -> {element_index: translated_text}
trans = {
    0: {0: "Wise: Openclaw (Clawbot) + Kimi K 2.5 Tri\u1ec3n khai + H\u01b0\u1edbng d\u1eabn s\u1eed d\u1ee5ng Feishu: \u0110\u1ec3 AI ti\u1ebfp qu\u1ea3n m\u1ecdi th\u1ee9, ho\u1ea1t \u0111\u1ed9ng 24 gi\u1edd kh\u00f4ng ng\u1eebng"},
    1: {0: "C\u00e1c b\u1ea1n c\u0169ng c\u00f3 th\u1ec3 tri\u1ec3n khai th\u00f4ng qua Alibaba Cloud Bailian ", 2: " \u0111\u1ec3 tri\u1ec3n khai", 3: ": "},
    2: {0: "Mua l\u1ea7n \u0111\u1ea7u ch\u1ec9 t\u1eeb 7.9 t\u1ec7, gia h\u1ea1n gi\u1ea3m t\u1eeb 50%, h\u1ed7 tr\u1ee3 Qwen3.5, Qwen3-max, Qwen3-coder, GLM-5, GLM-4.7, Kimi-k2.5 v\u00e0 c\u00e1c m\u00f4 h\u00ecnh kh\u00e1c"},
    3: {0: "\U0001f449 Nh\u1ea5n link truy c\u1eadp tr\u1ef1c ti\u1ebfp: "},
    4: {0: "\U0001f449 Xem h\u01b0\u1edbng d\u1eabn tri\u1ec3n khai chi ti\u1ebft: "},
    5: {0: "Ch\u1ec9 c\u1ea7n t\u1ed1i \u0111a ba b\u01b0\u1edbc, b\u1ea1n \u0111\u00e3 c\u00f3 tr\u1ee3 l\u00fd AI tr\u1ef1c tuy\u1ebfn 7x24 gi\u1edd, ph\u1ea3n h\u1ed3i m\u1ecdi l\u00fac"},
    6: {0: "G\u1ea7n \u0111\u00e2y c\u00f3 r\u1ea5t nhi\u1ec1u b\u1ea1n h\u1ecfi t\u00f4i, t\u1ea1i sao l\u01b0\u1ee3ng Token ti\u00eau th\u1ee5 c\u1ee7a t\u00f4i l\u1edbn nh\u01b0 v\u1eady, th\u1ef1c ra c\u00e2u tr\u1ea3 l\u1eddi ch\u1ec9 c\u00f3 m\u1ed9t, t\u00f4i \u0111\u00e3 d\u00f9ng CLI l\u1eadp tr\u00ecnh thay th\u1ebf cho m\u1ecdi th\u1ee9."},
    7: {0: "D\u00f9 l\u00e0 nghi\u00ean c\u1ee9u, l\u1eadp k\u1ebf ho\u1ea1ch, l\u1eadp tr\u00ecnh, ph\u00e2n t\u00edch d\u1eef li\u1ec7u, t\u1ea1o h\u00ecnh \u1ea3nh hay s\u00e1ng t\u1ea1o, n\u00f3 kh\u00f4ng ch\u1ec9 l\u00e0 m\u1ed9t c\u00f4ng c\u1ee5 l\u1eadp tr\u00ecnh nh\u01b0 ch\u00fang ta t\u01b0\u1edfng t\u01b0\u1ee3ng."},
    8: {0: "H\u00f4m nay ch\u00fang ta s\u1ebd d\u00f9ng Clawbot - d\u1ef1 \u00e1n \u0111ang r\u1ea5t hot g\u1ea7n \u0111\u00e2y, s\u1eed d\u1ee5ng Kimi Code v\u00e0 Claude Code (GLM) m\u1edbi ra \u0111\u1ec3 ho\u00e0n th\u00e0nh to\u00e0n b\u1ed9 quy tr\u00ecnh t\u1eeb nghi\u00ean c\u1ee9u \u0111\u1ebfn tri\u1ec3n khai v\u00e0 \u1ee9ng d\u1ee5ng Clawbot."},
    9: {0: "N\u1ed9i dung d\u01b0\u1edbi \u0111\u00e2y, t\u00f4i s\u1ebd nghi\u00ean c\u1ee9u th\u00f4ng qua Code CLI, g\u1ecdi script \u0111\u1ec3 t\u1ea1o h\u00ecnh \u1ea3nh."},
    10: {0: "Part 1: ClawtBot l\u00e0 g\u00ec"},
    11: {0: "Ngu\u1ed3n h\u00ecnh \u1ea3nh: Kimi Code"},
    12: {0: "N\u00f3i ng\u1eafn g\u1ecdn: ", 1: "Moltbot l\u00e0 m\u1ed9t AI c\u00f3 th\u1ec3 ch\u1ea1y tr\u00ean server, l\u00e0 Agent th\u1ef1c s\u1ef1 l\u00e0m vi\u1ec7c \u0111\u01b0\u1ee3c, kh\u00f4ng ph\u1ea3i lo\u1ea1i ch\u1ec9 bi\u1ebft chat v\u00f4 d\u1ee5ng."},
    13: {0: "Ngu\u1ed3n h\u00ecnh \u1ea3nh: Kimi Code + Claude Code (GLM)"},
    14: {0: "N\u00f3 c\u00f3 th\u1ec3 ", 1: "\u0111i\u1ec1u khi\u1ec3n m\u00e1y t\u00ednh c\u1ee7a b\u1ea1n \u0111\u1ec3 sinh code, gi\u00fap b\u1ea1n s\u1eafp x\u1ebfp file, ho\u1eb7c l\u00e0m nh\u1eefng vi\u1ec7c nh\u01b0 t\u1ea1o h\u00ecnh \u1ea3nh, s\u00e1ng t\u1ea1o v\u00e0 h\u00e0ng lo\u1ea1t th\u1ee9 kh\u00e1c m\u00e0 t\u00f4i \u0111\u00e3 n\u00f3i \u1edf tr\u00ean."},
    15: {0: "\u0110\u1ea7u v\u00e0o c\u1ee7a n\u00f3 c\u00f3 th\u1ec3 l\u00e0 WhatsApp ho\u1eb7c Telegram, nh\u01b0ng \u0111i\u1ec1u khi\u1ec3n tr\u1ef1c ti\u1ebfp m\u00e1y t\u00ednh v\u1eabn kh\u00e1 kh\u00f4ng an to\u00e0n, n\u00ean tr\u01b0\u1edbc \u0111\u00e2y nhi\u1ec1u b\u1ea1n \u0111\u00e3 mua Mac Mini, d\u00f9ng m\u00e1y n\u00e0y \u0111\u1ec3 ch\u1ea1y Clawbot, tr\u00e1nh thao t\u00e1c tr\u00ean m\u00e1y t\u00ednh c\u00e1 nh\u00e2n."},
    16: {0: "Sau khi Tencent Cloud, Alibaba Cloud k\u1ebft n\u1ed1i v\u00e0o, th\u00ec th\u00f4ng qua server \u0111\u00e1m m\u00e2y nh\u1eb9, s\u1eed d\u1ee5ng DingTalk, WeCom l\u00e0m \u0111\u1ea7u v\u00e0o \u0111\u1ec3 thao t\u00e1c."},
    17: {0: "Ngu\u1ed3n h\u00ecnh \u1ea3nh: Kimi Code"},
    18: {0: "S\u1ef1 kh\u00e1c bi\u1ec7t v\u1edbi tr\u1ee3 l\u00fd l\u1eadp tr\u00ecnh l\u00e0 g\u00ec, t\u00f4i ngh\u0129 ", 1: "kh\u00e1c bi\u1ec7t l\u1edbn nh\u1ea5t l\u00e0 kh\u00f4ng c\u1ea7n m\u1edf c\u00f4ng c\u1ee5 l\u1eadp tr\u00ecnh \u0111\u1ec3 ho\u00e0n th\u00e0nh nhi\u1ec7m v\u1ee5 n\u1eefa."},
    19: {0: "Ngu\u1ed3n h\u00ecnh \u1ea3nh: Kimi Code"},
    20: {0: "C\u00e1ch tri\u1ec3n khai c\u1ee7a c\u00e1c nh\u00e0 cung c\u1ea5p \u0111\u00e1m m\u00e2y g\u1ea7n nh\u01b0 gi\u1ed1ng nhau, t\u1eeb k\u1ebft qu\u1ea3 nghi\u00ean c\u1ee9u AI, ng\u01b0\u1eddi d\u00f9ng m\u1edbi \u0111\u1ec1u c\u00f3 g\u00f3i gi\u1ea3m gi\u00e1 th\u1ea5p, kho\u1ea3ng 68 t\u1ec7/n\u0103m, ng\u01b0\u1eddi d\u00f9ng c\u0169 tr\u1ea3 theo th\u00e1ng kho\u1ea3ng 40 t\u1ec7/th\u00e1ng, n\u00ean ch\u1ecdn g\u00f3i th\u1ebb n\u0103m."},
    21: {0: "N\u1ebfu kh\u00f4ng th\u1ef1c s\u1ef1 c\u1ea7n th\u00ec \u0111\u1eebng mua, theo t\u1ed1c \u0111\u1ed9 ti\u1ebfn h\u00f3a c\u1ee7a AI, s\u1edbm th\u00f4i s\u1ebd c\u00f3 c\u00f4ng ty l\u1edbn ra m\u1ed9t Case t\u01b0\u01a1ng t\u1ef1 \u0111\u1ec3 ti\u1ebfp qu\u1ea3n m\u00e1y t\u00ednh c\u1ee7a b\u1ea1n."},
    22: {0: "Ngu\u1ed3n h\u00ecnh \u1ea3nh: Claude Code (GLM)"},
    23: {0: "iMessage ch\u1ec9 d\u00f9ng \u0111\u01b0\u1ee3c tr\u00ean Mac, nh\u01b0ng server th\u01b0\u1eddng l\u00e0 Linux, n\u00ean ch\u00fang ta l\u1ea1i ph\u1ea3i \u0111\u1ed5i c\u00e1ch t\u01b0\u01a1ng t\u00e1c, hi\u1ec7n t\u1ea1i ng\u01b0\u1eddi d\u00f9ng doanh nghi\u1ec7p c\u01a1 b\u1ea3n \u0111\u1ec1u c\u00f3 th\u1ec3 d\u00f9ng WeCom, DingTalk, ng\u01b0\u1eddi d\u00f9ng kh\u00f4ng ph\u1ea3i doanh nghi\u1ec7p c\u00f3 th\u1ec3 d\u00f9ng bot Feishu ho\u1eb7c truy c\u1eadp qua tr\u00ecnh duy\u1ec7t."},
    24: {0: "C\u00f3 developer \u0111\u00e3 l\u00e0m b\u1ed9 c\u1ea7u n\u1ed1i Feishu, kh\u00f4ng c\u1ea7n server, kh\u00f4ng c\u1ea7n t\u00ean mi\u1ec1n \u0111\u1ec1u c\u00f3 th\u1ec3 s\u1eed d\u1ee5ng, nh\u00ecn v\u1eady th\u00ec c\u00e1ch n\u00e0y l\u00e0 th\u00e2n thi\u1ec7n nh\u1ea5t."},
    25: {0: "Ngu\u1ed3n h\u00ecnh \u1ea3nh: Kimi Code"},
    26: {0: "Kh\u00e1 \u0111\u01a1n gi\u1ea3n v\u00e0 ti\u1ec7n l\u1ee3i, v\u1ec1 nguy\u00ean t\u1eafc d\u00f9ng nh\u00e0 cung c\u1ea5p \u0111\u00e1m m\u00e2y + IM doanh nghi\u1ec7p t\u01b0\u01a1ng \u1ee9ng l\u00e0 \u0111\u01b0\u1ee3c, kh\u00f4ng mu\u1ed1n mua server th\u00ec d\u00f9ng Feishu, n\u1ebfu mu\u1ed1n online 7*24 gi\u1edd, t\u1eaft m\u00e1y t\u00ednh v\u1eabn mu\u1ed1n ch\u1ea1y th\u00ec v\u1eabn ph\u1ea3i d\u00f9ng server."},
    27: {0: "OK, ph\u1ea7n tr\u01b0\u1edbc \u0111\u1ec1u l\u00e0 k\u1ebft qu\u1ea3 nghi\u00ean c\u1ee9u m\u00e0 hai \"th\u1ea7y AI\" \u0111\u00e3 cho t\u00f4i, b\u1ea1n n\u00e0o mu\u1ed1n xem to\u00e0n v\u0103n c\u00f3 th\u1ec3 nh\u1ea5n link b\u00ean d\u01b0\u1edbi."},
    28: {0: "Kimi Code & Claude Code (GLM) Th\u1ef1c h\u00e0nh thao t\u00e1c"},
    29: {0: "B\u00e2y gi\u1edd ch\u00fang ta th\u1eed tri\u1ec3n khai, ti\u1ebfp theo t\u00f4i s\u1ebd ch\u1ecdn Kimi Code \u0111\u1ec3 gi\u00fap t\u00f4i x\u1eed l\u00fd vi\u1ec7c n\u00e0y."},
    30: {0: "\u1ee8ng d\u1ee5ng nh\u1eb9 Clawbot + Th\u1ef1c h\u00e0nh Feishu"},
    31: {0: "Khi mua server, \u1edf \u0111\u00e2y Clawbot xu\u1ea5t hi\u1ec7n 2 c\u00e1i, th\u1ef1c ra t\u00f4i kh\u00f4ng bi\u1ebft c\u00f3 g\u00ec kh\u00e1c bi\u1ec7t, t\u00f4i ti\u1ebfp t\u1ee5c h\u1ecfi Kimi, n\u00f3 c\u00f3 kh\u1ea3 n\u0103ng hi\u1ec3u h\u00ecnh \u1ea3nh, t\u00f4i r\u1ea5t t\u00f2 m\u00f2 li\u1ec7u n\u00f3 c\u00f3 th\u1ec3 nh\u1eadn di\u1ec7n v\u1ecb tr\u00ed khung \u0111\u1ecf c\u1ee7a t\u00f4i kh\u00f4ng."},
    32: {0: "T\u00f4i \u0111\u00e3 l\u01b0u h\u00ecnh \u1ea3nh v\u1ec1 m\u00e1y, \u0111\u1ec3 n\u00f3 truy c\u1eadp."},
    33: {0: "R\u1ea5t nhanh n\u00f3 \u0111\u00e3 \u0111\u01b0a ra c\u00e2u tr\u1ea3 l\u1eddi cho t\u00f4i, n\u00f3 c\u00f3 th\u1ec3 nh\u1eadn di\u1ec7n ch\u00ednh x\u00e1c v\u1ecb tr\u00ed khung \u0111\u1ecf c\u1ee7a t\u00f4i, v\u1eady l\u00e0 t\u00f4i b\u1eaft \u0111\u1ea7u tri\u1ec3n khai ngay."},
    34: {0: "Mua xong c\u0169ng theo c\u00e1ch t\u01b0\u01a1ng t\u1ef1, h\u1ecfi Kimi, ti\u1ebfp theo ph\u1ea3i l\u00e0m g\u00ec."},
    35: {0: "Ti\u1ebfp theo t\u00f4i s\u1ebd l\u00e0m theo s\u1eafp x\u1ebfp c\u1ee7a n\u00f3, ho\u00e0n th\u00e0nh c\u00e1c thao t\u00e1c \u1edf tr\u00ean."},
    36: {0: "Sau m\u1ed9t lo\u1ea1t thao t\u00e1c, m\u1edf \u0111\u01b0\u1ee3c trang n\u00e0y, ch\u1ecdn C\u00f3, ti\u1ebfp t\u1ee5c thao t\u00e1c ti\u1ebfp."},
    37: {0: "\u0110\u1ebfn \u0111\u00e2y t\u00f4i b\u1ed7ng ph\u00e1t hi\u1ec7n m\u1ed9t v\u1ea5n \u0111\u1ec1, c\u00e1c API c\u1ee7a t\u00f4i \u0111\u1ec1u l\u00e0 g\u00f3i l\u1eadp tr\u00ecnh, t\u00f4i kh\u00f4ng ch\u1eafc c\u00f3 s\u1eed d\u1ee5ng \u0111\u01b0\u1ee3c kh\u00f4ng, n\u00ean tr\u1ef1c ti\u1ebfp nh\u1edd AI ki\u1ec3m tra gi\u00fap."},
    38: {0: "Sau khi th\u1ef1c nghi\u1ec7m th\u00ec \u0111\u00fang l\u00e0 GLM v\u00e0 Volcano c\u00f3 th\u1ec3 d\u00f9ng, Kimi Coding th\u00ec ch\u01b0a \u0111\u01b0\u1ee3c."},
    39: {0: "\u0110\u1ebfn \u0111\u00e2y t\u00f4i b\u1eaft \u0111\u1ea7u ph\u1ea3i t\u1ea1o bot Feishu."},
    40: {0: "V\u00e0 \u0111\u00e3 b\u1eadt quy\u1ec1n tin nh\u1eafn, b\u1ea3ng \u0111a chi\u1ec1u v\u00e0 \u0111\u1ee7 th\u1ee9 quy\u1ec1n linh tinh."},
    41: {0: "Sau \u0111\u00f3 ph\u00e1t h\u00e0nh \u1edf \u0111\u00e2y."},
    42: {0: "Trong qu\u00e1 tr\u00ecnh g\u1eb7p v\u1ea5n \u0111\u1ec1, c\u00f3 th\u1ec3 tr\u1ef1c ti\u1ebfp h\u1ecfi tr\u1ee3 l\u00fd th\u00f4ng minh c\u1ee7a Feishu, t\u00f4i \u0111\u00e3 g\u1eb7p tr\u01b0\u1eddng h\u1ee3p kh\u00f4ng th\u1ec3 chat v\u1edbi bot, ph\u00e1t hi\u1ec7n l\u00e0 do t\u00f4i ch\u01b0a c\u1ea5u h\u00ecnh quy\u1ec1n v\u00e0 s\u1ef1 ki\u1ec7n, h\u1ecfi tr\u1ee3 l\u00fd th\u00f4ng minh xong th\u00ec \u0111\u00e3 gi\u1ea3i quy\u1ebft \u0111\u01b0\u1ee3c v\u1ea5n \u0111\u1ec1."},
    43: {0: "T\u00f3m l\u1ea1i, v\u1edbi s\u1ef1 gi\u00fap \u0111\u1ee1 c\u1ee7a th\u1ea7y Kimi, t\u00f4i \u0111\u00e3 tri\u1ec3n khai th\u00e0nh c\u00f4ng Clawbot."},
    44: {0: "Nh\u01b0ng ngay sau \u0111\u00f3 t\u00f4i ph\u00e1t hi\u1ec7n c\u00f3 r\u1ea5t nhi\u1ec1u vi\u1ec7c ph\u1ea3i l\u00e0m, c\u1ea7n chuy\u1ec3n Skills c\u1ee7a t\u00f4i sang, nh\u01b0ng t\u00f4i th\u1ef1c s\u1ef1 kh\u00f4ng mu\u1ed1n l\u1eadp tr\u00ecnh n\u1eefa, t\u00f4i quy\u1ebft \u0111\u1ecbnh giao lu\u00f4n server c\u1ee7a m\u00ecnh cho n\u00f3."},
    45: {0: "Nh\u01b0ng Kimi Code r\u1ea5t c\u00f3 nguy\u00ean t\u1eafc, giao ti\u1ebfp m\u1ea5y l\u1ea7n v\u1eabn kh\u00f4ng ch\u1ecbu \u0111\u0103ng nh\u1eadp server c\u1ee7a t\u00f4i."},
    46: {0: "Th\u1ebf n\u00ean ch\u1ec9 c\u00f2n c\u00e1ch quay sang nh\u1edd Claude Code x\u1eed l\u00fd, sau m\u1ed9t v\u00f2ng Battle cu\u1ed1i c\u00f9ng t\u00f4i \u0111\u00e3 cho n\u00f3 k\u1ebft n\u1ed1i \u0111\u01b0\u1ee3c, c\u00e1c thao t\u00e1c v\u00e0 \u0111\u1ed1i tho\u1ea1i sau \u0111\u00f3 kh\u00f4ng c\u00f3 g\u00ec kh\u00e1c bi\u1ec7t."},
    47: {0: "M\u1ed9t lo\u1ea1t thao t\u00e1c m\u00e3nh li\u1ec7t, ", 1: "b\u00e2y gi\u1edd ch\u00ednh l\u00e0 d\u00f9ng AI ph\u00e1t tri\u1ec3n AI, \u0111\u1ec3 Kimi th\u00eam n\u0103ng l\u1ef1c cho Openclaw."},
    48: {0: "Ki\u1ec3m tra n\u0103ng l\u1ef1c 1: T\u1ea1o h\u00ecnh \u1ea3nh & G\u1eedi tin nh\u1eafn h\u00ecnh \u1ea3nh"},
    49: {0: "M\u1ea5t kh\u00e1 l\u00e2u, cu\u1ed1i c\u00f9ng c\u0169ng ho\u00e0n th\u00e0nh kh\u1ea3 n\u0103ng t\u1ea1o h\u00ecnh \u1ea3nh v\u00e0 g\u1eedi tin nh\u1eafn h\u00ecnh \u1ea3nh cho bot, tr\u01b0\u1edbc \u0111\u00e2y kh\u00f4ng c\u1ea7n g\u1eedi tin nh\u1eafn h\u00ecnh \u1ea3nh v\u00ec \u0111\u1ec1u xem tr\u00ean m\u00e1y t\u00ednh, b\u00e2y gi\u1edd c\u1ea7n g\u1eedi tin nh\u1eafn tr\u1ef1c ti\u1ebfp ra ngo\u00e0i."},
    50: {0: "C\u00f3 l\u1ebd l\u00e0 scenario Feishu n\u00e0y ch\u01b0a \u0111\u01b0\u1ee3c train, th\u1eddi gian ph\u00e1t tri\u1ec3n c\u1ee7a Kimi kh\u00e1 l\u00e2u."},
    51: {0: "Ki\u1ec3m tra n\u0103ng l\u1ef1c 2: K\u1ebft n\u1ed1i repository code ri\u00eang"},
    52: {0: "Ban \u0111\u1ea7u b\u1ecb 404, sau khi c\u1ea5u h\u00ecnh token th\u00ec \u0111\u00e3 truy c\u1eadp \u0111\u01b0\u1ee3c, v\u1ec1 nguy\u00ean t\u1eafc c\u00f3 th\u1ec3 code \u0111\u01b0\u1ee3c, v\u00e0 c\u1ed9ng t\u00e1c qua Git, \u1edf tr\u01b0\u1edbc m\u00e1y t\u00ednh th\u00ec d\u00f9ng m\u00e1y t\u00ednh, kh\u00f4ng \u1edf th\u00ec d\u00f9ng \u0111i\u1ec7n tho\u1ea1i."},
    53: {0: "C\u1eadp nh\u1eadt real-time qua Git, tuy nhi\u00ean t\u00f4i ch\u01b0a test scenario Openclaw g\u1ecdi c\u00f4ng c\u1ee5 l\u1eadp tr\u00ecnh, khi kh\u00f4ng c\u00e0i \u0111\u1eb7t th\u00ec l\u1ea1i tr\u1edf th\u00e0nh cu\u1ed9c thi so s\u00e1nh n\u0103ng l\u1ef1c m\u00f4 h\u00ecnh."},
    54: {0: "Ki\u1ec3m tra n\u0103ng l\u1ef1c 3: T\u00ecm ki\u1ebfm tr\u1ef1c tuy\u1ebfn"},
    55: {0: "Ban \u0111\u1ea7u kh\u00f4ng c\u00f3 kh\u1ea3 n\u0103ng t\u00ecm ki\u1ebfm tr\u1ef1c tuy\u1ebfn, ph\u1ea3i g\u1eafn Key c\u1ee7a Brave, nh\u01b0ng t\u00f4i l\u01b0\u1eddi g\u1eafn th\u1ebb t\u00edn d\u1ee5ng n\u00ean tr\u1ef1c ti\u1ebfp \u0111\u1ed5i sang c\u00e1i kh\u00e1c, hi\u1ec7n t\u1ea1i 2 MCP t\u00ecm ki\u1ebfm mi\u1ec5n ph\u00ed kh\u00f4ng c\u1ea7n g\u1eafn th\u1ebb c\u00f3 th\u1ec3 d\u00f9ng nh\u01b0 sau:"},
    58: {0: "Sau khi thay \u0111\u1ed5i c\u0169ng t\u00ecm ki\u1ebfm \u0111\u01b0\u1ee3c r\u1ed3i, QoderWork m\u00e0 Alibaba m\u1edbi ph\u00e1t h\u00e0nh hai ng\u00e0y tr\u01b0\u1edbc, n\u00f3 c\u0169ng t\u00ecm ki\u1ebfm \u0111\u01b0\u1ee3c."},
    59: {0: "Ki\u1ec3m tra n\u0103ng l\u1ef1c 4: S\u1eed d\u1ee5ng Skills c\u1ee7a Claude Code"},
    60: {0: "T\u1ea1i sao ph\u1ea3i phi\u1ec1n ph\u1ee9c v\u1eady, r\u00f5 r\u00e0ng Openclaw c\u00f3 skills ri\u00eang, ch\u1ee7 y\u1ebfu l\u00e0 kh\u00f4ng mu\u1ed1n duy tr\u00ec hai b\u1ed9, t\u00f4i c\u00f3 th\u1ec3 d\u00f9ng Git \u0111\u1ea3m b\u1ea3o skills c\u1ee7a m\u00ecnh lu\u00f4n l\u00e0 m\u1edbi nh\u1ea5t m\u1ed7i l\u1ea7n."},
    61: {0: "\u1ede \u0111\u00e2y c\u00f3 2 c\u00e1ch ch\u01a1i:"},
    62: {0: "C\u00e1ch 1: \u0110\u1ec3 Openclaw m\u00f4 ph\u1ecfng Skills c\u1ee7a b\u1ea1n"},
    63: {0: "N\u00f3i v\u1edbi n\u00f3 r\u1eb1ng b\u1ea1n c\u00f3 th\u1ec3 m\u00f4 ph\u1ecfng thao t\u00e1c Skills c\u1ee7a t\u00f4i, sau \u0111\u00f3 ph\u00eda sau gi\u1ed1ng h\u1ec7t nh\u01b0 trong Claude Code"},
    64: {0: "\u0110\u00e2y l\u00e0 k\u1ebft qu\u1ea3 n\u00f3 t\u1ea1o cho t\u00f4i"},
    65: {0: "C\u00e1ch 2: G\u1ecdi Claude Code s\u1eed d\u1ee5ng Skills"},
    66: {0: "Ph\u1ea3i c\u00e0i Claude tr\u01b0\u1edbc, t\u00f4i v\u1eabn giao server c\u1ee7a m\u00ecnh cho AI ti\u1ebfp qu\u1ea3n, ph\u1ea7n n\u00e0y t\u00f4i giao cho Codex."},
    67: {0: "V\u00e0 c\u0169ng tr\u1ef1c ti\u1ebfp \u0111\u1ec3 Claude t\u1ea3i Skills c\u1ee7a t\u00f4i v\u1ec1."},
    68: {0: "H\u01a1n n\u1eefa t\u00f4i s\u1ebd thi\u00ean v\u1ec1 vi\u1ec7c ", 1: "coi Openclaw nh\u01b0 \u0111\u1ea7u v\u00e0o ph\u00e2n ph\u1ed1i, r\u1ed3i ch\u1ecdn tin t\u01b0\u1edfng Agent c\u1ee7a Claude, d\u00f9 sao m\u1ed9t ng\u00e0y c\u1eadp nh\u1eadt N phi\u00ean b\u1ea3n c\u1ee7a c\u00f4ng c\u1ee5 Coding, trong ng\u00e0nh kh\u00f4ng c\u00f2n nhi\u1ec1u n\u1eefa."},
    69: {0: "Cu\u1ed1i c\u00f9ng, prompt \u0111\u00e3 ra~"},
    70: {0: "T\u1eeb ph\u1ea3n h\u1ed3i v\u00e0 log server, x\u00e1c nh\u1eadn \u0111\u00e3 ho\u00e0n th\u00e0nh vi\u1ec7c g\u1ecdi Claude."},
    71: {0: "Ki\u1ec3m tra n\u0103ng l\u1ef1c 5: S\u1eed d\u1ee5ng Skills l\u00e0m t\u00e1c v\u1ee5 \u0111\u1ecbnh k\u1ef3"},
    72: {0: "C\u00e1ch l\u00e0m tr\u1ef1c ti\u1ebfp d\u00f9ng ng\u00f4n ng\u1eef t\u1ef1 nhi\u00ean t\u01b0\u01a1ng t\u00e1c v\u1edbi Clawbot l\u00e0 \u0111\u01b0\u1ee3c, v\u1ec1 nguy\u00ean t\u1eafc, t\u1eeb ng\u00e0y mai trong nh\u00f3m s\u1ebd c\u00f3 b\u00e1o c\u00e1o h\u00e0ng ng\u00e0y."},
    73: {0: "T\u1ea1o h\u00ecnh \u1ea3nh, t\u00ecm ki\u1ebfm tr\u1ef1c tuy\u1ebfn, k\u1ebft n\u1ed1i repository code, g\u1ecdi c\u00f4ng c\u1ee5 l\u1eadp tr\u00ecnh ", 1: "\u0111\u1ec1u \u0111\u00e3 xong."},
    74: {0: "V\u1eady c\u00f4ng vi\u1ec7c ti\u1ebfp theo l\u00e0 b\u1ed5 sung th\u00eam nhi\u1ec1u n\u0103ng l\u1ef1c t\u00edch h\u1ee3p Feishu linh tinh, v\u00ed d\u1ee5 t\u00e0i li\u1ec7u \u0111\u00e1m m\u00e2y, b\u1ea3ng \u0111a chi\u1ec1u, v.v."},
    75: {0: "Vi\u1ebft \u0111\u1ebfn cu\u1ed1i b\u1ed7ng ph\u00e1t hi\u1ec7n, c\u00f3 l\u1ebd kho\u1ea3ng c\u00e1ch c\u1ee7a ch\u00fang ta \u0111\u1ebfn AGI l\u00e0 r\u1ed1t cu\u1ed9c giao bao nhi\u00eau quy\u1ec1n ra ngo\u00e0i."},
    76: {0: "ClawBot c\u00f3 th\u1ec3 coi l\u00e0 s\u1ea3n ph\u1ea9m AI k\u1ebft n\u1ed1i ph\u1ea7n m\u1ec1m, Qwen tr\u01b0\u1edbc \u0111\u00e2y c\u00f3 th\u1ec3 coi l\u00e0 s\u1ea3n ph\u1ea9m AI k\u1ebft n\u1ed1i cu\u1ed9c s\u1ed1ng c\u1ee7a ch\u00fang ta, sau n\u00e0y s\u1ebd c\u00f3 s\u1ea3n ph\u1ea9m k\u1ebft n\u1ed1i ph\u1ea7n c\u1ee9ng, sau n\u00e0y t\u1ea5t c\u1ea3 s\u1ebd \u0111\u01b0\u1ee3c k\u1ebft n\u1ed1i."},
    77: {0: "Ngh\u0129 m\u00e0 th\u1ea5y th\u1eadt \u0111\u00e1ng s\u1ee3."},
}

# Apply translations
for bi, block in enumerate(data['blocks']):
    if bi in trans:
        for ei, el in enumerate(block['elements']):
            if el['type'] == 'text_run' and ei in trans[bi]:
                el['content'] = trans[bi][ei]

with open('_art34_trans.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Translated {len(trans)} blocks, saved to _art34_trans.json")
