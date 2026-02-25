"""
Game.board

Positions matrix:
[81, 82, 83, 84, 85, 86, 87, 88]
[71, 72, 73, 74, 75, 76, 77, 78]
[61, 62, 63, 64, 65, 66, 67, 68]
[51, 52, 53, 54, 55, 56, 57, 58]
[41, 42, 43, 44, 45, 46, 47, 48]
[31, 32, 33, 34, 35, 36, 37, 38]
[21, 22, 23, 24, 25, 26, 27, 28]
[11, 12, 13, 14, 15, 16, 17, 18]
"""

from typing import List
from pieces.piece import Piece
from pieces.color import Color

START_POSITIONS = [
    # White pawns
    "wP12",
    "wP22",
    "wP32",
    "wP42",
    "wP52",
    "wP62",
    "wP72",
    "wP82",
    # White figures
    "wR11",
    "wN21",
    "wB31",
    "wQ41",
    "wK51",
    "wB61",
    "wN71",
    "wR81",
    # Black pawns
    "bP17",
    "bP27",
    "bP37",
    "bP47",
    "bP57",
    "bP67",
    "bP77",
    "bP87",
    # Black figures
    "bR18",
    "bN28",
    "bB38",
    "bQ48",
    "bK58",
    "bB68",
    "bN78",
    "bR88",
]


class Board:
    field_names_x = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    field_names_x_rev = {value: key for key, value in field_names_x.items()}

    def __init__(self):
        self.pieces: List[Piece] = []

        for pos in START_POSITIONS:
            self.pieces.append(Piece(Color(pos[0]), pos[1], pos[2:4]))
