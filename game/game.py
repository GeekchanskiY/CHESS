import pygame

from .board import Board
from .assets import Assets

class Tile:
    def __init__(self, pos: int, width: int, offset_x: int, offset_y: int, color: pygame.Color):
        self.pos = pos
        
        self.pos_x = offset_x + width * (pos % 10)
        self.pos_y = offset_y + width * (pos // 10)

        self.width = width
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.color = color
    
    def get_rect(self) -> set[int, int, int, int]:
        return (self.pos_x, self.pos_y, self.width, self.width)
    
    def get_color(self):
        return self.color
    
    def pos_matches(self, pos: int) -> bool:
        return self.pos == pos

class Game:
    """
    Game is a view class which renders window using pygame, and
    matches user input with board actions
    """

    modes = {}

    def __init__(self):
        self._is_running = True
        self._cell_size = 80

        # Pygame config
        pygame.init()
        pygame.display.set_caption("CHESS")
        pygame.display.set_mode((self._cell_size * 10, self._cell_size * 10))

        self.surface = pygame.display.get_surface()
        self.surface.fill((211, 211, 211))


        # Board config
        self.board = Board()

        self.assets = Assets().load("pixel")

        # visualisation utils
        self.positions = {}
        self.tiles = []
        for z in range(1, 9):
            for i in range(1, 9):
                self.tiles.append(Tile(int(str(i) + str(9 - z)), self._cell_size, 0, 0, pygame.Color(255, 255, 255) if (i + z) % 2 == 0 else pygame.Color(50, 50, 50)))
                self.positions[int(str(z) + str(9 - i))] = [
                    self._cell_size * i,
                    self._cell_size * (i + 1),
                    self._cell_size * z,
                    self._cell_size * (z + 1),
                ]

    def _draw_board(self):
        """
        Draws board contents
        """

        for piece in self.board.pieces:
            self.surface.blit(pygame.image.load(self.assets.get_piece_image(piece)), (self._get_pos(piece.get_pos())))

    def _get_pos(self, pos: int) -> set[int, int]:
        return (self.positions.get(int(pos))[0], self.positions.get(int(pos))[2])

    def _draw(self):
        # draw board background
        for i in self.tiles:
                pygame.draw.rect(
                    self.surface,
                    i.get_color(),
                    i.get_rect(),
                )

        self._draw_board()

    def _mouse_pos(self): # TODO: optimize
        mouse_position = pygame.mouse.get_pos()
        for p in self.positions:
            cell = self.positions.get(p)
            if int(cell[0]) < mouse_position[1] < int(cell[1]):
                if int(cell[2]) < mouse_position[0] < int(cell[3]):
                    return p

    def run(self):
        while self._is_running:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._is_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # LMB
                        print(self._mouse_pos())
                    elif event.button == 3:  # RMB
                        pass

            self._draw()

            pygame.display.update()  # TODO: add freeze logic on no changes

        pygame.quit()
