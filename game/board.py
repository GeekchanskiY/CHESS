import os
from typing import List
from pieces.piece import Piece


START_POSITIONS = [
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


class Board:
    field_names_x = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    field_names_x_rev = {value: key for key, value in field_names_x.items()}

    img_folder = os.path.abspath("images/berlin/")
    dot_img = os.path.abspath("images/dot.png")

    def __init__(self):
        self.pieces: List[Piece] = []
