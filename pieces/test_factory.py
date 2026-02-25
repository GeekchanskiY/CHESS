from .factory import piece_factory
from .color import Color
from .pawn import Pawn


def test_factory_pawn():
    piece = piece_factory(Color("b"), "P", 12)

    assert type(piece) is Pawn

    assert piece.name == "Pawn"
    assert piece.pos == 12
    assert piece.color.color == Color("b").color
