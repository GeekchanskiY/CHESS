from .piece import Piece
from .color import Color, BLACK, WHITE
from .move import Move
from .exceptions import InvalidColorException, InvalidMoveException
from logging import debug
from .decorators import available_moves_time


class Pawn(Piece):
    def __init__(self, pos: int, color: Color):
        if type(color) is not Color:
            raise InvalidColorException()

        self.pos: int = pos
        self.moves: list[Move] = []
        self.color: Color = color
        self.name: str = "P"
        self.last_computed_turn: int = -1
        self.available_moves: list[Move] = []

        self.VALUE: int = 1

    def move(self, move: Move, other_pieces: list[Piece], turn: int):
        is_legit = False
        for pos in self.get_available_moves(other_pieces, turn):
            if pos == move:
                is_legit = True
                break

        if not is_legit:
            raise InvalidMoveException("Provided move is illegal!")

        self.moves.append(move)

        self.pos = move.new_pos

    def get_moves(self) -> list[Move]:
        return self.moves

    @available_moves_time
    def get_available_moves(self, other_pieces: list[Piece], turn: int) -> list[Move]:
        """
        Gets pawn available moves

        TODO: optimize iteration through all pieces, make it 1 time
        """
        if turn == self.last_computed_turn:
            debug("using pre-computed available moves")
            return self.available_moves

        available_moves: list[Move] = []

        # Beat moves
        left_beat: int = self.pos + 11 if self.get_color() == BLACK else self.pos - 11
        right_beat: int = self.pos + 9 if self.get_color() == BLACK else self.pos - 9

        for piece in other_pieces:
            if piece.get_color() != self.get_color():
                if piece.get_pos() == left_beat:
                    available_moves.append(
                        Move(
                            prev_pos=self.get_pos(),
                            new_pos=left_beat,
                            turn=turn,
                            beats=left_beat,
                        )
                    )

                if piece.get_pos() == right_beat:
                    available_moves.append(
                        Move(
                            prev_pos=self.get_pos(),
                            new_pos=right_beat,
                            turn=turn,
                            beats=right_beat,
                        )
                    )

        # En passant rule
        needed_right_piece_pos = self.pos + 1
        needed_left_piece_pos = self.pos - 1
        for piece in other_pieces:
            if piece.get_color() == self.get_color():
                continue

            if piece.get_name() != self.get_name():
                continue

            if len(piece.get_moves()) != 1:
                continue

            if piece.get_moves()[0].turn != turn - 1:
                continue

            if piece.get_pos() == needed_left_piece_pos:
                available_moves.append(
                    Move(
                        prev_pos=self.get_pos(),
                        new_pos=self.pos + 11 if self.get_color() == BLACK else self.pos - 11,
                        turn=turn,
                        beats=needed_left_piece_pos,
                    )
                )

            if piece.get_pos() == needed_right_piece_pos:
                available_moves.append(
                    Move(
                        prev_pos=self.get_pos(),
                        new_pos=self.pos + 9 if self.get_color() == BLACK else self.pos - 9,
                        turn=turn,
                        beats=needed_right_piece_pos,
                    )
                )

        # move forward for 1 cell
        expected_move: int = self.pos + 10 if self.get_color() == BLACK else self.pos - 10

        blocked = False
        for piece in other_pieces:
            if piece.get_pos() == expected_move:
                blocked = True
                break

        if not blocked:
            available_moves.append(Move(prev_pos=self.get_pos(), new_pos=expected_move, turn=turn, beats=None))

        # move forvard for 2 cells
        if not blocked and len(self.moves) == 0:
            expected_move: int = self.pos + 20 if self.get_color() == BLACK else self.pos - 20
            for piece in other_pieces:
                if piece.get_pos() == expected_move:
                    blocked = True

            if not blocked:
                available_moves.append(Move(prev_pos=self.get_pos(), new_pos=expected_move, turn=turn, beats=None))

        self.last_computed_turn = turn
        self.available_moves = available_moves

        debug("computed available moves")

        return self.available_moves

    def get_pos(self) -> int:
        return self.pos

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color
