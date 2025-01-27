import arcade

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WINDOW_TITLE = "bubble clicker"

BASE_SPAWN_RATE = 3
BASE_POINT_VALUE = 1

bubblepopsound = (
    arcade.load_sound('audio/bubblepop1.mp3'),
    arcade.load_sound('audio/bubblepop2.mp3'),
    arcade.load_sound('audio/bubblepop3.mp3')
)

# UI
UI_GLOBAL_PADDING = 20
