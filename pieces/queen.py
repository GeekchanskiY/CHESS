from .piece import Piece
from .color import Color, BLACK, WHITE
from .move import Move
from .exceptions import InvalidColorException, InvalidMoveException
from logging import debug
from .decorators import available_moves_time


class Queen(Piece):
    def __init__(self, pos: int, color: Color):
        if type(color) is not Color:
            raise InvalidColorException()

        self.pos = pos
        self.moves: list[Move] = []
        self.color = color
        self.name = "Q"
        self.last_computed_turn: int = -1
        self.available_moves: list[int] = []

        self.VALUE = 9

    def move(self, pos: int, other_pieces: list[Piece], turn: int):
        if pos not in self.get_available_moves(other_pieces, turn):
            raise InvalidMoveException()

        self.moves.append(Move(self.pos, pos, turn))

        self.pos = pos

    def get_moves(self) -> list[Move]:
        return self.moves

    @available_moves_time
    def get_available_moves(self, other_pieces: list[Piece], turn: int) -> list[int]:
        # TODO: finish
        if turn == self.last_computed_turn:
            debug("using pre-computed available moves")
            return self.available_moves

        self.available_moves = [self.pos + 10] if self.color == BLACK else [self.pos - 10]
        self.last_computed_turn = turn
        debug("computed available moves")

        return self.available_moves

    def get_pos(self) -> int:
        return self.pos

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color
