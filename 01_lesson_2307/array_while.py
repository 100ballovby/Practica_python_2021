import random

array = [random.randint(-100, 100) for i in range(20)]
print(array)

key = 17
num = 0
while array[num] != key:
    if num > len(array) - 1:
        break
    num += 1
print(num)