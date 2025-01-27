import arcade
from bubbles import BasicBubble

class Spawner():
    def __init__(self, view):
        self.view = view

    def setup(self):
        new_bubble = BasicBubble()
        new_bubble.position = self.view.center
        self.view.bubbles.append(new_bubble)

    def spawn_things(self, dt):
        pass
