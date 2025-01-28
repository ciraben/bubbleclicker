import arcade
from bubbles import BasicBubble
from constants import *
import random

class Spawner():
    def __init__(self, view):
        self.view = view
        self.elapsed_time_since_last_bubble = 0

    def setup(self):
        self.spawn_soap_bubble()

    def spawn_things(self, dt):
        self.elapsed_time_since_last_bubble += dt
        if self.elapsed_time_since_last_bubble > BASE_SPAWN_RATE:
            self.spawn_soap_bubble()
            self.elapsed_time_since_last_bubble = 0

    def spawn_soap_bubble(self):
        new_bubble = BasicBubble()
        new_bubble.position = (random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT))
        self.view.bubbles.append(new_bubble)
