import random

array = []
for i in range(16):
    array.append(random.randint(1, 50))

print(array)
for index in range(len(array)):
    if array[index] <= 10:
        array[index] = 0
    elif array[index] >= 20:
        array[index] = 1

print(array)