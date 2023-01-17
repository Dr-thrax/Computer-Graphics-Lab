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
pygame.display.set_caption("Bresenham Line Drawing Algorithm")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)

screen_surface.fill(BLACK)
height = 700


def bresenheim(x1, y1, x2, y2):
    # step 2 calculate difference
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    m = dy / dx

    # step 3 perform test to check if pk < 0
    flag = True

    points = [(x1, y1)]
    gfxdraw.pixel(screen_surface,round(x1),round(y1),WHITE)

    step = 1
    if x1 > x2 or y1 > y2:
        step = -1

    mm = False
    if m < 1:
        x1, x2, y1, y2 = y1, y2, x1, x2
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        mm = True

    p0 = 2 * dx - dy
    x = x1
    y = y1

    for i in range(abs(y2 - y1)):
        if flag:
            x_previous = x1
            p_previous = p0
            p = p0
            flag = False
        else:
            x_previous = x
            p_previous = p

        if p >= 0:
            x = x + step

        p = p_previous + 2 * dx - 2 * dy * (abs(x - x_previous))
        y = y + 1

        if mm:
            gfxdraw.pixel(screen_surface,round(x),round(y),WHITE)
            points.append((y, x))
        else:
            gfxdraw.pixel(screen_surface,round(x),round(y),WHITE)
            points.append((x, y))
    
    for point in points:
        print(point)



bresenheim(0,0,0,1000)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
