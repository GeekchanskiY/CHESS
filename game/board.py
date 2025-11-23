import os
from typing import List
from pieces.piece import Piece


class Board:
    field_names_x = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    field_names_x_rev = {value: key for key, value in field_names_x.items()}

    img_folder = os.path.abspath("images/berlin/")
    dot_img = os.path.abspath("images/dot.png")

    def __init__(self):
        self.pieces: List[Piece] = []
