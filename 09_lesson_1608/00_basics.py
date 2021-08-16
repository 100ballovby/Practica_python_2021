# SOLID
# S - single responsibility - принципп единой ответственности

class Car:
    def __init__(self, c, name):
        self.color = c
        self.name = name

    def drive(self):
        pass

    def turn_lights(self, time):
        pass


class EntireCarFunctions(Car):
    pass

# O - open/close
# Ваш класс должен быть открыт для расширения, но не для изменения
class Oleg:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def is_alive(self):
        return self.health > 0

    def get_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def talk(self):
        print(f'{self.name} says: My health is {self.health}. Hit me!')

    def final_cry(self):
        print('You won!')


class ManyEnemies(Oleg):
    def __init__(self, name: list, count):
        self.names = name
        self.enemy_list = []
        for i in range(count):
            self.enemy_list.append(Oleg.__init__(self, self.names[i]))
            print(self.names[i])
        print(self.enemy_list)

enemies_names = ['Storm', 'X', 'Ultra', 'Thunder']
el = ManyEnemies(enemies_names, len(enemies_names))


# L - обращаться к классу наследнику с теми же методами (просьбами), что и к родителю
class Shape:
    def __init__(self, c, x, y):
        self.color = c
        self.pos_x = x
        self.pos_y = y


class Circle(Shape):
    def __init__(self, c, x, y):
        Shape.__init__(c, x, y)

    def draw_circle(self):
        pass


    def draw_square(self):
        pass
    def draw_triangle(self):
        pass