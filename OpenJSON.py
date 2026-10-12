import json
#d={'black':'черный', 'white':'белый'}

with open('dic.json','r', encoding='utf-8') as f:
    d = json.load(f)

# with open('dic.json','w', encoding='utf-8') as f:
#     json.dump(d, f, ensure_ascii=False, indent=4)

word=input('введите слово для перевода:  ')
if word in d:
    print(f'{word}  - {d[word]}')
else:
    trans=input(f'Введите перевод слова "{word}":  ')
    d[word]=trans

    with open('dic.json', 'w', encoding='utf-8') as file:
        json.dump(d, file, indent=4)
