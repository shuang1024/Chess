import pygame
import chess
from constants import *

class Board:
    def __init__(self):
        self.board = chess.Board()

    def draw_board(self, display):
        for row in range(1, 9):
            for col in range(1, 9):
                if row % 2 == 0:
                    if col % 2 == 0:
                        pygame.draw.rect(display, LIGHT, (PADDING * row, PADDING * col, SQ_SIZE, SQ_SIZE))
                    else:
                        pygame.draw.rect(display, DARK, (PADDING * row, PADDING * col, SQ_SIZE, SQ_SIZE))
                else:
                    if col % 2 == 0:
                        pygame.draw.rect(display, DARK, (PADDING * row, PADDING * col, SQ_SIZE, SQ_SIZE))
                    else:
                        pygame.draw.rect(display, LIGHT, (PADDING * row, PADDING * col, SQ_SIZE, SQ_SIZE))