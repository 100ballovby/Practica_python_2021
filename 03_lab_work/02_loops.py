# 7 задача
a = int(input('Insert number: '))

# Variant 1
if 0 <= a <= 50:
    summary = 0
    for number in range(a, 51):
        summary += number ** 2
    print(summary)
else:
    print('Number must be between 0 and 50')


# variant 2
summary = 0
for number in range(a, 51):
    summary += number ** 2
print(summary)
