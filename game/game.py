from itertools import product
import pygame
from typing import Dict

from .board import Board
from .assets import Assets


class Tile:
    """
    Tile is a class which represents one cell on the board, and contains info about its position on screen and color
    """

    def __init__(self, pos: int, width: int, offset_x: int, offset_y: int, color: pygame.Color):
        self.pos = pos

        self.pos_x = offset_x + width * (pos % 10 - 1)
        self.pos_y = offset_y + width * (pos // 10 - 1)

        self.width = width
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.color = color

    def get_rect(self) -> pygame.Rect:
        """Returns coordinates of tile in pixels"""
        return pygame.Rect(self.pos_x, self.pos_y, self.width, self.width)

    def get_color(self):
        """Returns color of tile"""
        return self.color

    def pos_matches(self, pos: int) -> bool:
        """Returns true if tile position matches given position"""
        return self.pos == pos

    def get_piece_coords(self) -> pygame.Rect:
        """Gets coordinates of piece on tile in pixels"""
        return pygame.Rect(self.pos_x, self.pos_y, self.width, self.width)


class Game:
    """
    Game is a view class which renders window using pygame, and
    matches user input with board actions
    """

    modes = {}

    def __init__(self):
        self._is_running: bool = True
        self._cell_size: int = 80

        # Pygame config
        pygame.init()
        pygame.display.set_caption("CHESS")
        pygame.display.set_mode((self._cell_size * 8, self._cell_size * 8))

        self.surface: pygame.Surface = pygame.display.get_surface()
        self.surface.fill((211, 211, 211))
        self._offset_x: int = 0
        self._offset_y: int = 0

        # Board config
        self.board: Board = Board()
        self.assets: Assets = Assets().load("pixel")

        # Tiles
        self.tiles: list[Tile] = []
        self.tiles_dict: Dict[int, Tile] = {}

        for i, z in product(range(1, 9), range(1, 9)):
            new_tile: Tile = Tile(
                i * 10 + z,
                self._cell_size,
                self._offset_x,
                self._offset_y,
                pygame.Color(50, 50, 50) if (i + z) % 2 == 0 else pygame.Color(205, 205, 205),
            )

            self.tiles.append(new_tile)
            self.tiles_dict[int(str(i) + str(9 - z))] = new_tile

    def _draw_pieces(self):
        """Draws board pieces"""

        for piece in self.board.pieces:
            self.surface.blit(pygame.image.load(self.assets.get_piece_image(piece)), self._get_pos(piece.get_pos()))

    def _get_pos(self, pos: int) -> set[int]:
        """Get position of tile in pixels"""
        return self.tiles_dict[pos].get_piece_coords()

    def _draw(self):
        """Draws tiles and pieces"""
        for i in self.tiles:
            pygame.draw.rect(
                self.surface,
                i.get_color(),
                i.get_rect(),
            )

        self._draw_pieces()

    def _mouse_pos(self) -> int:
        """Returns tile number from current mouse coordinates"""

        mouse_position: tuple[int, int] = pygame.mouse.get_pos()
        mouse_x: int = mouse_position[0]
        mouse_y: int = mouse_position[1]

        coord_x: int = (mouse_x - self._offset_x) // self._cell_size + 1
        if coord_x > 8:
            return None

        coord_y: int = (mouse_y - self._offset_y) // self._cell_size + 1
        if coord_y > 8:
            return None

        return coord_x + coord_y * 10

    def _get_piece_on_tile(self, pos: int):
        """Returns piece on tile with given position, or None if there is no piece"""
        for piece in self.board.pieces:
            if piece.get_pos() == pos:
                return piece

        return None

    def run(self):
        """Game loop, which handles user input and renders window"""
        while self._is_running:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._is_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # LMB
                        print("LMB", self._mouse_pos())
                        piece = self._get_piece_on_tile(self._mouse_pos())
                        print(piece.get_name() if piece else "no piece")
                    elif event.button == 3:  # RMB
                        print("RMB", self._mouse_pos())

            self._draw()

            pygame.display.update()  # TODO: add freeze logic on no changes

        pygame.quit()
