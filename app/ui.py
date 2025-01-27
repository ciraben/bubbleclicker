import arcade.gui
from constants import *

class GameUI(arcade.gui.UIAnchorLayout):
    def __init__(self):
        super().__init__()
        self.with_padding(all = UI_GLOBAL_PADDING)
        self.add_points_sidebar()

    def add_points_sidebar(self):
        self.bp_label = arcade.gui.UILabel(text = "0 BP")
        points_sidebar = arcade.gui.UIBoxLayout(align="right")
        points_sidebar.add(self.bp_label)
        self.add(points_sidebar, anchor_x="right", anchor_y="top")
