"""Native V5-B screen evidence; ranking uses an isolated temporary SQLite database."""
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import arcade
from game import (GameWindow, TelaMenu, TelaLoja, TelaJogo, TelaOpcoes,
                  TelaSobre, TelaInstrucoes, TelaRanking, TelaGameOver)
from models import banco, Pontuacao


def main():
    output = ROOT / 'docs/evidence/v5-b'
    output.mkdir(parents=True, exist_ok=True)
    original = banco.database
    with tempfile.TemporaryDirectory() as folder:
        banco.close()
        banco.init(str(Path(folder) / 'ranking.db'))
        banco.connect()
        banco.create_tables([Pontuacao])
        window = GameWindow(visible=True)
        window.audio.muted = True
        try:
            game = TelaJogo()
            for name, view in [('menu', TelaMenu()), ('shop', TelaLoja(game)),
                               ('options', TelaOpcoes()), ('instructions', TelaInstrucoes()),
                               ('about', TelaSobre()), ('ranking-empty', TelaRanking()),
                               ('gameover', TelaGameOver(0, 0))]:
                window.show_view(view)
                view.ui.time = 1
                view.on_draw()
                arcade.get_image().save(output / (name + '.png'))
            window.show_view(game)
            game.entrance = game.banner = 0
            game.mouse_aim = True
            game.mouse = (480, 320)
            game.on_draw()
            arcade.get_image().save(output / 'hud.png')
            game.weapon.ammo -= 1
            assert game.weapon.reload() and game.weapon.reloading
            game.on_draw()
            arcade.get_image().save(output / 'hud-reload.png')
            game.on_key_press(arcade.key.P, 0)
            game.pause_ui.time = 1
            game.on_draw()
            arcade.get_image().save(output / 'pause.png')
        finally:
            window.close()
            banco.close()
            banco.init(original)


if __name__ == '__main__':
    main()
