from .piece import Piece
from .color import Color, BLACK, WHITE
from .move import Move
from .exceptions import InvalidColorException, InvalidMoveException


class Pawn(Piece):
    def __init__(self, pos: int, color: Color):
        if type(color) is not Color:
            raise InvalidColorException()

        self.pos = pos
        self.moves: list[Move] = []
        self.color = color
        self.name = "P"

    def move(self, pos: int, other_pieces: list[Piece]):
        if pos not in self.get_available_moves(other_pieces):
            raise InvalidMoveException()
        pass

    def get_moves(self) -> list[Move]:
        return []

    def get_available_moves(self, other_pieces: list[Piece]) -> list[int]:
        moves = []
        f1 = True
        f2 = True
        for piece in other_pieces:
            if self.color == WHITE:
                if piece.pos == self.pos + 11 and piece.color != self.color:
                    moves.append([piece.pos, piece])
                if piece.pos == self.pos - 9 and piece.color != self.color:
                    moves.append([piece.pos, piece])
                if self.last_turn is None:
                    if piece.pos == self.pos + 1:
                        f1 = False
                        f2 = False
                    if piece.pos == self.pos + 2:
                        f2 = False
                else:
                    if piece.pos == self.pos + 1:
                        f1 = False
                    f2 = False
            else:
                if piece.pos == self.pos + 9 and piece.color != self.color:
                    moves.append([piece.pos, piece])
                if piece.pos == self.pos - 11 and piece.color != self.color:
                    moves.append([piece.pos, piece])
                if self.last_turn is None:
                    if piece.pos == self.pos - 1:
                        f1 = False
                        f2 = False
                    if piece.pos == self.pos - 2:
                        f2 = False
                else:
                    f2 = False
                    if piece.pos == self.pos - 1:
                        f1 = False

            # En passant rule
            if piece.pos == self.pos + 10:
                if piece.name == "P" and piece.last_turn == turn - 1 and piece.color != instance.color:
                    if self.color == "w":
                        moves.append([self.pos + 11, piece])
                    else:
                        moves.append([self.pos + 9, piece])
            if piece.pos == self.pos - 10:
                if piece.name == "P" and piece.last_turn == turn - 1 and piece.color != self.color:
                    if self.color == "w":
                        moves.append([self.pos - 9, piece])
                    else:
                        moves.append([self.pos - 11, piece])

        if f1:
            if self.color == WHITE:
                moves.append([self.pos + 1, None])
            else:
                moves.append([self.pos - 1, None])
        if f2:
            if self.color == WHITE:
                moves.append([self.pos + 2, None])
            else:
                moves.append([self.pos - 2, None])

        return moves

    def get_pos(self) -> int:
        return self.pos

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color
