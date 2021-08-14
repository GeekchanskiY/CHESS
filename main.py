"""
    Chess game written by DMT
    https://github.com/GeekchanskiY/CHESS

    base api for chess experiments

    Future plan:
        - Finish piece movement logic
        - add "en passant" rule

        - add AI
        - add chess.com support for AI learning by analyzing games
        - Create vk api for playing with friends
        - have fun :)


"""

import pygame
import os
#
#   Constants
#

# Current turn constant for AI, log and "en passant" rule
turn = 0

# Size of cell. By default it's 80 because of piece images resolution.
size = 80

# App running
run = True

# List of all pieces in game
pieces = []

# Argument for making a link on current selected piece
selected_piece = None

# Argument for future smooth dragging animation
dragging = False

# Turn log for AI
turn_log = ""

# Counter of dead pieces for correct rendering
white_dead_pieces_counter = 0
black_dead_pieces_counter = 0

# Pieces short and full names
piece_names = {
    "P": "Pawn",
    "K": "King",
    "Q": "Queen",
    "R": "Rook",
    "B": "Bishop",
    "N": "Knight"
}

# Const for first creating pieces
start_positions = [
        'wP12', 'wP22', "wP32", "wP42", "wP52", "wP62", "wP72", "wP82",
        'wR11', "wN21", "wB31", "wQ41", "wK51", "wB61", "wN71", "wR81",
        'bP17', 'bP27', "bP37", "bP47", "bP57", "bP67", "bP77", "bP87",
        'bR18', "bN28", "bB38", "bQ48", "bK58", "bB68", "bN78", "bR88",
    ]

# Dictionaries for translating numeric pos name to classic and vice versa
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


# Generating coordinates
for z in range(1, 9):
    for i in range(1, 9):
        positions[int(str(z) + str(9-i))] = [size * z, size * (z+1), size * i, size * (i+1)]

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

# Image folders
img_folder = (os.path.abspath("images/berlin/"))
dot_img = os.path.abspath("images/dot.png")


def pawn_move(instance):
    moves = []
    f1 = True
    f2 = True
    for piece in pieces:
        if instance.color == "w":
            if piece.pos == instance.pos + 11:
                moves.append(piece.pos)
            if piece.pos == instance.pos - 9:
                moves.append(piece.pos)
            if instance.moved is False:
                if piece.pos == instance.pos + 1:
                    f1 = False
                    f2 = False
                if piece.pos == instance.pos + 2:
                    f2 = False
            else:
                if piece.pos == instance.pos + 1:
                    f1 = False
                f2 = False
        else:
            if piece.pos == instance.pos + 9:
                moves.append(piece.pos)
            if piece.pos == instance.pos - 11:
                moves.append(piece.pos)
            if instance.moved:
                f2 = False
                if piece.pos == instance.pos - 1:
                    f1 = False
            else:
                if piece.pos == instance.pos - 1:
                    f1 = False
                    f2 = False
                if piece.pos == instance.pos - 2:
                    f2 = False

    if f1:
        if instance.color == "w":
            moves.append(instance.pos + 1)
        else:
            moves.append(instance.pos - 1)
    if f2:
        if instance.color == "w":
            moves.append(instance.pos + 2)
        else:
            moves.append(instance.pos - 2)
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


def draw_hints(instance):
    # Hint drawing for each possible move of selected piece. Also useful for creating logic.
    for move in instance.moves:
        window.blit(pygame.image.load(dot_img), (positions.get(move)[0], positions.get(move)[2]))


class Piece:
    """
        Main dynamic piece class with all it's actions

        Color, name, dead and position are for rendering and logic

        moved is an argument for AI and pawn logic

        first turn is also an argument for AI, but also it's
        for an "en passant" rule in chess
        To read more about the "en passant" rule you can visit:
            https://en.wikipedia.org/wiki/En_passant

        img argument is for holding rendering image only

    """
    def __init__(self, color, name, pos):
        self.color = color
        self.name = name
        self.pos = int(pos)

        self.dead = True
        self.moved = False
        self.first_turn = None

        self.moves = self.what_can_i_do()

        self.img = img_folder+"/{}.png".format(self.color+self.name)

    def what_can_i_do(self):
        """

        Analyzing possible moves

        :return:
        """
        return {
            "P": pawn_move(self),
            "K": king_move(self),
            "Q": queen_move(self),
            "R": rook_move(self),
            "B": bishop_move(self),
            "N": knight_move(self),
        }.get(self.name)

    def move(self, pos):
        """

        Moving piece with build-in validation
        also "Killing" validation is in the movement method
        after moving deselecting piece

        :param pos:
        :return:
        """
        global selected_piece
        for move in self.what_can_i_do():
            if pos == move:
                self.pos = pos
                self.moved = True
                self.moves = self.what_can_i_do()
                selected_piece = None

    def die(self):
        """

        Removing piece from board with build-in validation

        :return:
        """
        self.dead = True

    def get_pos_coord(self):
        """

            Method for returning position coordinates of each piece

        :return:
        """
        return positions.get(self.pos)[0], positions.get(self.pos)[2]


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
    """

        Function for finding the cell on which the mouse is located

    :return:
    """
    mouse_position = pygame.mouse.get_pos()
    for p in positions:
        cell = positions.get(p)
        if int(cell[0]) < mouse_position[0] < int(cell[1]):
            if int(cell[2]) < mouse_position[1] < int(cell[3]):
                return p


def mouse_down():
    """

        Logic for LMB click

    :return:
    """
    global selected_piece
    pos = mouse_pos()
    if selected_piece is None:
        for piece in pieces:
            if pos == piece.pos:
                selected_piece = piece
                print(piece.color, piece.name, "Selected")
    else:
        selected_piece.move(pos)


def draw_figures():
    # Rendering of each piece
    for piece in pieces:
        window.blit(pygame.image.load(piece.img), (piece.get_pos_coord()))


while run:
    # Delay for reducing the CPU load
    pygame.time.delay(100)

    # Event listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Pausing the main game loop on quitting the game
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # LMB click logic
                mouse_down()
            elif event.button == 3:
                # RMB click logic
                if selected_piece is not None:
                    print(selected_piece.color, selected_piece.name, "Deselected")
                    selected_piece = None
    # Calling main piece and board rendering functions
    draw_board()
    draw_figures()
    # Creating hints
    if selected_piece is not None:
        draw_hints(selected_piece)
    # Updating display
    pygame.display.update()

print("See you next time!")
# Quitting the app
pygame.quit()
