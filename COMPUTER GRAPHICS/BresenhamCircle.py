import pygame, sys
from pygame.locals import *
from pygame import gfxdraw


# a0 = int(input("input x0 ->"))
# b0 = int(input("input y0 ->"))
# a1 = int(input("input x1 ->"))
# b1 = int(input("input y1 ->"))

pygame.init()

size = (700, 700)
screen_surface = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption("Bresenham Circle Algorithm")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)

screen_surface.fill(BLACK)
height = 700

points = []

def eight_way_symmetric_plot(xc, yc, x, y):
    points.append((x + xc, y + yc))
    gfxdraw.pixel(screen_surface,round(x+xc),round(y+yc),WHITE)
    points.append((x + xc, -y + yc))
    gfxdraw.pixel(screen_surface,round(x+xc),round(-y+yc),WHITE)

    points.append((-x + xc, -y + yc))
    gfxdraw.pixel(screen_surface,round(-x+xc),round(-y+yc),WHITE)
    points.append((-x + xc, y + yc))
    gfxdraw.pixel(screen_surface,round(-x+xc),round(y+yc),WHITE)

    points.append((y + xc, x + yc))
    gfxdraw.pixel(screen_surface,round(y+xc),round(x+yc),WHITE)
    points.append((y + xc, -x + yc))
    gfxdraw.pixel(screen_surface,round(y+xc),round(-x+yc),WHITE)

    points.append((-y + xc, -x + yc))
    gfxdraw.pixel(screen_surface,round(-y+xc),round(-x+yc),WHITE)
    points.append((-y + xc, x + yc))
    gfxdraw.pixel(screen_surface,round(-y+xc),round(x+yc),WHITE)


def draw_bresenham_circle(xc, yc, r):
    x = 0
    y = r
    d = 3 - (2 * r)
    eight_way_symmetric_plot(xc, yc, x, y)

    while x <= y:
        if d <= 0:
            d = d + (4 * x) + 6
        else:
            d = d + (4 * x) - (4 * y) + 10
            y = y - 1
        x = x + 1
        eight_way_symmetric_plot(xc, yc, x, y)


draw_bresenham_circle(200,200,100)


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
