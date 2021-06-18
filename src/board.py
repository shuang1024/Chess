import pygame
import chess
from constants import *

class Board:
    def __init__(self):
        self.board = chess.Board()

    def draw_board(self, display):
        for row in range(8):
            for col in range(8):
                if row % 2 == 0:
                    if col % 2 == 0:
                        pygame.draw.rect(display, LIGHT, (SQ_SIZE*row, SQ_SIZE*col, SQ_SIZE, SQ_SIZE))
                    else:
                        pygame.draw.rect(display, DARK, (SQ_SIZE*row, SQ_SIZE*col, SQ_SIZE, SQ_SIZE))
                else:
                    if col % 2 == 0:
                        pygame.draw.rect(display, DARK, (SQ_SIZE*row, SQ_SIZE*col, SQ_SIZE, SQ_SIZE))
                    else:
                        pygame.draw.rect(display, LIGHT, (SQ_SIZE*row, SQ_SIZE*col, SQ_SIZE, SQ_SIZE))