"""Pixel lettering and CRT cabinet treatment; UI stays fully interactive."""

from pathlib import Path
from functools import lru_cache
import math
import unicodedata
from PIL import Image, ImageDraw
import arcade

# Exact bitmap alphabet: native UI assets, no system font dependency.
ROWS = {
    "%": "11001/11010/00010/00100/01000/01011/10011",
    "A": "01110/10001/10001/11111/10001/10001/10001",
    "B": "11110/10001/10001/11110/10001/10001/11110",
    "C": "01111/10000/10000/10000/10000/10000/01111",
    "D": "11110/10001/10001/10001/10001/10001/11110",
    "E": "11111/10000/10000/11110/10000/10000/11111",
    "F": "11111/10000/10000/11110/10000/10000/10000",
    "G": "01111/10000/10000/10111/10001/10001/01111",
    "H": "10001/10001/10001/11111/10001/10001/10001",
    "I": "11111/00100/00100/00100/00100/00100/11111",
    "J": "00111/00010/00010/00010/10010/10010/01100",
    "K": "10001/10010/10100/11000/10100/10010/10001",
    "L": "10000/10000/10000/10000/10000/10000/11111",
    "M": "10001/11011/10101/10101/10001/10001/10001",
    "N": "10001/11001/10101/10011/10001/10001/10001",
    "O": "01110/10001/10001/10001/10001/10001/01110",
    "P": "11110/10001/10001/11110/10000/10000/10000",
    "Q": "01110/10001/10001/10001/10101/10010/01101",
    "R": "11110/10001/10001/11110/10100/10010/10001",
    "S": "01111/10000/10000/01110/00001/00001/11110",
    "T": "11111/00100/00100/00100/00100/00100/00100",
    "U": "10001/10001/10001/10001/10001/10001/01110",
    "V": "10001/10001/10001/10001/10001/01010/00100",
    "W": "10001/10001/10001/10101/10101/10101/01010",
    "X": "10001/10001/01010/00100/01010/10001/10001",
    "Y": "10001/10001/01010/00100/00100/00100/00100",
    "Z": "11111/00001/00010/00100/01000/10000/11111",
    "0": "01110/10001/10011/10101/11001/10001/01110",
    "1": "00100/01100/00100/00100/00100/00100/01110",
    "2": "01110/10001/00001/00010/00100/01000/11111",
    "3": "11110/00001/00001/01110/00001/00001/11110",
    "4": "00010/00110/01010/10010/11111/00010/00010",
    "5": "11111/10000/10000/11110/00001/00001/11110",
    "6": "01111/10000/10000/11110/10001/10001/01110",
    "7": "11111/00001/00010/00100/01000/01000/01000",
    "8": "01110/10001/10001/01110/10001/10001/01110",
    "9": "01110/10001/10001/01111/00001/00001/11110",
    ":": "00000/00100/00100/00000/00100/00100/00000",
    "/": "00001/00010/00010/00100/01000/01000/10000",
    "-": "00000/00000/00000/11111/00000/00000/00000",
    "!": "00100/00100/00100/00100/00100/00000/00100",
    ".": "00000/00000/00000/00000/00000/00100/00100",
    "+": "00000/00100/00100/11111/00100/00100/00000",
}


@lru_cache(maxsize=256)
def lettering(message, scale, color, style):
    message = "".join(
        c
        for c in unicodedata.normalize("NFD", message.upper())
        if not unicodedata.combining(c)
    )
    mask = Image.new("L", (len(message) * 6 + 4, 11))
    d = ImageDraw.Draw(mask)
    for i, char in enumerate(message):
        for y, row in enumerate(ROWS.get(char, "00000/" * 6 + "00000").split("/")):
            for x, value in enumerate(row):
                if value == "1":
                    d.point((i * 6 + x + 2, y + 1), 255)
    im = Image.new("RGBA", mask.size)
    draw = ImageDraw.Draw(im)
    # One-pixel outline and extrusion before nearest-neighbour scaling.
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1)):
        im.paste((9, 12, 10, 255), (dx, dy), mask)
    fill = Image.new("RGBA", mask.size)
    fd = ImageDraw.Draw(fill)
    for y in range(fill.height):
        if style == "metal":
            c = (
                (246, 247, 255, 255)
                if y < 4
                else ((165, 161, 210, 255) if y < 6 else (218, 219, 245, 255))
            )
        elif style == "gold":
            c = (
                (255, 247, 103, 255)
                if y < 4
                else ((255, 175, 34, 255) if y < 6 else (243, 88, 31, 255))
            )
        else:
            c = (*color[:3], 255)
        fd.line((0, y, fill.width, y), fill=c)
    im.paste(fill, (0, 0), mask)
    return arcade.Texture(
        im.resize((im.width * scale, im.height * scale), Image.Resampling.NEAREST)
    )


