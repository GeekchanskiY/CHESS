from abc import ABC, abstractmethod
from .color import Color
from .move import Move


class Piece(ABC):
    @abstractmethod
    def get_color(self) -> Color:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def move(self, pos: int, turn: int) -> Move:
        pass

    @abstractmethod
    def get_pos(self) -> int:
        pass

    @abstractmethod
    def get_moves(self) -> list[Move]:
        pass

    @abstractmethod
    def get_available_moves(self, other_pieces: list["Piece"], turn: int) -> list[int]:
        pass
