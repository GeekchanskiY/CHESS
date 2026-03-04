class BoardException(Exception):
    """Board base exception class"""


class InvalidPieceException(BoardException):
    """Provided piece is invalid"""

    def __init__(self, message="Invalid piece."):
        self.message = message
        super().__init__(self.message)


class InvalidMoveException(BoardException):
    """Provided move is invalid"""

    def __init__(self, message="Invalid move."):
        self.message = message
        super().__init__(self.message)
