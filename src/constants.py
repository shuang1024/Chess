import os
import pygame

WIDTH, HEIGHT = 800, 800
FPS = 60

BLACK = (0, 0, 0)
DARK = (60, 45, 0)
LIGHT = (225, 200, 150)

SQ_SIZE = 100

pieces = {}

for f in ("p", "n", "b", "r", "q", "k"):
    for l in ("w", "b"):
        img = pygame.transform.scale(pygame.image.load(os.path.abspath("img/" + f + l + ".png")), (SQ_SIZE, SQ_SIZE))
        if l == "w":
            pieces[f.upper()] = img
        else:
            pieces[f] = img