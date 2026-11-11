"""Cached artist sprites and pack effects; geometry stays in the owning gameplay classes."""
from functools import lru_cache
from pathlib import Path
import json
import arcade

BASE = Path(__file__).resolve().parent / 'assets/v6'
REGISTRY = json.loads((BASE / 'sprites.json').read_text(encoding='utf-8'))


@lru_cache(maxsize=None)
def frames(name):
    spec = REGISTRY[name]
    return arcade.load_spritesheet(str(BASE / spec.get("file", name + ".png"))).get_texture_grid(
        size=tuple(spec['size']), columns=spec['count'], count=spec['count'])


@lru_cache(maxsize=None)
def mirrored(name):
    return [tex.flip_left_right() for tex in frames(name)]


def preload():
    for name in REGISTRY:
        frames(name)
        if name.startswith("fighter-") or name in ("boss", "drone"):
            mirrored(name)


def texture(name, age=0, loop=True, flip=False):
    spec = REGISTRY[name]
    index = int(max(0, age) * spec['fps'])
    return (mirrored(name) if flip else frames(name))[index % spec['count'] if loop else min(index, spec['count'] - 1)]


def draw(name, x, y, width, height, age=0, *, angle=0, alpha=255, loop=True):
    arcade.draw_texture_rect(texture(name, age, loop),
        arcade.LBWH(x - width/2, y - height/2, width, height),
        angle=angle, alpha=alpha, pixelated=True)
