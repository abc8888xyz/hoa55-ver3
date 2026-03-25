# -*- coding: utf-8 -*-
"""Translate _art_b6_2_orig.json CN->VI and save _art_b6_2_trans.json"""
import json, sys, copy

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

with open('_art_b6_2_orig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Translation mapping: block_index -> list of translations for each text_run
# None means keep original (for code, proper nouns, numbers, commands, etc.)
vi = {
    0: ['L\u1ed9c \u0111\u1ea1o: OpenClaw kh\u00f4ng d\u1ec5 d\u00f9ng? \u0110\u00f3 l\u00e0 v\u00ec b\u1ea1n ch\u01b0a d\u00f9ng Cursor \u0111\u1ec3 "b\u1ea1o c\u1ea3i" \u0110\u1ea1i T\u00f4m H\u00f9m "T\u00e0 \u0110\u1ea1o \u0110\u1ea1i Ph\u00e1p T\u1eadp 4"'],
    1: ['Lo\u1ea1t h\u01b0\u1edbng d\u1eabn | Kh\u00f4ng c\u1ea7n code | Ph\u00f9 h\u1ee3p cho t\u1ea5t c\u1ea3 nh\u1eefng ai mu\u1ed1n d\u00f9ng t\u1ed1t OpenClaw'],
    2: ['\u0110i\u1ec1u ki\u1ec7n ti\u00ean quy\u1ebft: \u0110\u00e3 ho\u00e0n th\u00e0nh T\u1eadp 2', ' (Claude Code Hooks kh\u00f4ng c\u1ea7n polling)'],
    3: ['T\u1eadp 4: Codex kh\u00f4ng c\u1ea7n polling + H\u1ec7 th\u1ed1ng ki\u1ec3m th\u1eed t\u1ef1 \u0111\u1ed9ng b\u1eb1ng Git'],
    4: ['\U0001f4d6 T\u00f3m t\u1eaft n\u1ed9i dung tr\u01b0\u1edbc'],
    5: ['Trong T\u1eadp 2, ch\u00fang ta \u0111\u00e3 th\u1ef1c hi\u1ec7n m\u1ed9t cu\u1ed9c "ph\u1eabu thu\u1eadt" cho \u0110\u1ea1i T\u00f4m H\u00f9m: d\u00f9ng Hooks \u0111\u1ec3 th\u1ef1c hi\u1ec7n ch\u1ebf \u0111\u1ed9 kh\u00f4ng c\u1ea7n polling cho Claude Code. \u0110\u1ea1i T\u00f4m H\u00f9m t\u1eeb m\u1ed9t \u00f4ng s\u1ebfp kh\u00f3 ch\u1ecbu "c\u1ee9 5 gi\u00e2y l\u1ea1i h\u1ecfi m\u1ed9t l\u1ea7n \u0111\u00e3 xong ch\u01b0a", tr\u1edf th\u00e0nh m\u1ed9t PM hi\u1ec7u qu\u1ea3 "giao vi\u1ec7c xong kh\u00f4ng c\u1ea7n qu\u1ea3n, l\u00e0m xong t\u1ef1 \u0111\u1ed9ng nh\u1eadn th\u00f4ng b\u00e1o".'],
    6: ['Nh\u01b0ng \u0111\u00f3 ch\u1ec9 l\u00e0 chi\u1ebfn \u0111\u1ea5u \u0111\u01a1n l\u1ebb.'],
    7: ['T\u1eadp n\u00e0y, ch\u00fang ta s\u1ebd l\u00e0m hai vi\u1ec7c:'],
    8: ['Sao ch\u00e9p ch\u1ebf \u0111\u1ed9 kh\u00f4ng c\u1ea7n polling t\u01b0\u01a1ng t\u1ef1 sang Codex CLI', ' (Agent code c\u1ee7a OpenAI)'],
    9: ['X\u00e2y d\u1ef1ng h\u1ec7 th\u1ed1ng ki\u1ec3m th\u1eed t\u1ef1 \u0111\u1ed9ng b\u1eb1ng Git', ' \u2014\u2014 B\u1ea1n push code tr\u00ean MacBook, Agent Team tr\u00ean Mac Mini t\u1ef1 \u0111\u1ed9ng ki\u1ec3m th\u1eed'],
    10: ['\U0001f527 Part 1: Codex CLI c\u0169ng c\u1ea7n kh\u00f4ng polling'],
    11: ['T\u1ea1i sao c\u1ea7n Codex?'],
    12: ['Claude Code gi\u1ecfi vi\u1ec7c ph\u00e1t tri\u1ec3n \u0111a file ph\u1ee9c t\u1ea1p, nh\u01b0ng m\u1ed9t s\u1ed1 t\u00ecnh hu\u1ed1ng d\u00f9ng Codex ph\u00f9 h\u1ee3p h\u01a1n:'],
    13: ['T\u00ecnh hu\u1ed1ng'],
    14: ['C\u00f4ng c\u1ee5 \u0111\u1ec1 xu\u1ea5t'],
    15: ['L\u00fd do'],
    16: ['D\u1ef1 \u00e1n m\u1edbi x\u00e2y t\u1eeb \u0111\u1ea7u'],
    17: [None],
    18: ['Agent Teams ph\u00e1t tri\u1ec3n song song'],
    19: ['Ki\u1ec3m th\u1eed b\u1ea3o m\u1eadt + T\u1ef1 \u0111\u1ed9ng s\u1eeda l\u1ed7i'],
    20: [None],
    21: [None, ' m\u1ed9t b\u01b0\u1edbc l\u00e0 xong'],
    22: ['Review code (ch\u1ec9 \u0111\u1ecdc)'],
    23: [None],
    24: [None, ' chuy\u00ean l\u00e0m review'],
    25: ['S\u1eeda nhanh file \u0111\u01a1n l\u1ebb'],
    26: [None],
    27: ['Nhanh, 2 ph\u00fat xong'],
    28: ['Ch\u1ebf \u0111\u1ed9 kh\u00f4ng c\u1ea7n polling c\u1ee7a Codex v\u00e0 Claude Code kh\u00e1c nhau nh\u01b0 th\u1ebf n\u00e0o?'],
    29: ['Claude Code c\u00f3 h\u1ec7 th\u1ed1ng Hook t\u00edch h\u1ee3p s\u1eb5n \u2014\u2014 Khi ho\u00e0n th\u00e0nh nhi\u1ec7m v\u1ee5 s\u1ebd t\u1ef1 \u0111\u1ed9ng k\u00edch ho\u1ea1t script callback.'],
    30: ['Codex CLI kh\u00f4ng c\u00f3 Hook t\u00edch h\u1ee3p s\u1eb5n. Nh\u01b0ng ch\u00fang ta c\u00f3 th\u1ec3 d\u00f9ng m\u1ed9t shell wrapper \u0111\u1ec3 m\u00f4 ph\u1ecfng:'],
    31: ['Hi\u1ec7u qu\u1ea3 ho\u00e0n to\u00e0n gi\u1ed1ng nhau, ch\u1ec9 l\u00e0 c\u00e1ch th\u1ef1c hi\u1ec7n h\u01a1i kh\u00e1c.'],
    32: ['T\u1ea3i script'],
    33: ['Gi\u1ed1ng nh\u01b0 T\u1eadp 2, t\u1ea5t c\u1ea3 script \u0111\u00e3 \u0111\u01b0\u1ee3c \u0111\u00f3ng g\u00f3i tr\u00ean Gist, ch\u1ec9 c\u1ea7n ch\u1ea1y tr\u00ean terminal:'],
    34: ['\u0110\u1ecba ch\u1ec9 Gist \u0111\u1ea7y \u0111\u1ee7 script:'],
    35: ['T\u1ea3i script ph\u00e1t l\u1ec7nh v\u00e0 callback cho Codex'],
    36: ['C\u1ea5p quy\u1ec1n th\u1ef1c thi'],
    37: ['Ch\u1ea1y ng\u1ea7m, tr\u1ea3 v\u1ec1 ngay'],
    38: ['Ch\u1ebf \u0111\u1ed9 Review', ' (ki\u1ec3m th\u1eed ch\u1ec9 \u0111\u1ecdc):'],
    39: ['\U0001f916 Part 2: T\u1eeb \u0111\u01a1n l\u1ebb \u0111\u1ebfn Agent Team'],
    40: ['\u0110\u1ebfn th\u1eddi \u0111i\u1ec3m n\u00e0y, ch\u00fang ta \u0111\u00e3 c\u00f3 hai "s\u00e1t th\u1ee7 h\u00e0ng \u0111\u1ea7u":'],
    41: [None, ' \u2014\u2014 Ph\u00e1t tri\u1ec3n ph\u1ee9c t\u1ea1p, x\u00e2y d\u1ef1ng d\u1ef1 \u00e1n m\u1edbi'],
    42: [None, ' \u2014\u2014 Ki\u1ec3m th\u1eed code, ki\u1ec3m tra b\u1ea3o m\u1eadt, s\u1eeda nhanh'],
    43: ['Nh\u01b0ng t\u1ea5t c\u1ea3 \u0111\u1ec1u c\u1ea7n b\u1ea1n k\u00edch ho\u1ea1t th\u1ee7 c\u00f4ng. Ti\u1ebfp theo ch\u00fang ta s\u1ebd x\u00e2y d\u1ef1ng m\u1ed9t', ' h\u1ec7 th\u1ed1ng ki\u1ec3m th\u1eed ho\u00e0n to\u00e0n t\u1ef1 \u0111\u1ed9ng', '.'],
    44: ['Ki\u1ebfn tr\u00fac cu\u1ed1i c\u00f9ng'],
    45: ['B\u1ea1n kh\u00f4ng c\u1ea7n l\u00e0m b\u1ea5t k\u1ef3 \u0111i\u1ec1u g\u00ec t\u1eeb \u0111\u1ea7u \u0111\u1ebfn cu\u1ed1i.', ' Vi\u1ebft code, push, r\u1ed3i \u0111\u1ee3i th\u00f4ng b\u00e1o t\u1eeb Feishu.'],
    46: ['C\u00e1c b\u01b0\u1edbc x\u00e2y d\u1ef1ng'],
    47: ['Step 1: \u0110\u0103ng k\u00fd GitHub Self-hosted Runner tr\u00ean Mac Mini'],
    48: ['Self-hosted Runner cho ph\u00e9p GitHub Actions ch\u1ea1y tr\u00ean m\u00e1y c\u1ee7a b\u1ea1n, thay v\u00ec tr\u00ean m\u00e1y ch\u1ee7 \u0111\u00e1m m\u00e2y c\u1ee7a GitHub.'],
    49: ['L\u1ee3i \u00edch:'],
    50: ['Mac Mini v\u1ed1n \u0111\u00e3 ch\u1ea1y 7x24'],
    51: ['C\u00f3 th\u1ec3 truy c\u1eadp tr\u1ef1c ti\u1ebfp Codex CLI, OpenClaw t\u1ea1i m\u00e1y local'],
    52: ['Kh\u00f4ng c\u1ea7n m\u1edf c\u1ed5ng m\u1ea1ng'],
    53: ['T\u1ea1o m\u1ed9t b\u1ea3n sao d\u1ef1 \u00e1n \u0111\u1ed9c l\u1eadp (Kh\u00f4ng d\u00f9ng th\u01b0 m\u1ee5c \u0111\u1ed3ng b\u1ed9 iCloud!)'],
    54: ['T\u1ea3i GitHub Actions Runner'],
    55: ['V\u00e0o GitHub repo \u2192 Settings \u2192 Actions \u2192 Runners \u2192 New self-hosted runner'],
    56: ['L\u00e0m theo h\u01b0\u1edbng d\u1eabn tr\u00ean trang \u0111\u1ec3 t\u1ea3i v\u00e0 c\u1ea5u h\u00ecnh'],
    57: [' \u0110\u0103ng k\u00fd Runner'],
    58: ['C\u00e0i \u0111\u1eb7t l\u00e0m d\u1ecbch v\u1ee5 h\u1ec7 th\u1ed1ng (t\u1ef1 kh\u1edfi \u0111\u1ed9ng c\u00f9ng m\u00e1y)'],
    59: [None, None],
    60: [' Step 2: T\u1ea1o GitHub Actions Workflow'],
    61: [' Step 3: Ch\u1ec9 d\u1eabn Forge c\u00e1ch x\u1eed l\u00fd nhi\u1ec7m v\u1ee5 ki\u1ec3m th\u1eed'],
    62: ['\U0001f4ca So s\u00e1nh chi ph\u00ed'],
    63: ['T\u00ecnh hu\u1ed1ng'],
    64: ['Ki\u1ec3m th\u1eed th\u1ee7 c\u00f4ng'],
    65: ['Ki\u1ec3m th\u1eed t\u1ef1 \u0111\u1ed9ng'],
    66: ['C\u00e1ch k\u00edch ho\u1ea1t'],
    67: ['Ch\u1ea1y th\u1ee7 c\u00f4ng khi b\u1ea1n nh\u1edb'],
    68: ['push t\u1ef1 \u0111\u1ed9ng k\u00edch ho\u1ea1t'],
    69: ['Ti\u00eau hao Token c\u1ee7a \u0110\u1ea1i T\u00f4m H\u00f9m'],
    70: ['15,000-50,000/l\u1ea7n'],
    71: ['~700/l\u1ea7n'],
    72: ['B\u1ea1n c\u1ea7n l\u00e0m g\u00ec'],
    73: ['M\u1edf terminal, nh\u1eadp l\u1ec7nh, \u0111\u1ee3i k\u1ebft qu\u1ea3'],
    74: ['Kh\u00f4ng c\u1ea7n l\u00e0m g\u00ec c\u1ea3'],
    75: ['\u0110\u1ed9 ph\u1ee7'],
    76: ['Khi n\u00e0o nh\u1edb m\u1edbi ki\u1ec3m th\u1eed'],
    77: ['M\u1ed7i l\u1ea7n push \u0111\u1ec1u ki\u1ec3m th\u1eed'],
    78: ['Th\u00f4ng b\u00e1o'],
    79: ['T\u1ef1 xem'],
    80: ['Feishu t\u1ef1 \u0111\u1ed9ng th\u00f4ng b\u00e1o'],
    81: ['\U0001f9e0 T\u1ed5ng k\u1ebft: Ki\u1ebfn tr\u00fac ba t\u1ea7ng'],
    82: ['\u0110\u00e2y ch\u00ednh l\u00e0 gi\u00e1 tr\u1ecb th\u1ef1c s\u1ef1 c\u1ee7a OpenClaw v\u1edbi t\u01b0 c\u00e1ch m\u1ed9t con t\u00e0u \u2014\u2014 N\u00f3 kh\u00f4ng ph\u1ea3i l\u00e0 m\u1ed9t c\u00f4ng c\u1ee5 vi\u1ebft code, m\u00e0 l\u00e0 m\u1ed9t', ' h\u1ec7 \u0111i\u1ec1u h\u00e0nh ch\u1ec9 huy Agent Team', '.'],
    83: ['B\u1ea1n l\u00e0 thuy\u1ec1n tr\u01b0\u1edfng, \u0110\u1ea1i T\u00f4m H\u00f9m l\u00e0 ph\u00f3 thuy\u1ec1n tr\u01b0\u1edfng, Claude Code v\u00e0 Codex l\u00e0 th\u1ee7y th\u1ee7. Th\u1ee7y th\u1ee7 l\u00e0m vi\u1ec7c d\u01b0\u1edbi boong t\u00e0u, b\u1ea1n ng\u1ed3i u\u1ed1ng c\u00e0 ph\u00ea trong ph\u00f2ng thuy\u1ec1n tr\u01b0\u1edfng, ch\u1ec9 khi l\u00e0m xong ph\u00f3 thuy\u1ec1n tr\u01b0\u1edfng m\u1edbi \u0111\u1ebfn g\u00f5 c\u1eeda b\u00e1o c\u00e1o.'],
    84: ['\U0001f51c D\u1ef1 b\u00e1o t\u1eadp ti\u1ebfp theo'],
    85: ['T\u1eadp 4:', ' OpenClaw \u0111a Agent ph\u1ed1i h\u1ee3p', ' \u2014\u2014 \u0110\u1ec3 Jarvis (CEO), Forge (CTO), Sentinel (V\u1eadn h\u00e0nh), Muse (N\u1ed9i dung) b\u1ed1n Agent l\u00e0m \u0111\u00fang nhi\u1ec7m v\u1ee5, x\u00e2y d\u1ef1ng c\u00f4ng ty AI c\u1ee7a b\u1ea1n.'],
    86: ['H\u01b0\u1edbng d\u1eabn n\u00e0y \u0111\u00e3 \u0111\u01b0\u1ee3c ki\u1ec3m ch\u1ee9ng tr\u00ean m\u00f4i tr\u01b0\u1eddng th\u1ef1c t\u1ebf. T\u1ea5t c\u1ea3 script \u0111\u00e3 \u0111\u01b0\u1ee3c test tr\u00ean Mac Mini M4 + OpenClaw 2026.2.12 + Codex v0.94.0 + Claude Code.'],
    87: ['Li\u00ean h\u1ec7 L\u1ed9c \u0111\u1ea1o+Ludao112'],
}

# Apply translations
translated = copy.deepcopy(data)
total_text = 0
translated_text = 0
kept_text = 0

for i, block in enumerate(translated['blocks']):
    text_idx = 0
    for el in block['elements']:
        if el['type'] == 'text_run':
            total_text += 1
            if i in vi:
                vi_list = vi[i]
                if text_idx < len(vi_list) and vi_list[text_idx] is not None:
                    el['content'] = vi_list[text_idx]
                    translated_text += 1
                else:
                    kept_text += 1
            else:
                kept_text += 1
            text_idx += 1

# Add space between adjacent Vietnamese text_runs where needed
for block in translated['blocks']:
    elements = block['elements']
    for j in range(len(elements) - 1):
        curr = elements[j]
        nxt = elements[j + 1]
        if curr['type'] == 'text_run' and nxt['type'] == 'text_run':
            if curr['content'] and nxt['content']:
                if not curr['content'].endswith((' ', '\n', '\t')) and not nxt['content'].startswith((' ', '\n', '\t')):
                    if nxt['content'][0] not in '.,:;!?)]}':
                        curr['content'] = curr['content'] + ' '

with open('_art_b6_2_trans.json', 'w', encoding='utf-8') as f:
    json.dump(translated, f, ensure_ascii=False, indent=2)

print(f'Total text_runs: {total_text}')
print(f'Translated: {translated_text}')
print(f'Kept as-is: {kept_text}')
print(f'Blocks: {len(translated["blocks"])}')
print('Saved to _art_b6_2_trans.json')
