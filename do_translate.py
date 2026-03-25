import json, re, sys

def has_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

def translate_article(input_file, output_file, translations):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    stats = {'total_blocks': len(data['blocks']), 'translated': 0, 'kept': 0, 'total_text': 0, 'errors': []}
    
    for i, block in enumerate(data['blocks']):
        for j, elem in enumerate(block.get('elements', [])):
            content = elem.get('content', '')
            if not content.strip():
                continue
            stats['total_text'] += 1
            key = f'B{i}E{j}'
            if key in translations:
                elem['content'] = translations[key]
                stats['translated'] += 1
            elif not has_chinese(content):
                stats['kept'] += 1
            else:
                stats['errors'].append(key)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return stats

if __name__ == '__main__':
    input_f = sys.argv[1]
    output_f = sys.argv[2]
    trans_f = sys.argv[3]
    
    with open(trans_f, 'r', encoding='utf-8') as f:
        translations = json.load(f)
    
    stats = translate_article(input_f, output_f, translations)
    print(json.dumps(stats, ensure_ascii=False))
