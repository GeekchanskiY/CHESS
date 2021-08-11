"""
    Chess game written by DMT
    https://github.com/GeekchanskiY/CHESS

    base api for chess experiments

    Future plans:
        - add AI
        - add chess.com support
        - have fun :)
"""

import pygame
from constants import Const
from classes import Piece
import os


img_folder = (os.path.abspath("images/berlin/"))

# game init and window options
pygame.init()
window = pygame.display.set_mode((1800, 1000))
window.fill((211, 211, 211))
pygame.display.set_caption("CHESS")

size = 80
ft = 0
coord_list = []
run = True
pieces = []


def create_figure_instances(start_positions):
    for pos in start_positions:
        for i in Const.positions:
            if i[0] == pos[2:4]:
                z = Piece(i[1][0], i[2][1], pos[0], pos[1], img_folder)
                pieces.append(z)


create_figure_instances(Const.start_positions)


def draw_board():
    cnt = 0
    for i in range(1, 9):
        for z in range(1, 9):
            if cnt % 2 == 0:
                pygame.draw.rect(window, pygame.Color(50, 50, 50), (size*z, size*i, size, size))
                w = False
            else:
                pygame.draw.rect(window, pygame.Color(255, 255, 255), (size*z, size*i, size, size))
                w = True
            if ft == 0:
                coord_list.append({size * z, size * i})
            cnt += 1
        cnt -= 1


def mouse_pos():
    pos = pygame.mouse.get_pos()
    for i in Const.positions:
        if i[1][0] < pos[0] < i[2][0]:
            if i[1][1] > pos[1] > i[2][1]:
                print(i[0])


def mouse_down():
    mouse_pos()


def draw_figures():
    for piece in pieces:
        window.blit(pygame.image.load(piece.img), (piece.pos_x, piece.pos_y))


while run:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down()

    draw_board()
    draw_figures()
    # Updating display
    pygame.display.update()

print("See you next time!")
pygame.quit()
