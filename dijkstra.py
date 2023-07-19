import pygame
from collections import deque
import math

size = (width, height) = (640, 480)
pygame.init()

win = pygame.display.set_mode(size)
pygame.display.set_caption("Dijkstra's Path Finding")
clock = pygame.time.Clock()

cols, rows = width/10, height/10
w = width
h = height

grid = []
queue, visited = deque(), []
path = []


class Spot:
    def __init__(self, i, j):
        self.x, self.y = i, j
        self.f, self.g, self.h = 0, 0, 0
        self.neighbours = []
        self.prev = None
        self.wall = False
        self.visited = False

    def show(self, win, col, shape=1):
        if self.wall == True:
            col = (0, 0, 0)
        if shape == 1:
            pygame.draw.rect(win, col, (self.x*w, self.y*h, w-1, h-1))
        else:
            pygame.draw.circle(
                win, col, (self.x*w + w//2, self.y*h + h//2), w//3)
