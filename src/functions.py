import pygame
from constants import *

def get_row_col(mouse_pos):
    return mouse_pos[0]//SQ_SIZE, mouse_pos[1]//SQ_SIZE
