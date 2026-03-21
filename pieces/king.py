from .piece import Piece
from .color import Color, BLACK, WHITE
from .move import Move
from .exceptions import InvalidColorException, InvalidMoveException
from logging import debug
from .decorators import available_moves_time
from .utils import is_pos_in_bounds
from copy import deepcopy


class King(Piece):
    def __init__(self, pos: int, color: Color):
        if type(color) is not Color:
            raise InvalidColorException()

        self.pos = pos
        self.moves: list[Move] = []
        self.color = color
        self.name = "K"
        self.last_computed_turn: int = -1
        self.available_moves: list[int] = []

        self.VALUE = 0

    @available_moves_time
    def get_available_moves(self, other_pieces: list[Piece], turn: int) -> list[int]:
        moves: list[Move] = self._get_last_computed_turn(turn)
        if moves is not None:
            debug("using pre-computed available moves")
            return self.available_moves

        moves: list[Move] = []

        # compute base moves
        offsets: list[int] = [10, 9, 11, 1, -1, -10, -9, -11]
        for offset in offsets:
            new_pos: int = self.pos + offset

            if not is_pos_in_bounds(new_pos):
                continue

            piece_found = False
            for piece in other_pieces:
                if piece.pos == new_pos:
                    piece_found = True

                    if piece.get_color() != self.get_color():
                        moves.append(Move(prev_pos=self.pos, new_pos=new_pos, turn=turn, beats=new_pos))

            if not piece_found:
                moves.append(Move(prev_pos=self.pos, new_pos=new_pos, turn=turn, beats=None))

        # TODO: fix
        if turn == -1:
            return moves
        
        # validate moves: king can't move to pos where it will be beaten
        self_copy: King = deepcopy(self)
        other_pieces_copy: list[Piece] = deepcopy(other_pieces)
        for elem in other_pieces_copy:
            if elem == self:
                other_pieces_copy.remove(elem)
                break
            
        other_pieces_copy.append(self_copy)
        for move in moves:
            self_copy.moves.append(move)
            is_invalid = False

            for piece in other_pieces_copy:
                if piece.get_color() != self.get_color():
                    next_available_moves: list[Move] = piece.get_available_moves(other_pieces_copy, -1)
                    for next_move in next_available_moves:
                        if next_move.beats == move.new_pos:
                            is_invalid = True
                            break

                if is_invalid:
                    break

            if is_invalid:
                moves.remove(move)

            self_copy.moves.remove(move)

        self._save_computed_turn(turn, moves)
        debug("computed moves")
        return moves
