"""Perigos com aviso visual e desenho de armas rotacionadas no mundo."""

import arcade


class Hazard(arcade.SpriteSolidColor):
    def __init__(self, x, kind):
        super().__init__(
            14 if kind == "laser" else 42,
            410 if kind == "laser" else 15,
            color=(235, 75, 52),
        )
        self.kind = kind
        self.center_x = x
        self.bottom = 96
        self.fuse = None
        self.phase = 0.0
        self.exploded = False

    @property
    def warning(self):
        return self.kind == "laser" and 2 < self.phase < 2.9

    @property
    def active(self):
        return self.kind == "spikes" or (self.kind == "laser" and self.phase >= 2.9)

    def tick(self, dt, clock, player):
        self.phase = (clock + self.center_x * 0.001) % 4
        if self.kind == "mine" and not self.exploded:
            if (
                self.fuse is None
                and abs(player.center_x - self.center_x) < 100
                and player.bottom < 165
            ):
                self.fuse = 0.75
            if self.fuse is not None:
                self.fuse -= dt
                if self.fuse <= 0:
                    self.exploded = True
                    return True
        return False

    def draw_fx(self, clock):
        from sprite_assets import draw
        x = self.center_x
        if self.kind == "laser":
            draw("emitter", x, 114, 44, 48, clock)
            draw("emitter", x, 489, 44, 48, clock, angle=180)
            if self.warning or self.active:
                draw("laser-beam", x, 297, 30 if self.active else 12, 400, clock,
                     alpha=255 if self.active else 90)
        elif self.kind == "mine" and not self.exploded:
            draw("mine", x, 107, 42, 22, clock if self.fuse is not None else 0)
            if self.fuse is not None:
                arcade.draw_circle_outline(x, 105, 72, (255, 100, 60, 130), 2)
        elif self.kind == "spikes":
            draw("spikes", x, 107, 42, 22, clock)


class Barrel(arcade.SpriteSolidColor):
    def __init__(self, x, y):
        super().__init__(24, 34, color=(177, 63, 39))
        self.position = x, y
        self.hp = 1

    def draw_fx(self):
        from sprite_assets import draw
        draw("jerrycan", self.center_x, self.center_y + 5, 32, 44,
             arcade.get_window().current_view.run.time)



def draw_gun(x, y, angle, kind, recoil=0):
    from weapon_art import GunPose, draw_weapon

    draw_weapon(GunPose((x, y), angle, kind, recoil))