def pixel_text(
    message, x, y, scale=3, color=(244, 245, 255), center=False, style="plain"
):
    tex = lettering(message, scale, tuple(color), style)
    arcade.draw_texture_rect(
        tex,
        arcade.LBWH(x - tex.width / 2 if center else x, y, tex.width, tex.height),
        pixelated=True,
    )


@lru_cache(maxsize=4)
def scanline_texture(width, height):
    im = Image.new("RGBA", (width, height))
    draw = ImageDraw.Draw(im)
    for y in range(0, height, 4):
        draw.line((7, y, width - 7, y), fill=(6, 6, 15, 55))
    return arcade.Texture(im)


def cabinet_overlay(window, width=960, height=640):
    if not getattr(window, "arcade_filter", False):
        return
    if not window.reduced_effects:
        tex = scanline_texture(width, height)
        arcade.draw_texture_rect(tex, arcade.LBWH(0, 0, width, height), pixelated=True)
    for left in (0, width - 7):
        arcade.draw_rect_filled(arcade.LBWH(left, 0, 7, height), (6, 5, 19, 245))
    for y in (0, height - 7):
        arcade.draw_rect_filled(arcade.LBWH(0, y, width, 7), (6, 5, 19, 245))
    for x in (8, width - 10):
        arcade.draw_rect_filled(arcade.LBWH(x, 14, 2, height - 28), (103, 111, 84, 100))
    for x in (0, width):
        for y in (0, height):
            sx = 1 if x == 0 else -1
            sy = 1 if y == 0 else -1
            arcade.draw_triangle_filled(
                x, y, x + sx * 19, y, x, y + sy * 19, (4, 4, 14)
            )


# V5 palette shared by menu panels and focused controls; V5-B migrates other Views.
MILITARY = {"ink": (20, 25, 22), "steel": (52, 59, 48),
            "sand": (224, 210, 170), "ammo": (239, 188, 65), "rust": (139, 62, 38)}


def draw_menu_buttons(ui):
    hovered = next((b.id for b in ui.buttons if b.contains(*ui.pointer)), None)
    for index, b in enumerate(ui.buttons):
        x, y, w, h = b.box
        active = b.id == (hovered or ui.selection)
        border = MILITARY["ammo"] if active else (103, 111, 84)
        arcade.draw_rect_filled(arcade.LBWH(x + 4, y - 4, w, h), (9, 12, 10, 220))
        arcade.draw_rect_filled(arcade.LBWH(x, y, w, h),
                                MILITARY["steel"] if active else MILITARY["ink"])
        arcade.draw_rect_outline(arcade.LBWH(x, y, w, h), border, 2)
        arcade.draw_rect_filled(arcade.LBWH(x, y, 5, h), border)
        pixel_text(str(index + 1), x + 14, y + (h - 22) / 2, 2, color=border)
        pixel_text(b.label, x + 43, y + (h - (22 if len(b.label) > 12 else 33)) / 2,
                   2 if len(b.label) > 12 else 3, color=MILITARY["sand"])
        if active:
            arcade.draw_triangle_filled(x + w - 20, y + h/2,
                x + w - 27, y + h/2 + 5, x + w - 27, y + h/2 - 5, border)


