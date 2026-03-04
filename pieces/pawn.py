from .piece import Piece
from .color import Color, BLACK, WHITE
from .move import Move
from .exceptions import InvalidColorException, InvalidMoveException


class Pawn(Piece):
    def __init__(self, pos: int, color: Color):
        if type(color) is not Color:
            raise InvalidColorException()

        self.pos: int = pos
        self.moves: list[Move] = []
        self.color: Color = color
        self.name: str = "P"

        self.VALUE: int = 1

    def move(self, pos: int, other_pieces: list[Piece], turn: int):
        if pos not in self.get_available_moves(other_pieces, turn):
            raise InvalidMoveException()

        self.pos = pos
        # TODO: add move creation

    def get_moves(self) -> list[Move]:
        return []

    def get_available_moves(self, other_pieces: list[Piece], turn: int) -> list[int]:
        moves = [self.pos + 10] if self.color == BLACK else [self.pos - 10]

        return moves

    def get_pos(self) -> int:
        return self.pos

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color
