"""Capture real native OpenGL frames without opening the production database."""
from pathlib import Path
import argparse
import math
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import arcade
from game import GameWindow, TelaMenu, TelaJogo, TelaSobre
from actors import Jogador
from weapon_art import GunPose, draw_weapon


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--visible', action='store_true')
    args = parser.parse_args()
    output = ROOT / 'docs/evidence/v5-a'
    output.mkdir(parents=True, exist_ok=True)
    window = GameWindow(visible=args.visible)
    window.audio.muted = True
    try:
        menu = TelaMenu()
        window.show_view(menu)
        menu.ui.time = 1
        menu.on_draw()
        arcade.get_image().save(output / 'menu-after.png')
        about = TelaSobre()
        window.show_view(about)
        about.ui.time = 1
        about.on_draw()
        arcade.get_image().save(output / 'about-after.png')
        game = TelaJogo()
        window.show_view(game)
        game.entrance = 0
        game.on_draw()
        arcade.get_image().save(output / 'game-after.png')
        window.clear((36, 40, 32))
        menu.camera.use()
        sprites = arcade.SpriteList()
        poses = []
        for row, kind in enumerate(('glock', 'ak', 'minigun')):
            for col, angle in enumerate((0, .8, math.pi, -1.2)):
                player = Jogador()
                player.position = (col * 240 + 90, 540 - row * 150)
                player.aim_facing = 1 if math.cos(angle) >= 0 else -1
                player.update(0)
                sprites.append(player)
                poses.append(GunPose((player.center_x + 9 * player.aim_facing,
                                      player.center_y + 3), angle, kind))
        sprites.draw(pixelated=True)
        for pose in poses:
            draw_weapon(pose)
            arcade.draw_circle_outline(*pose.muzzle, 3, (255, 190, 70))
            arcade.draw_text(pose.kind, pose.pivot[0] - 35, pose.pivot[1] - 60,
                             (235, 220, 180), 12)
        arcade.get_image().save(output / 'weapons-after.png')
    finally:
        window.close()


if __name__ == '__main__':
    main()
