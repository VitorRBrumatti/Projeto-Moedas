"""Apresentação em slots de texto reutilizáveis e sinais visuais dos inimigos."""

import arcade


class TextPool:
    def __init__(self):
        self.slots = {}

    def draw(self, key, value, x, y, size=12, color=(237, 242, 218), bold=False):
        label = self.slots.get(key)
        if label is None:
            label = arcade.Text(
                str(value), x, y, color, size, font_name="DejaVu Sans", bold=bold
            )
            self.slots[key] = label
        else:
            if label.text != str(value):
                label.text = str(value)
            label.x = x
            label.y = y
            label.color = color
        label.draw()


def enemy_role(enemy, player=None):
    # Target marker is UI; the body, equipment and damage flash belong to the sprite.
    if enemy.kind == "boss" and enemy.alert:
        from arcade_style import ui_icon
        ui_icon("crosshair", getattr(enemy, "target_x", enemy.center_x) - 12, 98, 24)
    elif enemy.kind == "shooter" and enemy.alert and enemy.aim_time > 0.15 and player is not None:
        ox, oy = enemy.shot_origin
        arcade.draw_line(ox, oy, player.center_x, player.center_y, (78, 226, 255, 85), 1.5)
