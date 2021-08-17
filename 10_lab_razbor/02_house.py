import pygame as pg
from pygame.draw import circle, line, rect, ellipse, polygon
import sys

colors = {
    'yellow': (255, 224, 18),
    'red': (255, 18, 18),
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'baby-blue': (141, 241, 255),
    'grass-green': (57, 191, 62),
}

pg.init()

screen = pg.display.set_mode((400, 400))
# background
rect(screen, colors['baby-blue'], (0, 0, 400, 300))
rect(screen, colors['grass-green'], (0, 150, 400, 300))

rect(screen, colors['yellow'], (150, 160, 130, 140))
polygon(screen, colors['red'], [[150, 160], [215, 100], [280, 160]])
rect(screen, colors['baby-blue'], (200, 190, 30, 50))

pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    pg.time.delay(1000)
