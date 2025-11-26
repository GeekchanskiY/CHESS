from .errors import InvalidColor

class Color:
    WHITE = 'w'
    BLACK = 'b'

    def __init__(self, color: str):
        if color != self.BLACK and color != self.WHITE:
            raise InvalidColor()
        
        self.color = color

    def __call__(self, *args, **kwds):
        return self.color