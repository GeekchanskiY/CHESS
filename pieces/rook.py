from .piece import Piece
from .color import Color
from .move import Move
from .exceptions import InvalidColorException
from logging import debug
from .decorators import available_moves_time


class Rook(Piece):
    def __init__(self, pos: int, color: Color):
        if type(color) is not Color:
            raise InvalidColorException()

        self.pos = pos
        self.moves: list[Move] = []
        self.color = color
        self.name = "R"
        self.last_computed_turn: int = -1
        self.available_moves: list[Move] = []

        self.VALUE = 5

    @available_moves_time
    def get_available_moves(self, other_pieces: list[Piece], turn: int) -> list[Move]:
        moves = self._get_last_computed_turn(turn)
        if moves is not None:
            debug("using pre-computed available moves")

            return moves

        moves = self._walk_positions(other_pieces, turn, (-1, 1, 10, -10))
        self._save_computed_turn(turn, moves)

        return moves
    
    def _force_get_available_moves(self, other_pieces: list[Piece], turn: int) -> list[Move]:
        return self.get_available_moves(other_pieces, turn)
