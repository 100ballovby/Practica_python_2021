from turtle import *

t = Turtle()
t.color('red')
t.width(4)
t.speed(10)

t.up()
t.goto(10, 50)
t.down()
for i in range(4):
    t.fd(100)
    t.rt(90)


t.up()
t.goto(-100, 90)
t.down()
for i in range(4):
    t.fd(30)
    t.rt(90)

t.up()
t.goto(40, 120)
t.down()
for i in range(4):
    t.fd(80)
    t.rt(90)

done()