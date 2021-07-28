array = [-2, -6, -3, -12, -6, -5, 1]
summary = 0
i = 0

while i < len(array) - 1:
    summary += array[i]
    i += 1

print(summary / (len(array) - 1))
