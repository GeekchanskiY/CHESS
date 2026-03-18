import pytest

from .utils import is_pos_in_bounds


# --- VALID POSITIONS ---


def test_valid_corner_positions():
    assert is_pos_in_bounds(11)
    assert is_pos_in_bounds(18)
    assert is_pos_in_bounds(81)
    assert is_pos_in_bounds(88)


def test_valid_middle_positions():
    assert is_pos_in_bounds(44)
    assert is_pos_in_bounds(55)
    assert is_pos_in_bounds(27)
    assert is_pos_in_bounds(72)


# --- OUT OF RANGE (GLOBAL BOUNDS) ---


def test_position_below_min():
    assert not is_pos_in_bounds(10)
    assert not is_pos_in_bounds(9)
    assert not is_pos_in_bounds(0)


def test_position_above_max():
    assert not is_pos_in_bounds(19)
    assert not is_pos_in_bounds(89)
    assert not is_pos_in_bounds(99)
    assert not is_pos_in_bounds(100)


# --- INVALID COLUMNS (FILE OUT OF 1–8 RANGE) ---


def test_invalid_column_zero():
    assert not is_pos_in_bounds(20)
    assert not is_pos_in_bounds(30)
    assert not is_pos_in_bounds(80)


def test_invalid_column_nine():
    assert not is_pos_in_bounds(19)
    assert not is_pos_in_bounds(29)
    assert not is_pos_in_bounds(89)


# --- EDGE CASES ---


def test_edges_are_valid():
    for col in range(1, 9):
        assert is_pos_in_bounds(10 + col)  # row 1
        assert is_pos_in_bounds(80 + col)  # row 8


def test_all_valid_board_positions():
    for row in range(1, 9):
        for col in range(1, 9):
            pos = row * 10 + col
            assert is_pos_in_bounds(pos)
