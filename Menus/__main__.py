import arcade

from .constants import *

import SpaceGame

class GameMenu(arcade.Window):

    def __init__(self):

        super().__init__(fullscreen=True)

        arcade.set_background_color(arcade.color.GRAPE)

    def on_draw(self):

        arcade.start_render()

        arcade.draw_circle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, RADIUS, arcade.color.BLUE)

    def on_key_press(self, symbol: int, modifiers: int):
        """Handle user keyboard input
        Q: Quit the game
        P: Pause the game
        I/J/K/L: Move Up, Left, Down, Right
        Arrows: Move Up, Left, Down, Right

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """

        if symbol == arcade.key.G:
            SpaceGame.run_this_game()


if __name__ == "__main__":
    print("press G to launch the test game")

    app = GameMenu()
    arcade.run()
