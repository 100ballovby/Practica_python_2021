'''
ООП - объектно-ориентированное программирование

объект - переменная классового типа.
Класс - это род.
экземпляр (объект) - это вид.
'''


class Car:
    name = 'Tesla'

    def drive(self, speed):  # метод
        print(f'Car {self.name} is driving at {speed} mph')


model_s = Car()
model_s.name = 'My Tesla'
print(model_s.name)

model_e = Car()
model_e.name = 'Eelon'
model_x = Car()
model_y = Car()

model_s.drive(50)
model_x.drive(50)

