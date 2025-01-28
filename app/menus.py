import arcade.gui
from constants import *

class ShopMenu(arcade.gui.UIBoxLayout):
    def __init__(self):
        super().__init__()
        self.title = "Bubble Shop"

        self.with_background(color = arcade.color.ARSENIC)
        self.with_padding(all = UI_MENU_PADDING)

        self.add(arcade.gui.UILabel(text = self.title, font_size = UI_MENU_TITLE_FONTSIZE))
        self.add(arcade.gui.UISpace(height = UI_MENU_VERTICAL_SPACE_AFTER_TITLE))
        self.add(ShopItems())

        self.visible = False

    def toggle(self):
        self.visible = not self.visible

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
