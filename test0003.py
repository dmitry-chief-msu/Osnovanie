import math
import time
from decimal import Decimal, getcontext

k=input('Enter the number:   ')

def time_run(func):
    def wrapper(*args, **kwargs):
        start = time.time()


def time_run(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        duration = round(end - start, 2)
        print(f'Working time of {func.__name__} is {duration} seconds')
    return wrapper

@time_run


def factorial(k):
    fact = Decimal(math.factorial(int(k)))      # не называй переменную f, чтобы не путать с f-строками
    print (f"{fact:.6e}")                       # правильное форматирование: {переменная:.6e}




#def factorial(k):
#    fact = Decimal (math.factorial(int(k)))
#    print(f"Факториал = {fact:6e}")

factorial(k)
print (k)



