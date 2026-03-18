from .piece import Piece
from .color import Color, BLACK, WHITE
from .move import Move
from .exceptions import InvalidColorException
from logging import debug
from .decorators import available_moves_time


class Bishop(Piece):
    def __init__(self, pos: int, color: Color):
        if type(color) is not Color:
            raise InvalidColorException()

        self.pos = pos
        self.moves: list[Move] = []
        self.color = color
        self.name = "B"
        self.last_computed_turn: int = -1
        self.available_moves: list[int] = []

        self.VALUE = 3

    @available_moves_time
    def get_available_moves(self, other_pieces: list[Piece], turn: int) -> list[int]:
        if turn == self.last_computed_turn:
            debug("using pre-computed available moves")
            return self.available_moves

        self.available_moves = self._walk_positions(other_pieces, turn, (-11, -9, 11, 9))
        self.last_computed_turn = turn
        return self.available_moves
