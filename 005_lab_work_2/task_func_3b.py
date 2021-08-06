from math import factorial


def my_factorial(n: int = 1) -> int:
    factor = 1
    for i in range(1, n + 1):
        factor *= i
    return factor

n = int(input('Input number: '))
print(f'Factorial of {n} = {my_factorial(n)}')
print(factorial(n))  # вариант 2