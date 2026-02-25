"""
Game.board

Positions matrix:
   A   B   C   D   E   F   G   H
8 [81, 82, 83, 84, 85, 86, 87, 88] 8
7 [71, 72, 73, 74, 75, 76, 77, 78] 7
6 [61, 62, 63, 64, 65, 66, 67, 68] 6
5 [51, 52, 53, 54, 55, 56, 57, 58] 5
4 [41, 42, 43, 44, 45, 46, 47, 48] 4
3 [31, 32, 33, 34, 35, 36, 37, 38] 3
2 [21, 22, 23, 24, 25, 26, 27, 28] 2
1 [11, 12, 13, 14, 15, 16, 17, 18] 1
   A   B   C   D   E   F   G   H

"""

from typing import List
from pieces.piece import Piece
from pieces.color import Color

START_POSITIONS = [
    # White pawns
    "wP21",
    "wP22",
    "wP23",
    "wP24",
    "wP25",
    "wP26",
    "wP27",
    "wP28",
    # White figures
    "wR11",
    "wN12",
    "wB13",
    "wQ14",
    "wK15",
    "wB16",
    "wN17",
    "wR18",
    # Black pawns
    "bP71",
    "bP72",
    "bP73",
    "bP74",
    "bP75",
    "bP76",
    "bP77",
    "bP78",
    # Black figures
    "bR81",
    "bN82",
    "bB83",
    "bQ84",
    "bK85",
    "bB86",
    "bN87",
    "bR88",
]


class Board:
    """Board is a main object containing info about the game"""
    field_names_x = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    field_names_x_rev = {value: key for key, value in field_names_x.items()}

    def __init__(self):
        self.pieces: List[Piece] = []
        self.turn = 0

        for pos in START_POSITIONS:
            self.pieces.append(Piece(Color(pos[0]), pos[1], pos[2:4]))