# 10 задача (шахматы)

x1 = int(input('Insert x1: '))
y1 = int(input('Insert y1: '))
x2 = int(input('Insert x2: '))
y2 = int(input('Insert y2: '))

if 1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
    print((x1 + y1 + x2 + y2) % 2 == 0)
else:
    print('Numbers must be between 1 and 8')
