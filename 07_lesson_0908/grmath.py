def power(n: int, deg: int) -> int:
    res = n ** deg
    return res


def multiply(*n) -> int:
    res = 1
    for i in n:
        res *= i
    return res


def main():
    print(power(2, 5))
    print(multiply(2, 5, 4, 2, 7))


if __name__ == "__main__":
    print(f'Я запустился с именем {__name__}')
    main()
    print(power(10, -1))


