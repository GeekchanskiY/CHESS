from .piece import Piece
from .color import Color, BLACK, WHITE
from .move import Move
from .exceptions import InvalidColorException, InvalidMoveException


class Queen(Piece):
    def __init__(self, pos: int, color: Color):
        if type(color) is not Color:
            raise InvalidColorException()

        self.pos = pos
        self.moves: list[Move] = []
        self.color = color
        self.name = "Q"

        self.VALUE = 9

    def move(self, pos: int, other_pieces: list[Piece]):
        if pos not in self.get_available_moves(other_pieces):
            raise InvalidMoveException()
        pass

    def get_moves(self) -> list[Move]:
        return []

    def get_available_moves(self, other_pieces: list[Piece]) -> list[int]:
        return []

    def get_pos(self) -> int:
        return self.pos

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color
