from abc import ABC, abstractmethod
from .color import Color
from .move import Move
from .exceptions import InvalidMoveException, InvalidColorException
from .utils import is_pos_in_bounds


class Piece(ABC):
    def get_color(self) -> Color:
        return self.color

    def get_name(self) -> str:
        return self.name

    def move(self, move: Move, other_pieces: list["Piece"], turn: int) -> Move:
        if move not in self.get_available_moves(other_pieces, turn):
            raise InvalidMoveException("Provided move is illegal!")

        self.moves.append(move)

        self.pos = move.new_pos

    def get_pos(self) -> int:
        return self.pos

    def get_moves(self) -> list[Move]:
        return self.moves

    @abstractmethod
    def get_available_moves(self, other_pieces: list["Piece"], turn: int) -> list[int]:
        pass

    # Utilitary methods

    def _walk_positions(self, other_pieces: list["Piece"], turn: int, offsets: set[int]) -> list[Move]:
        """walks through all positions using each offset. used for Q, R, B moves."""
        available_moves: list[Move] = []
        for offset in offsets:
            pos: int = self.get_pos() + offset

            while is_pos_in_bounds(pos):
                break_found = False
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
