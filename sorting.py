import pygame
import random

array = [0] * 100
highlighted = [0] * 100

for i in range(len(array)):
    array[i] = i

random.shuffle(array)


def draw(win, width, height):
    for i in range(len(array)):
        pygame.draw.rect(win, (255, 255, 255) if highlighted[i] == 0 else (255, 0, 0), (i * (width // len(array)), height - array[i] * 6, width // len(array), array[i] * 6))


def highlight(k):
    highlighted[k] = 1


def unhighlight(k):
    highlighted[k] = 0


def unhighlight_all():
    for k in range(len(array)):
        highlighted[k] = 0


index = 0


def tick(win, width, height):
    global index

    if index >= len(array):
        unhighlight_all()
        return False

    min_index = index
    for k in range(index, len(array)):
        if array[k] < array[min_index]:
            min_index = k

    unhighlight_all()
    highlight(index)
    highlight(min_index)
    draw(win, width, height)
    swap(index, min_index)

    index += 1


def reset():
    global index
    random.shuffle(array)
    index = 0

def swap(i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
