import arcade

class BasicBubble(arcade.Sprite):
    ART_PATH = "art/mainbubble.png"

    def __init__(self, *args):
        super().__init__(path_or_texture=self.ART_PATH, *args)

class MilkBubble(BasicBubble):
    ART_PATH = "art/milkbubble.png"

class SlimeBubble(BasicBubble):
    ART_PATH = "art/slimebubble.png"

class RoyalJellyBubble(BasicBubble):
    ART_PATH = "art/royaljellybubble.png"

class MagmaBubble(BasicBubble):
    ART_PATH = "art/magmabubble.png"
