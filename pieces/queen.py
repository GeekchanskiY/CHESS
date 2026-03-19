from .piece import Piece
from .color import Color
from .move import Move
from .exceptions import InvalidColorException
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

    @available_moves_time
    def get_available_moves(self, other_pieces: list[Piece], turn: int) -> list[int]:
        moves = self._get_last_computed_turn(turn)
        if moves is not None:
            return moves

        if turn == self.last_computed_turn:
            debug("using pre-computed available moves")
            return self.available_moves

        moves = self._walk_positions(other_pieces, turn, (-11, -9, 11, 9, -1, 1, 10, -10))
        self._save_computed_turn(turn, moves)

        return moves
