import pygame as pg
from pygame.draw import circle, line, rect
import sys

colors = {
    'yellow': (255, 224, 18),
    'red': (255, 18, 18),
    'white': (255, 255, 255),
    'black': (0, 0, 0)
}

pg.init()

screen = pg.display.set_mode((400, 400))

# drawing face
circle(screen, colors['yellow'], (200, 200), 150)

# drawing eyes
circle(screen, colors['white'], (145, 140), 40)
circle(screen, colors['white'], (245, 140), 40)

# drawing rainbow eyes
circle(screen, colors['red'], (130, 140), 20)
circle(screen, colors['red'], (230, 140), 20)

# drawing entire eyes
circle(screen, colors['black'], (130, 140), 7)
circle(screen, colors['black'], (230, 140), 6)

# draw eyebrow
line(screen, colors['black'], [50, 50], [190, 120], 10)
line(screen, colors['black'], [200, 120], [290, 70], 10)

# mouth
rect(screen, colors['black'], (100, 230, 170, 30))


pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    pg.time.delay(1000)