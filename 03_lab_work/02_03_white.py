# Нахождение НОД
from math import gcd

'''
30 и 18
30 / 18 = 1 (остаток 12)
18 / 12 = 1 (остаток 6)
12 / 6 = 2 (остаток 0)
НОД - 6
'''

a = int(input('Input number: '))
b = int(input('input number: '))

while a > 0 and b > 0:
    if a > b:
        a %= b
    else:
        b %= a

print(a + b)
