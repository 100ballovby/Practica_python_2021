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


def main():
    enemy = Oleg('Oleg')
    finish = False
    while not finish:
        enemy.talk()
        hit = int(input())
        enemy.get_damage(hit)
        if not enemy.is_alive():
            enemy.final_cry()
            finish = True

main()