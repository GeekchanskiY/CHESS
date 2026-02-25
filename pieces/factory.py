from .color import Color
from .pawn import Pawn
from .piece import Piece


def piece_factory(color: Color, piece_name: str, pos: int) -> Piece:
    match piece_name:
        case "P":
            return Pawn(pos, color)
        case _:
            raise ValueError("cant build piece")
