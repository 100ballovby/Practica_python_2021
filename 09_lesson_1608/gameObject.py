class GameObject:
    def __init__(self, x, y, is_alive):
        self.x_cor = x
        self.y_cor = y
        self.is_alive = is_alive

    def move(self, steps):
        pass

    def destroy(self):
        pass

    def draw(self):
        pass


class Cannon(GameObject):
    def __init__(self, x, y, is_alive):
        GameObject.__init__(self, x, y, is_alive)

    def move(self, steps):
        print(f'Moved {steps}')


class Shell(GameObject):
    def __init__(self, x, y, is_alive):
        GameObject.__init__(self, x, y, is_alive)