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

# Current color 0 - white, 1 - black

current_color = 0

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
    "N": "Knight",
}

# Const for first creating pieces
start_positions = [
    "wP12",
    "wP22",
    "wP32",
    "wP42",
    "wP52",
    "wP62",
    "wP72",
    "wP82",
    "wR11",
    "wN21",
    "wB31",
    "wQ41",
    "wK51",
    "wB61",
    "wN71",
    "wR81",
    "bP17",
    "bP27",
    "bP37",
    "bP47",
    "bP57",
    "bP67",
    "bP77",
    "bP87",
    "bR18",
    "bN28",
    "bB38",
    "bQ48",
    "bK58",
    "bB68",
    "bN78",
    "bR88",
]

# Dictionaries for translating numeric pos name to classic and vice versa
field_names_x = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
field_names_x_rev = {value: key for key, value in field_names_x.items()}


positions = {}


# Generating coordinates
for z in range(1, 9):
    for i in range(1, 9):
        positions[int(str(z) + str(9 - i))] = [
            size * z,
            size * (z + 1),
            size * i,
            size * (i + 1),
        ]

# Image folders
img_folder = os.path.abspath("images/berlin/")
dot_img = os.path.abspath("images/dot.png")


# Movement functions. It takes an instance and returns a list of lists with 2 elements.
# 1 - possible move
# 2 - returns piece that dies after possible move. None if there's no such piece


def pawn_move(instance):
    moves = []
    f1 = True
    f2 = True
    for piece in pieces:
        # Pawn movement and killing logic
        if instance.color == "w":
            if piece.pos == instance.pos + 11 and piece.color != instance.color:
                moves.append([piece.pos, piece])
            if piece.pos == instance.pos - 9 and piece.color != instance.color:
                moves.append([piece.pos, piece])
            if instance.last_turn is None:
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
            if piece.pos == instance.pos + 9 and piece.color != instance.color:
                moves.append([piece.pos, piece])
            if piece.pos == instance.pos - 11 and piece.color != instance.color:
                moves.append([piece.pos, piece])
            if instance.last_turn is None:
                if piece.pos == instance.pos - 1:
                    f1 = False
                    f2 = False
                if piece.pos == instance.pos - 2:
                    f2 = False
            else:
                f2 = False
                if piece.pos == instance.pos - 1:
                    f1 = False

        # En passant rule
        if piece.pos == instance.pos + 10:
            if (
                piece.name == "P"
                and piece.last_turn == turn - 1
                and piece.color != instance.color
            ):
                if instance.color == "w":
                    moves.append([instance.pos + 11, piece])
                else:
                    moves.append([instance.pos + 9, piece])
        if piece.pos == instance.pos - 10:
            if (
                piece.name == "P"
                and piece.last_turn == turn - 1
                and piece.color != instance.color
            ):
                if instance.color == "w":
                    moves.append([instance.pos - 9, piece])
                else:
                    moves.append([instance.pos - 11, piece])

    if f1:
        if instance.color == "w":
            moves.append([instance.pos + 1, None])
        else:
            moves.append([instance.pos - 1, None])
    if f2:
        if instance.color == "w":
            moves.append([instance.pos + 2, None])
        else:
            moves.append([instance.pos - 2, None])
    return moves


def king_move(instance):
    moves = []
    if instance.pos > 20:
        found = False
        for piece in pieces:
            if piece.pos == instance.pos - 10:
                found = True
                if piece.color != instance.color:
                    moves.append([piece.pos, piece])
        if not found:
            moves.append([instance.pos - 10, None])
        if instance.pos % 10 > 1:
            found = False
            for piece in pieces:
                if piece.pos == instance.pos - 11:
                    found = True
                    if piece.color != instance.color:
                        moves.append([piece.pos, piece])
            if not found:
                moves.append([instance.pos - 11, None])
        if instance.pos % 10 < 8:
            found = False
            for piece in pieces:
                if piece.pos == instance.pos - 9:
                    found = True
                    if piece.color != instance.color:
                        moves.append([piece.pos, piece])
            if not found:
                moves.append([instance.pos - 9, None])

    if instance.pos < 70:
        found = False
        for piece in pieces:
            if piece.pos == instance.pos + 10:
                found = True
                if piece.color != instance.color:
                    moves.append([piece.pos, piece])
        if not found:
            moves.append([instance.pos + 10, None])
        if instance.pos % 10 > 1:
            found = False
            for piece in pieces:
                if piece.pos == instance.pos + 9:
                    found = True
                    if piece.color != instance.color:
                        moves.append([piece.pos, piece])
            if not found:
                moves.append([instance.pos + 9, None])
        if instance.pos % 10 < 8:
            found = False
            for piece in pieces:
                if piece.pos == instance.pos + 11:
                    found = True
                    if piece.color != instance.color:
                        moves.append([piece.pos, piece])
            if not found:
                moves.append([instance.pos + 11, None])
    if instance.pos % 10 > 1:
        for piece in pieces:
            found = False
            if piece.pos == instance.pos - 1:
                found = True
                if piece.color != instance.color:
                    moves.append([piece.pos, piece])
            if not found:
                moves.append([instance.pos - 1, None])
    if instance.pos % 10 < 8:
        for piece in pieces:
            found = False
            if piece.pos == instance.pos + 1:
                found = True
                if piece.color != instance.color:
                    moves.append([piece.pos, piece])
            if not found:
                moves.append([instance.pos + 1, None])

    return moves


