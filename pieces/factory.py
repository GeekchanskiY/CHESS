from .color import Color
from .pawn import Pawn
from .rook import Rook
from .knight import Knight
from .bishop import Bishop
from .queen import Queen
from .king import King
from .piece import Piece


def piece_factory(color: Color, piece_name: str, pos: int) -> Piece:
    if type(color) is not Color:
        raise ValueError("color must be of type Color")
    
    match piece_name:
        case "P":
            return Pawn(pos, color)
        case "R":
            return Rook(pos, color)
        case "N":
            return Knight(pos, color)
        case "B":
            return Bishop(pos, color)
        case "Q":
            return Queen(pos, color)
        case "K":
            return King(pos, color)
        case _:
            raise ValueError("cant build piece")
