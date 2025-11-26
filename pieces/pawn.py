from .piece import Piece, IMG_FOLDER
from .color import Color
from .errors import InvalidColor


class Pawn(Piece):
    def __init__(self, pos: int, color: Color):
        self.pos = pos

        if type(color) is not Color:
            raise InvalidColor
        
        self.color = color
        self.name = 'Pawn'

    def move(self, pos):
        pass

    def get_available_moves(self, other_pieces: list[Piece]):
        return super().get_available_moves()

    def get_pos(self) -> int:
        return self.pos

    def get_image_path(self) -> str:
        self.img = IMG_FOLDER + "/{}.png".format(self.color + self.name)