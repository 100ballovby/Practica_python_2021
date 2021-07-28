# Площадь сектора
'''
s = pi * r^2 * angle / 360
'''
from math import pi

radius = float(input('Input radius: '))
angle = float(input('Input angle: '))

res = pi * radius ** 2 * (angle / 360)

#  округлить результат
print(round(res, 3))  # округлить(число, количество_знаков_необязательно)


#  Корень из числа
from math import sqrt
print(sqrt(121))  # 11
print(121 ** 0.5)

