"""
    Chess game written by DMT
    https://github.com/GeekchanskiY/CHESS

    base api for chess experiments

    Future plans:
        - add AI
        - add freaking en passant rule
        - add chess.com support
        - have fun :)
"""

import pygame
import os

# Constants

turn = 0

size = 80
ft = 0
coord_list = []
run = True
pieces = []
selected_piece = None
dragging = False
possible_moves = []
turn_log = ""
white_dead_pieces_counter = 0
black_dead_pieces_counter = 0
piece_names = [
        ["P", "Pawn"],
        ["K", "King"],
        ["Q", "Queen"],
        ["R", "Rook"],
        ["B", "Bishop"],
        ["N", "Knight"]
    ]


start_positions = [
        'wP12', 'wP22', "wP32", "wP42", "wP52", "wP62", "wP72", "wP82",
        'wR11', "wN21", "wB31", "wQ41", "wK51", "wB61", "wN71", "wR81",
        'bP17', 'bP27', "bP37", "bP47", "bP57", "bP67", "bP77", "bP87",
        'bR18', "bN28", "bB38", "bQ48", "bK58", "bB68", "bN78", "bR88",
    ]

field_names_x = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8
}
field_names_x_rev = {value: key for key, value in field_names_x.items()}

positions = [
        ["11", [80, 720], [160, 640]],
        ["12", [80, 640], [160, 560]],
        ["13", [80, 560], [160, 480]],
        ["14", [80, 480], [160, 400]],
        ["15", [80, 400], [160, 320]],
        ["16", [80, 320], [160, 240]],
        ["17", [80, 240], [160, 160]],
        ["18", [80, 180], [160, 80]],
        ["21", [160, 720], [240, 640]],
        ["22", [160, 640], [240, 560]],
        ["23", [160, 560], [240, 480]],
        ["24", [160, 480], [240, 400]],
        ["25", [160, 400], [240, 320]],
        ["26", [160, 320], [240, 240]],
        ["27", [160, 240], [240, 160]],
        ["28", [160, 180], [240, 80]],
        ["31", [240, 720], [320, 640]],
        ["32", [240, 640], [320, 560]],
        ["33", [240, 560], [320, 480]],
        ["34", [240, 480], [320, 400]],
        ["35", [240, 400], [320, 320]],
        ["36", [240, 320], [320, 240]],
        ["37", [240, 240], [320, 160]],
        ["38", [240, 180], [320, 80]],
        ["41", [320, 720], [400, 640]],
        ["42", [320, 640], [400, 560]],
        ["43", [320, 560], [400, 480]],
        ["44", [320, 480], [400, 400]],
        ["45", [320, 400], [400, 320]],
        ["46", [320, 320], [400, 240]],
        ["47", [320, 240], [400, 160]],
        ["48", [320, 180], [400, 80]],
        ["51", [400, 720], [480, 640]],
        ["52", [400, 640], [480, 560]],
        ["53", [400, 560], [480, 480]],
        ["54", [400, 480], [480, 400]],
        ["55", [400, 400], [480, 320]],
        ["56", [400, 320], [480, 240]],
        ["57", [400, 240], [480, 160]],
        ["58", [400, 180], [480, 80]],
        ["61", [480, 720], [560, 640]],
        ["62", [480, 640], [560, 560]],
        ["63", [480, 560], [560, 480]],
        ["64", [480, 480], [560, 400]],
        ["65", [480, 400], [560, 320]],
        ["66", [480, 320], [560, 240]],
        ["67", [480, 240], [560, 160]],
        ["68", [480, 180], [560, 80]],
        ["71", [560, 720], [640, 640]],
        ["72", [560, 640], [640, 560]],
        ["73", [560, 560], [640, 480]],
        ["74", [560, 480], [640, 400]],
        ["75", [560, 400], [640, 320]],
        ["76", [560, 320], [640, 240]],
        ["77", [560, 240], [640, 160]],
        ["78", [560, 180], [640, 80]],
        ["81", [640, 720], [720, 640]],
        ["82", [640, 640], [720, 560]],
        ["83", [640, 560], [720, 480]],
        ["84", [640, 480], [720, 400]],
        ["85", [640, 400], [720, 320]],
        ["86", [640, 320], [720, 240]],
        ["87", [640, 240], [720, 160]],
        ["88", [640, 180], [720, 80]],
    ]
black_dead_pieces_positions = {
    1: (980, 80),
    2: (980, 160),
    3: (980, 240),
    4: (980, 320),
    5: (980, 400)
}
white_dead_pieces_positions = {
    1: (900, 80),
    2: (900, 160),
    3: (900, 240),
    4: (900, 320),
    5: (900, 400)
}
img_folder = (os.path.abspath("images/berlin/"))
dot_img = os.path.abspath("images/dot.png")


def pawn_move(instance):
    moves = []
    return moves


def king_move(instance):
    pass


def queen_move(instance):
    pass


def rook_move(instance):
    pass


def bishop_move(instance):
    pass


def knight_move(instance):
    pass


def hint(instance):
    pass


class Piece:
    """
        Main piece class with all it's actions
    """
    def __init__(self, color, name, pos):
        self.dead = True
        self.moved = False
        self.color = color
        self.name = name
        self.pos = pos
        pass

    def what_can_i_do(self):
        """

        Analyzing possible moves

        :return:
        """
        pass

    def update_pos(self):
        """

        Updating piece position

        :param pos_name:
        :return:
        """
        pass

    def move(self):
        """

        Moving piece with build-in validation

        :param pos_name:
        :return:
        """
        pass

    def die(self):
        """

        Removing piece from board with build-in validation

        :return:
        """
        pass


# game init and window options
pygame.init()
window = pygame.display.set_mode((1800, 1000))
window.fill((211, 211, 211))
pygame.display.set_caption("CHESS")


def create_figure_instances(start_pos):
    pass


create_figure_instances(start_positions)


def draw_board():
    cnt = 0
    for i in range(1, 9):
        for z in range(1, 9):
            if cnt % 2 == 0:
                pygame.draw.rect(window, pygame.Color(50, 50, 50), (size*z, size*i, size, size))
            else:
                pygame.draw.rect(window, pygame.Color(255, 255, 255), (size*z, size*i, size, size))
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
    print(pos)


def draw_figures():
    for piece in pieces:
        window.blit(pygame.image.load(piece.img), (piece.pos_x, piece.pos_y))


while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_down()
            elif event.button == 3:
                selected_piece = None
                possible_moves = None

    draw_board()
    draw_figures()
    # Creating hints
    if selected_piece is not None:
        hint(selected_piece)
    # Updating display
    pygame.display.update()

print("See you next time!")
pygame.quit()
