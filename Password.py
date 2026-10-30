import re
from string import ascii_letters, digits
import random


def get_password (n):

    #data = set(ascii_letters + digits) - {'0', '1', 'o', 'O', 'l', 'I'}
    #data = ''.join(data)
    data1 = ''.join(re.findall(r'[^01oOlI]', ascii_letters + digits))
    #print(data)
    #print(data1)
    #password = random.sample(list(data1), n)
    # pos = random.sample(range(n), 3)
    # password[pos[0]] = password[pos[0]].lower()
    # password[pos[1]] = password[pos[1]].upper()
    # password[pos[2]] = str(random.randint(2,9))
    password = ''
    while (not re.search(r'[a-z]', password)
        or not re.search(r'[A-Z]', password)
        or not re.search(r'[2-9]', password)):
        password = ''.join(random.sample(data1, n))



    return password

def main(n, m):
    res = set()
    while len(res) < n:
        res.add(get_password(m))

    for p in res:
        print(p)


#main(10, 8)


""" ПРОВЕРКА ТЕЛЕФОННЫХ НОМЕРОВ"""

regex = r'^[+8]\d{10,11}'
phone_number = '+79111234567'
res = re.search(regex, phone_number)
if res:
    print(res.group())
else:
    print('Ошибка в номере')



