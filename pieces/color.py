from .exceptions import InvalidColorException


class Color:
    WHITE = "w"
    BLACK = "b"

    def __init__(self, color: str):
        if color != self.BLACK and color != self.WHITE:
            raise InvalidColorException()

        self.color = color

    def __call__(self, *args, **kwds):
        return self.color

    def __eq__(self, value):
        if type(value) != type(self):
            return False

        return self.color == value.color


BLACK = Color("b")
WHITE = Color("w")
