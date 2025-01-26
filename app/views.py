import arcade
from bubbles import BasicBubble

class BaseView(arcade.View):
    def setup(self):
        self.bubbles = arcade.SpriteList()

        new_bubble = BasicBubble()
        new_bubble.position = self.center
        self.bubbles.append(new_bubble)

    def on_update(self, dt):
        self.bubbles.update(dt)

    def on_draw(self):
        self.clear()
        self.bubbles.draw()
