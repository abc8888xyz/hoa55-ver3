# -*- coding: utf-8 -*-
"""Translate article 15 using JSON translation map"""
import json
import sys
import re

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')


def main():
    # Load translation map
    with open('_art15_trans_map.json', 'r', encoding='utf-8') as f:
        trans_map = json.load(f)

    # Load original
    with open('_art15_orig.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    total_text = 0
    translated_text = 0
    kept_text = 0
    warnings = []

    for block in data['blocks']:
        for el in block['elements']:
            if el['type'] == 'text_run':
                total_text += 1
                content = el['content']

                # Exact match
                if content in trans_map:
                    el['content'] = trans_map[content]
                    translated_text += 1
                    continue

                # Pure whitespace/newlines - keep
                if not content.strip():
                    kept_text += 1
                    continue

                # No Chinese chars - keep as-is
                if not re.search(r'[\u4e00-\u9fff]', content):
                    kept_text += 1
                    continue

                # Try stripped match
                stripped = content.strip()
                if stripped in trans_map:
                    leading = content[:len(content) - len(content.lstrip())]
                    trailing = content[len(content.rstrip()):]
                    el['content'] = leading + trans_map[stripped] + trailing
                    translated_text += 1
                    continue

                # Untranslated Chinese text
                warnings.append(repr(content))
                kept_text += 1

    # Save
    with open('_art15_trans.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Translation complete!")
    print(f"Total text elements: {total_text}")
    print(f"Translated: {translated_text}")
    print(f"Kept as-is: {kept_text}")

    if warnings:
        print(f"\nWARNINGS - {len(warnings)} untranslated Chinese texts:")
        for w in warnings:
            print(f"  {w}")
    else:
        print("\nAll Chinese texts translated successfully!")

    print(f"\nSaved to _art15_trans.json")


if __name__ == '__main__':
    main()
