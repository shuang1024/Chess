import pygame
import chess
from constants import *

class Board:
    def __init__(self):
        self.board = chess.Board()

    def move(self, move):
        self.board.push_uci(move)

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
                        
    def draw_pieces(self, display):
        self.l_board = str(self.board).split("\n")
        for row in range(8):
            for col in range(8):
                board_row = self.l_board[row].replace(" ", "")
                if board_row[col] != ".":
                    display.blit(pieces[board_row[col]], (col*SQ_SIZE, row*SQ_SIZE))
