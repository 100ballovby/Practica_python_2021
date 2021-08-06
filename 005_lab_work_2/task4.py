array = [1, 1, 2, 5, 3, 2, 3, 6, 7, 5]
clear_array = []

print(set(array))  # убрать дубликаты И ОТСОРТИРОВАТЬ => множество

for element in array:
    if element not in clear_array:
        clear_array.append(element)
print(clear_array)