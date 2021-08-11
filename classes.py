class Piece:
    def __init__(self, pos_x, pos_y, color, figure_name, img_folder):
        self.color = color
        self.pos_x = int(pos_x)
        self.pos_y = int(pos_y)
        self.figure_name = figure_name
        self.img = img_folder+"/{}.png".format(color+figure_name)
        self.dead = False

    def move(self):
        pass
