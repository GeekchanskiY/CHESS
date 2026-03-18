import pytest

from .exceptions import InvalidMoveException
from .pawn import Pawn
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


def test_pawn_single_forward_move_white():
    pawn = Pawn(pos=55, color=WHITE)

    moves = pawn.get_available_moves(other_pieces=[], turn=1)

    assert any(m.new_pos == 45 for m in moves)


def test_pawn_single_forward_move_black():
    pawn = Pawn(pos=55, color=BLACK)

    moves = pawn.get_available_moves(other_pieces=[], turn=1)

    assert any(m.new_pos == 65 for m in moves)


def test_pawn_blocked_forward():
    pawn = Pawn(pos=55, color=WHITE)
    blocker = DummyPiece(pos=45, color=BLACK)

    moves = pawn.get_available_moves(other_pieces=[blocker], turn=1)

    assert not any(m.new_pos == 45 for m in moves)


# --- DOUBLE MOVE ---


def test_pawn_double_move_initial():
    pawn = Pawn(pos=55, color=WHITE)

    moves = pawn.get_available_moves(other_pieces=[], turn=1)

    assert any(m.new_pos == 35 for m in moves)


def test_pawn_no_double_after_move():
    pawn = Pawn(pos=55, color=WHITE)
    pawn.moves.append(Move(55, 45, 1, None))

    moves = pawn.get_available_moves(other_pieces=[], turn=2)

    assert not any(m.new_pos == 35 for m in moves)


# --- CAPTURES ---


def test_pawn_capture_left_white():
    pawn = Pawn(pos=55, color=WHITE)
    enemy = DummyPiece(pos=44, color=BLACK)

    moves = pawn.get_available_moves(other_pieces=[enemy], turn=1)

    assert any(m.new_pos == 44 and m.beats == 44 for m in moves)


def test_pawn_capture_right_white():
    pawn = Pawn(pos=55, color=WHITE)
    enemy = DummyPiece(pos=46, color=BLACK)

    moves = pawn.get_available_moves(other_pieces=[enemy], turn=1)

    assert any(m.new_pos == 46 and m.beats == 46 for m in moves)


def test_pawn_cannot_capture_same_color():
    pawn = Pawn(pos=55, color=WHITE)
    ally = DummyPiece(pos=44, color=WHITE)

    moves = pawn.get_available_moves(other_pieces=[ally], turn=1)

    assert not any(m.new_pos == 44 for m in moves)


# --- EN PASSANT ---


def test_en_passant_left():
    pawn = Pawn(pos=55, color=WHITE)

    enemy_move = Move(prev_pos=65, new_pos=56, turn=1, beats=None)
    enemy = DummyPiece(pos=54, color=BLACK, moves=[enemy_move])

    moves = pawn.get_available_moves(other_pieces=[enemy], turn=2)

    assert any(m.beats == 54 for m in moves)


def test_en_passant_right():
    pawn = Pawn(pos=55, color=WHITE)

    enemy_move = Move(prev_pos=65, new_pos=56, turn=1, beats=None)
    enemy = DummyPiece(pos=56, color=BLACK, moves=[enemy_move])

    moves = pawn.get_available_moves(other_pieces=[enemy], turn=2)

    assert any(m.beats == 56 for m in moves)


def test_en_passant_invalid_if_not_last_turn():
    pawn = Pawn(pos=55, color=WHITE)

    enemy_move = Move(prev_pos=65, new_pos=56, turn=0, beats=None)
    enemy = DummyPiece(pos=56, color=BLACK, moves=[enemy_move])

    moves = pawn.get_available_moves(other_pieces=[enemy], turn=2)

    assert not any(m.beats == 56 for m in moves)


# --- MOVE EXECUTION ---


def test_move_updates_position():
    pawn = Pawn(pos=55, color=WHITE)
    move = Move(prev_pos=55, new_pos=45, turn=1, beats=None)

    pawn.move(move, other_pieces=[], turn=1)

    assert pawn.get_pos() == 45
    assert pawn.get_moves()[-1] == move


def test_invalid_move_raises():
    pawn = Pawn(pos=55, color=WHITE)
    invalid_move = Move(prev_pos=55, new_pos=99, turn=1, beats=None)

    with pytest.raises(InvalidMoveException):
        pawn.move(invalid_move, other_pieces=[], turn=1)


# --- CACHE BEHAVIOR ---


def test_cached_moves_same_turn():
    pawn = Pawn(pos=55, color=WHITE)

    moves1 = pawn.get_available_moves([], turn=1)
    moves2 = pawn.get_available_moves([], turn=1)

    assert moves1 is moves2  # same cached object


def test_recompute_on_new_turn():
    pawn = Pawn(pos=55, color=WHITE)

    moves1 = pawn.get_available_moves([], turn=1)
    moves2 = pawn.get_available_moves([], turn=2)

    assert moves1 is not moves2
