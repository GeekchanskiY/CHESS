from pygame import Rect, Color

class Tile:
    """
    Tile is a class which represents one cell on the board, and contains info about its position on screen and color
    """

    def __init__(self, pos: int, width: int, offset_x: int, offset_y: int, color: Color):
        self.pos = pos

        self.pos_x = offset_x + width * (pos % 10 - 1)
        self.pos_y = offset_y + width * (pos // 10 - 1)

        self.width = width
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.color = color

    def get_rect(self) -> Rect:
        """Returns coordinates of tile in pixels"""
        return Rect(self.pos_x, self.pos_y, self.width, self.width)

    def get_color(self):
        """Returns color of tile"""
        return self.color

    def pos_matches(self, pos: int) -> bool:
        """Returns true if tile position matches given position"""
        return self.pos == pos

    def get_piece_coords(self) -> Rect:
        """Gets coordinates of piece on tile in pixels"""
        return Rect(self.pos_x, self.pos_y, self.width, self.width)