import pytest

from .exceptions import InvalidMoveException
from .rook import Rook
from .color import BLACK, WHITE
from .move import Move


class DummyPiece:
    def __init__(self, pos, color, name="P", moves=None):
        self._pos = pos
        self._color = color
        self._name = name
        self._moves = moves or []

    def get_pos(self):
        return self._pos

    def get_color(self):
        return self._color

    def get_name(self):
        return self._name

    def get_moves(self):
        return self._moves


# --- BASIC MOVEMENT ---


def test_rook_moves_straight():
    rook = Rook(pos=55, color=WHITE)

    moves = rook.get_available_moves(other_pieces=[], turn=1)

    expected_positions = [
        54,
        53,
        52,
        51,  
        56,
        57,
        58,  
        45,
        35,
        25,
        15,  
        65,
        75,
        85,  
    ]

    for pos in expected_positions:
        assert any(m.new_pos == pos for m in moves)


def test_rook_cannot_move_diagonal():
    rook = Rook(pos=55, color=WHITE)

    moves = rook.get_available_moves(other_pieces=[], turn=1)

    invalid_positions = [44, 46, 64, 66]

    for pos in invalid_positions:
        assert not any(m.new_pos == pos for m in moves)


# --- BLOCKING ---


def test_rook_blocked_by_same_color():
    rook = Rook(pos=55, color=WHITE)
    blocker = DummyPiece(pos=54, color=WHITE)

    moves = rook.get_available_moves(other_pieces=[blocker], turn=1)

    assert not any(m.new_pos == 54 for m in moves)
    assert not any(m.new_pos == 53 for m in moves)  # cannot jump over


def test_rook_blocked_by_enemy_and_can_capture():
    rook = Rook(pos=55, color=WHITE)
    enemy = DummyPiece(pos=54, color=BLACK)

    moves = rook.get_available_moves(other_pieces=[enemy], turn=1)

    assert any(m.new_pos == 54 and m.beats == 54 for m in moves)
    assert not any(m.new_pos == 53 for m in moves)  # cannot go past


# --- CAPTURES ---


def test_rook_capture_vertical():
    rook = Rook(pos=55, color=WHITE)
    enemy = DummyPiece(pos=45, color=BLACK)

    moves = rook.get_available_moves(other_pieces=[enemy], turn=1)

    assert any(m.new_pos == 45 and m.beats == 45 for m in moves)


def test_rook_cannot_capture_same_color():
    rook = Rook(pos=55, color=WHITE)
    ally = DummyPiece(pos=45, color=WHITE)

    moves = rook.get_available_moves(other_pieces=[ally], turn=1)

    assert not any(m.new_pos == 45 for m in moves)


# --- MOVE EXECUTION ---


def test_rook_move_updates_position():
    rook = Rook(pos=55, color=WHITE)
    move = Move(prev_pos=55, new_pos=54, turn=1, beats=None)

    rook.move(move, other_pieces=[], turn=1)

    assert rook.get_pos() == 54
    assert rook.get_moves()[-1] == move


def test_rook_invalid_move_raises():
    rook = Rook(pos=55, color=WHITE)
    invalid_move = Move(prev_pos=55, new_pos=44, turn=1, beats=None)  # diagonal

    with pytest.raises(InvalidMoveException):
        rook.move(invalid_move, other_pieces=[], turn=1)


# --- CACHE BEHAVIOR ---


def test_rook_cached_moves_same_turn():
    rook = Rook(pos=55, color=WHITE)

    moves1 = rook.get_available_moves([], turn=1)
    moves2 = rook.get_available_moves([], turn=1)

    assert moves1 is moves2


def test_rook_recompute_on_new_turn():
    rook = Rook(pos=55, color=WHITE)

    moves1 = rook.get_available_moves([], turn=1)
    moves2 = rook.get_available_moves([], turn=2)

    assert moves1 is not moves2
