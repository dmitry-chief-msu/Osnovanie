l=[22,33,44]

def gen():
    i=0
    while i<3:
        i+=1
        yield i # Это определяет функцию - генератор
#
# res=gen()
#
# for i in res:
#     print(i)
res=(i for i in gen()) # Это выражение - генератор
print(res)

res  = map(str, l)
print (list(res))


res = map(str, l)
