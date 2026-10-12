file=open('list.txt','r', encoding='utf-8')
# print(file.read())
# print('Step 2')
# print(file.read())
s=file.readlines()
# s= file.readline()

#print (s)
#file.close()

# for i in open('list.txt','r', encoding='utf-8'):
#     print(i)

#file.close тут не нужен! for закрывает всё сам.

with open('list.txt','r', encoding='utf-8') as file:
    ls=file.read().title().split()
#     print (ls)
#
# ls.sort()
# print (ls)

with open('list1.txt','w', encoding='utf-8') as file:

    for n, f in enumerate(ls,1):
        file.write(f'{n}. {f}\n')

file2 = open('list1.txt','r', encoding='utf-8')
print(file2.read())