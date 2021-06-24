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
                        
    def draw_pieces(self, display):
        l_board = str(self.board).split("\n")
        for row in range(8):
            for col in range(8):
                board_row = l_board[row].replace(" ", "")
                if board_row[col] == "P":
                    display.blit(pieces["pw"], (col*SQ_SIZE, row*SQ_SIZE))
                elif board_row[col] == "N":
                    display.blit(pieces["nw"], (col*SQ_SIZE, row*SQ_SIZE))
                elif board_row[col] == "B":
                    display.blit(pieces["bw"], (col*SQ_SIZE, row*SQ_SIZE))
                elif board_row[col] == "R":
                    display.blit(pieces["rw"], (col*SQ_SIZE, row*SQ_SIZE))
                elif board_row[col] == "Q":
                    display.blit(pieces["qw"], (col*SQ_SIZE, row*SQ_SIZE))
                elif board_row[col] == "K":
                    display.blit(pieces["kw"], (col*SQ_SIZE, row*SQ_SIZE))
                elif board_row[col] == "p":
                    display.blit(pieces["pb"], (col*SQ_SIZE, row*SQ_SIZE))
                elif board_row[col] == "n":
                    display.blit(pieces["nb"], (col*SQ_SIZE, row*SQ_SIZE))
                elif board_row[col] == "b":
                    display.blit(pieces["bb"], (col*SQ_SIZE, row*SQ_SIZE))
                elif board_row[col] == "r":
                    display.blit(pieces["rb"], (col*SQ_SIZE, row*SQ_SIZE))
                elif board_row[col] == "q":
                    display.blit(pieces["qb"], (col*SQ_SIZE, row*SQ_SIZE))
                elif board_row[col] == "k":
                    display.blit(pieces["kb"], (col*SQ_SIZE, row*SQ_SIZE))
