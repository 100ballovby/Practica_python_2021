

def cows(n: int = 1):
    res = 'коров'
    # 1 - а, 2 - ы, 5-20 - _
    count = n % 10
    if 5 <= n <= 20:
        res += ''
    elif count == 1:
        res += 'а'
    elif 2 <= count < 5:
        res += 'ы'
    return res

print(cows(10563))


