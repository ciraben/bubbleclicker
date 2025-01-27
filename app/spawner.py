import arcade
from bubbles import BasicBubble

class Spawner():
    def __init__(self, view):
        self.view = view
        self.elapsed_time_since_last_bubble = 0

    def setup(self):
        self.spawn_soap_bubble()

    def spawn_things(self, dt):
        self.elapsed_time_since_last_bubble += dt
        if self.elapsed_time_since_last_bubble > 1:
            self.spawn_soap_bubble()
            self.elapsed_time_since_last_bubble = 0

    def spawn_soap_bubble(self):
        new_bubble = BasicBubble()
        new_bubble.position = self.view.center
        self.view.bubbles.append(new_bubble)