class ArcadeMenuScene:
    def __init__(self):
        from actors import player_frames
        base = Path(__file__).parent
        self.background = arcade.load_texture(str(base / "assets/ruins.png"))
        self.frames = player_frames()
        self.hero = arcade.Sprite(self.frames[0], scale=2.6)
        self.hero.position = (660, 264)
        self.sprites = arcade.SpriteList()
        self.sprites.append(self.hero)

    def draw(self, t):
        from weapon_art import GunPose, draw_weapon
        drift = math.sin(t * 0.16) * 10
        arcade.draw_texture_rect(self.background,
            arcade.LBWH(-12 + drift, -8, 984, 656), pixelated=True)
        arcade.draw_rect_filled(arcade.LBWH(0, 0, 960, 640), (19, 26, 20, 105))
        arcade.draw_rect_filled(arcade.LBWH(24, 42, 356, 464), (20, 25, 22, 235))
        arcade.draw_rect_outline(arcade.LBWH(24, 42, 356, 464), (103, 111, 84), 2)
        arcade.draw_rect_filled(arcade.LBWH(0, 522, 960, 118), (20, 25, 22, 240))
        pixel_text("COIN COMMANDO", 42, 559, 7, color=MILITARY["sand"])
        pixel_text("OPERACAO / LINHA DE FRENTE", 46, 531, 2, color=MILITARY["ammo"])
        pixel_text("01 / PREPARAR MISSAO", 52, 486, 2, color=MILITARY["sand"])
        # Idle is a real individual frame, never a full spritesheet or fake walk.
        self.sprites.draw(pixelated=True)
        draw_weapon(GunPose((745, 250), 0, "ak", scale=3))
        arcade.draw_rect_filled(arcade.LBWH(430, 44, 482, 48), (20, 25, 22, 230))
        pixel_text("QUATRO FRENTES. UMA MISSAO.", 448, 70, 2, color=MILITARY["sand"])
        pixel_text("COLETE / SOBREVIVA / AVANCE", 448, 48, 2, color=MILITARY["ammo"])
        arcade.draw_rect_filled(arcade.LBWH(0, 0, 960, 30), MILITARY["ink"])
        pixel_text("SETAS / SELECIONAR   ENTER / CONFIRMAR   F9 / EFEITOS", 42, 6, 2,
                   color=MILITARY["sand"])


def military_panel(x, y, width, height):
    arcade.draw_rect_filled(arcade.LBWH(x, y, width, height), (*MILITARY["ink"], 245))
    arcade.draw_rect_outline(arcade.LBWH(x, y, width, height), (103, 111, 84), 2)
    arcade.draw_rect_filled(arcade.LBWH(x, y + height - 4, width, 4), MILITARY["rust"])


def ui_icon(name, x, y, size=24):
    texture = arcade.get_window().ui_assets[name]
    arcade.draw_texture_rect(texture, arcade.LBWH(x, y, size, size), pixelated=True)


def draw_field_buttons(ui):
    hovered = next((b.id for b in ui.buttons if b.contains(*ui.pointer)), None)
    for b in ui.buttons:
        x, y, w, h = b.box
        active = b.id == (hovered or ui.selection)
        unavailable = getattr(b, "unavailable", False)
        color = MILITARY["ammo"] if active else (103, 111, 84)
        arcade.draw_rect_filled(arcade.LBWH(x, y, w, h),
            MILITARY["steel"] if active else MILITARY["ink"])
        arcade.draw_rect_outline(arcade.LBWH(x, y, w, h), color, 2 if active else 1)
        arcade.draw_rect_filled(arcade.LBWH(x, y, 4, h), color)
        scale = 2 if (len(b.label) * 6 + 4) * 2 <= w - 32 else 1
        title_y = y + h - 34 if getattr(b, "card", False) else y + (h - 22) / 2 + (7 if b.subtitle else 0)
        pixel_text(b.label, x + 16, title_y, scale,
                   color=(143, 148, 125) if unavailable else MILITARY["sand"])
        if getattr(b, "render_extra", None):
            b.render_extra()
        if b.id in ("heal", "damage", "rate", "knives") and not (b.id == "rate" and getattr(b, "unavailable", False)):
            ui_icon("repair" if b.id == "heal" else "armor" if b.id == "damage" else "ammo",
                    x + w - 28, y + 7, 18)
        if b.subtitle:
            arcade.draw_text(b.subtitle, x + 16, y + 8, MILITARY["sand"], 9)
