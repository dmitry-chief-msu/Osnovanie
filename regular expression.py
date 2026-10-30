"""Match    match = re.search(regex, string, flags=re.IGNORECASE)"""

import re

res = re.match(r'AV', 'A1V-Avia') #совпадение в начале строки
res = re.search(r'..V', 'A1V-Avia') #совпадение где-то в строке, выдает ПЕРВОЕ
res = re.findall(r'..V', 'A1V-Avia') #совпадение где-то в строке, выдает ВСЕ
res = re.finditer(r'.V', 'AV-AVia') #совпадение где-то в строке, выдает ПО ОЧЕРЕДИ
res = re.sub(r'то меняем', 'на что меняем', r'где меняем')
res = re.split(r'p', 'perspective', maxsplit=1)

pattern = re.compile(r'AV')
res = pattern.findall('AV-AVia')

print(res)

# print(next(res))
# print(next(res))

#"""
# СПЕЦСИМВОЛЫ
# экранирование
# \d - любая цифра
# \D - любое НЕ числовое значение
# 
# \s - символы пробелов
# \S - всё, кроме пробела
# 
# \w - буква, цифра или нихнее подчеркивание (_)
# \W - всё, кроме \w
# 
# без экранирования
# . - любой символ, кроме переноса строки (\n)
# ^ - начало строки
# $ - конец строки
# 
# [abc] - любой из символов в скобках
# 
# ^ - имеет и второе значение: 
# [^abc] - любой символ, кроме тех, что в скобках
# 
# a|b - a или b
# (ab) - определяется одним элементом
# 
# \bслово\b - целое слово
# 
# """

result = re.findall(r'[abcd]', 'dmitry-chief@gmail.com')
print(result)

"""

# КВАНТИФИКАТОРЫ
# 
# regex+ - встречается один или более раз
# regex* - встречается ноль или более раз (???)
# regex? - встречается ноль или один раз
# regex{n} - встречается n раз
# regex{n, } - встречается n или более раз
# regex{n, m} - встречается от n до m раз
# regex{ , m} - встречается от 0 до m раз
# 
# """

regex = re.compile(r'^.+#') # это все символы от начала строки до решетки

print(regex.findall('kbhvbvb#vmsvjnskcm'))

