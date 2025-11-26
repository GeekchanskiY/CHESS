class PieceException(Exception):
    """Piece base exception class"""


class InvalidColor(PieceException):
    """Exception raised when piece has invalid color"""

    def __init__(self, message="Invalid color."):
        self.message = message
        super().__init__(self.message)