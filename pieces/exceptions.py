class PieceException(Exception):
    """Piece base exception class"""


class InvalidMoveException(Exception):
    """Provided piece move is invalid"""

    def __init__(self, message="Invalid move."):
        self.message = message
        super().__init__(self.message)


class InvalidColorException(PieceException):
    """Exception raised when piece has invalid color"""

    def __init__(self, message="Invalid color."):
        self.message = message
        super().__init__(self.message)
