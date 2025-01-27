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

        self.bubble_points = 0
        self.BP_label = arcade.gui.UILabel(text = "0 BP")
        points_sidebar.add(self.BP_label)

    def on_update(self, dt):
        self.bubbles.update(dt)

    def on_draw_before_ui(self):
        self.bubbles.draw()

    def on_mouse_press(self, x, y, button, mods):
        if button != arcade.MOUSE_BUTTON_LEFT:
            return

        clicked_bubbles = arcade.get_sprites_at_point((x, y), self.bubbles)
        for bubble in clicked_bubbles:
            bubble.remove_from_sprite_lists()
            self.bubble_points += 1
        self.BP_label.text = f"{self.bubble_points} BP"
