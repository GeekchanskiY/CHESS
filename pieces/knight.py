from .piece import Piece
from .color import Color, BLACK, WHITE
from .move import Move
from .exceptions import InvalidColorException, InvalidMoveException
from logging import debug
from .decorators import available_moves_time
from .utils import is_pos_in_bounds


class Knight(Piece):
    def __init__(self, pos: int, color: Color):
        if type(color) is not Color:
            raise InvalidColorException()

        self.pos = pos
        self.moves: list[Move] = []
        self.color = color
        self.name = "N"
        self.last_computed_turn: int = -1
        self.available_moves: list[int] = []

        self.VALUE = 3

    @available_moves_time
    def get_available_moves(self, other_pieces: list[Piece], turn: int) -> list[Move]:
        moves = self._get_last_computed_turn(turn)
        if moves is not None:
            debug("using pre-computed available moves")
            return moves

        available_moves: list[Move] = []

        offsets = [-21, -19, -12, -8, 8, 12, 19, 21]

        for offset in offsets:
            new_pos = self.pos + offset

            if not is_pos_in_bounds(new_pos):
                continue

            found = False
            for piece in other_pieces:
                if piece.get_pos() == new_pos:
                    if piece.get_color() == self.color:
                        found = True

                        break
                    else:
                        available_moves.append(
                            Move(
                                prev_pos=self.pos,
                                new_pos=new_pos,
                                turn=turn,
                                beats=new_pos,
                            )
                        )

                        found = True
                        break

            if not found:
                available_moves.append(
                    Move(
                        prev_pos=self.pos,
                        new_pos=new_pos,
                        turn=turn,
                        beats=None,
                    )
                )

        self._save_computed_turn(turn, moves)
        debug("computed available moves")
        return available_moves
