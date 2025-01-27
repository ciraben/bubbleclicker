import arcade
import arcade.gui
from bubbles import BasicBubble


class BaseView(arcade.gui.view.UIView):
    def setup(self):
        self.bubbles = arcade.SpriteList()

        new_bubble = BasicBubble()
        new_bubble.position = self.center
        self.bubbles.append(new_bubble)

        # UI

        ui_layout = arcade.gui.UIAnchorLayout()
        self.add_widget(ui_layout)

        points_sidebar = arcade.gui.UIBoxLayout(align="right")
        ui_layout.add(points_sidebar, anchor_x="right", anchor_y="top")

        self.points_label = arcade.gui.UILabel(text = "0 BP")
        self.points_label_2 = arcade.gui.UILabel(text = "343 BP")
        points_sidebar.add(self.points_label)
        points_sidebar.add(self.points_label_2)

    def on_update(self, dt):
        self.bubbles.update(dt)

    def on_draw_before_ui(self):
        self.bubbles.draw()
