class Divider:
    def __init__(self):
        self.__div = 2
        print(f'Создал делитель {self.__div}')

    def set_divider(self, value):
        if value != 0:
            self.__div = value
        else:
            print('Incorrect divider value!')

    def get_divider(self):
        print(self.__div)

    def divide(self, number):
        print(number / self.__div)


class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 1

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0.1 <= age <= 149.9:
            self.__age = age
        else:
            print("Incorrect age value.")

    def display_info(self):
        print(f'Person {self.name} is {self.__age} years old.')



if __name__ == '__main__':
    five = Divider()
    five.set_divider(3)
    five.div = 0  # создался статический атрибут класса div

    oleg = Person('Oleg')
    oleg.name = 'Oksana'
    print(oleg.age)
    oleg.age = 15
    oleg.display_info()
    oleg.age = -12
    oleg.display_info()




