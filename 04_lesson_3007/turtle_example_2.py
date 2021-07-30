from turtle import *

t = Turtle()
t.color('red')
t.width(4)
t.speed(10)

def square(turtle, x, y, length):
    turtle.goto(x, y)
    turtle.down()
    for i in range(4):
        turtle.fd(length)
        turtle.rt(90)
    turtle.up()

square(t, 10, 50, 100)
square(t, -100, 90, 30)
square(t, 40, 120, 80)


done()