import os
import pygame

WIDTH, HEIGHT = 800, 800
FPS = 60

BLACK = (0, 0, 0)
DARK = (50, 50, 50)
LIGHT = (80, 165, 80)

SQ_SIZE = 100

pieces = {}

for f in ("p", "n", "b", "r", "q", "k"):
    for l in ("w", "b"):
        img = pygame.transform.scale(pygame.image.load(os.path.join("imgs", f + l + ".png")), (SQ_SIZE, SQ_SIZE))
        pieces[f + l] = img
