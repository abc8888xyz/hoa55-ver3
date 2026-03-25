"""Build translated JSON for article b6_3"""
import sys, json

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

with open('_art_b6_3_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Translation mapping: (block_index, element_index) -> translated content
# Rules: keep URLs, code terms (inline_code), emojis, style intact
trans = {
    (0,0): 'Lam Nguyet Ban Tu: Hoa don Token OpenClaw cua toi giam 72%, chi nho cai plugin nay',
    (1,0): '\U0001f517 Link bai goc: ',
    (2,0): 'Nguyen ban Lam Nguyet Ban Tu noi ve AI Lam Nguyet Ban Tu noi ve AI Ghi chep AI cua Lam Nguyet Ban Tu',
    (2,1): 'Ngay 13 thang 2 nam 2026, 19:01 Chiet Giang',
    (3,0): 'Cac ban cung co the trien khai thong qua Alibaba Cloud Bailian',
    (3,2): 'de trien khai',
    (3,3): ':',
    (4,0): 'Mua lan dau chi tu 7.9 te, gia han giam tu 50%, ho tro Qwen3.5, Qwen3-max, Qwen3-coder, GLM-5, GLM-4.7, Kimi-k2.5 va cac mo hinh khac',
    (5,0): '\U0001f449 Nhan link truy cap ngay:',
    (6,0): '\U0001f449 Xem huong dan trien khai chi tiet:',
    (7,0): 'Chi can toi da ba buoc, ban da co tro ly AI hoat dong 7x24 gio, phan hoi moi luc',
    (8,0): 'Gan day OpenClaw co rat nhieu cach choi, xay dung doi AI di lam, nuoi AI ban gai, moi cai deu khien nguoi ta me man.',
    (9,0): 'Nhung sau con hung phan, mo hoa don API ra, lap tuc toat mo hoi lanh.',
    (10,0): 'Voi toc do dot tien nay, chua noi den chay ung dung, noi chuyen vai cau thoi cung xot.',
    (11,0): 'Tai sao lai tro thanh "con thu nuot vang"?',
    (12,0): 'Boi vi trong linh vuc mo hinh lon, Context chinh la chi phi.',
}

# OK the approach above won't preserve Vietnamese diacritics well when written inline in Python.
# Let me use a different approach - write the translations with proper Unicode.

trans = {}

# Block 0 - page title
trans[(0,0)] = "L\u00e2m Nguy\u1ec7t B\u00e1n T\u1eed: H\u00f3a \u0111\u01a1n Token OpenClaw c\u1ee7a t\u00f4i gi\u1ea3m 72%, ch\u1ec9 nh\u1edd c\u00e0i plugin n\u00e0y"
# Block 1 - quote
trans[(1,0)] = "\U0001f517 Link b\u00e0i g\u1ed1c: "
# Block 2
trans[(2,0)] = "Nguy\u00ean b\u1ea3n L\u00e2m Nguy\u1ec7t B\u00e1n T\u1eed n\u00f3i v\u1ec1 AI L\u00e2m Nguy\u1ec7t B\u00e1n T\u1eed n\u00f3i v\u1ec1 AI Ghi ch\u00e9p AI c\u1ee7a L\u00e2m Nguy\u1ec7t B\u00e1n T\u1eed"
trans[(2,1)] = "Ng\u00e0y 13 th\u00e1ng 2 n\u0103m 2026, 19:01 Chi\u1ebft Giang"
# Block 3
trans[(3,0)] = "C\u00e1c b\u1ea1n c\u0169ng c\u00f3 th\u1ec3 tri\u1ec3n khai th\u00f4ng qua Alibaba Cloud Bailian"
trans[(3,2)] = "\u0111\u1ec3 tri\u1ec3n khai"
trans[(3,3)] = ":"
# Block 4
trans[(4,0)] = "Mua l\u1ea7n \u0111\u1ea7u ch\u1ec9 t\u1eeb 7.9 t\u1ec7, gia h\u1ea1n gi\u1ea3m t\u1eeb 50%, h\u1ed7 tr\u1ee3 Qwen3.5, Qwen3-max, Qwen3-coder, GLM-5, GLM-4.7, Kimi-k2.5 v\u00e0 c\u00e1c m\u00f4 h\u00ecnh kh\u00e1c"
# Block 5
trans[(5,0)] = "\U0001f449 Nh\u1ea5n link truy c\u1eadp ngay:"
# Block 6
trans[(6,0)] = "\U0001f449 Xem h\u01b0\u1edbng d\u1eabn tri\u1ec3n khai chi ti\u1ebft:"
# Block 7
trans[(7,0)] = "Ch\u1ec9 c\u1ea7n t\u1ed1i \u0111a ba b\u01b0\u1edbc, b\u1ea1n \u0111\u00e3 c\u00f3 tr\u1ee3 l\u00fd AI ho\u1ea1t \u0111\u1ed9ng 7x24 gi\u1edd, ph\u1ea3n h\u1ed3i m\u1ecdi l\u00fac"
# Block 8
trans[(8,0)] = "G\u1ea7n \u0111\u00e2y OpenClaw c\u00f3 r\u1ea5t nhi\u1ec1u c\u00e1ch ch\u01a1i, x\u00e2y d\u1ef1ng \u0111\u1ed9i AI \u0111i l\u00e0m, nu\u00f4i AI b\u1ea1n g\u00e1i, m\u1ed7i c\u00e1i \u0111\u1ec1u khi\u1ebfn ng\u01b0\u1eddi ta m\u00ea m\u1ea9n."
# Block 9
trans[(9,0)] = "Nh\u01b0ng sau c\u01a1n h\u01b0ng ph\u1ea5n, m\u1edf h\u00f3a \u0111\u01a1n API ra, l\u1eadp t\u1ee9c to\u00e1t m\u1ed3 h\u00f4i l\u1ea1nh."
# Block 10
trans[(10,0)] = "V\u1edbi t\u1ed1c \u0111\u1ed9 \u0111\u1ed1t ti\u1ec1n n\u00e0y, ch\u01b0a n\u00f3i \u0111\u1ebfn ch\u1ea1y \u1ee9ng d\u1ee5ng, n\u00f3i chuy\u1ec7n v\u00e0i c\u00e2u th\u00f4i c\u0169ng x\u00f3t."
# Block 11
trans[(11,0)] = "T\u1ea1i sao l\u1ea1i tr\u1edf th\u00e0nh \"con th\u00fa nu\u1ed1t v\u00e0ng\"?"
# Block 12
trans[(12,0)] = "B\u1edfi v\u00ec trong l\u0129nh v\u1ef1c m\u00f4 h\u00ecnh l\u1edbn, Context ch\u00ednh l\u00e0 chi ph\u00ed."
# Block 13
trans[(13,0)] = "OpenClaw m\u1eb7c \u0111\u1ecbnh nh\u1ed3i to\u00e0n b\u1ed9 cu\u1ed9c h\u1ed9i tho\u1ea1i v\u00e0o ng\u1eef c\u1ea3nh, Agent mang theo \u0111\u1ed1ng th\u00f4ng tin kh\u00f4ng li\u00ean quan, ti\u00eau hao Token t\u0103ng theo c\u1ea5p s\u1ed1 nh\u00e2n. T\u1ec7 h\u01a1n n\u1eefa, qu\u00e1 nhi\u1ec1u nhi\u1ec5u, m\u00f4 h\u00ecnh b\u1ecb ph\u00e2n t\u00e1n ch\u00fa \u00fd, th\u1eadm ch\u00ed xu\u1ea5t hi\u1ec7n \u1ea3o gi\u00e1c."
# Block 14
trans[(14,0)] = "H\u01a1n n\u1eefa t\u00f4i ph\u00e1t hi\u1ec7n m\u1ed9t hi\u1ec7n t\u01b0\u1ee3ng ph\u1ed5 bi\u1ebfn, kh\u00f4ng \u00edt b\u1ea1n trong group d\u00f9ng OpenClaw, \u0111\u1ec1u d\u00f9ng m\u1ed9t Agent ch\u00ednh l\u00e0m m\u1ecdi th\u1ee9, vi\u1ebft code, brainstorm, vi\u1ebft b\u00e0i, t\u00ecm t\u00e0i li\u1ec7u... L\u00e2u d\u1ea7n, file b\u1ed9 nh\u1edb ch\u1ea5t \u0111\u1ed1ng ng\u00e0y c\u00e0ng nhi\u1ec1u, m\u1ed7i l\u1ea7n th\u1ef1c hi\u1ec7n task \u0111\u1ec1u ph\u1ea3i \u0111\u1ecdc c\u1ea3 \u0111\u1ed1ng l\u1ecbch s\u1eed."
# Block 15
trans[(15,0)] = "K\u1ebft qu\u1ea3 l\u00e0, "
trans[(15,1)] = "Agent b\u1eaft \u0111\u1ea7u \"lo\u1ea1n th\u1ea7n\"."
# Block 16
trans[(16,0)] = "B\u1ea1n b\u1ea3o n\u00f3 vi\u1ebft code, n\u00f3 b\u1ea5t ng\u1edd nh\u1ea3y ra d\u00e0n \u00fd b\u00e0i c\u00f4ng ch\u00fang tu\u1ea7n tr\u01b0\u1edbc; b\u1ea1n b\u1ea3o n\u00f3 ph\u00e2n t\u00edch y\u00eau c\u1ea7u, n\u00f3 nh\u00e9t c\u1ea3 b\u1ed9 nh\u1edb debug Bug v\u00e0o. Ng\u1eef c\u1ea3nh c\u00e1c task kh\u00e1c nhau b\u1ecb \u00f4 nhi\u1ec5m ch\u00e9o, \u0111\u1ed9 ch\u00ednh x\u00e1c t\u1ee5t th\u1eb3ng \u0111\u1ee9ng, Token v\u1eabn \u0111ang ch\u00e1y \u0111i\u00ean cu\u1ed3ng."
# Block 17
trans[(17,0)] = "T\u00f4i l\u01b0\u1edbt th\u1ea5y m\u1ed9t gi\u1ea3i ph\u00e1p local tr\u00ean X, r\u1ed3i b\u1ecf cu\u1ed9c"
# Block 18
trans[(18,0)] = "\u0110\u1ecdc \u0111\u1ebfn \u0111\u00e2y, c\u00e1c player hardcore c\u00f3 l\u1ebd s\u1ebd n\u00f3i, \"T\u1ef1 d\u1ef1ng m\u1ed9t vector database local l\u00e0 xong ch\u1ee9 g\u00ec?\""
# Block 19
trans[(19,0)] = "T\u00f4i c\u0169ng t\u1eebng ngh\u0129 v\u1eady."
# Block 20
trans[(20,0)] = "Tr\u01b0\u1edbc \u0111\u00f3 tr\u00ean X, t\u00f4i l\u01b0\u1edbt th\u1ea5y c\u00f3 ng\u01b0\u1eddi chia s\u1ebb m\u1ed9t gi\u1ea3i ph\u00e1p t\u00ean QMD, tr\u00f4ng kh\u00e1 tuy\u1ec7t, c\u00f3 th\u1ec3 cho OpenClaw s\u1edf h\u1eefu b\u1ed9 nh\u1edb t\u00ecm ki\u1ebfm local."
# Block 21
trans[(21,0)] = "Nh\u01b0ng m\u1edf t\u00e0i li\u1ec7u ra, \u0111\u1ecdc \u0111o\u1ea1n n\u00e0y, c\u00f3 l\u1ebd s\u1ebd h\u00edt m\u1ed9t h\u01a1i l\u1ea1nh:"
# Block 22
trans[(22,0)] = "\u0110i\u1ec1u n\u00e0y c\u00f3 ngh\u0129a l\u00e0 g\u00ec?"
# Block 23
trans[(23,0)] = "B\u1ea1n ph\u1ea3i tr\u1ea3 tr\u01b0\u1edbc m\u1ed9t kho\u1ea3n \"thu\u1ebf thi\u1ebft b\u1ecb\":"
# Block 24
trans[(24,0)] = "Th\u1ee9 nh\u1ea5t, t\u1ea3i m\u00f4 h\u00ecnh, l\u1ea7n ch\u1ea1y \u0111\u1ea7u ti\u00ean s\u1ebd t\u1ef1 \u0111\u1ed9ng pull kho\u1ea3ng 2G m\u00f4 h\u00ecnh GGUF v\u1ec1 m\u00e1y."
# Block 25
trans[(25,0)] = "Th\u1ee9 hai, ti\u1ebfn tr\u00ecnh th\u01b0\u1eddng tr\u00fa, n\u1ec1n ph\u1ea3i ch\u1ea1y m\u1ed9t node-llama-cpp, ch\u1eebng n\u00e0o Agent c\u00f2n d\u00f9ng th\u00ec kh\u00f4ng \u0111\u01b0\u1ee3c t\u1eaft."
# Block 26
trans[(26,0)] = "Th\u1ee9 ba, t\u00e0i nguy\u00ean b\u00f9ng n\u1ed5, vector h\u00f3a v\u00e0 re-ranking \u0111\u1ec1u l\u00e0 t\u00e1c v\u1ee5 t\u1ed1n CPU."
# Block 27
trans[(27,0)] = "Tr\u1ea3i nghi\u1ec7m th\u1ef1c t\u1ebf l\u00e0, b\u1ea1n kh\u1edfi \u0111\u1ed9ng Agent chu\u1ea9n b\u1ecb l\u00e0m vi\u1ec7c, qu\u1ea1t laptop b\u1eaft \u0111\u1ea7u quay \u0111i\u00ean cu\u1ed3ng, CPU usage t\u0103ng v\u1ecdt."
# Block 28
trans[(28,0)] = "Ch\u01b0a vi\u1ebft \u0111\u01b0\u1ee3c d\u00f2ng code \u0111\u1ea7u ti\u00ean, 16G RAM \u0111\u00e3 ng\u1ed1n h\u01a1n n\u1eeda."
# Block 29
trans[(29,0)] = "\u0110\u1ec3 ti\u1ebft ki\u1ec7m ph\u00ed API, bi\u1ebfn c\u00f4ng c\u1ee5 n\u0103ng su\u1ea5t th\u00e0nh tr\u00ecnh gi\u1ea3 l\u1eadp gi\u1eadt lag."
# Block 30
trans[(30,0)] = "Kh\u00f4ng \u0111\u00e1ng."
# Block 31
trans[(31,0)] = "MemOS: Chuy\u1ec3n \"v\u1ecf n\u00e3o\" l\u00ean \u0111\u00e1m m\u00e2y"
# Block 32
trans[(32,0)] = "R\u1ed3i t\u00f4i th\u1ea5y MemOS tr\u00ean GitHub."
# Block 33
trans[(33,0)] = "N\u00f3i th\u1eadt, project l\u00e0m b\u1ed9 nh\u1edb AI kh\u00f4ng \u00edt, mem0, supermemory, memU \u0111\u1ec1u \u0111\u00e3 th\u1eed."
# Block 34
trans[(34,0)] = "Nh\u01b0ng MemOS c\u00f3 v\u00e0i \u0111i\u1ec3m khi\u1ebfn t\u00f4i quy\u1ebft \u0111\u1ecbnh th\u1eed nghi\u1ec7m s\u00e2u."
# Block 35
trans[(35,0)] = "Th\u1ee9 nh\u1ea5t, n\u00f3 th\u1ef1c s\u1ef1 nh\u1eb9."
# Block 36
trans[(36,0)] = "Kh\u00e1c ho\u00e0n to\u00e0n v\u1edbi t\u01b0 duy gi\u1ea3i ph\u00e1p local, MemOS \u0111\u01b0a to\u00e0n b\u1ed9 nh\u1eefng vi\u1ec7c t\u1ed1n t\u00e0i nguy\u00ean nh\u1ea5t - vector h\u00f3a, t\u00ecm ki\u1ebfm, qu\u1ea3n l\u00fd b\u1ed9 nh\u1edb - l\u00ean \u0111\u00e1m m\u00e2y. Kh\u00f4ng c\u1ea7n t\u1ea3i m\u00f4 h\u00ecnh GGUF, kh\u00f4ng c\u1ea7n ti\u1ebfn tr\u00ecnh n\u1eb7ng ch\u1ea1y n\u1ec1n, ch\u1ec9 c\u1ea7n m\u1ed9t Plugin nh\u1eb9, v\u00e0i d\u00f2ng c\u1ea5u h\u00ecnh, c\u00e0i l\u00e0 d\u00f9ng ngay."
# Block 37
trans[(37,0)] = "Th\u1ee9 hai, kh\u00f4ng ph\u1ea3i nh\u1ed3i nh\u00e9t ng\u1eef c\u1ea3nh th\u00f4 b\u1ea1o, m\u00e0 l\u00e0 \"truy h\u1ed3i ch\u00ednh x\u00e1c\"."
# Block 38
trans[(38,0)] = "MemOS \u0111\u01b0a v\u00e0o c\u01a1 ch\u1ebf k\u00edch ho\u1ea1t b\u1ed9 nh\u1edb, n\u00f3 kh\u00f4ng nh\u1ed3i to\u00e0n b\u1ed9 l\u1ecbch s\u1eed h\u1ed9i tho\u1ea1i v\u00e0o m\u00f4 h\u00ecnh, m\u00e0 d\u1ef1a tr\u00ean \u00fd \u0111\u1ecbnh task hi\u1ec7n t\u1ea1i, t\u00ecm ki\u1ebfm ch\u00ednh x\u00e1c v\u00e0i m\u1ee5c b\u1ed9 nh\u1edb li\u00ean quan nh\u1ea5t."
# Block 39
trans[(39,0)] = "Ch\u1ec9 tr\u1ea3 ti\u1ec1n cho \"th\u00f4ng tin h\u1eefu \u00edch\"."
# Block 40
trans[(40,0)] = "Theo d\u1eef li\u1ec7u ch\u00ednh th\u1ee9c, m\u1ee9c ti\u00eau hao Token c\u00f3 th\u1ec3 gi\u1ea3m 72%. C\u1ea3m nh\u1eadn c\u00e1 nh\u00e2n t\u00f4i c\u0169ng r\u1ea5t r\u00f5, c\u00f9ng m\u1ed9t task, tr\u01b0\u1edbc v\u00e0 sau khi t\u00edch h\u1ee3p kh\u00e1c bi\u1ec7t th\u1ea5y r\u00f5."
# Block 41
trans[(41,0)] = "Th\u1ee9 ba, tr\u1ea3i nghi\u1ec7m c\u00e1 nh\u00e2n h\u00f3a."
# Block 42
trans[(42,0)] = "Sau khi d\u00f9ng m\u1ed9t th\u1eddi gian, b\u1ea1n s\u1ebd ph\u00e1t hi\u1ec7n, Agent th\u1ef1c s\u1ef1 \"nh\u1eadn ra b\u1ea1n\" r\u1ed3i."
# Block 43
trans[(43,0)] = "N\u00f3 nh\u1edb s\u1edf th\u00edch c\u1ee7a b\u1ea1n, nh\u1edb b\u1ed1i c\u1ea3nh d\u1ef1 \u00e1n c\u1ee7a b\u1ea1n, nh\u1edb c\u00e1c quy\u1ebft \u0111\u1ecbnh tr\u01b0\u1edbc \u0111\u00f3 c\u1ee7a b\u1ea1n."
# Block 44
trans[(44,0)] = "Kh\u00f4ng nh\u01b0 tr\u01b0\u1edbc, m\u1ed7i l\u1ea7n m\u1edf phi\u00ean m\u1edbi, Agent nh\u01b0 b\u1ecb m\u1ea5t tr\u00ed nh\u1edb, b\u1ea1n ph\u1ea3i gi\u1edbi thi\u1ec7u l\u1ea1i t\u1eeb \u0111\u1ea7u."
# Block 45
trans[(45,0)] = "Theo d\u1eef li\u1ec7u benchmark ch\u00ednh th\u1ee9c, tr\u00ean PrefEval-10, \u0111\u1ed9 ch\u00ednh x\u00e1c c\u1ee7a MemOS cao h\u01a1n OpenAI Memory t\u1edbi 43.70%."
# Block 46
trans[(46,0)] = "\u0110\u00e2y kh\u00f4ng ph\u1ea3i con s\u1ed1 nh\u1ecf."
# Block 47
trans[(47,0)] = "T\u00ednh n\u0103ng th\u1ef1c s\u1ef1 khi\u1ebfn t\u00f4i \"kh\u00f4ng th\u1ec3 quay l\u1ea1i\": Chia s\u1ebb b\u1ed9 nh\u1edb \u0111a Agent"
# Block 48
trans[(48,0)] = "Ti\u1ebft ki\u1ec7m ti\u1ec1n t\u1ea5t nhi\u00ean t\u1ed1t, nh\u01b0ng \u0111i\u1ec1u th\u1ef1c s\u1ef1 khi\u1ebfn t\u00f4i c\u1ea3m th\u1ea5y \u0111\u00e1ng gi\u00e1, l\u00e0 MemOS gi\u1ea3i quy\u1ebft \u0111i\u1ec3m \u0111au l\u1edbn nh\u1ea5t trong c\u1ed9ng t\u00e1c \u0111a Agent \u2014\u2014 "
trans[(48,1)] = "s\u1ef1 c\u00f4 l\u1eadp b\u1ed9 nh\u1edb gi\u1eefa c\u00e1c Agent "
trans[(48,2)] = "."
# Block 49
trans[(49,0)] = "Tr\u01b0\u1edbc h\u1ebft n\u00f3i v\u1ec1 t\u1ea1i sao c\u1ea7n d\u00f9ng \u0111a Agent."
# Block 50
trans[(50,0)] = "Nh\u01b0 \u0111\u00e3 \u0111\u1ec1 c\u1eadp \u1edf tr\u00ean, nh\u1ed3i t\u1ea5t c\u1ea3 task v\u00e0o m\u1ed9t Agent, l\u00e2u d\u1ea7n s\u1ebd lo\u1ea1n."
# Block 51
trans[(51,0)] = "V\u00ec v\u1eady c\u00e1ch l\u00e0m \u0111\u00fang l\u00e0, "
trans[(51,1)] = "task kh\u00e1c nhau, Agent kh\u00e1c nhau, workspace kh\u00e1c nhau."
# Block 52
trans[(52,0)] = "V\u00e0i Agent t\u00f4i th\u01b0\u1eddng d\u00f9ng hi\u1ec7n t\u1ea1i:"
# Block 53
trans[(53,0)] = "\U0001f9e0 "
trans[(53,1)] = "Agent Brainstorm "
trans[(53,2)] = ": ch\u1ecbu tr\u00e1ch nhi\u1ec7m t\u01b0 duy ph\u00e1t t\u00e1n, thu th\u1eadp t\u00e0i li\u1ec7u, t\u1ea1o \u00fd t\u01b0\u1edfng, d\u00f9ng m\u00f4 h\u00ecnh r\u1ebb l\u00e0 \u0111\u01b0\u1ee3c, v\u00ed d\u1ee5 gemini-2.5-flash."
# Block 54
trans[(54,0)] = "\u270d\ufe0f "
trans[(54,1)] = "Agent Vi\u1ebft b\u00e0i c\u00f4ng ch\u00fang "
trans[(54,2)] = ": ch\u1ecbu tr\u00e1ch nhi\u1ec7m thu g\u1ecdn \u00fd t\u01b0\u1edfng th\u00e0nh b\u00e0i vi\u1ebft."
# Block 55
trans[(55,0)] = "\U0001f4bb "
trans[(55,1)] = "Coding Agent "
trans[(55,2)] = ": ch\u1ecbu tr\u00e1ch nhi\u1ec7m vi\u1ebft code, debug."
# Block 56
trans[(56,0)] = "L\u1ee3i \u00edch c\u1ee7a c\u00e1ch chia t\u00e1ch n\u00e0y r\u1ea5t r\u00f5 r\u00e0ng."
# Block 57
trans[(57,0)] = "M\u1ed7i Agent c\u00f3 b\u1ed9 nh\u1edb \u0111\u1ed9c l\u1eadp, kh\u00f4ng b\u1ecb lo\u1ea1n v\u00ec load b\u1ed9 nh\u1edb ph\u1ee9c t\u1ea1p; ng\u1eef c\u1ea3nh kh\u00f4ng b\u1ecb \u00f4 nhi\u1ec5m ch\u00e9o, vi\u1ebft code kh\u00f4ng nh\u1ea3y ra b\u1ed9 nh\u1edb vi\u1ebft b\u00e0i; chi ph\u00ed c\u0169ng d\u1ec5 ki\u1ec3m so\u00e1t, task \u0111\u01a1n gi\u1ea3n d\u00f9ng m\u00f4 h\u00ecnh r\u1ebb, task ph\u1ee9c t\u1ea1p d\u00f9ng m\u00f4 h\u00ecnh m\u1ea1nh."
# Block 58
trans[(58,0)] = "Nh\u01b0ng v\u1ea5n \u0111\u1ec1 \u0111\u1ebfn r\u1ed3i\u2014\u2014"
# Block 59
trans[(59,0)] = "Sau khi chia t\u00e1ch, c\u00e1c Agent tr\u1edf th\u00e0nh \u0111\u1ea3o th\u00f4ng tin c\u00f4 l\u1eadp. 20 \u00fd t\u01b0\u1edfng t\u1eeb brainstorm, Agent vi\u1ebft b\u00e0i ho\u00e0n to\u00e0n kh\u00f4ng bi\u1ebft. B\u1ea1n ch\u1ec9 c\u00f3 th\u1ec3 copy paste th\u1ee7 c\u00f4ng, l\u00e0m \"ng\u01b0\u1eddi truy\u1ec1n tin b\u1eb1ng tay\"."
# Block 60
trans[(60,0)] = "MemOS gi\u1ea3i quy\u1ebft ch\u00ednh m\u00e2u thu\u1eabn n\u00e0y: workspace c\u00f4 l\u1eadp, nh\u01b0ng th\u00f4ng tin quan tr\u1ecdng \u0111\u01b0\u1ee3c chia s\u1ebb."
# Block 61
trans[(61,0)] = "Sau khi t\u00edch h\u1ee3p MemOS, c\u00e1ch ch\u01a1i thay \u0111\u1ed5i."
# Block 62
trans[(62,0)] = "V\u00ed d\u1ee5 t\u00f4i n\u00f3i v\u1edbi Agent brainstorm: \"Gi\u00fap t\u00f4i l\u00ean ph\u01b0\u01a1ng \u00e1n h\u1ec7 th\u1ed1ng \u0111i\u1ec1u khi\u1ec3n nh\u00e0 th\u00f4ng minh.\""
# Block 63
trans[(63,0)] = "Agent tr\u1ea3 l\u1eddi b\u00ecnh th\u01b0\u1eddng, \u0111\u01b0a ra chi ti\u1ebft ph\u01b0\u01a1ng \u00e1n."
# Block 64
trans[(64,0)] = "Trong su\u1ed1t qu\u00e1 tr\u00ecnh h\u1ed9i tho\u1ea1i, b\u1ea1n kh\u00f4ng c\u1ea7n thao t\u00e1c g\u00ec th\u00eam, n\u1ed9i dung h\u1ed9i tho\u1ea1i s\u1ebd t\u1ef1 \u0111\u1ed9ng \u0111\u1ed3ng b\u1ed9 \u0111\u1ebfn MemOS (log n\u1ec1n hi\u1ec3n th\u1ecb l\u00e0 addMessage)"
# Block 65
trans[(65,0)] = "R\u1ed3i t\u00f4i chuy\u1ec3n sang Agent vi\u1ebft b\u00e0i, n\u00f3i th\u1eb3ng: \"T\u00f4i tr\u01b0\u1edbc \u0111\u00f3 \u0111\u00e3 trao \u0111\u1ed5i trong brainstorm v\u1ec1 ph\u01b0\u01a1ng \u00e1n nh\u00e0 th\u00f4ng minh, d\u1ef1a tr\u00ean ph\u01b0\u01a1ng \u00e1n \u0111\u00f3, gi\u00fap t\u00f4i vi\u1ebft m\u1ed9t b\u00e0i c\u00f4ng ch\u00fang.\""
# Block 66
trans[(66,0)] = "Agent t\u1ef1 \u0111\u1ed9ng g\u1ecdi search_memory, truy xu\u1ea5t ch\u00ednh x\u00e1c ph\u01b0\u01a1ng \u00e1n v\u1eeba n\u00e3y."
# Block 67
trans[(67,0)] = "L\u01b0u \u00fd, t\u00f4i kh\u00f4ng ch\u1ec9 \u0111\u1ecbnh tag, c\u0169ng kh\u00f4ng l\u01b0u th\u1ee7 c\u00f4ng."
# Block 68
trans[(68,0)] = "Vi\u1ec7c t\u00ecm ki\u1ebfm c\u1ee7a MemOS d\u1ef1a tr\u00ean ng\u1eef ngh\u0129a, b\u1ea1n d\u00f9ng ng\u00f4n ng\u1eef t\u1ef1 nhi\u00ean m\u00f4 t\u1ea3 \"tr\u01b0\u1edbc \u0111\u00f3 \u0111\u00e3 trao \u0111\u1ed5i g\u00ec\", n\u00f3 c\u00f3 th\u1ec3 t\u00ecm ra."
# Block 69
trans[(69,0)] = "Kh\u00f4ng c\u1ea7n copy paste, kh\u00f4ng c\u1ea7n l\u1eb7p l\u1ea1i b\u1ed1i c\u1ea3nh."
# Block 70
trans[(70,0)] = "Tri th\u1ee9c m\u00e0 Agent A t\u1ea1o ra, Agent B hi\u1ec3u ngay."
# Block 71
trans[(71,0)] = "V\u00e0 to\u00e0n b\u1ed9 qu\u00e1 tr\u00ecnh l\u00e0 \"kh\u00f4ng c\u1ea3m nh\u1eadn \u0111\u01b0\u1ee3c\", output h\u1ed9i tho\u1ea1i s\u1ebd t\u1ef1 \u0111\u1ed9ng ghi l\u1ea1i v\u00e0o MemOS, kh\u00f4ng c\u1ea7n l\u01b0u th\u1ee7 c\u00f4ng, kh\u00f4ng c\u1ea7n ch\u1ec9 \u0111\u1ecbnh format, n\u00f3 t\u1ef1 ho\u00e0n th\u00e0nh ph\u00e2n lo\u1ea1i v\u00e0 \u0111\u00e1nh index. Vi\u1ec7c b\u1ea1n c\u1ea7n l\u00e0m ch\u1ec9 l\u00e0 h\u1ed9i tho\u1ea1i b\u00ecnh th\u01b0\u1eddng."
# Block 72
trans[(72,0)] = "Logic t\u01b0\u01a1ng t\u1ef1 \u00e1p d\u1ee5ng cho Coding Agent."
# Block 73
trans[(73,0)] = "V\u00ed d\u1ee5 t\u00f4i th\u1ea3o lu\u1eadn xong ph\u01b0\u01a1ng \u00e1n k\u1ef9 thu\u1eadt trong brainstorm, chuy\u1ec3n sang Coding Agent n\u00f3i th\u1eb3ng \"b\u1eaft \u0111\u1ea7u vi\u1ebft code\", n\u00f3 c\u00f3 th\u1ec3 truy xu\u1ea5t tech stack v\u00e0 ki\u1ebfn tr\u00fac t\u1eeb b\u1ed9 nh\u1edb, kh\u00f4ng c\u1ea7n gi\u1edbi thi\u1ec7u l\u1ea1i."
# Block 74
trans[(74,0)] = "\u0110\u00e2y m\u1edbi l\u00e0 h\u00ecnh d\u00e1ng \u0111\u00fang c\u1ee7a c\u1ed9ng t\u00e1c \u0111a Agent."
# Block 75
trans[(75,0)] = "H\u01a1n n\u1eefa v\u00ec m\u1ed7i Agent ch\u1ec9 t\u00ecm ki\u1ebfm b\u1ed9 nh\u1edb m\u00ecnh c\u1ea7n, ch\u1ee9 kh\u00f4ng load to\u00e0n b\u1ed9 l\u1ecbch s\u1eed, n\u00ean ti\u00eau hao Token l\u1ea1i th\u1ea5p h\u01a1n."
# Block 76
trans[(76,0)] = "Ti\u1ebft ki\u1ec7m ti\u1ec1n, ch\u1ed1ng lo\u1ea1n, c\u1ed9ng t\u00e1c th\u1eadt s\u1ef1, ba vi\u1ec7c gi\u1ea3i quy\u1ebft c\u00f9ng l\u00fac."
# Block 77
trans[(77,0)] = "C\u00e0i \u0111\u1eb7t si\u00eau t\u1ed1c trong 30 gi\u00e2y"
# Block 78
trans[(78,0)] = "C\u00f4ng c\u1ee5 t\u1ed1t ph\u1ea3i \u0111\u01a1n gi\u1ea3n, quy tr\u00ecnh t\u00edch h\u1ee3p MemOS r\u1ea5t th\u00e2n thi\u1ec7n."
# Block 79
trans[(79,0)] = "Step 1: L\u1ea5y API Key"
# Block 80
trans[(80,0)] = "Truy c\u1eadp MemOS Dashboard ( "
trans[(80,2)] = ") \u0111\u0103ng k\u00fd, nh\u1eadn API Key mi\u1ec5n ph\u00ed."
# Block 81
trans[(81,0)] = "Step 2: C\u1ea5u h\u00ecnh bi\u1ebfn m\u00f4i tr\u01b0\u1eddng"
# Block 82
trans[(82,0)] = "Step 3: C\u00e0i \u0111\u1eb7t plugin m\u1ed9t l\u1ec7nh"
# Block 83
trans[(83,0)] = "Sau khi kh\u1edfi \u0111\u1ed9ng l\u1ea1i, OpenClaw c\u1ee7a b\u1ea1n \u0111\u00e3 c\u00f3 m\u1ed9t b\u1ed9 n\u00e3o ngo\u00e0i."
# Block 84
trans[(84,0)] = "L\u1eddi k\u1ebft"
# Block 85
trans[(85,0)] = "Sau khi th\u1eed nghi\u1ec7m nhi\u1ec1u c\u00f4ng c\u1ee5 AI, t\u00f4i ng\u00e0y c\u00e0ng nh\u1eadn ra m\u1ed9t \u0111i\u1ec1u:"
# Block 86
trans[(86,0)] = "T\u01b0\u01a1ng lai cu\u1ed9c c\u1ea1nh tranh AI kh\u00f4ng n\u1eb1m \u1edf tham s\u1ed1 m\u00f4 h\u00ecnh l\u1edbn \u0111\u1ebfn \u0111\u00e2u, m\u00e0 \u1edf kh\u1ea3 n\u0103ng qu\u1ea3n l\u00fd ng\u1eef c\u1ea3nh v\u00e0 b\u1ed9 nh\u1edb m\u1ea1nh \u0111\u1ebfn m\u1ee9c n\u00e0o."
# Block 87
trans[(87,0)] = "N\u0103ng l\u1ef1c m\u00f4 h\u00ecnh \u0111ang h\u1ed9i t\u1ee5, nh\u01b0ng kho\u1ea3ng c\u00e1ch trong qu\u1ea3n l\u00fd b\u1ed9 nh\u1edb quy\u1ebft \u0111\u1ecbnh Agent c\u1ee7a b\u1ea1n l\u00e0 ng\u01b0\u1eddi l\u1ea1 m\u1ed7i l\u1ea7n g\u1eb7p, hay l\u00e0 \u0111\u1ed1i t\u00e1c d\u00e0i h\u1ea1n th\u1ef1c s\u1ef1 hi\u1ec3u b\u1ea1n."
# Block 88
trans[(88,0)] = "MemOS hi\u1ec7n c\u00f3 5.2k Star tr\u00ean GitHub, m\u00e3 ngu\u1ed3n m\u1edf theo gi\u1ea5y ph\u00e9p Apache 2.0, \u0111\u00e1ng \u0111\u1ec3 theo d\u00f5i."
# Block 89
trans[(89,0)] = "\u0110\u1ecba ch\u1ec9 GitHub: "
# Block 90
trans[(90,0)] = "N\u1ebfu th\u1ea5y h\u1eefu \u00edch, ti\u1ec7n tay l\u00ean GitHub b\u1ea5m Star, \u0111\u1ec3 project t\u1ed1t \u0111\u01b0\u1ee3c nhi\u1ec1u ng\u01b0\u1eddi bi\u1ebft \u0111\u1ebfn h\u01a1n."
# Block 91
trans[(91,0)] = "C\u1ea3m \u01a1n b\u1ea1n \u0111\u00e3 \u0111\u1ecdc \u0111\u1ebfn \u0111\u00e2y \U0001f44f"
# Block 92
trans[(92,0)] = "N\u1ebfu th\u1ea5y h\u1eefu \u00edch, h\u00e3y th\u1ea3 like \U0001f44d / \u0111\u00e1nh d\u1ea5u \u0111\u00e3 xem \U0001f440 / chia s\u1ebb \U0001faf1 / b\u00ecnh lu\u1eadn \U0001f4e3"
# Block 93
trans[(93,0)] = "\u0110\u00e1nh d\u1ea5u sao \u2b50 nh\u00e9, l\u1ea7n c\u1eadp nh\u1eadt sau kh\u00f4ng b\u1ecb l\u1ea1c"

# Apply translations
for bi, block in enumerate(data['blocks']):
    for ei, el in enumerate(block['elements']):
        if el['type'] == 'text_run':
            key = (bi, ei)
            if key in trans:
                el['content'] = trans[key]

# Add spaces between adjacent Vietnamese text_runs where needed
for block in data['blocks']:
    elements = block['elements']
    for i in range(len(elements) - 1):
        curr = elements[i]
        nxt = elements[i+1]
        if curr['type'] == 'text_run' and nxt['type'] == 'text_run':
            c = curr['content']
            n = nxt['content']
            if c and n:
                last_char = c[-1]
                first_char = n[0]
                # Add space if both ends are alphanumeric and no space exists
                if (last_char.isalpha() or last_char in ')\"') and first_char.isalpha() and not c.endswith(' ') and not n.startswith(' '):
                    curr['content'] = c + ' '

with open('_art_b6_3_trans.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Count stats
total_text_runs = 0
translated_count = 0
kept_count = 0
for bi, b in enumerate(data['blocks']):
    for ei, e in enumerate(b['elements']):
        if e['type'] == 'text_run':
            total_text_runs += 1
            if (bi, ei) in trans:
                translated_count += 1
            else:
                kept_count += 1

print(f'Total blocks: {len(data["blocks"])}')
print(f'Total text_runs: {total_text_runs}')
print(f'Translated: {translated_count}')
print(f'Kept as-is: {kept_count}')
print('Saved _art_b6_3_trans.json')
