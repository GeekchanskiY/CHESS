"""
Game.board

Positions matrix:
   A   B   C   D   E   F   G   H
8 [11, 12, 13, 14, 15, 16, 17, 18] 8
7 [21, 22, 23, 24, 25, 26, 27, 28] 7
6 [31, 32, 33, 34, 35, 36, 37, 38] 6
5 [41, 42, 43, 44, 45, 46, 47, 48] 5
4 [51, 52, 53, 54, 55, 56, 57, 58] 4
3 [61, 62, 63, 64, 65, 66, 67, 68] 3
2 [71, 72, 73, 74, 75, 76, 77, 78] 2
1 [81, 82, 83, 84, 85, 86, 87, 88] 1
   A   B   C   D   E   F   G   H

Positions start from top-left corner due to pygame coordinate system.
"""

from typing import List
from pieces.factory import piece_factory
from pieces.piece import Piece
from pieces.color import Color

START_POSITIONS = [
    # White pawns
    "wP71",
    "wP72",
    "wP73",
    "wP74",
    "wP75",
    "wP76",
    "wP77",
    "wP78",
    # White figures
    "wR81",
    "wN82",
    "wB83",
    "wQ84",
    "wK85",
    "wB86",
    "wN87",
    "wR88",
    # Black pawns
    "bP21",
    "bP22",
    "bP23",
    "bP24",
    "bP25",
    "bP26",
    "bP27",
    "bP28",
    # Black figures
    "bR11",
    "bN12",
    "bB13",
    "bQ14",
    "bK15",
    "bB16",
    "bN17",
    "bR18",
]


class Board:
    """Board is a main object containing info about the game"""

    field_names_x = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    field_names_x_rev = {value: key for key, value in field_names_x.items()}

    def __init__(self):
        self.pieces: List[Piece] = []
        self.turn = 0

        for pos in START_POSITIONS:
            try:
                self.pieces.append(piece_factory(Color(pos[0]), pos[1], int(pos[2:4])))
            except ValueError:
                print(f"Warning: piece {pos} is not implemented yet")
