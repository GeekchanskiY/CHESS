import pytest

from .exceptions import InvalidMoveException
from .queen import Queen
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


def test_queen_moves_straight_and_diagonal():
    queen = Queen(pos=55, color=WHITE)

    moves = queen.get_available_moves(other_pieces=[], turn=1)
    for move in moves:
        print(f"{move.new_pos},")

    expected_positions = [
        44,
        33,
        22,
        11,
        46,
        37,
        28,
        66,
        77,
        88,
        64,
        73,
        82,
        54,
        53,
        52,
        51,
        56,
        57,
        58,
        65,
        75,
        85,
        45,
        35,
        25,
        15,
    ]

    for pos in expected_positions:
        assert any(m.new_pos == pos for m in moves)


# --- BLOCKING ---


def test_queen_blocked_by_same_color():
    queen = Queen(pos=55, color=WHITE)
    blocker = DummyPiece(pos=54, color=WHITE)

    moves = queen.get_available_moves(other_pieces=[blocker], turn=1)

    assert not any(m.new_pos == 54 for m in moves)
    assert not any(m.new_pos == 53 for m in moves)  # cannot jump over


def test_queen_blocked_by_enemy_and_can_capture():
    queen = Queen(pos=55, color=WHITE)
    enemy = DummyPiece(pos=54, color=BLACK)

    moves = queen.get_available_moves(other_pieces=[enemy], turn=1)

    assert any(m.new_pos == 54 and m.beats == 54 for m in moves)
    assert not any(m.new_pos == 53 for m in moves)  # cannot go past


# --- CAPTURES ---


def test_queen_capture_diagonal():
    queen = Queen(pos=55, color=WHITE)
    enemy = DummyPiece(pos=44, color=BLACK)

    moves = queen.get_available_moves(other_pieces=[enemy], turn=1)

    assert any(m.new_pos == 44 and m.beats == 44 for m in moves)


def test_queen_cannot_capture_same_color():
    queen = Queen(pos=55, color=WHITE)
    ally = DummyPiece(pos=44, color=WHITE)

    moves = queen.get_available_moves(other_pieces=[ally], turn=1)

    assert not any(m.new_pos == 44 for m in moves)


# --- MOVE EXECUTION ---


def test_queen_move_updates_position():
    queen = Queen(pos=55, color=WHITE)
    move = Move(prev_pos=55, new_pos=45, turn=1, beats=None)

    queen.move(move, other_pieces=[], turn=1)

    assert queen.get_pos() == 45
    assert queen.get_moves()[-1] == move


def test_queen_invalid_move_raises():
    queen = Queen(pos=55, color=WHITE)
    invalid_move = Move(prev_pos=55, new_pos=23, turn=1, beats=None)  # not reachable

    with pytest.raises(InvalidMoveException):
        queen.move(invalid_move, other_pieces=[], turn=1)


# --- CACHE BEHAVIOR ---


def test_queen_cached_moves_same_turn():
    queen = Queen(pos=55, color=WHITE)

    moves1 = queen.get_available_moves([], turn=1)
    moves2 = queen.get_available_moves([], turn=1)

    assert moves1 is moves2


def test_queen_recompute_on_new_turn():
    queen = Queen(pos=55, color=WHITE)

    moves1 = queen.get_available_moves([], turn=1)
    moves2 = queen.get_available_moves([], turn=2)

    assert moves1 is not moves2
