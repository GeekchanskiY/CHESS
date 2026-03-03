from itertools import product
import pygame

from .board import Board
from .assets import Assets


class Tile:
    def __init__(self, pos: int, width: int, offset_x: int, offset_y: int, color: pygame.Color):
        self.pos = pos

        self.pos_x = offset_x + width * (pos % 10 - 1)
        self.pos_y = offset_y + width * (pos // 10 - 1)

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

    def get_piece_coords(self) -> set[int]:
        return (
            self.pos_x,
            self.pos_y,
            self.pos_x + self.width,
            self.pos_y + self.width,
        )


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
        pygame.display.set_mode((self._cell_size * 8, self._cell_size * 8))

        self.surface = pygame.display.get_surface()
        self.surface.fill((211, 211, 211))
        self._offset_x = 0
        self._offset_y = 0

        # Board config
        self.board: Board = Board()
        self.assets = Assets().load("pixel")

        # Tiles
        self.tiles: list[Tile] = []
        self.tiles_dict = {}
        for i, z in product(range(1, 9), range(1, 9)):
            new_tile = Tile(
                i * 10 + z,
                self._cell_size,
                self._offset_x,
                self._offset_y,
                pygame.Color(50, 50, 50) if (i + z) % 2 == 0 else pygame.Color(205, 205, 205),
            )
            self.tiles.append(new_tile)
            self.tiles_dict[int(str(i) + str(9 - z))] = new_tile

    def _draw_pieces(self):
        """
        Draws board pieces
        """

        for piece in self.board.pieces:
            self.surface.blit(pygame.image.load(self.assets.get_piece_image(piece)), (self._get_pos(piece.get_pos())))

    def _get_pos(self, pos: int) -> set[int]:
        return self.tiles_dict[pos].get_piece_coords()

    def _draw(self):
        """
        Draws tiles and pieces
        """
        for i in self.tiles:
            pygame.draw.rect(
                self.surface,
                i.get_color(),
                i.get_rect(),
            )

        self._draw_pieces()

    def _mouse_pos(self) -> int:
        """
        Returns tile number from current mouse coordinates
        """

        mouse_position = pygame.mouse.get_pos()
        mouse_x = mouse_position[0]
        mouse_y = mouse_position[1]
        coord_x = (mouse_x - self._offset_x) // self._cell_size + 1

        if coord_x > 8:
            return None

        coord_y = (mouse_y - self._offset_y) // self._cell_size + 1
        if coord_y > 8:
            return None

        return coord_x + coord_y * 10

    def run(self):
        while self._is_running:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._is_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # LMB
                        print("LMB", self._mouse_pos())
                    elif event.button == 3:  # RMB
                        print("RMB", self._mouse_pos())

            self._draw()

            pygame.display.update()  # TODO: add freeze logic on no changes

        pygame.quit()
