#!/usr/bin/env python3.9

import arcade
from views import BaseView

def main():
    window = arcade.Window()
    view = BaseView()
    view.setup()
    window.show_view(view)
    arcade.run()

if __name__ == "__main__":
    main()
