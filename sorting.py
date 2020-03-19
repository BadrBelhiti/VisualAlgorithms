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


def tick():
    global index

    if index >= len(array):
        unhighlight_all()
        return

    min_index = index
    for k in range(index, len(array)):
        if array[k] < array[min_index]:
            min_index = k

    unhighlight_all()
    swap(index, min_index)
    highlight(index)
    highlight(min_index)

    index += 1


def reset():
    global index
    random.shuffle(array)
    index = 0


def sort():
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        pygame.time.delay(50)
        swap(i, min_index)


def swap(i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
