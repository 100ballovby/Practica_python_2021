print('Hello, World!')

a = input('What is your name? ')

print(5 ** 2)
print('Hello, ', a)

print(dir('__builtins__'))


def is_valid_password(password) -> bool: # аннотация возвращаемого типа данных
    valid_pass = '12345qwerty'
    return valid_pass == password

is_valid_password('rjkgr')