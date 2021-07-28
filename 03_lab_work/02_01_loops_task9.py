''' Задача 9.
Известны оценки по физике каждого из 20 учеников класса.
Определить среднюю оценку. Решить задачу используя циклическую
конструкцию for.
'''
from random import randint
import mark as mark

marks1 = []
for i in range(20):
    marks1.append(randint(1, 10))
print(marks1)

# Variant 1
marks = [8, 9, 2, 6, 4, 8, 3, 7, 10, 8, 9, 5, 7, 8, 5, 4, 6, 9, 10, 7]
summary = 0
for mark in marks:
    summary += mark

print(summary / len(marks))

# Variant 2
print(sum(marks1) / len(marks1))
