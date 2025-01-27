#!/usr/bin/env python3.9

import arcade
from views import BaseView
from constants import *

def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    view = BaseView()
    view.setup()
    window.show_view(view)
    arcade.run()

if __name__ == "__main__":
    main()
