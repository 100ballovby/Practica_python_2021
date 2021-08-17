import pygame as pg
import sys

pg.init()

# И создать окно:
screen = pg.display.set_mode((600, 400))

pg.draw.rect(screen, (97, 255, 229), (100, 150, 100, 50))
pg.draw.rect(screen, (97, 255, 229), (210, 150, 100, 50), 15)

pg.draw.line(screen, (97, 255, 229), [10, 30], [250, 90])
pg.draw.rect(screen, (255, 255, 255), (10, 30, 250, 90), 3)

pg.draw.polygon(screen, (255, 255, 255),
               [[150, 200], [190, 300], [90, 250]])

pg.draw.circle(screen, (255, 255, 255), (400, 250), 30, 5)

pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    pg.time.delay(1000)       
    