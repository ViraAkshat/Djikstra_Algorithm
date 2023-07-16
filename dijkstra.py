import pygame
from collections import deque
import math

size = (width, height) = (640, 480)
pygame.init()

win = pygame.display.set_mode(size)
pygame.display.set_caption("Dijkstra's Path Finding")
clock = pygame.time.Clock()

cols, rows = width/10, height/10

grid = []
queue, visited = deque(), []
path = []
