import pygame as pg
from pygame.draw import circle, lines
import sys


#  TODO: нарисовать злобный смайл желтого цвета


pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    pg.time.delay(1000)