def queen_move(instance):
    moves = []
    for move in rook_move(instance):
        moves.append(move)
    for move in bishop_move(instance):
        moves.append(move)
    return moves


def rook_move(instance):
    moves = []

    forward = True
    backward = True
    left = True
    right = True

    if instance.pos % 10 == 8:
        forward = False
    if instance.pos % 10 == 1:
        backward = False
    if instance.pos >= 81:
        right = False
    if instance.pos <= 18:
        left = False

    if forward:
        temp_pos = instance.pos + 1
        found = False
        while temp_pos % 10 <= 8 and not found:
            for piece in pieces:
                if piece.pos == temp_pos:
                    if piece.color == instance.color:
                        found = True
                    else:
                        moves.append([temp_pos, piece])
                        found = True
            if not found:
                moves.append([temp_pos, None])
                temp_pos += 1

    if backward:
        temp_pos = instance.pos - 1
        found = False
        while temp_pos % 10 >= 1 and not found:
            for piece in pieces:
                if piece.pos == temp_pos:
                    if piece.color == instance.color:
                        found = True
                    else:
                        moves.append([temp_pos, piece])
                        found = True
            if not found:
                moves.append([temp_pos, None])
                temp_pos -= 1

    if right:
        temp_pos = instance.pos + 10
        found = False
        while temp_pos <= 88 and not found:
            for piece in pieces:
                if piece.pos == temp_pos:
                    if piece.color == instance.color:
                        found = True
                    else:
                        moves.append([temp_pos, piece])
                        found = True
            if not found:
                moves.append([temp_pos, None])
                temp_pos += 10

    if left:
        temp_pos = instance.pos - 10
        found = False
        while temp_pos >= 11 and not found:
            for piece in pieces:
                if piece.pos == temp_pos:
                    if piece.color == instance.color:
                        found = True
                    else:
                        moves.append([temp_pos, piece])
                        found = True
            if not found:
                moves.append([temp_pos, None])
                temp_pos -= 10

    return moves


def bishop_move(instance):
    moves = []

    fl1 = True
    fr1 = True
    bl1 = True
    br1 = True

    if instance.pos % 10 == 8:
        fl1 = False
        fr1 = False
    if instance.pos % 10 == 1:
        bl1 = False
        br1 = False
    if instance.pos <= 21:
        fl1 = False
        bl1 = False
    if instance.pos >= 81:
        fr1 = False
        br1 = False

    if fr1:
        temp_pos = instance.pos
        found = False
        while temp_pos % 10 < 8 and temp_pos <= 78 and not found:
            for piece in pieces:
                if piece.pos == temp_pos + 11:
                    if piece.color == instance.color:
                        found = True
                    else:
                        found = True
                        moves.append([piece.pos, piece])
            if not found:
                temp_pos += 11
                moves.append([temp_pos, None])

    if fl1:
        temp_pos = instance.pos
        found = False
        while temp_pos % 10 < 8 and temp_pos > 20 and not found:
            for piece in pieces:
                if piece.pos == temp_pos - 9:
                    if piece.color == instance.color:
                        found = True
                    else:
                        found = True
                        moves.append([piece.pos, piece])
            if not found:
                temp_pos -= 9
                moves.append([temp_pos, None])

    if bl1:
        temp_pos = instance.pos
        found = False
        while temp_pos % 10 > 1 and temp_pos > 20 and not found:
            for piece in pieces:
                if piece.pos == temp_pos - 11:
                    if piece.color == instance.color:
                        found = True
                    else:
                        found = True
                        moves.append([piece.pos, piece])
            if not found:
                temp_pos -= 11
                moves.append([temp_pos, None])

    if br1:
        temp_pos = instance.pos
        found = False
        while temp_pos % 10 > 1 and temp_pos <= 78 and not found:
            for piece in pieces:
                if piece.pos == temp_pos + 9:
                    if piece.color == instance.color:
                        found = True
                    else:
                        found = True
                        moves.append([piece.pos, piece])
            if not found:
                moves.append([temp_pos + 9, None])
                temp_pos += 9

    return moves


