from .piece import Piece


class Pawn(Piece):
    def __init__(self, pos):
        self.pos = pos