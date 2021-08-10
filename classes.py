class Cell:
    def __init__(self, pos_x, pos_y, bg_color):
        self.posX = pos_x
        self.posY = pos_y
        self.bg_color = bg_color


class Figure(Cell):
    possible_moves = []

    def __init__(self, pos_x, pos_y, bg_color, color):
        super().__init__(pos_x, pos_y, bg_color)
        self.color = color

    def move(self):
        pass


class Pawn(Figure):
    possible_moves = ["y+1", "y+2", "y+1.x+1"]

    def __init__(self, pos_x, pos_y, bg_color, color):
        super().__init__(pos_x, pos_y, bg_color, color)


class Bishop(Figure):
    possible_moves = []

    def __init__(self, pos_x, pos_y, bg_color, color):
        super().__init__(pos_x, pos_y, bg_color, color)


class Knight(Figure):
    possible_moves = ["y2x1", 'x2y1']

    def __init__(self, pos_x, pos_y, bg_color, color):
        super().__init__(pos_x, pos_y, bg_color, color)


class Rook(Figure):
    def __init__(self, pos_x, pos_y, bg_color, color):
        super().__init__(pos_x, pos_y, bg_color, color)


class Queen(Figure):
    def __init__(self, pos_x, pos_y, bg_color, color):
        super().__init__(pos_x, pos_y, bg_color, color)


class King(Figure):
    def __init__(self, pos_x, pos_y, bg_color, color):
        super().__init__(pos_x, pos_y, bg_color, color)


class Board:
    def __init__(self):
        self.width = 800
        self.height = 800
        self.vertical_positions = ["1", "2", "3", "4", "5", "6", "7", "8"]
        self.horizontal_positions = ["A", "B", "C", "D", "E", "F", "G", "H"]
