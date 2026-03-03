from game.game import Game
import logging


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)
    game = Game()
    game.run()
