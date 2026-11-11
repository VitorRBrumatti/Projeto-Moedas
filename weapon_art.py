"""Geometria única e sprites pixelados do arsenal, sem alterar balanceamento."""

from dataclasses import dataclass
from functools import lru_cache
import math
import arcade

MUZZLES = {"glock": 22, "ak": 36, "minigun": 42}
RECOIL = {"glock": 1.1, "ak": 4.0, "minigun": 1.8}
FLASH_TIME = {"glock": 0.035, "ak": 0.05, "minigun": 0.025}
TRAILS = {"glock": 10, "ak": 16, "minigun": 12, "hostile": 9}
COLORS = {
    "glock": (255, 219, 125),
    "minigun": (255, 185, 94),
    "ak": (255, 211, 89),
    "smg": (162, 236, 224),
    "shotgun": (255, 177, 108),
    "rifle": (189, 215, 255),
    "hostile": (255, 123, 164),
}


@dataclass(frozen=True)
class GunPose:
    pivot: tuple
    angle: float
    kind: str
    recoil: float = 0.0
    scale: float = 1.0
    anim_time: float = 0.0

    def point(self, x, y=0):
        x, y = x * self.scale, y * self.scale
        c, s = math.cos(self.angle), math.sin(self.angle)
        flip = -1 if c < 0 else 1
        return (
            self.pivot[0] + (x - self.recoil) * c - y * flip * s,
            self.pivot[1] + (x - self.recoil) * s + y * flip * c,
        )

    @property
    def muzzle(self):
        return self.point(MUZZLES[self.kind])

    @property
    def grip(self):
        return self.point(-5, -5)

    @property
    def support(self):
        return self.point(12, -3)


@lru_cache(maxsize=96)
def gun_texture(kind, flip=False, frame=0):
    from sprite_assets import frames
    tex = frames("weapon-" + kind)[frame % 8]
    return tex.flip_top_bottom() if flip else tex


def draw_weapon(pose, hands=True):
    tex = gun_texture(pose.kind, math.cos(pose.angle) < 0, int(pose.anim_time * 24))
    center = pose.point((MUZZLES[pose.kind] - 16) / 2, -1)
    arcade.draw_texture_rect(
        tex,
        arcade.LBWH(
            center[0] - tex.width * pose.scale / 2, center[1] - tex.height * pose.scale / 2,
            tex.width * pose.scale, tex.height * pose.scale
        ),
        angle=-math.degrees(pose.angle),
        pixelated=True,
    )
    if hands:
        for x, y in (pose.grip, pose.support):
            arcade.draw_rect_filled(
                arcade.LBWH(x - 3 * pose.scale, y - 2 * pose.scale,
                            6 * pose.scale, 5 * pose.scale), (38, 31, 31)
            )
            arcade.draw_rect_filled(
                arcade.LBWH(x - 2 * pose.scale, y - pose.scale,
                            4 * pose.scale, 3 * pose.scale), (235, 181, 120)
            )
