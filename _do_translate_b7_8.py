"""Translate _art_b7_8_orig.json CN->VI, save _art_b7_8_trans.json"""
import sys, json, re

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

with open('_art_b7_8_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Translation map: Chinese -> Vietnamese
# Rules: preserve URLs, code terms (ASR, TTS, OGG/Opus, etc.), emoji, style
trans = {
    'Day05\uff5c\u9f99\u867e Lucky \u7684\u7b2c\u4e94\u5929\uff1a \u4ece\u201c\u8bed\u97f3\u7559\u8a00\u201d\u5230\u201c\u5b9e\u65f6\u5bf9\u8bdd\u201d':
        'Day05\uff5cNg\u00e0y th\u1ee9 n\u0103m c\u1ee7a T\u00f4m H\u00f9m Lucky: T\u1eeb "tin nh\u1eafn tho\u1ea1i" \u0111\u1ebfn "h\u1ed9i tho\u1ea1i th\u1eddi gian th\u1ef1c"',

    '\U0001f517 \u539f\u6587\u94fe\u63a5\uff1a ':
        '\U0001f517 Link b\u00e0i g\u1ed1c: ',

    '\u539f\u521b Larkspur\u6280\u672f\u5206\u4eab Larkspur\u6280\u672f\u5206\u4eab Little Shock':
        'Nguy\u00ean t\u00e1c Larkspur chia s\u1ebb c\u00f4ng ngh\u1ec7 Larkspur chia s\u1ebb c\u00f4ng ngh\u1ec7 Little Shock',

    '2026\u5e743\u67088\u65e5 20:42  \u4e0a\u6d77':
        '08/03/2026 20:42  Th\u01b0\u1ee3ng H\u1ea3i',

    '2026\u5e743\u67088\u65e5 20:38':
        '08/03/2026 20:38',

    '\u5f88\u591a\u4eba\u4ee5\u4e3a\u201c\u652f\u6301\u8bed\u97f3\u201d\u5c31\u662f\u628a\u97f3\u9891\u8f6c\u6210\u6587\u5b57\u3002':
        'Nhi\u1ec1u ng\u01b0\u1eddi ngh\u0129 r\u1eb1ng "h\u1ed7 tr\u1ee3 gi\u1ecdng n\u00f3i" ch\u1ec9 \u0111\u01a1n gi\u1ea3n l\u00e0 chuy\u1ec3n \u00e2m thanh th\u00e0nh v\u0103n b\u1ea3n.',

    '\u5176\u5b9e\u90a3\u53ea\u662f\u5b8c\u6210\u4e86\u4e00\u534a\u3002':
        'Th\u1ef1c ra \u0111\u00f3 m\u1edbi ch\u1ec9 ho\u00e0n th\u00e0nh m\u1ed9t n\u1eeda.',

    '\u771f\u6b63\u6709\u4f53\u9a8c\u63d0\u5347\u7684\uff0c\u662f\u8fd9\u6761\u95ed\u73af\uff1a':
        '\u0110i\u1ec1u th\u1ef1c s\u1ef1 n\u00e2ng cao tr\u1ea3i nghi\u1ec7m ch\u00ednh l\u00e0 v\u00f2ng l\u1eb7p kh\u00e9p k\u00edn n\u00e0y:',

    '\u7528\u6237\u8bf4\u8bdd\uff08ASR\uff09 -> \u6a21\u578b\u7406\u89e3 -> AI \u7528\u6307\u5b9a\u97f3\u8272\u8bf4\u56de\u53bb\uff08TTS\uff09\u3002':
        'Ng\u01b0\u1eddi d\u00f9ng n\u00f3i (ASR) -> M\u00f4 h\u00ecnh hi\u1ec3u -> AI ph\u1ea3n h\u1ed3i b\u1eb1ng gi\u1ecdng \u0111\u01b0\u1ee3c ch\u1ec9 \u0111\u1ecbnh (TTS).',

    '\u4eca\u5929\u8fd9\u7bc7\u5c31\u8bb2\u8fd9\u4ef6\u4e8b\u600e\u4e48\u843d\u5730\uff0c\u5e76\u91cd\u70b9\u8bb2\u6e05\u695a Voice Design\uff08\u97f3\u8272\u8bbe\u8ba1\uff09\u5230\u5e95\u8be5\u600e\u4e48\u505a\u3002':
        'B\u00e0i vi\u1ebft h\u00f4m nay s\u1ebd n\u00f3i v\u1ec1 c\u00e1ch tri\u1ec3n khai vi\u1ec7c n\u00e0y, v\u00e0 t\u1eadp trung gi\u1ea3i th\u00edch r\u00f5 Voice Design (thi\u1ebft k\u1ebf gi\u1ecdng n\u00f3i) n\u00ean l\u00e0m nh\u01b0 th\u1ebf n\u00e0o.',

    '\u4e00\u3001\u5148\u770b\u6700\u7ec8\u5f62\u6001\uff1a\u4ec0\u4e48\u53eb\u201c\u8bed\u97f3\u5bf9\u8bdd\u771f\u7684\u6210\u7acb\u201d':
        '1. Tr\u01b0\u1edbc ti\u00ean h\u00e3y xem h\u00ecnh th\u00e1i cu\u1ed1i c\u00f9ng: Th\u1ebf n\u00e0o g\u1ecdi l\u00e0 "h\u1ed9i tho\u1ea1i b\u1eb1ng gi\u1ecdng n\u00f3i th\u1ef1c s\u1ef1 th\u00e0nh c\u00f4ng"',

    '\u5982\u679c\u7cfb\u7edf\u53ea\u6709 ASR\uff0c\u90a3\u66f4\u50cf\u201c\u8bed\u97f3\u8f93\u5165\u7684\u804a\u5929\u673a\u5668\u4eba\u201d\u3002':
        'N\u1ebfu h\u1ec7 th\u1ed1ng ch\u1ec9 c\u00f3 ASR, th\u00ec n\u00f3 gi\u1ed1ng "chatbot nh\u1eadp li\u1ec7u b\u1eb1ng gi\u1ecdng n\u00f3i" h\u01a1n.',

    '\u5982\u679c\u7cfb\u7edf\u540c\u65f6\u5177\u5907 ASR + TTS\uff0c\u5e76\u4e14\u97f3\u8272\u53ef\u63a7\uff0c\u90a3\u624d\u66f4\u63a5\u8fd1\u201c\u5bf9\u8bdd\u52a9\u624b\u201d\u3002':
        'N\u1ebfu h\u1ec7 th\u1ed1ng \u0111\u1ed3ng th\u1eddi c\u00f3 ASR + TTS, v\u00e0 gi\u1ecdng n\u00f3i c\u00f3 th\u1ec3 ki\u1ec3m so\u00e1t, th\u00ec m\u1edbi g\u1ea7n v\u1edbi "tr\u1ee3 l\u00fd h\u1ed9i tho\u1ea1i" h\u01a1n.',

    '\u4f53\u611f\u5dee\u5f02\u4f1a\u975e\u5e38\u660e\u663e\uff1a':
        'S\u1ef1 kh\u00e1c bi\u1ec7t trong tr\u1ea3i nghi\u1ec7m s\u1ebd r\u1ea5t r\u00f5 r\u00e0ng:',

    '\u4e0d\u662f\u201c\u53d1\u8bed\u97f3\uff0c\u6536\u6587\u5b57\u201d':
        'Kh\u00f4ng ph\u1ea3i "g\u1eedi gi\u1ecdng n\u00f3i, nh\u1eadn v\u0103n b\u1ea3n"',

    '\u800c\u662f\u201c\u53d1\u8bed\u97f3\uff0c\u6536\u8bed\u97f3\u201d':
        'M\u00e0 l\u00e0 "g\u1eedi gi\u1ecdng n\u00f3i, nh\u1eadn gi\u1ecdng n\u00f3i"',

    '\u800c\u4e14\u56de\u590d\u58f0\u97f3\u53ef\u4ee5\u7ef4\u6301\u7edf\u4e00\u4eba\u8bbe\u3001\u6309\u573a\u666f\u5fae\u8c03':
        'H\u01a1n n\u1eefa gi\u1ecdng ph\u1ea3n h\u1ed3i c\u00f3 th\u1ec3 duy tr\u00ec nh\u00e2n v\u1eadt th\u1ed1ng nh\u1ea5t, tinh ch\u1ec9nh theo ng\u1eef c\u1ea3nh',

    '\u8fd9\u5c31\u662f\u4ece\u201c\u529f\u80fd\u53ef\u7528\u201d\u5230\u201c\u4f53\u9a8c\u53ef\u7528\u201d\u7684\u5206\u754c\u7ebf\u3002':
        '\u0110\u00e2y ch\u00ednh l\u00e0 ranh gi\u1edbi t\u1eeb "ch\u1ee9c n\u0103ng kh\u1ea3 d\u1ee5ng" \u0111\u1ebfn "tr\u1ea3i nghi\u1ec7m kh\u1ea3 d\u1ee5ng".',

    '\u4e8c\u3001\u94fe\u8def\u62c6\u89e3':
        '2. Ph\u00e2n t\u00edch chu\u1ed7i x\u1eed l\u00fd',

    '\u53ef\u4ee5\u628a\u5b83\u7406\u89e3\u6210\u4e24\u6761\u7ba1\u7ebf\u3002':
        'C\u00f3 th\u1ec3 hi\u1ec3u n\u00f3 nh\u01b0 hai \u0111\u01b0\u1eddng \u1ed1ng x\u1eed l\u00fd.',

    '\u7ba1\u7ebf A\uff1a\u542c\u61c2\u7528\u6237\uff08ASR\uff09':
        '\u0110\u01b0\u1eddng \u1ed1ng A: Nghe hi\u1ec3u ng\u01b0\u1eddi d\u00f9ng (ASR)',

    'Discord \u6536\u5230\u8bed\u97f3\u9644\u4ef6\uff08\u5e38\u89c1 OGG/Opus\uff09':
        'Discord nh\u1eadn \u0111\u01b0\u1ee3c t\u1ec7p \u0111\u00ednh k\u00e8m gi\u1ecdng n\u00f3i (th\u01b0\u1eddng l\u00e0 OGG/Opus)',

    'OpenClaw \u547d\u4e2d tools.media.audio \u89c4\u5219':
        'OpenClaw kh\u1edbp v\u1edbi quy t\u1eafc tools.media.audio',

    '\u8c03\u7528\u8f6c\u5199\u811a\u672c transcribe.py ':
        'G\u1ecdi script chuy\u1ec3n \u0111\u1ed5i transcribe.py ',

    '\u8f93\u51fa transcript\uff08\u6587\u672c\uff09':
        'Xu\u1ea5t transcript (v\u0103n b\u1ea3n)',

    'transcript \u6ce8\u5165\u4f1a\u8bdd\uff0c\u4f9b\u6a21\u578b\u7406\u89e3':
        'Transcript \u0111\u01b0\u1ee3c \u0111\u01b0a v\u00e0o h\u1ed9i tho\u1ea1i, cung c\u1ea5p cho m\u00f4 h\u00ecnh hi\u1ec3u',

    '\u4e00\u53e5\u8bdd\uff1a ':
        'T\u00f3m l\u1ea1i: ',

    'ASR = \u8033\u6735 + \u901f\u8bb0\u3002':
        'ASR = Tai nghe + Ghi ch\u00e9p nhanh.',

    '\u7ba1\u7ebf B\uff1a\u628a\u56de\u590d\u8bf4\u51fa\u6765\uff08TTS\uff09':
        '\u0110\u01b0\u1eddng \u1ed1ng B: Ph\u00e1t ph\u1ea3n h\u1ed3i b\u1eb1ng gi\u1ecdng n\u00f3i (TTS)',

    'Agent \u5148\u4ea7\u51fa\u56de\u590d\u6587\u672c':
        'Agent t\u1ea1o ra v\u0103n b\u1ea3n ph\u1ea3n h\u1ed3i tr\u01b0\u1edbc',

    '\u547d\u4e2d TTS \u914d\u7f6e\uff08\u5168\u5c40\u5c42 + Discord voice \u5c42\uff09':
        'Kh\u1edbp c\u1ea5u h\u00ecnh TTS (t\u1ea7ng to\u00e0n c\u1ee5c + t\u1ea7ng Discord voice)',

    '\u7528\u6307\u5b9a model + voice \u5408\u6210\u97f3\u9891':
        'T\u1ed5ng h\u1ee3p \u00e2m thanh b\u1eb1ng model + voice \u0111\u01b0\u1ee3c ch\u1ec9 \u0111\u1ecbnh',

    '\u5728 Discord \u8f93\u51fa\u8bed\u97f3\u56de\u590d':
        'Xu\u1ea5t ph\u1ea3n h\u1ed3i gi\u1ecdng n\u00f3i tr\u00ean Discord',

    'TTS = \u914d\u97f3 + \u64ad\u653e\u3002':
        'TTS = L\u1ed3ng ti\u1ebfng + Ph\u00e1t l\u1ea1i.',

    '\u5f53 A+B \u540c\u65f6\u8dd1\u901a\uff0c\u8bed\u97f3\u5bf9\u8bdd\u624d\u7b97\u95ed\u73af\u3002':
        'Khi A+B \u0111\u1ed3ng th\u1eddi ch\u1ea1y th\u00f4ng su\u1ed1t, h\u1ed9i tho\u1ea1i gi\u1ecdng n\u00f3i m\u1edbi t\u1ea1o th\u00e0nh v\u00f2ng l\u1eb7p kh\u00e9p k\u00edn.',

    '\u4e09\u3001\u5173\u952e\u914d\u7f6e\uff08\u7ed9\u590d\u76d8\u8005\uff09':
        '3. C\u1ea5u h\u00ecnh quan tr\u1ecdng (d\u00e0nh cho ng\u01b0\u1eddi review)',

    '\u672c\u6b21\u94fe\u8def\u91cc\u7684\u6838\u5fc3\u53c2\u6570\u5982\u4e0b\uff1a':
        'C\u00e1c tham s\u1ed1 c\u1ed1t l\u00f5i trong chu\u1ed7i x\u1eed l\u00fd l\u1ea7n n\u00e0y nh\u01b0 sau:',

    'ASR \u5165\u53e3\uff1a tools.media.audio.models[0] \uff08CLI\uff09':
        '\u0110\u1ea7u v\u00e0o ASR: tools.media.audio.models[0] (CLI)',

    '\u8f6c\u5199\u811a\u672c\uff1a transcribe.py':
        'Script chuy\u1ec3n \u0111\u1ed5i: transcribe.py',

    'ASR \u6a21\u578b\uff1a fun-asr-realtime':
        'M\u00f4 h\u00ecnh ASR: fun-asr-realtime',

    'TTS \u6a21\u578b\uff1a qwen3-tts-vd-realtime':
        'M\u00f4 h\u00ecnh TTS: qwen3-tts-vd-realtime',

    'Base voice\uff1a qwen-tts-vd-lucky_guardian-voice':
        'Base voice: qwen-tts-vd-lucky_guardian-voice',

    'TTS bridge\uff1a OPENAI_TTS_BASE_URL=http://127.0.0.1:19790/v1':
        'TTS bridge: OPENAI_TTS_BASE_URL=http://127.0.0.1:19790/v1',

    '\u53e6\u5916\u4e00\u4e2a\u975e\u5e38\u5b9e\u7528\u7684\u7ec6\u8282\uff1a transcribe.py \u5df2\u5904\u7406 Discord \u5e38\u89c1\u97f3\u9891\u683c\u5f0f\u517c\u5bb9\u548c\u91c7\u6837\u7387\u5bb9\u9519\u3002 \u8fd9\u7c7b\u201c\u770b\u4e0d\u89c1\u201d\u7684\u9002\u914d\uff0c\u5f80\u5f80\u6bd4\u6a21\u578b\u540d\u66f4\u5f71\u54cd\u7a33\u5b9a\u6027\u3002':
        'Ngo\u00e0i ra m\u1ed9t chi ti\u1ebft r\u1ea5t th\u1ef1c t\u1ebf: transcribe.py \u0111\u00e3 x\u1eed l\u00fd t\u01b0\u01a1ng th\u00edch \u0111\u1ecbnh d\u1ea1ng \u00e2m thanh ph\u1ed5 bi\u1ebfn c\u1ee7a Discord v\u00e0 dung sai t\u1ea7n s\u1ed1 l\u1ea5y m\u1eabu. Nh\u1eefng th\u00edch \u1ee9ng "v\u00f4 h\u00ecnh" ki\u1ec3u n\u00e0y th\u01b0\u1eddng \u1ea3nh h\u01b0\u1edfng \u0111\u1ebfn t\u00ednh \u1ed5n \u0111\u1ecbnh nhi\u1ec1u h\u01a1n c\u1ea3 t\u00ean m\u00f4 h\u00ecnh.',

    '\u56db\u3001Voice Design\uff1a\u97f3\u8272\u4e3a\u4ec0\u4e48\u80fd\u53d8\uff0c\u4f46\u201c\u8fd8\u662f\u540c\u4e00\u4e2a\u4eba\u201d':
        '4. Voice Design: T\u1ea1i sao gi\u1ecdng n\u00f3i c\u00f3 th\u1ec3 thay \u0111\u1ed5i, nh\u01b0ng "v\u1eabn l\u00e0 c\u00f9ng m\u1ed9t ng\u01b0\u1eddi"',

    '\u8fd9\u662f\u6700\u5bb9\u6613\u8bb2\u7a7a\u3001\u4f46\u6700\u5f71\u54cd\u4f53\u9a8c\u7684\u90e8\u5206\u3002':
        '\u0110\u00e2y l\u00e0 ph\u1ea7n d\u1ec5 n\u00f3i su\u00f4ng nh\u1ea5t, nh\u01b0ng \u1ea3nh h\u01b0\u1edfng \u0111\u1ebfn tr\u1ea3i nghi\u1ec7m nhi\u1ec1u nh\u1ea5t.',

    '\u63a8\u8350\u91c7\u7528\u201c\u4e24\u5c42\u6cd5\u201d\uff1a':
        'Khuy\u1ebfn ngh\u1ecb s\u1eed d\u1ee5ng "ph\u01b0\u01a1ng ph\u00e1p hai t\u1ea7ng":',

    '\u5c42 1\uff1aBase Voice\uff08\u8eab\u4efd\u5c42\uff09':
        'T\u1ea7ng 1: Base Voice (T\u1ea7ng danh t\u00ednh)',

    '\u51b3\u5b9a\u201c\u662f\u8c01\u5728\u8bf4\u8bdd\u201d\uff1a':
        'Quy\u1ebft \u0111\u1ecbnh "ai \u0111ang n\u00f3i":',

    '\u58f0\u7ebf\u57fa\u7840\u8d28\u611f':
        'Ch\u1ea5t gi\u1ecdng c\u01a1 b\u1ea3n',

    '\u5e74\u9f84\u611f':
        'C\u1ea3m gi\u00e1c tu\u1ed5i t\u00e1c',

    '\u4eba\u8bbe\u8bc6\u522b\u5ea6':
        '\u0110\u1ed9 nh\u1eadn di\u1ec7n nh\u00e2n v\u1eadt',

    '\u8fd9\u4e00\u5c42\u5efa\u8bae\u7a33\u5b9a\uff0c\u4e0d\u8981\u9891\u7e41\u6362\u3002':
        'T\u1ea7ng n\u00e0y n\u00ean gi\u1eef \u1ed5n \u0111\u1ecbnh, kh\u00f4ng n\u00ean thay \u0111\u1ed5i th\u01b0\u1eddng xuy\u00ean.',

    '\u5c42 2\uff1aRuntime Instructions\uff08\u72b6\u6001\u5c42\uff09':
        'T\u1ea7ng 2: Runtime Instructions (T\u1ea7ng tr\u1ea1ng th\u00e1i)',

    '\u51b3\u5b9a\u201c\u8fd9\u4e2a\u4eba\u73b0\u5728\u600e\u4e48\u8bf4\u8bdd\u201d\uff1a':
        'Quy\u1ebft \u0111\u1ecbnh "ng\u01b0\u1eddi n\u00e0y hi\u1ec7n t\u1ea1i n\u00f3i nh\u01b0 th\u1ebf n\u00e0o":',

    '\u8bed\u901f':
        'T\u1ed1c \u0111\u1ed9 n\u00f3i',

    '\u547c\u5438\u611f':
        'C\u1ea3m gi\u00e1c h\u01a1i th\u1edf',

    '\u5c3e\u97f3':
        '\u00c2m cu\u1ed1i',

    '\u60c5\u7eea\u6e29\u5ea6':
        'Nhi\u1ec7t \u0111\u1ed9 c\u1ea3m x\u00fac',

    '\u4eb2\u5bc6/\u7406\u6027\u7a0b\u5ea6':
        'M\u1ee9c \u0111\u1ed9 th\u00e2n m\u1eadt / l\u00fd tr\u00ed',

    '\u8fd9\u6837\u505a\u7684\u597d\u5904\u662f\uff1a':
        'L\u1ee3i \u00edch c\u1ee7a c\u00e1ch l\u00e0m n\u00e0y:',

    '\u65e2\u80fd\u505a\u573a\u666f\u5316\u53d8\u5316\uff08\u5de5\u4f5c/\u966a\u4f34/\u591c\u804a\uff09':
        'V\u1eeba c\u00f3 th\u1ec3 thay \u0111\u1ed5i theo ng\u1eef c\u1ea3nh (c\u00f4ng vi\u1ec7c / \u0111\u1ed3ng h\u00e0nh / tr\u00f2 chuy\u1ec7n \u0111\u00eam)',

    '\u53c8\u4e0d\u4f1a\u628a\u89d2\u8272\u4e00\u81f4\u6027\u6253\u6563':
        'V\u1eeba kh\u00f4ng l\u00e0m m\u1ea5t t\u00ednh nh\u1ea5t qu\u00e1n c\u1ee7a nh\u00e2n v\u1eadt',

    '\u4e5f\u5c31\u662f\uff1a ':
        'N\u00f3i c\u00e1ch kh\u00e1c: ',

    '\u72b6\u6001\u53ef\u53d8\uff0c\u8eab\u4efd\u4e0d\u4e22\u3002':
        'Tr\u1ea1ng th\u00e1i c\u00f3 th\u1ec3 thay \u0111\u1ed5i, danh t\u00ednh kh\u00f4ng m\u1ea5t.',

    '\u4e94\u3001\u97f3\u8272\u8c03\u4f18\u5efa\u8bae\uff08\u5b9e\u6218\u987a\u5e8f\uff09':
        '5. G\u1ee3i \u00fd tinh ch\u1ec9nh gi\u1ecdng n\u00f3i (th\u1ee9 t\u1ef1 th\u1ef1c chi\u1ebfn)',

    '别一上来就疯狂换 voice id。':
        'Đừng vội vàng thay đổi voice id ngay từ đầu.',

    '\u6b63\u786e\u987a\u5e8f\u901a\u5e38\u662f\uff1a':
        'Th\u1ee9 t\u1ef1 \u0111\u00fang th\u01b0\u1eddng l\u00e0:',

    '\u5148\u9501\u5b9a Base Voice\uff08\u4fdd\u8bc1\u4eba\u683c\u8fde\u7eed\uff09':
        'Tr\u01b0\u1edbc ti\u00ean kh\u00f3a Base Voice (\u0111\u1ea3m b\u1ea3o t\u00ednh li\u00ean t\u1ee5c c\u1ee7a nh\u00e2n c\u00e1ch)',

    '\u518d\u8c03 instructions\uff08\u62ff\u5230\u60f3\u8981\u7684\u542c\u611f\uff09':
        'Sau \u0111\u00f3 \u0111i\u1ec1u ch\u1ec9nh instructions (\u0111\u1ea1t \u0111\u01b0\u1ee3c c\u1ea3m gi\u00e1c nghe mong mu\u1ed1n)',

    '\u6700\u540e\u6309\u573a\u666f\u6c89\u6dc0\u9884\u8bbe':
        'Cu\u1ed1i c\u00f9ng l\u01b0u preset theo ng\u1eef c\u1ea3nh',

    '\u793a\u4f8b\u9884\u8bbe\uff1a':
        'Preset m\u1eabu:',

    '\u5de5\u4f5c\u6a21\u5f0f\uff1a\u6e05\u6670\u3001\u5229\u843d\u3001\u8bed\u901f\u7565\u5feb':
        'Ch\u1ebf \u0111\u1ed9 l\u00e0m vi\u1ec7c: R\u00f5 r\u00e0ng, g\u1ecdn g\u00e0ng, t\u1ed1c \u0111\u1ed9 n\u00f3i h\u01a1i nhanh',

    '\u966a\u4f34\u6a21\u5f0f\uff1a\u67d4\u548c\u3001\u7a0d\u6162\u3001\u505c\u987f\u81ea\u7136':
        'Ch\u1ebf \u0111\u1ed9 \u0111\u1ed3ng h\u00e0nh: Nh\u1eb9 nh\u00e0ng, h\u01a1i ch\u1eadm, ng\u1eaft ngh\u1ec9 t\u1ef1 nhi\u00ean',

    '\u591c\u95f4\u6a21\u5f0f\uff1a\u52a8\u6001\u66f4\u5c0f\u3001\u8bed\u6c14\u66f4\u8f7b':
        'Ch\u1ebf \u0111\u1ed9 ban \u0111\u00eam: Bi\u00ean \u0111\u1ed9 nh\u1ecf h\u01a1n, gi\u1ecdng nh\u1eb9 h\u01a1n',

    '\u8fd9\u6837\u8c03\uff0c\u7a33\u5b9a\u4e14\u53ef\u590d\u7528\u3002':
        '\u0110i\u1ec1u ch\u1ec9nh nh\u01b0 v\u1eady, \u1ed5n \u0111\u1ecbnh v\u00e0 c\u00f3 th\u1ec3 t\u00e1i s\u1eed d\u1ee5ng.',

    '\u516d\u3001\u8fd9\u6761\u94fe\u8def\u7684\u957f\u671f\u4ef7\u503c':
        '6. Gi\u00e1 tr\u1ecb d\u00e0i h\u1ea1n c\u1ee7a chu\u1ed7i x\u1eed l\u00fd n\u00e0y',

    '\u77ed\u671f\u770b\uff0c\u662f\u201c\u7ec8\u4e8e\u80fd\u8bed\u97f3\u804a\u4e86\u201d\u3002':
        'Nh\u00ecn ng\u1eafn h\u1ea1n, \u0111\u00f3 l\u00e0 "cu\u1ed1i c\u00f9ng c\u0169ng c\u00f3 th\u1ec3 tr\u00f2 chuy\u1ec7n b\u1eb1ng gi\u1ecdng n\u00f3i".',

    '\u957f\u671f\u770b\uff0c\u662f\u642d\u597d\u4e86\u4e00\u4e2a\u6301\u7eed\u4f18\u5316\u63a5\u53e3\uff1a':
        'Nh\u00ecn d\u00e0i h\u1ea1n, \u0111\u00f3 l\u00e0 \u0111\u00e3 x\u00e2y d\u1ef1ng m\u1ed9t giao di\u1ec7n t\u1ed1i \u01b0u h\u00f3a li\u00ean t\u1ee5c:',

    'ASR \u70ed\u8bcd':
        'T\u1eeb kh\u00f3a n\u00f3ng ASR',

    '\u53e3\u8bed\u7ea0\u9519':
        'S\u1eeda l\u1ed7i kh\u1ea9u ng\u1eef',

    '\u65ad\u53e5\u7b56\u7565':
        'Chi\u1ebfn l\u01b0\u1ee3c ng\u1eaft c\u00e2u',

    '\u60c5\u7eea\u5316\u8bed\u97f3\u6a21\u677f':
        'M\u1eabu gi\u1ecdng n\u00f3i c\u1ea3m x\u00fac',

    '\u591a\u97f3\u8272 persona \u9884\u8bbe':
        'Preset persona \u0111a gi\u1ecdng',

    '\u6bcf\u4e00\u6b21\u5fae\u8c03\uff0c\u90fd\u4f1a\u76f4\u63a5\u53cd\u6620\u5728\u771f\u5b9e\u5bf9\u8bdd\u4f53\u9a8c\u4e0a\u3002':
        'M\u1ed7i l\u1ea7n tinh ch\u1ec9nh \u0111\u1ec1u ph\u1ea3n \u00e1nh tr\u1ef1c ti\u1ebfp l\u00ean tr\u1ea3i nghi\u1ec7m h\u1ed9i tho\u1ea1i th\u1ef1c t\u1ebf.',

    '\u8fd9\u624d\u662f\u503c\u5f97\u6295\u5165\u7684\u5730\u65b9\u3002':
        '\u0110\u00e2y m\u1edbi l\u00e0 n\u01a1i \u0111\u00e1ng \u0111\u1ec3 \u0111\u1ea7u t\u01b0.',

    '\u4e03\u3001\u7ed3\u8bed':
        '7. K\u1ebft lu\u1eadn',

    '\u4e00\u5957\u8bed\u97f3 AI \u7cfb\u7edf\u6700\u96be\u7684\uff0c\u4ece\u6765\u4e0d\u662f\u201c\u8ba9\u5b83\u4f1a\u8bf4\u8bdd\u201d\u3002 \u800c\u662f\u8ba9\u5b83\u5728\u771f\u5b9e\u573a\u666f\u91cc\uff0c ':
        '\u0110i\u1ec1u kh\u00f3 nh\u1ea5t c\u1ee7a m\u1ed9t h\u1ec7 th\u1ed1ng AI gi\u1ecdng n\u00f3i, ch\u01b0a bao gi\u1edd l\u00e0 "l\u00e0m cho n\u00f3 bi\u1ebft n\u00f3i". M\u00e0 l\u00e0 l\u00e0m cho n\u00f3 trong ng\u1eef c\u1ea3nh th\u1ef1c t\u1ebf, ',

    '\u542c\u5f97\u51c6\u3001\u56de\u5f97\u7a33\u3001\u58f0\u97f3\u50cf\u540c\u4e00\u4e2a\u4eba ':
        'nghe ch\u00ednh x\u00e1c, ph\u1ea3n h\u1ed3i \u1ed5n \u0111\u1ecbnh, gi\u1ecdng n\u00f3i gi\u1ed1ng c\u00f9ng m\u1ed9t ng\u01b0\u1eddi ',

    '\u3002':
        '.',

    '\u5f53 ASR\u3001TTS\u3001Voice Design \u8fdb\u5165\u540c\u4e00\u6761\u95ed\u73af\u540e\uff0c':
        'Khi ASR, TTS, Voice Design c\u00f9ng \u0111i v\u00e0o m\u1ed9t v\u00f2ng l\u1eb7p kh\u00e9p k\u00edn,',

    '\u8bed\u97f3\u52a9\u624b\u624d\u4f1a\u4ece\u201c\u6f14\u793a\u6548\u679c\u201d\u8d70\u5411\u201c\u65e5\u5e38\u53ef\u7528\u201d\u3002':
        'tr\u1ee3 l\u00fd gi\u1ecdng n\u00f3i m\u1edbi \u0111i t\u1eeb "hi\u1ec7u \u1ee9ng demo" \u0111\u1ebfn "s\u1eed d\u1ee5ng h\u00e0ng ng\u00e0y".',
}

# Keep these as-is
keep_as_is = {'Original Lucky'}

translated_count = 0
kept_count = 0
untranslated = []

for block in data['blocks']:
    for el in block['elements']:
        if el['type'] != 'text_run':
            continue
        content = el['content']

        if content in keep_as_is:
            kept_count += 1
            continue

        if el.get('style', {}).get('link'):
            kept_count += 1
            continue

        if content in trans:
            el['content'] = trans[content]
            translated_count += 1
        else:
            has_chinese = bool(re.search(r'[\u4e00-\u9fff]', content))
            if has_chinese:
                untranslated.append(content[:80])
            else:
                kept_count += 1

with open('_art_b7_8_trans.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'Translated: {translated_count}, Kept: {kept_count}')
if untranslated:
    print(f'UNTRANSLATED ({len(untranslated)}):')
    for t in untranslated:
        print(f'  - {t}')
else:
    print('All Chinese text translated successfully!')
print(f'Saved to _art_b7_8_trans.json')
