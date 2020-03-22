import pygame
from pygame import gfxdraw


class TreeNode(object):

    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


root = TreeNode()

nodes = []


def traverse(node):
    if node is None:
        return
    traverse(node.left)
    nodes.append(node)
    traverse(node.right)


def init():
    traverse(root)


def draw(win, width, height):
    for k in range(len(nodes)):
        gfxdraw.aacircle(win, 50, 50, 30, (255, 255, 255))
        gfxdraw.filled_circle(win, 50, 50, 30, (255, 255, 255))