def knight_move(instance):
    moves = []
    if instance.pos % 10 <= 6:
        if instance.pos < 80:
            found = False
            for piece in pieces:
                if piece.pos == instance.pos + 12:
                    found = True
                    if piece.color != instance.color:
                        moves.append([piece.pos, piece])
            if not found:
                moves.append([instance.pos + 12, None])
        if instance.pos > 20:
            found = False
            for piece in pieces:
                if piece.pos == instance.pos - 8:
                    found = True
                    if piece.color != instance.color:
                        moves.append([piece.pos, piece])
            if not found:
                moves.append([instance.pos - 8, None])

    if instance.pos % 10 >= 3:
        if instance.pos < 80:
            found = False
            for piece in pieces:
                if piece.pos == instance.pos + 8:
                    found = True
                    if piece.color != instance.color:
                        moves.append([piece.pos, piece])
            if not found:
                moves.append([instance.pos + 8, None])
        if instance.pos > 20:
            found = False
            for piece in pieces:
                if piece.pos == instance.pos - 12:
                    found = True
                    if piece.color != instance.color:
                        moves.append([piece.pos, piece])
            if not found:
                moves.append([instance.pos - 12, None])

    if instance.pos > 30:
        if instance.pos % 10 > 1:
            found = False
            for piece in pieces:
                if piece.pos == instance.pos - 21:
                    found = True
                    if piece.color != instance.color:
                        moves.append([piece.pos, piece])
            if not found:
                moves.append([instance.pos - 21, None])
        if instance.pos % 10 < 8:
            found = False
            for piece in pieces:
                if piece.pos == instance.pos - 19:
                    found = True
                    if piece.color != instance.color:
                        moves.append([piece.pos, piece])
            if not found:
                moves.append([instance.pos - 19, None])

    if instance.pos < 70:
        if instance.pos % 10 < 8:
            found = False
            for piece in pieces:
                if piece.pos == instance.pos + 21:
                    found = True
                    if piece.color != instance.color:
                        moves.append([piece.pos, piece])
            if not found:
                moves.append([instance.pos + 21, None])
        if instance.pos % 10 > 1:
            found = False
            for piece in pieces:
                if piece.pos == instance.pos + 19:
                    found = True
                    if piece.color != instance.color:
                        moves.append([piece.pos, piece])
            if not found:
                moves.append([instance.pos + 19, None])

    return moves


def draw_hints(instance):
    # Hint drawing for each possible move of selected piece. Also useful for creating logic.
    if instance.moves is not None and len(instance.moves) > 0:
        for move in instance.moves:
            window.blit(
                pygame.image.load(dot_img),
                (positions.get(move[0])[0], positions.get(move[0])[2]),
            )
    else:
        print("I cant move :(")


class Piece:
    """
    Main dynamic piece class with all it's actions

    Color, name, dead and position are for rendering and logic

    last_turn is an argument for AI and pawn logic (1st move & en passant rule)
    To read more about the "en passant" rule you can visit:
        https://en.wikipedia.org/wiki/En_passant

    img argument is for holding rendering image only

    """

    def __init__(self, color, name, pos):
        self.color = color
        self.name = name
        self.pos = int(pos)

        self.last_turn = None

        self.moves = None

        self.img = None
        self.create_img()

    def create_img(self):
        self.img = img_folder + "/{}.png".format(self.color + self.name)

    def what_can_i_do(self):
        """

        Analyzing possible moves

        :return:
        """
        self.moves = {
            "P": pawn_move(self),
            "K": king_move(self),
            "Q": queen_move(self),
            "R": rook_move(self),
            "B": bishop_move(self),
            "N": knight_move(self),
        }.get(self.name)
        return self.moves

    def move(self, pos):
        """

        Moving piece with build-in validation
        also "Killing" validation is in the movement method
        after moving deselecting piece

        :param pos:
        :return:
        """
        global selected_piece
        global turn
        global current_color
        print(current_color)
        moved = False
        for move in self.moves:
            if (
                self.color == "w"
                and current_color == 0
                or self.color == "b"
                and current_color == 1
            ):
                if pos == move[0]:
                    moved = True
                    if current_color == 0:
                        current_color = 1
                    else:
                        current_color = 0
                    if move[1] is not None:
                        move[1].die()
                    self.pos = pos
                    selected_piece = None
                    self.last_turn = turn
                    turn += 1
                    for piece in pieces:
                        piece.what_can_i_do()

        # Pawn to Queen
        if self.name == "P":
            if self.color == "w":
                if self.pos % 10 == 8:
                    self.name = "Q"
                    self.create_img()
                    self.what_can_i_do()
            else:
                if self.pos % 10 == 1:
                    self.name = "Q"
                    self.create_img()
                    self.what_can_i_do()

        return moved

    def die(self):
        """

        Removing piece from board with build-in validation

        :return:
        """
        global pieces
        pieces.remove(self)

    def get_pos_coord(self):
        """

            Method for returning position coordinates of each piece

        :return:
        """
        return positions.get(self.pos)[0], positions.get(self.pos)[2]


def create_figure_instances(start_pos):
    for pos in start_pos:
        pieces.append(Piece(pos[0], pos[1], pos[2:4]))

    for piece in pieces:
        piece.what_can_i_do()


def draw_board():
    cnt = 0
    for i in range(1, 9):
        for z in range(1, 9):
            if cnt % 2 == 0:
                pygame.draw.rect(
                    window, pygame.Color(50, 50, 50), (size * z, size * i, size, size)
                )
            else:
                pygame.draw.rect(
                    window,
                    pygame.Color(255, 255, 255),
                    (size * z, size * i, size, size),
                )
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


# game init and window options
pygame.init()
window = pygame.display.set_mode((1800, 1000))
window.fill((211, 211, 211))
pygame.display.set_caption("CHESS")
create_figure_instances(start_positions)

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
quit()
