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


positions = {}
cnt = 0
# Generating coordinates
for z in range(1, 9):
    for i in range(1, 9):
        positions[str(z) + str(9-i)] = [size * z, size * (z+1), size * i, size * (i+1)]
print(positions)
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
        self.img = img_folder+"/{}.png".format(self.color+self.name)

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

    def get_pos_coord(self):
        return positions.get(self.pos)[0], positions.get(self.pos)[2]

    def draw(self):
        window.blit(pygame.image.load(self.img), (self.get_pos_coord()))


# game init and window options
pygame.init()
window = pygame.display.set_mode((1800, 1000))
window.fill((211, 211, 211))
pygame.display.set_caption("CHESS")


def create_figure_instances(start_pos):

    for pos in start_pos:
        pieces.append(Piece(pos[0], pos[1], pos[2:4]))


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
    for z in positions:
        i = positions.get(z)
        if int(i[0]) < pos[0] < int(i[1]):
            if int(i[2]) < pos[1] < int(i[3]):
                return z

def mouse_down():
    print(mouse_pos())


def draw_figures():
    for piece in pieces:
        piece.draw()


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
