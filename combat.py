"""Granadas balísticas e efeitos legíveis sem alterar as colisões dos tiros."""

import math
import arcade
from weapon_art import TRAILS, COLORS


class Grenade(arcade.SpriteSolidColor):
    def __init__(self, x, y, vx=0):
        super().__init__(14, 16, color=(139, 211, 86))
        self.position = x, y
        self.change_x = vx
        self.change_y = -0.8
        self.fuse = 3.0
        self.grounded = False
        self.exploded = False
        self.age = 0.0

    def tick(self, dt, walls):
        if self.exploded:
            return False
        self.age += dt
        if not self.grounded:
            previous = self.bottom
            self.change_y = max(-8, self.change_y - 0.12)
            self.center_x += self.change_x
            self.center_y += self.change_y
            supports = [
                b
                for b in arcade.check_for_collision_with_list(self, walls)
                if previous >= b.top - 9
            ]
            if supports:
                self.bottom = max(b.top for b in supports)
                self.change_x = 0
                self.change_y = 0
                self.grounded = True
                self.fuse = min(self.fuse, 0.95)
        self.fuse -= dt
        if self.fuse <= 0:
            self.exploded = True
            return True
        return False

    def draw_fx(self):
        from sprites_v6 import draw
        draw("grenade", *self.position, 18, 22, self.age)
        if self.grounded:
            arcade.draw_circle_outline(*self.position, 72, (255, 126, 58, 180), 2)


class Impact:
    def __init__(self, x, y, explosion=False):
        self.x = x
        self.y = y
        self.explosion = explosion
        self.age = 0.0
        self.life = 1.26 if explosion else 0.4

    def update(self, dt):
        self.age += dt
        self.life -= dt

    def draw(self):
        from sprites_v6 import draw
        draw("explosion" if self.explosion else "hit", self.x, self.y,
             190 if self.explosion else 45, 190 if self.explosion else 45,
             self.age, loop=False)


def draw_projectile(bullet):
    from sprites_v6 import draw
    draw("knife" if bullet.knife else "hostile-tracer" if bullet.hostile else "tracer", *bullet.position,
         28 if bullet.knife else 32 if bullet.hostile else 20,
         24 if bullet.knife else 12 if bullet.hostile else 7,
         age=1.8-bullet.life, angle=-bullet.angle)


def muzzle_flash(x, y, angle, kind="glock"):
    from sprites_v6 import draw
    from weapon_art import FLASH_TIME
    remaining = getattr(arcade.get_window().current_view, "muzzle", 0)
    age = max(0, 1 - remaining / FLASH_TIME[kind]) * .3
    draw("hit", x, y, 30, 22, age=age, angle=-math.degrees(angle), loop=False)


class Cover(arcade.SpriteSolidColor):
    """Explicit ballistic cover; also a small jumpable physical obstacle."""

    def __init__(self, x, floor=96):
        super().__init__(36, 48, color=(67, 86, 96))
        from sprites_v6 import texture
        self.texture = texture("cover")
        self.left = x
        self.bottom = floor
        self.ballistic = True
        self.is_cover = True

    def draw_fx(self, theme="jungle", clock=0):
        from sprites_v6 import draw
        draw("cover", self.center_x, self.center_y, self.width, self.height, clock)


def segment_box(start, end, bounds, radius=2.0):
    """Slab intersection, returning first time along segment (0..1)."""
    left, bottom, right, top = bounds
    lo, hi = 0.0, 1.0
    for origin, delta, minimum, maximum in (
        (start[0], end[0] - start[0], left - radius, right + radius),
        (start[1], end[1] - start[1], bottom - radius, top + radius),
    ):
        if abs(delta) < 1e-10:
            if origin < minimum or origin > maximum:
                return None
            continue
        a, b = (minimum - origin) / delta, (maximum - origin) / delta
        if a > b:
            a, b = b, a
        lo = max(lo, a)
        hi = min(hi, b)
        if lo > hi:
            return None
    return lo


def swept_contacts(start, end, groups, radius=2.0):
    contacts = []
    for category, sprites in groups:
        for sprite in sprites:
            hb = sprite.hit_box
            t = segment_box(start, end, (hb.left, hb.bottom, hb.right, hb.top), radius)
            if t is not None:
                point = (
                    start[0] + (end[0] - start[0]) * t,
                    start[1] + (end[1] - start[1]) * t,
                )
                contacts.append(
                    (t, 0 if category == "cover" else 1, category, sprite, point)
                )
    contacts.sort(key=lambda item: (item[0], item[1]))
    return contacts
