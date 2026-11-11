"""Capture current native screens and a menu animation without using the real ranking DB."""
from pathlib import Path
import sys
from PIL import Image, ImageDraw
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import arcade
from game import GameWindow, TelaMenu, TelaLoja, TelaJogo
from campaign import Campaign, Weapon
from weapon_art import GunPose, draw_weapon
from actors import Jogador
from sprite_assets import REGISTRY, frames


def main():
    out = ROOT / 'docs/evidence/current'
    out.mkdir(parents=True, exist_ok=True)
    window = GameWindow(visible=True)
    window.audio.muted = True
    def shot(name, view):
        window.show_view(view)
        if hasattr(view, 'ui'):
            view.ui.time = 1
        if isinstance(view, TelaJogo):
            view.entrance = view.banner = 0
        view.on_draw()
        arcade.get_image().save(out / (name + '.png'))
    try:
        menu = TelaMenu()
        shot('menu', menu)
        menu.ui.buttons[0].action = lambda: None
        menu.ui.trigger('play')
        pictures = []
        for i in range(33):
            menu.on_update(1/30)
            menu.on_draw()
            picture = arcade.get_image()
            if i == 12:
                picture.save(out / 'menu-bomb.png')
            picture.thumbnail((640, 427))
            pictures.append(picture.convert('RGB'))
        pictures[0].save(out / 'menu-bomb.gif', save_all=True, append_images=pictures[1:], duration=33, loop=0)
        game = TelaJogo()
        shot('shop-glock', TelaLoja(game))
        shot('jungle', game)
        window.toggle_fullscreen()
        window.dispatch_events()
        window.fit_view()
        assert not game.paused
        game.on_draw()
        arcade.get_image().save(out / 'fullscreen.png')
        box = window.content_viewport(window.width, window.height)
        assert window.logical_mouse(box.x, box.y) == (480, 320)
        assert game.ui_camera.viewport == box
        window.toggle_fullscreen()
        window.dispatch_events()
        window.fit_view()
        assert not window.fullscreen

        from game import Bullet
        for x in (250, 400, 550):
            game.hostile.append(Bullet(x, 180, -3.45, hostile=True))
        shot('hostile-visibility', game)
        game.hostile.clear()
        game.run.wallet = 999
        game.run.buy('minigun')
        shot('shop-minigun', TelaLoja(game))
        run = Campaign()
        run.stage = 2
        foundry = TelaJogo(run)
        foundry.player.position = (650, 150)
        foundry.run.time = 2.45
        for h in foundry.hazards:
            h.tick(0, foundry.run.time, foundry.player)
        shot('laser-base', foundry)
        run = Campaign()
        run.stage = 3
        run.weapons['ak'] = Weapon('ak')
        run.equip('ak')
        boss = TelaJogo(run)
        window.show_view(boss)
        boss.player.position = (3200, 131)
        boss.on_update(1/60)
        shot('boss-arena', boss)
        # Render each real animation in a contact sheet, preserving alpha on dark backdrop.
        names = list(REGISTRY)
        sheet = Image.new('RGB', (960, len(names)*95), (31,36,30))
        d = ImageDraw.Draw(sheet)
        for row, name in enumerate(names):
            d.text((4, row*95), name, fill='white')
            for i, tex in enumerate(frames(name)[:8]):
                im = tex.image.copy()
                im.thumbnail((100, 72), Image.Resampling.NEAREST)
                sheet.paste(im, (i*120+10, row*95+20), im)
        sheet.save(out / 'integrated-sprites.png')
        window.clear((31,36,30))
        menu.camera.use()
        players = arcade.SpriteList()
        poses = []
        import math
        for row, kind in enumerate(('glock','ak','minigun')):
            for col, angle in enumerate((0,.8,math.pi,-1.2)):
                p = Jogador()
                p.position = (90+col*240, 530-row*180)
                p.aim_facing = 1 if math.cos(angle)>=0 else -1
                p.update(0)
                players.append(p)
                poses.append(GunPose((p.center_x+9*p.aim_facing,p.center_y+3),angle,kind))
        players.draw(pixelated=True)
        for pose in poses:
            draw_weapon(pose)
            arcade.draw_circle_outline(*pose.muzzle,3,(255,190,70))
        arcade.get_image().save(out / 'weapons-alignment.png')
        html = '<!doctype html><meta charset="utf-8"><title>Coin Commando — capturas atuais</title><style>body{background:#171d17;color:#e0d2aa;font:18px system-ui;margin:30px}img{max-width:100%;image-rendering:pixelated}</style><h1>Capturas atuais</h1><p>OpenGL nativo. Carteira, projéteis e arena são estados preparados para QA; não representam campanha humana concluída.</p>'
        for filename in ('menu.png', 'shop-glock.png', 'jungle.png', 'fullscreen.png', 'hostile-visibility.png', 'boss-arena.png', 'menu-bomb.gif', 'weapons-alignment.png'):
            html += '<h2>' + filename + '</h2><img src="' + filename + '">'
        (out / 'gallery.html').write_text(html, encoding='utf-8')
    finally:
        window.audio.stop_menu_music()
        window.close()


if __name__ == '__main__':
    main()
