from decimal import Decimal
import math

def factorial(k):
    fact = Decimal(math.factorial(int(k)))      # не называй переменную f, чтобы не путать с f-строками
    print(f"{fact:.6e}")                       # правильное форматирование: {переменная:.6e}

factorial(1000)
