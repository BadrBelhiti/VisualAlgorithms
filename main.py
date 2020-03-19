import pygame
import sorting

pygame.init()

width = 800
height = 600

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Algorithm Visualizer")


def clear():
    win.fill((0, 0, 0))


def draw():
    pygame.draw.rect(win, (255, 255, 255), (0, 0, 50, 50))


def update():
    pygame.display.update()


tps = 20
running = True

while running:
    pygame.time.delay(1000 // tps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clear()
    if not sorting.tick(win, width, height):
        sorting.draw(win, width, height)
    update()
