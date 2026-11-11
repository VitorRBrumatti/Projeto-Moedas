"""Botões animados, mira e seleção por disparo reutilizados em todas as Views."""

from dataclasses import dataclass
import math
import random
import arcade


@dataclass
class Button:
    id: str
    label: str
    box: tuple
    action: object
    subtitle: str = ""
    hover: float = 0.0

    def contains(self, x, y):
        bx, by, w, h = self.box
        return bx <= x <= bx + w and by <= y <= by + h


class ScreenMotion:
    def __init__(self, view):
        self.view = view
        self.time = 0.0
        self.pointer = (-100, -100)
        self.buttons = []
        self.selection = None
        self.pending = None
        self.shot = None
        rng = random.Random(19)
        self.motes = [
            (rng.randrange(960), rng.randrange(640), rng.uniform(7, 24))
            for _ in range(28)
        ]

    def add(self, id, label, box, action, subtitle=""):
        button = Button(id, label, box, action, subtitle)
        self.buttons.append(button)
        return button

    def trigger(self, id):
        if self.pending:
            return False
        button = next((b for b in self.buttons if b.id == id), None)
        if not button:
            return False
        x, y, w, h = button.box
        target = (
            self.pointer
            if button.contains(*self.pointer)
            else (x + w * 0.65, y + h * 0.5)
        )
        delay = .25 if getattr(self.view.window, "reduced_effects", False) else .85
        self.pending = [delay, button.action]
        self.shot = [target, delay, delay]
        self.bomb_sounded = False
        return True

    def click(self, x, y):
        self.pointer = (x, y)
        for b in self.buttons:
            if b.contains(x, y):
                return self.trigger(b.id)
        return False

    def update(self, dt):
        dt = min(dt, 0.1)
        self.time += dt
        for b in self.buttons:
            target = 1.0 if b.contains(*self.pointer) else 0.0
            b.hover += (target - b.hover) * min(1, dt * 14)
        if self.shot:
            if not self.bomb_sounded and self.shot[2] - self.shot[1] >= .12:
                self.view.window.audio.play("boom_v4")
                self.bomb_sounded = True
            self.shot[1] -= dt
            if self.shot[1] <= 0:
                self.shot = None
        if self.pending:
            self.pending[0] -= dt
            if self.pending[0] <= 0:
                action = self.pending[1]
                self.pending = None
                action()

    def atmosphere(self):
        for x, y, speed in self.motes:
            px = (x + math.sin(self.time * 0.2 + y) * 13) % 960
            py = (y + self.time * speed) % 640
            arcade.draw_circle_filled(px, py, 1.5, (255, 219, 140, 40))

    def draw(self):
        if getattr(self, "arcade_menu", False):
            from arcade_style import draw_menu_buttons

            draw_menu_buttons(self)
        else:
            from arcade_style import draw_field_buttons

            draw_field_buttons(self)
        if self.shot:
            (tx, ty), remaining, duration = self.shot
            if not self.view.window.reduced_effects:
                from sprites_v6 import draw
                elapsed = duration - remaining
                if elapsed < .12:
                    t = elapsed / .12
                    draw("grenade", 920 + (tx - 920) * t,
                         50 + (ty - 50) * t + math.sin(t * math.pi) * 160,
                         28, 34, elapsed)
                else:
                    draw("explosion", tx, ty + 65, 230, 230, (elapsed - .12) * 1.9, loop=False)
        alpha = max(0, int(255 * (1 - self.time / 0.35)))
        if alpha:
            arcade.draw_rect_filled(arcade.LBWH(0, 0, 960, 640), (9, 21, 28, alpha))
        from arcade_style import cabinet_overlay

        cabinet_overlay(self.view.window)
