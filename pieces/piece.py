from __future__ import annotations
from abc import ABC, abstractmethod

IMG_FOLDER = 'images/berlin/'

class Piece(ABC):
    @abstractmethod
    def get_moves(self):
        pass

    @abstractmethod
    def move(self, pos):
        pass

    @abstractmethod
    def get_pos(self) -> int:
        pass

    @abstractmethod
    def get_available_moves(self, other_pieces: list[Piece]) -> list[int]:
        pass

    @abstractmethod
    def get_image_path(self) -> str:
        pass
