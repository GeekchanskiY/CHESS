from .factory import piece_factory
from .color import Color
from .pawn import Pawn


def test_factory_pawn():
    piece = piece_factory(Color("b"), "P", 12)

    assert type(piece) is Pawn

    assert piece.name == "P"
    assert piece.pos == 12
    assert piece.color.color == Color("b").color


def test_factory_rook():
    piece = piece_factory(Color("w"), "R", 12)

    assert piece.name == "R"
    assert piece.pos == 12
    assert piece.color.color == Color("w").color


def test_factory_knight():
    piece = piece_factory(Color("b"), "N", 12)

    assert piece.name == "N"
    assert piece.pos == 12
    assert piece.color.color == Color("b").color


def test_factory_bishop():
    piece = piece_factory(Color("w"), "B", 12)

    assert piece.name == "B"
    assert piece.pos == 12
    assert piece.color.color == Color("w").color


def test_factory_queen():
    piece = piece_factory(Color("b"), "Q", 12)

    assert piece.name == "Q"
    assert piece.pos == 12
    assert piece.color.color == Color("b").color


def test_factory_king():
    piece = piece_factory(Color("w"), "K", 12)

    assert piece.name == "K"
    assert piece.pos == 12
    assert piece.color.color == Color("w").color


def test_factory_wrong_piece():
    try:
        piece_factory(Color("b"), "X", 12)
        assert False
    except ValueError:
        assert True


def test_factory_wrong_color():
    try:
        piece_factory("b", "P", 12)
        assert False
    except ValueError:
        assert True

    try:
        piece_factory(Color("b"), "P", 12)
        assert True
    except ValueError:
        assert False
