from incaps_01 import Person


class Student(Person):
    def details(self, university):
        return f'{self.name} studies in {university}'

Oleg = Student('Сергей')
Oleg.age = 21
Oleg.display_info()

print(Oleg.details('BSU'))