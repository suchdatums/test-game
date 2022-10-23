from arcade import run

import SpaceGame.MainGame as MainGame
from SpaceGame.constants import *


def run_this_game():
    space_game = MainGame.SpaceShooter()
    space_game.setup()
    run()


if __name__ == "__main__":
    run_this_game()
