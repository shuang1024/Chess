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
        for row in range(len(l_board)):
            for col in range(len(row)):
                if l_board[row][col] == "P":
                    display.blit(pieces["wp"], (row*SQ_SIZE, col*SQ_SIZE))
                if l_board[row][col] == "N":
                    display.blit(pieces["wn"], (row*SQ_SIZE, col*SQ_SIZE))
                if l_board[row][col] == "B":
                    display.blit(pieces["wb"], (row*SQ_SIZE, col*SQ_SIZE))
                if l_board[row][col] == "R":
                    display.blit(pieces["wr"], (row*SQ_SIZE, col*SQ_SIZE))
                if l_board[row][col] == "Q":
                    display.blit(pieces["wq"], (row*SQ_SIZE, col*SQ_SIZE))
                if l_board[row][col] == "K":
                    display.blit(pieces["wk"], (row*SQ_SIZE, col*SQ_SIZE))
                if l_board[row][col] == "p":
                    display.blit(pieces["bp"], (row*SQ_SIZE, col*SQ_SIZE))
                if l_board[row][col] == "n":
                    display.blit(pieces["bn"], (row*SQ_SIZE, col*SQ_SIZE))
                if l_board[row][col] == "b":
                    display.blit(pieces["bb"], (row*SQ_SIZE, col*SQ_SIZE))
                if l_board[row][col] == "r":
                    display.blit(pieces["br"], (row*SQ_SIZE, col*SQ_SIZE))
                if l_board[row][col] == "q":
                    display.blit(pieces["bq"], (row*SQ_SIZE, col*SQ_SIZE))
                if l_board[row][col] == "k":
                    display.blit(pieces["bk"], (row*SQ_SIZE, col*SQ_SIZE))
