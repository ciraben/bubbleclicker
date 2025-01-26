import arcade
import arcade.gui
from bubbles import BasicBubble


class BaseView(arcade.gui.view.UIView):
    def setup(self):
        self.bubbles = arcade.SpriteList()

        new_bubble = BasicBubble()
        new_bubble.position = self.center
        self.bubbles.append(new_bubble)

        points_label = arcade.gui.UIDummy()
        self.add_widget(points_label)

    def on_update(self, dt):
        self.bubbles.update(dt)

    def on_draw_before_ui(self):
        self.bubbles.draw()
