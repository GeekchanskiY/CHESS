from abc import ABC, abstractmethod


class Piece(ABC):
    @abstractmethod
    def get_moves(self):
        pass

    @abstractmethod
    def move(self, pos):
        pass

    @abstractmethod
    def get_pos(self) -> tuple[int, int]:
        pass

    @abstractmethod
    def get_image_path(self) -> str:
        pass
