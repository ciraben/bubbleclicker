import arcade
import arcade.gui
import random
from spawner import Spawner
from constants import *
from ui import GameUI

class BaseView(arcade.gui.view.UIView):
    def setup(self):
        self.bubbles = arcade.SpriteList()

        self.spawner = Spawner(self)
        self.spawner.setup()

        self.gui = GameUI()
        self.add_widget(self.gui)

        self.bubble_points = 0

    def on_update(self, dt):
        self.spawner.spawn_things(dt)
        self.bubbles.update(dt)

    def on_draw_before_ui(self):
        self.bubbles.draw()

    def on_mouse_press(self, x, y, button, mods):
        if button != arcade.MOUSE_BUTTON_LEFT:
            return

        clicked_bubbles = arcade.get_sprites_at_point((x, y), self.bubbles)
        for bubble in clicked_bubbles:
            bubble.remove_from_sprite_lists()
            self.bubble_points += BASE_POINT_VALUE
            arcade.play_sound(random.choice(bubblepopsound))
        self.gui.points_sidebar.bp_label.text = f"{self.bubble_points} BP"
