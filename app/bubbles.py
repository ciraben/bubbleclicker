import arcade

class BasicBubble(arcade.Sprite):
    ART_PATH = "art/mainbubble.png"

    def __init__(self, *args):
        super().__init__(path_or_texture=self.ART_PATH, *args)
