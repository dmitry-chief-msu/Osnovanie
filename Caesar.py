with open('text.txt','r', encoding='utf-8') as f:
    s=f.read()
    key=input('ВВЕДИТЕ КЛЮЧ:  ')
    secret = ''
    for c in s:
        code = ord(c)+int(key)
        symbol=chr(code)
        secret+=symbol
print ('Зашифровано')
print(chr(128512))
print (secret)

with open('text21.txt','w', encoding='utf-8') as f:
    f.write(secret)

#+++++++++++++++++++++++++++++++++++++

with open('text21.txt','r', encoding='utf-8') as uf:
    s=uf.read()
    key=input('ВВЕДИТЕ КЛЮЧ:  ')
    secret2 = ''
    for c in s:
        decode = ord(c)-int(key)
        symbol=chr(decode)
        secret2+=symbol
print ('Расшифровано')

print (secret2)

with open('text221.txt','w', encoding='utf-8') as f:
    f.write(secret2)


