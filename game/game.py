import pygame

from .board import Board

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



    def _draw_board(self):
        """
        Draws board contents
        """

        pass

    def _draw(self):
        # draw board background
        for i in range(1, 9):
            for z in range(1, 9):
                tile_color = (
                    pygame.Color(255, 255, 255)
                    if (i + z) % 2 == 0
                    else pygame.Color(50, 50, 50)
                )

                pygame.draw.rect(
                    self.surface,
                    tile_color,
                    (
                        self._cell_size * z,
                        self._cell_size * i,
                        self._cell_size,
                        self._cell_size,
                    ),
                )

        self._draw_board()

    def run(self):
        while self._is_running:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._is_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # LMB
                        pass
                    elif event.button == 3:  # RMB
                        pass

            self._draw()

            pygame.display.update()  # TODO: add freeze logic on no changes

        pygame.quit()
