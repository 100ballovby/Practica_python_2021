class Car:
    engine = True  # статический атрибут

    def __init__(self, nm, d, wc, col='black'):
        self.name = nm
        self.doors = d
        self.wheels_count = wc
        self.color = col
        print(f'Car {self.name}\nColor: {self.color}')

    def run(self, speed):  # обычный метод
        print(f'Car {self.name} is running at {speed} mph.')

    @staticmethod  # метка-декоратор
    def my_static_method():
        print('static')

    @classmethod  # классовый метод
    def my_class_method(cls):
        """cls - название вашего класса"""
        print('класс метод')


tesla_s = Car('Model S', 4, 4, 'red')
bmw_5 = Car('535', 4, 4, 'cyan')
bmw_5.color = 'yellow'
print(bmw_5.color)
print(tesla_s.color)

tesla_s.run(100)
bmw_5.run(50)
Car.my_class_method()



