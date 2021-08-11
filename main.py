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
import os

# Constants
size = 80
ft = 0
coord_list = []
run = True
pieces = []

selected_piece = None

piece_names = [
        ["P", "Pawn"],
        ["K", "King"],
        ["Q", "Queen"],
        ["R", "Rook"],
        ["B", "Bishop"],
        ["N", "Knight"]
    ]

start_positions = [
        'wPA2', 'wPB2', "wPC2", "wPD2", "wPE2", "wPF2", "wPG2", "wPH2",
        'wRA1', "wNB1", "wBC1", "wQD1", "wKE1", "wBF1", "wNG1", "wRH1",
        'bPA7', 'bPB7', "bPC7", "bPD7", "bPE7", "bPF7", "bPG7", "bPH7",
        'bRA8', "bNB8", "bBC8", "bQD8", "bKE8", "bBF8", "bNG8", "bRH8",
    ]

positions = [
        ["A1", [80, 720], [160, 640]],
        ["A2", [80, 640], [160, 560]],
        ["A3", [80, 560], [160, 480]],
        ["A4", [80, 480], [160, 400]],
        ["A5", [80, 400], [160, 320]],
        ["A6", [80, 320], [160, 240]],
        ["A7", [80, 240], [160, 160]],
        ["A8", [80, 180], [160, 80]],
        ["B1", [160, 720], [240, 640]],
        ["B2", [160, 640], [240, 560]],
        ["B3", [160, 560], [240, 480]],
        ["B4", [160, 480], [240, 400]],
        ["B5", [160, 400], [240, 320]],
        ["B6", [160, 320], [240, 240]],
        ["B7", [160, 240], [240, 160]],
        ["B8", [160, 180], [240, 80]],
        ["C1", [240, 720], [320, 640]],
        ["C2", [240, 640], [320, 560]],
        ["C3", [240, 560], [320, 480]],
        ["C4", [240, 480], [320, 400]],
        ["C5", [240, 400], [320, 320]],
        ["C6", [240, 320], [320, 240]],
        ["C7", [240, 240], [320, 160]],
        ["C8", [240, 180], [320, 80]],
        ["D1", [320, 720], [400, 640]],
        ["D2", [320, 640], [400, 560]],
        ["D3", [320, 560], [400, 480]],
        ["D4", [320, 480], [400, 400]],
        ["D5", [320, 400], [400, 320]],
        ["D6", [320, 320], [400, 240]],
        ["D7", [320, 240], [400, 160]],
        ["D8", [320, 180], [400, 80]],
        ["E1", [400, 720], [480, 640]],
        ["E2", [400, 640], [480, 560]],
        ["E3", [400, 560], [480, 480]],
        ["E4", [400, 480], [480, 400]],
        ["E5", [400, 400], [480, 320]],
        ["E6", [400, 320], [480, 240]],
        ["E7", [400, 240], [480, 160]],
        ["E8", [400, 180], [480, 80]],
        ["F1", [480, 720], [560, 640]],
        ["F2", [480, 640], [560, 560]],
        ["F3", [480, 560], [560, 480]],
        ["F4", [480, 480], [560, 400]],
        ["F5", [480, 400], [560, 320]],
        ["F6", [480, 320], [560, 240]],
        ["F7", [480, 240], [560, 160]],
        ["F8", [480, 180], [560, 80]],
        ["G1", [560, 720], [640, 640]],
        ["G2", [560, 640], [640, 560]],
        ["G3", [560, 560], [640, 480]],
        ["G4", [560, 480], [640, 400]],
        ["G5", [560, 400], [640, 320]],
        ["G6", [560, 320], [640, 240]],
        ["G7", [560, 240], [640, 160]],
        ["G8", [560, 180], [640, 80]],
        ["H1", [640, 720], [720, 640]],
        ["H2", [640, 640], [720, 560]],
        ["H3", [640, 560], [720, 480]],
        ["H4", [640, 480], [720, 400]],
        ["H5", [640, 400], [720, 320]],
        ["H6", [640, 320], [720, 240]],
        ["H7", [640, 240], [720, 160]],
        ["H8", [640, 180], [720, 80]],
    ]

img_folder = (os.path.abspath("images/berlin/"))


class Piece:
    def __init__(self, pos_x, pos_y, color, figure_name, img_folder, pos_name):
        self.color = color
        self.pos_x = int(pos_x)
        self.pos_y = int(pos_y)
        self.pos_name = pos_name
        self.figure_name = figure_name
        self.img = img_folder+"/{}.png".format(color+figure_name)
        self.dead = False

    def update_pos(self, pos_name):
        for i in positions:
            if pos_name == i[0]:
                self.pos_x = i[1][0]
                self.pos_y = i[2][1]


# game init and window options
pygame.init()
window = pygame.display.set_mode((1800, 1000))
window.fill((211, 211, 211))
pygame.display.set_caption("CHESS")


def create_figure_instances(start_pos):
    for pos in start_pos:
        for i in positions:
            if i[0] == pos[2:4]:
                z = Piece(i[1][0], i[2][1], pos[0], pos[1], img_folder, pos[2:4])
                pieces.append(z)


create_figure_instances(start_positions)


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
    for i in positions:
        if i[1][0] < pos[0] < i[2][0]:
            if i[1][1] > pos[1] > i[2][1]:
                return i[0]


def mouse_down():
    pos = mouse_pos()
    found = False
    global selected_piece
    for piece in pieces:
        if pos == piece.pos_name:
            found = True
            if selected_piece is None:
                selected_piece = piece
    if not found:
        if selected_piece is not None:
            selected_piece.update_pos(pos)
            selected_piece = None


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
