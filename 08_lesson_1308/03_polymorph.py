from incaps_01 import Person


class Employee(Person):
    def __init__(self, name, company):
        Person.__init__(self, name)
        self.company = company

    def display_info(self):
        Person.display_info(self)
        print(f'works on {self.company}')

    def __str__(self):
        return f'Class {Person.__name__}, name of the person is: {self.name}'

oksana = Employee('Oksana', 'Roga-i-kopita')
oksana.age = 21
oksana.display_info()

print(oksana)
