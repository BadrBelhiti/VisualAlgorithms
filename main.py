import pygame

pygame.init()

width = 800
height = 600

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Algorithm Visualizer")

tps = 20

running = True

while running:
    pygame.time.delay(1000 // 20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
