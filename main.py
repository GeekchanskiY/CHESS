from game.game import Game


if __name__ == "__main__":
    for z in range(1, 9):
        print([i + (9 - z) * 10 for i in range(1, 9)])

    game = Game()
    game.run()
