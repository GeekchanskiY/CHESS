from itertools import product
import pygame
from typing import Dict

from board.board import Board
from .tile import Tile
from .assets import Assets
from pieces.piece import Piece
from pieces.color import BLACK, WHITE

from logging import debug


class Game:
    """
    Game is a view class which renders window using pygame, and
    matches user input with board actions
    """

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
            self.tiles_dict[i * 10 + z] = new_tile

        # Game state
        self.selected_piece = None
        self.available_moves = []

    # DRAW METHODS (TODO: move to separate class)

    def _draw_pieces(self):
        """Draws board pieces"""

        # TODO: pre-load images for better performance
        for piece in self.board.pieces:
            self.surface.blit(pygame.image.load(self.assets.get_piece_image(piece)), self._get_pos(piece.get_pos()))

    def _draw_hints(self):
        """Draws hints for selected piece"""

        for move in self.available_moves:
            self.surface.blit(pygame.image.load(self.assets.get_hint_image()), self._get_pos(move))

    def _draw(self):
        """Draws tiles and pieces"""
        debug("drawing scene")

        for i in self.tiles:
            pygame.draw.rect(
                self.surface,
                i.get_color(),
                i.get_rect(),
            )

        self._draw_pieces()
        self._draw_hints()

        pygame.display.update()

    # Click handling metgods
    def _get_pos(self, pos: int) -> pygame.Rect:
        """Get position of tile in pixels"""
        tile: Tile = self.tiles_dict[pos]
        return tile.get_piece_coords()

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

    def _clear_cursor(self):
        """Clears cursor state"""
        self.selected_piece = None
        self.available_moves = []
        debug("Cursor cleared")

    def _select_piece(self, pos: int):
        """Selects piece and shows available moves"""
        piece: Piece = self._get_piece_on_tile(pos)

        self.selected_piece = piece
        self.available_moves = piece.get_available_moves(self.board.pieces, self.board.turn)

        debug(f"Selected piece {piece.get_name()} at {piece.get_pos()}, available moves: {self.available_moves}")

    def _lmb_click(self):
        debug(f"LMB {self._mouse_pos()}")

        pos = self._mouse_pos()
        if self.selected_piece != None:
            if pos in self.available_moves:
                self.board.make_turn(self.selected_piece, pos)
                self._clear_cursor()
                self._draw()

                return

        piece = self._get_piece_on_tile(pos)
        if piece:
            if (
                self.board.turn % 2 == 0
                and piece.get_color() == WHITE
                or self.board.turn % 2 == 1
                and piece.get_color() == BLACK
            ):
                self._select_piece(self._mouse_pos())
                self._draw()

                return

    def _rmb_click(self):
        debug(f"RMB {self._mouse_pos()}")

        if self.selected_piece is not None:
            self._clear_cursor()
            self._draw()

    def run(self):
        """Game loop, which handles user input and renders window"""

        self._draw()

        while self._is_running:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._is_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # LMB
                        self._lmb_click()
                    elif event.button == 3:  # RMB
                        self._rmb_click()

            pygame.display.update()

        pygame.quit()
