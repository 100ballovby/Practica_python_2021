class Base:
    def __init__(self, a):
        self.a = a

    def get_a(self):
        return self.a


class Car:
    pass


class Derivative(Base):
    def __init__(self, a):
        super().__init__(a)


a = Base(2)
b = Derivative(4)

print(a.get_a())
print(b.get_a())