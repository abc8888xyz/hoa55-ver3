import sys
sys.stdout.reconfigure(encoding='utf-8')
import json, copy

with open('_art_b7_6_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

trans = copy.deepcopy(data)

# Translation map: block index -> list of translated content for each text_run element
# None = keep original (for URLs, UUIDs, technical terms that should not be translated)
translations_vi = {
    0: ['Day03 | Ng\u00e0y th\u1ee9 ba c\u1ee7a T\u00f4m h\u00f9m Lucky: Tr\u01b0\u1edbc ti\u00ean h\u00e3y t\u1ea1o h\u00ecnh \u1ea3nh, NETA l\u00e0 con dao h\u1eefu \u00edch nh\u1ea5t c\u1ee7a t\u00f4i h\u00f4m nay'],
    1: ['\U0001f517 Link b\u00e0i g\u1ed1c: ', None],
    2: ['Larkspur chia s\u1ebb k\u1ef9 thu\u1eadt Larkspur chia s\u1ebb k\u1ef9 thu\u1eadt Little Shock', 'Ng\u00e0y 3 th\u00e1ng 3 n\u0103m 2026 21:35 Th\u01b0\u1ee3ng H\u1ea3i'],
    3: ['Original Lucky'],
    4: ['Ng\u00e0y 3 th\u00e1ng 3 n\u0103m 2026 19:29'],
    5: ['\u0110\u00e2y l\u00e0 \u1ea3nh b\u00eca \u0111\u01b0\u1ee3c t\u1ea1o th\u1ef1c t\u1ebf b\u1eb1ng NETA h\u00f4m nay (16:9, 2720\u00d71568).'],
    6: ['M\u1ed9t, T\u1ea1i sao h\u00f4m nay l\u1ea1i vi\u1ebft v\u1ec1 NETA tr\u01b0\u1edbc'],
    7: ['H\u00f4m qua ch\u00fang t\u00f4i \u0111ang l\u00e0m "T\u1ef1 \u0111\u1ed9ng h\u00f3a l\u01b0u tr\u1eef" \u2014 \u0111\u1ea7u v\u00e0o, li\u00ean k\u1ebft, nh\u1eadp kho, t\u1ea5t c\u1ea3 \u0111\u1ec1u ch\u1ea1y tr\u01a1n.'],
    8: ['H\u00f4m nay Lark \u0111\u01b0a ra m\u1ed9t y\u00eau c\u1ea7u r\u1ea5t thi\u1ebft th\u1ef1c:'],
    9: ['Nh\u1eadt k\u00fd kh\u00f4ng ch\u1ec9 c\u1ea7n vi\u1ebft \u0111\u01b0\u1ee3c, m\u00e0 c\u00f2n ph\u1ea3i c\u00f3 th\u1ec3 ch\u00e8n h\u00ecnh minh h\u1ecda; h\u01a1n n\u1eefa kh\u1ea3 n\u0103ng t\u1ea1o h\u00ecnh n\u00e0y ph\u1ea3i c\u00f3 th\u1ec3 t\u00e1i s\u1eed d\u1ee5ng.'],
    10: ['V\u00ec v\u1eady Day03 kh\u00f4ng tham nhi\u1ec1u, tr\u01b0\u1edbc ti\u00ean h\u00e3y gi\u1ea3i th\u00edch k\u1ef9 v\u1ec1 "t\u1ea1o h\u00ecnh" c\u1ee7a NETA.'],
    11: ['\u00c2m nh\u1ea1c v\u00e0 video s\u1ebd m\u1edf r\u1ed9ng sau, kh\u00f4ng gi\u00e0nh s\u00e2n kh\u1ea5u.'],
    12: ['Hai, V\u1ecb tr\u00ed c\u1ee7a NETA trong quy tr\u00ecnh l\u00e0m vi\u1ec7c c\u1ee7a ch\u00fang t\u00f4i'],
    13: ['M\u1ed9t c\u00e2u:'],
    14: ['OpenClaw ph\u1ee5 tr\u00e1ch th\u1ef1c thi, Obsidian ph\u1ee5 tr\u00e1ch ghi nh\u1edb, NETA ph\u1ee5 tr\u00e1ch bi\u1ec3u \u0111\u1ea1t tr\u1ef1c quan.'],
    15: ['Khi b\u00e0i vi\u1ebft c\u00f3 c\u1ea5u tr\u00fac, c\u00f3 quan \u0111i\u1ec3m, th\u00eam v\u00e0o \u0111\u00f3 h\u00ecnh \u1ea3nh minh h\u1ecda \u0111\u1ed3ng nh\u1ea5t v\u1ec1 phong c\u00e1ch, ch\u1ea5t l\u01b0\u1ee3ng xu\u1ea5t b\u1ea3n s\u1ebd n\u00e2ng l\u00ean m\u1ed9t t\u1ea7m r\u00f5 r\u1ec7t.'],
    16: ['\u0110\u00e2y kh\u00f4ng ch\u1ec9 l\u00e0 "\u0111\u1eb9p h\u01a1n m\u1ed9t ch\u00fat", m\u00e0 l\u00e0 gi\u1ea3m ng\u01b0\u1ee1ng hi\u1ec3u bi\u1ebft cho ng\u01b0\u1eddi \u0111\u1ecdc.'],
    17: ['Ba, B\u1ed5 sung m\u1ed9t b\u1ed1i c\u1ea3nh quan tr\u1ecdng: NETA \u0111\u01b0\u1ee3c c\u00e0i \u0111\u1eb7t \u1edf \u0111\u00e2u, c\u00f3 th\u1ec3 l\u00e0m g\u00ec'],
    18: ['Nhi\u1ec1u \u0111\u1ecdc gi\u1ea3 s\u1ebd h\u1ecfi: NETA c\u1ee7a b\u1ea1n ch\u00ednh x\u00e1c l\u00e0 g\u00ec? C\u00e0i \u0111\u1eb7t \u1edf \u0111\u00e2u?'],
    19: ['T\u00f4i \u0111ang d\u00f9ng kho k\u1ef9 n\u0103ng n\u00e0y (c\u1ea3m \u01a1n Ni\u1ebf ta, c\u1ea3m \u01a1n \u0110\u1ea7u gia):'],
    20: ['\u0110\u1ecba ch\u1ec9 d\u1ef1 \u00e1n: https://github.com/talesofai/neta-skills'],
    21: ['\u0110i\u1ec1u ki\u1ec7n s\u1eed d\u1ee5ng: C\u1ea7n c\u1ea5u h\u00ecnh bi\u1ebfn m\u00f4i tr\u01b0\u1eddng NETA_TOKEN'],
    22: ['N\u1ebfu b\u1ea1n l\u00e0 ng\u01b0\u1eddi d\u00f9ng OpenClaw, con \u0111\u01b0\u1eddng c\u00e0i \u0111\u1eb7t t\u1ed1i thi\u1ec3u c\u00f3 th\u1ec3 theo 4 b\u01b0\u1edbc n\u00e0y:'],
    23: ['N\u00f3 kh\u00f4ng ch\u1ec9 t\u1ea1o h\u00ecnh, m\u00e0 kh\u1ea3 n\u0103ng l\u00e0 chu\u1ed7i media ho\u00e0n ch\u1ec9nh:'],
    24: ['T\u1ea1o h\u00ecnh \u1ea3nh: make-image'],
    25: ['T\u1ea1o video: make-video'],
    26: ['T\u1ea1o b\u00e0i h\u00e1t: make-song'],
    27: ['Gh\u00e9p video / MV: merge-video'],
    28: ['T\u00e1ch n\u1ec1n: remove-background'],
    29: ['T\u00ecm ki\u1ebfm nh\u00e2n v\u1eadt/y\u1ebfu t\u1ed1: search-tcp, request-character'],
    30: ['Nghi\u00ean c\u1ee9u hashtag: get-hashtag-info, get-hashtag-characters, get-hashtag-collections'],
    31: ['B\u00e0i h\u00f4m nay tr\u01b0\u1edbc ti\u00ean t\u1eadp trung v\u00e0o ', 't\u1ea1o h\u00ecnh ', '. Sau n\u00e0y t\u00f4i s\u1ebd vi\u1ebft th\u00eam hai b\u00e0i n\u1eefa: t\u1ea1o nh\u1ea1c, t\u1ea1o video.'],
    32: ['B\u1ed1n, K\u1ebft lu\u1eadn tr\u01b0\u1edbc: Quy tr\u00ecnh t\u1ea1o h\u00ecnh t\u1ed1i thi\u1ec3u (3 b\u01b0\u1edbc)'],
    33: ['B\u01b0\u1edbc 1) X\u00e1c \u0111\u1ecbnh m\u1ee5c ti\u00eau h\u00ecnh \u1ea3nh'],
    34: ['Tr\u01b0\u1edbc ti\u00ean vi\u1ebft m\u1ed9t c\u00e2u "B\u1ee9c h\u00ecnh n\u00e0y d\u00f9ng \u0111\u1ec3 l\u00e0m g\u00ec":'],
    35: ['L\u00e0 \u1ea3nh b\u00eca hay h\u00ecnh gi\u1ea3i th\u00edch trong b\u00e0i?'],
    36: ['Mu\u1ed1n n\u1ed5i b\u1eadt nh\u00e2n v\u1eadt hay n\u1ed5i b\u1eadt quy tr\u00ecnh?'],
    37: ['Cho t\u00e0i kho\u1ea3n c\u00f4ng khai xem hay cho b\u00eca video ng\u1eafn?'],
    38: ['B\u01b0\u1edbc 2) Vi\u1ebft Prompt'],
    39: ['C\u1ea5u tr\u00fac t\u00f4i \u0111ang d\u00f9ng l\u00e0:'],
    40: ['N\u1ec1n t\u1ea3ng nh\u00e2n v\u1eadt + Y\u1ebfu t\u1ed1 n\u1ed9i dung b\u00e0i vi\u1ebft + R\u00e0ng bu\u1ed9c phong c\u00e1ch v\u00e0 ch\u1ea5t l\u01b0\u1ee3ng'],
    41: ['V\u00ed d\u1ee5 c\u1ed1t l\u00f5i c\u1ee7a b\u1ee9c h\u00ecnh h\u00f4m nay l\u00e0:'],
    42: ['N\u1ec1n t\u1ea3ng nh\u00e2n v\u1eadt: T\u00f3c h\u1ed3ng ng\u1eafn, vest xanh \u0111\u1eadm, m\u0169 t\u00f4m h\u00f9m (\u0111i\u1ec3m neo th\u1ecb gi\u00e1c c\u1ee7a Lucky)'],
    43: ['Y\u1ebfu t\u1ed1 n\u1ed9i dung: B\u00e0n l\u00e0m vi\u1ec7c t\u1ea1o h\u00ecnh NETA, \u00f4 nh\u1eadp prompt, aspect 16:9, b\u1ea3ng k\u1ebft qu\u1ea3 t\u1ea1o h\u00ecnh'],
    44: ['R\u00e0ng bu\u1ed9c phong c\u00e1ch: Anime, c\u1ea3m gi\u00e1c Jujutsu Kaisen, b\u1ed1 c\u1ee5c s\u1ea1ch s\u1ebd, kh\u00f4ng watermark'],
    45: ['B\u01b0\u1edbc 3) T\u1ea1o h\u00ecnh v\u00e0 l\u1eb7p l\u1ea1i'],
    46: ['L\u1ec7nh s\u1eed d\u1ee5ng tr\u1ef1c ti\u1ebfp:'],
    47: ['N\u1ebfu h\u00ecnh \u0111\u1ea7u ti\u00ean \u0111\u00fang h\u01b0\u1edbng, ch\u1ec9 th\u1ef1c hi\u1ec7n thay \u0111\u1ed5i t\u1ed1i thi\u1ec3u \u0111\u1ec3 l\u1eb7p l\u1ea1i, kh\u00f4ng n\u00ean l\u00e0m l\u1ea1i t\u1eeb \u0111\u1ea7u m\u1ed7i l\u1ea7n.'],
    48: ['N\u0103m, Phi\u00ean b\u1ea3n th\u1ef1c h\u00e0nh cho ng\u01b0\u1eddi d\u00f9ng OpenClaw (c\u00f3 th\u1ec3 sao ch\u00e9p)'],
    49: ['1) L\u1ec7nh c\u01a1 b\u1ea3n'],
    50: ['T\u1ef7 l\u1ec7 th\u01b0\u1eddng d\u00f9ng (\u01b0u ti\u00ean t\u00e0i kho\u1ea3n c\u00f4ng khai):'],
    51: ['16:9: B\u00eca \u0111a n\u0103ng, c\u00f3 th\u1ec3 c\u1eaft sau'],
    52: ['3:4: Poster d\u1ecdc / h\u00ecnh nh\u00e2n v\u1eadt'],
    53: ['1:1: Avatar, th\u1ebb, h\u00ecnh vu\u00f4ng'],
    54: ['2) Nh\u1eadt k\u00fd s\u1ea3n ph\u1ea9m t\u00f4i khuy\u00ean n\u00ean gi\u1eef l\u1ea1i'],
    55: ['M\u1ed7i l\u1ea7n t\u1ea1o h\u00ecnh \u0111\u1ec1u ghi l\u1ea1i 4 tr\u01b0\u1eddng n\u00e0y:'],
    56: ['prompt'],
    57: ['aspect'],
    58: ['task_uuid'],
    59: ['image_url'],
    60: ['V\u00ed d\u1ee5 h\u00f4m nay:'],
    61: ['task_uuid:', None],
    62: ['image_url:', None],
    63: ['3) C\u00e1ch x\u1eed l\u00fd c\u00e1c l\u1ed7i th\u01b0\u1eddng g\u1eb7p'],
    64: [None, ': Tr\u01b0\u1edbc ti\u00ean r\u00fat ng\u1eafn prompt, gi\u1ea3m m\u00f4 t\u1ea3 th\u1eeba r\u1ed3i th\u1eed l\u1ea1i'],
    65: [None, ': Tr\u01b0\u1edbc ti\u00ean c\u1ed1 \u0111\u1ecbnh n\u1ec1n t\u1ea3ng nh\u00e2n v\u1eadt, sau \u0111\u00f3 b\u1ed5 sung y\u1ebfu t\u1ed1 n\u1ed9i dung'],
    66: [None, ': Ghi r\u00f5 "ch\u1ee7 th\u1ec3 \u1edf gi\u1eefa + danh s\u00e1ch y\u1ebfu t\u1ed1 b\u1eaft bu\u1ed9c" trong prompt'],
    67: ['S\u00e1u, H\u00f4m nay t\u00f4i \u0111\u00e3 vi\u1ebft Prompt cho b\u1ee9c h\u00ecnh n\u00e0y nh\u01b0 th\u1ebf n\u00e0o'],
    68: ['M\u1ee5c ti\u00eau phi\u00ean b\u1ea3n n\u00e0y r\u1ea5t \u0111\u01a1n gi\u1ea3n: ', 'Tr\u01b0\u1edbc ti\u00ean gi\u1ea3i th\u00edch r\u00f5 r\u00e0ng "NETA c\u00f3 th\u1ec3 t\u1ea1o h\u00ecnh", sau \u0111\u00f3 c\u1ed1 \u0111\u1ecbnh danh t\u00ednh tr\u1ef1c quan c\u1ee7a Lucky.'],
    69: ['B\u1ea3y, K\u1ebft th\u00fac Day03'],
    70: ['H\u00f4m nay ch\u00fang t\u00f4i kh\u00f4ng theo \u0111u\u1ed5i "\u0111\u1ea7y \u0111\u1ee7 v\u00e0 to\u00e0n di\u1ec7n".'],
    71: ['Ch\u1ec9 l\u00e0m m\u1ed9t vi\u1ec7c c\u00f3 th\u1ec3 t\u00e1i s\u1eed d\u1ee5ng:'],
    72: ['NETA t\u1ea1o h\u00ecnh, t\u1eeb c\u1ea3m h\u1ee9ng \u0111\u1ebfn s\u1ea3n ph\u1ea9m, \u0111\u00e3 tr\u1edf th\u00e0nh m\u1ed9t thao t\u00e1c ti\u00eau chu\u1ea9n.'],
    73: ['B\u00e0i ti\u1ebfp theo ch\u00fang t\u00f4i s\u1ebd n\u00f3i v\u1ec1:'],
    74: ['NETA t\u1ea1o nh\u1ea1c (c\u00e1ch t\u1ed5 ch\u1ee9c l\u1eddi b\u00e0i v\u00e0 phong c\u00e1ch)'],
    75: ['NETA t\u1ea1o video (c\u00e1ch bi\u1ebfn h\u00ecnh t\u0129nh th\u00e0nh \u0111\u1ed9ng)'],
    76: ['Tr\u01b0\u1edbc ti\u00ean h\u00e3y ch\u1ea1y \u1ed5n \u0111\u1ecbnh m\u1ea3ng h\u00ecnh \u1ea3nh, sau \u0111\u00f3 m\u1edbi m\u1edf r\u1ed9ng.'],
}

# Stats
total_text_runs = 0
translated_runs = 0
kept_runs = 0

for i, block in enumerate(trans['blocks']):
    if i not in translations_vi:
        continue

    t_list = translations_vi[i]
    text_run_idx = 0

    for j, el in enumerate(block['elements']):
        if el['type'] == 'text_run':
            if text_run_idx < len(t_list):
                total_text_runs += 1
                new_content = t_list[text_run_idx]
                if new_content is not None:
                    el['content'] = new_content
                    translated_runs += 1
                else:
                    kept_runs += 1
            text_run_idx += 1

print(f'Total text_runs processed: {total_text_runs}')
print(f'Translated: {translated_runs}')
print(f'Kept original: {kept_runs}')

with open('_art_b7_6_trans.json', 'w', encoding='utf-8') as f:
    json.dump(trans, f, ensure_ascii=False, indent=2)

print('Saved _art_b7_6_trans.json')
