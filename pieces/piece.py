from abc import ABC, abstractmethod
from .color import Color
from .move import Move
from .exceptions import InvalidMoveException, InvalidColorException


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
