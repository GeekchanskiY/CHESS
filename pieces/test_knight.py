import pytest

from .exceptions import InvalidMoveException
from .knight import Knight
from .color import BLACK, WHITE
from .move import Move


# --- BASIC MOVEMENT ---


def test_knight_all_moves_center():
    knight = Knight(pos=55, color=WHITE)

    moves = knight.get_available_moves(other_pieces=[], turn=1)

    expected_positions = [34, 36, 43, 47, 63, 67, 74, 76]

    for pos in expected_positions:
        assert any(m.new_pos == pos for m in moves)


def test_knight_moves_near_edge():
    knight = Knight(pos=11, color=WHITE)

    moves = knight.get_available_moves(other_pieces=[], turn=1)

    # only valid moves from corner
    expected_positions = [23, 32]

    assert len(moves) == len(expected_positions)

    for pos in expected_positions:
        assert any(m.new_pos == pos for m in moves)


# --- NO WRAP AROUND (IMPORTANT BUG TEST) ---


def test_knight_does_not_wrap_board():
    knight = Knight(pos=18, color=WHITE)

    moves = knight.get_available_moves(other_pieces=[], turn=1)

    # these are invalid wrap-around positions
    invalid_positions = [29, 39]

    for pos in invalid_positions:
        assert not any(m.new_pos == pos for m in moves)


# --- CAPTURES ---


def test_knight_capture_enemy():
    knight = Knight(pos=55, color=WHITE)
    enemy = Knight(pos=34, color=BLACK)

    moves = knight.get_available_moves(other_pieces=[enemy], turn=1)

    assert any(m.new_pos == 34 and m.beats == 34 for m in moves)


def test_knight_cannot_capture_same_color():
    knight = Knight(pos=55, color=WHITE)
    ally = Knight(pos=34, color=WHITE)

    moves = knight.get_available_moves(other_pieces=[ally], turn=1)

    assert not any(m.new_pos == 34 for m in moves)


# --- MIXED BOARD ---


def test_knight_mixed_pieces():
    knight = Knight(pos=55, color=WHITE)

    enemy = Knight(pos=34, color=BLACK)
    ally = Knight(pos=36, color=WHITE)

    moves = knight.get_available_moves(other_pieces=[enemy, ally], turn=1)

    # can capture enemy
    assert any(m.new_pos == 34 and m.beats == 34 for m in moves)

    # cannot move to ally square
    assert not any(m.new_pos == 36 for m in moves)


# --- MOVE EXECUTION ---


def test_knight_move_updates_position():
    knight = Knight(pos=55, color=WHITE)
    move = Move(prev_pos=55, new_pos=34, turn=1, beats=None)

    knight.move(move, other_pieces=[], turn=1)

    assert knight.get_pos() == 34
    assert knight.get_moves()[-1] == move


def test_knight_invalid_move_raises():
    knight = Knight(pos=55, color=WHITE)
    invalid_move = Move(prev_pos=55, new_pos=54, turn=1, beats=None)

    with pytest.raises(InvalidMoveException):
        knight.move(invalid_move, other_pieces=[], turn=1)


# --- CACHE BEHAVIOR ---


def test_knight_cached_moves_same_turn():
    knight = Knight(pos=55, color=WHITE)

    moves1 = knight.get_available_moves([], turn=1)
    moves2 = knight.get_available_moves([], turn=1)

    assert moves1 is moves2


def test_knight_recompute_on_new_turn():
    knight = Knight(pos=55, color=WHITE)

    moves1 = knight.get_available_moves([], turn=1)
    moves2 = knight.get_available_moves([], turn=2)

    assert moves1 is not moves2
