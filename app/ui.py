import arcade.gui
from menus import ShopMenu
from constants import *

class GameUI(arcade.gui.UIAnchorLayout):
    def __init__(self):
        super().__init__()
        self.with_padding(all = UI_GLOBAL_PADDING)

        self.points_sidebar = self.add(
            PointsSidebar(), anchor_x="right", anchor_y="top"
        )
        self.shop_bottombar = self.add(
            ShopBottomBar(), anchor_x="left", anchor_y="bottom"
        )
        self.shop_menu = self.add(
            ShopMenu()
        )

        @self.shop_bottombar.bubble_shop_button.event("on_click")
        def toggle_menu(event):
            self.shop_menu.toggle()

class PointsSidebar(arcade.gui.UIBoxLayout):
    def __init__(self):
        super().__init__(align = "right")
        self.bp_label = arcade.gui.UILabel(text = "0 BP")
        self.add(self.bp_label)

class ShopBottomBar(arcade.gui.UIBoxLayout):
    def __init__(self):
        super().__init__(vertical = False)
        self.bubble_shop_button = arcade.gui.UIFlatButton(text = "Bubble Shop")
        self.add(self.bubble_shop_button)
