from abc import ABC, abstractmethod
from .color import Color
from .move import Move
from .exceptions import InvalidMoveException, InvalidColorException
from .utils import is_pos_in_bounds
from logging import debug
from copy import deepcopy


class Piece(ABC):
    def get_color(self) -> Color:
        """Gets piece color."""
        return self.color

    def get_name(self) -> str:
        """Gets piece name."""
        return self.name

    def move(self, move: Move, other_pieces: list["Piece"], turn: int) -> Move:
        self.moves.append(move)

        self.pos = move.new_pos

    def get_pos(self) -> int:
        """Gets current position of piece."""
        return self.pos

    def get_moves(self) -> list[Move]:
        """Gets all moves made by piece."""
        return self.moves

    @abstractmethod
    def get_available_moves(self, other_pieces: list["Piece"], turn: int) -> list[Move]:
        """Gets available moves for piece. Uses caching to optimize performance."""
        pass

    @abstractmethod
    def _force_get_available_moves(self, other_pieces: list["Piece"], turn: int) -> list[Move]:
        """Forces to compute available moves, ignoring cache and other p. Used for check detection."""
        pass

    # Utilitary methods

    def _walk_positions(self, other_pieces: list["Piece"], turn: int, offsets: set[int]) -> list[Move]:
        """walks through all positions using each offset. used for Q, R, B moves."""
        available_moves: list[Move] = []
        for offset in offsets:
            pos: int = self.get_pos() + offset

            while is_pos_in_bounds(pos):
                break_found: bool = False
                for piece in other_pieces:
                    if piece.get_pos() == pos:
                        if piece.get_color() != self.get_color():
                            available_moves.append(
                                Move(
                                    prev_pos=self.get_pos(),
                                    new_pos=pos,
                                    turn=turn,
                                    beats=pos,
                                )
                            )

                        break_found = True

                        break

                if break_found:
                    break

                available_moves.append(
                    Move(
                        prev_pos=self.get_pos(),
                        new_pos=pos,
                        turn=turn,
                        beats=None,
                    )
                )

                pos += offset

        return available_moves

    def _get_last_computed_turn(self, turn: int) -> list[Move] | None:
        """Gets last computed turn if exists. If turn = -1 forces to re-compute moves."""
        if turn == -1:
            return None

        if turn == self.last_computed_turn:
            debug("using pre-computed available moves")
            return self.available_moves

    def _save_computed_turn(self, turn: int, moves: list[Move]):
        """Saves computed turn to cache. Ignores if turn equals -1."""
        if turn == -1:
            return

        debug("saving computed moves")
        self.last_computed_turn = turn
        self.available_moves = moves

    def __eq__(self, value):
        if type(value) != type(self):
            return False

        return (
            self.get_color() == value.get_color()
            and self.get_name() == value.get_name()
            and self.get_pos() == value.get_pos()
        )
    
    def _avoid_check(self, other_pieces: list["Piece"], turn: int, moves: list[Move]) -> list[Move]:
        """
            Removes moves that would put the king in check.

            Piece checks if move is valid by simulating it on a copy of the board and checking if the king is in check after the move.
        """
        if turn == -1: # avoid infinite recursion
            return moves
        
        valid_moves: list[Move] = []

        current_king_pos: int = None
        for piece in other_pieces:
            if piece.get_color() == self.get_color() and piece.get_name() == "K":
                current_king_pos = piece.get_pos()
                break

        for move in moves:
            other_pieces_copy: list[Piece] = deepcopy(other_pieces)
            self_copy: Piece = deepcopy(self)

            self_copy.move(move, other_pieces_copy, turn)
            king_in_check = False
            for piece in other_pieces_copy:
                if piece.get_color() != self.get_color(): # no need to check pieces of the same color
                    if current_king_pos in [move.new_pos for move in piece._force_get_available_moves(other_pieces_copy, -1)]:
                        king_in_check = True
                        break
       
            if not king_in_check:
                valid_moves.append(move)
        
        return valid_moves
       