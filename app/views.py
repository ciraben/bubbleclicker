import arcade

class BaseView(arcade.View):
    def setup(self):
        self.bubbles = arcade.SpriteList()

        new_bubble = arcade.Sprite("art/mainbubble.png")
        new_bubble.position = self.center
        self.bubbles.append(new_bubble)

    def on_update(self, dt):
        self.bubbles.update(dt)

    def on_draw(self):
        self.clear()
        self.bubbles.draw()
