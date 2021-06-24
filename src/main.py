import pygame
import chess
from board import *
from constants import *
from functions import *

pygame.init()


def main():
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess")

    clock = pygame.time.Clock()

    board = Board()

    while True:
        clock.tick(FPS)
        pygame.display.update()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        mouse_pos = pygame.mouse.get_pos()

        display.fill(BLACK)

        board.draw_board(display)
        board.draw_pieces(display)


main()
