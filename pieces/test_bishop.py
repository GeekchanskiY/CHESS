import pytest

from .exceptions import InvalidMoveException
from .bishop import Bishop
from .color import BLACK, WHITE
from .move import Move


# --- BASIC MOVEMENT ---


def test_bishop_moves_diagonally():
    bishop = Bishop(pos=55, color=WHITE)

    moves = bishop.get_available_moves(other_pieces=[], turn=1)
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
    ]

    for pos in expected_positions:
        assert any(m.new_pos == pos for m in moves)


def test_bishop_cannot_move_straight():
    bishop = Bishop(pos=55, color=WHITE)

    moves = bishop.get_available_moves(other_pieces=[], turn=1)

    invalid_positions = [54, 56, 45, 65]  # straight moves

    for pos in invalid_positions:
        assert not any(m.new_pos == pos for m in moves)


# --- BLOCKING ---


def test_bishop_blocked_by_same_color():
    bishop = Bishop(pos=55, color=WHITE)
    blocker = Bishop(pos=44, color=WHITE)

    moves = bishop.get_available_moves(other_pieces=[blocker], turn=1)

    assert not any(m.new_pos == 44 for m in moves)
    assert not any(m.new_pos == 33 for m in moves)  # cannot jump over


def test_bishop_blocked_by_enemy_and_can_capture():
    bishop = Bishop(pos=55, color=WHITE)
    enemy = Bishop(pos=44, color=BLACK)

    moves = bishop.get_available_moves(other_pieces=[enemy], turn=1)

    assert any(m.new_pos == 44 and m.beats == 44 for m in moves)
    assert not any(m.new_pos == 33 for m in moves)  # cannot go past


# --- CAPTURES ---


def test_bishop_capture_other_diagonal():
    bishop = Bishop(pos=55, color=WHITE)
    enemy = Bishop(pos=66, color=BLACK)

    moves = bishop.get_available_moves(other_pieces=[enemy], turn=1)

    assert any(m.new_pos == 66 and m.beats == 66 for m in moves)


def test_bishop_cannot_capture_same_color():
    bishop = Bishop(pos=55, color=WHITE)
    ally = Bishop(pos=44, color=WHITE)

    moves = bishop.get_available_moves(other_pieces=[ally], turn=1)

    assert not any(m.new_pos == 44 for m in moves)


# --- MOVE EXECUTION ---


def test_bishop_move_updates_position():
    bishop = Bishop(pos=55, color=WHITE)
    move = Move(prev_pos=55, new_pos=44, turn=1, beats=None)

    bishop.move(move, other_pieces=[], turn=1)

    assert bishop.get_pos() == 44
    assert bishop.get_moves()[-1] == move


def test_bishop_invalid_move_raises():
    bishop = Bishop(pos=55, color=WHITE)
    invalid_move = Move(prev_pos=55, new_pos=54, turn=1, beats=None)  # not diagonal

    with pytest.raises(InvalidMoveException):
        bishop.move(invalid_move, other_pieces=[], turn=1)


# --- CACHE BEHAVIOR ---


def test_bishop_cached_moves_same_turn():
    bishop = Bishop(pos=55, color=WHITE)

    moves1 = bishop.get_available_moves([], turn=1)
    moves2 = bishop.get_available_moves([], turn=1)

    assert moves1 is moves2


def test_bishop_recompute_on_new_turn():
    bishop = Bishop(pos=55, color=WHITE)

    moves1 = bishop.get_available_moves([], turn=1)
    moves2 = bishop.get_available_moves([], turn=2)

    assert moves1 is not moves2
