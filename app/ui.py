import arcade.gui
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

class ShopMenu(arcade.gui.UIBoxLayout):
    def __init__(self):
        super().__init__()
        self.title = "Bubble Shop"

        self.with_background(color = arcade.color.ARSENIC)
        self.with_padding(all = UI_MENU_PADDING)

        self.add(arcade.gui.UILabel(text = self.title, font_size = UI_MENU_TITLE_FONTSIZE))
        self.add(arcade.gui.UISpace(height = UI_MENU_VERTICAL_SPACE_AFTER_TITLE))
        self.add(ShopItems())

class ShopItems(arcade.gui.UIBoxLayout):
    def __init__(self):
        super().__init__()
        self.with_background(color = arcade.color.AFRICAN_VIOLET)
        self.with_padding(left = UI_MENU_PADDING_AROUND_LINE_ITEMS, right = UI_MENU_PADDING_AROUND_LINE_ITEMS)
        self.add(ShopItem())
        self.add(ShopItem())
        self.add(ShopItem())
        self.add(ShopItem())

class ShopItem(arcade.gui.UIBoxLayout):
    def __init__(self):
        super().__init__(vertical = False)
        self.with_padding(all = UI_MENU_PADDING_BETWEEN_LINE_ITEMS)
        self.add(LineItemInfo(text = "0x"))
        self.add(LineItemInfo(text = "Frequency"))
        self.add(LineItemBuyButton(text = "Buy"))
        self.add(LineItemInfoNoPad(text = "10 BP"))

class LineItemInfo(arcade.gui.UILabel):
    def __init__(self, text):
        super().__init__(text = text)
        self.with_padding(right = UI_MENU_PADDING_WITHIN_LINE_ITEM)

class LineItemBuyButton(arcade.gui.UIFlatButton):
    def __init__(self, text):
        super().__init__(text = text)
        self.with_padding(right = UI_MENU_PADDING_WITHIN_LINE_ITEM)

class LineItemInfoNoPad(LineItemInfo):
    def __init__(self, text):
        super().__init__(text = text)
        self.with_padding(right = 0)
