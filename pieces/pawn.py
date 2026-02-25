from .piece import Piece
from .color import Color
from .exceptions import InvalidColorException, InvalidMoveException


class Pawn(Piece):
    def __init__(self, pos: int, color: Color):
        self.pos = pos

        if type(color) is not Color:
            raise InvalidColorException()

        self.color = color
        self.name = "Pawn"

    def move(self, pos: int, other_pieces: list[Piece]):
        if pos not in self.get_available_moves(other_pieces):
            raise InvalidMoveException()
        pass

    def get_available_moves(self, other_pieces: list[Piece]) -> list[int]:
        return super().get_available_moves()

    def get_pos(self) -> int:
        return self.pos

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color
