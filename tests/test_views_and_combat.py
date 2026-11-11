import os

os.environ["ARCADE_HEADLESS"] = "1"
os.environ["ALSOFT_DRIVERS"] = "null"
import arcade
import pytest
from game import GameWindow, TelaJogo, Enemy


@pytest.fixture(scope="module")
def window():
    w = GameWindow(visible=False)
    w.audio.muted = True
    yield w
    w.close()


def test_guard_cannot_shoot_backwards_and_has_slow_cadence(window):
    v = TelaJogo()
    window.show_view(v)
    v.enemies.clear()
    v.barrels.clear()
    # Isolate orientation from the new authored cover at x500.
    v.ballistic.clear()
    e = Enemy(520, 130, "guard", 0, 100, 1000)
    e.direction = 1
    e.shot_clock = 0
    v.enemies.append(e)
    v.player.position = (140, 130)
    for _ in range(45):
        v.on_update(1 / 60)
    assert len(v.hostile) == 0
    e.direction = -1
    for _ in range(45):
        v.on_update(1 / 60)
    assert len(v.hostile) == 1
    assert e.shot_clock > 2
    assert max(abs(b.change_x) for b in v.hostile) <= 4


def test_drone_drops_grenades_instead_of_bullets(window):
    v = TelaJogo()
    window.show_view(v)
    v.enemies.clear()
    v.barrels.clear()
    e = Enemy(180, 410, "drone", 0)
    e.shot_clock = 0
    v.enemies.append(e)
    v.player.position = (140, 130)
    for _ in range(60):
        v.on_update(1 / 60)
    assert len(v.hostile) == 0
    assert len(v.grenades) == 1
    g = v.grenades[0]
    assert g.center_y < e.center_y and g.fuse > 0


def test_grenade_lands_warns_and_explodes_only_once(window):
    from combat import Grenade

    v = TelaJogo()
    window.show_view(v)
    g = Grenade(160, 220)
    for _ in range(120):
        if g.grounded:
            break
        assert not g.tick(1 / 60, v.blocks)
    assert g.grounded and g.bottom >= 95 and g.fuse >= 0.8
    explosions = 0
    for _ in range(150):
        explosions += int(g.tick(1 / 60, v.blocks))
    assert explosions == 1


def test_enemy_wont_shoot_through_cover(window):
    # V4: support platforms are transparent to bullets; cover is explicit.
    from combat import Cover

    v = TelaJogo()
    window.show_view(v)
    v.ballistic.append(Cover(270, 96))
    e = Enemy(170, 130, "guard", 0, 100, 240)
    e.direction = 1
    v.player.position = (470, 130)
    assert not e.can_aim(v.player, v.ballistic)


def test_menu_has_reference_structure_and_real_options(window):
    from game import TelaMenu, TelaOpcoes

    m = TelaMenu()
    window.show_view(m)
    assert [b.id for b in m.ui.buttons] == ["play", "instructions", "shop", "options", "about", "exit", "ranking"]
    m.ui.trigger("options")
    for _ in range(100):
        m.on_update(1 / 60)
    assert isinstance(window.current_view, TelaOpcoes)
    options = window.current_view
    old = window.arcade_filter
    options.ui.trigger("crt")
    for _ in range(100):
        options.on_update(1 / 60)
    assert window.arcade_filter != old


def test_menu_button_positions_fully_visible(window):
    from game import TelaMenu, HEIGHT

    m = TelaMenu()
    window.show_view(m)
    from game import WIDTH
    for b in m.ui.buttons:
        x, y, w, h = b.box
        assert 0 <= x < x + w <= WIDTH
        assert 0 <= y < y + h <= HEIGHT
        for other in m.ui.buttons:
            if other is b:
                continue
            ox, oy, ow, oh = other.box
            assert x + w <= ox or ox + ow <= x or y + h <= oy or oy + oh <= y
    m.on_key_press(arcade.key.UP, 0)
    assert m.ui.selection == "ranking"
    m.on_key_press(arcade.key.DOWN, 0)
    assert m.ui.selection == "play"


def test_all_combat_effects_render_with_live_projectiles(window):
    from game import Bullet
    from combat import Grenade

    v = TelaJogo()
    window.show_view(v)
    v.bullets.append(Bullet(210, 180, 12, 3))
    v.bullets.append(Bullet(280, 200, 10, 0, knife=True))
    v.hostile.append(Bullet(480, 210, -3, 0, True))
    v.grenades.append(Grenade(400, 260))
    v.muzzle = 0.05
    v.impact(360, 190)
    v.impact(540, 190, True)
    v.on_draw()
    assert arcade.get_image().size == (960, 640)


def test_v5_player_keeps_hitbox_and_reuses_frames(window):
    from actors import Jogador, player_frames, original_collision_frame
    p, other = Jogador(), Jogador()
    original = arcade.Sprite(original_collision_frame(), scale=0.55)
    assert p.hit_box.points == original.hit_box.points
    assert p.scale == original.scale
    assert p.textura_idle_direita is other.textura_idle_direita is player_frames()[0]
    assert len(p.texturas_andando_direita) == 8


def test_menu_keyboard_actions_and_mouse_bounds(window):
    from game import TelaMenu, TelaInstrucoes
    menu = TelaMenu()
    window.show_view(menu)
    menu.on_key_press(arcade.key.DOWN, 0)
    menu.on_key_press(arcade.key.ENTER, 0)
    for _ in range(100):
        menu.on_update(1 / 60)
    assert isinstance(window.current_view, TelaInstrucoes)


def test_weapon_render_matches_pose_geometry(window, monkeypatch):
    import math
    from weapon_art import GunPose, draw_weapon, MUZZLES
    calls = []
    monkeypatch.setattr(arcade, "draw_texture_rect", lambda tex, rect, **kw: calls.append((tex, rect, kw)))
    for kind in MUZZLES:
        for angle in (0, .8, 2.9, -1.2):
            pose = GunPose((300, 300), angle, kind, recoil=2)
            draw_weapon(pose, hands=False)
            tex, rect, kw = calls[-1]
            # Native Arcade rotates clockwise; map the image muzzle pixel back to world.
            dx = MUZZLES[kind] - (MUZZLES[kind] - 16) / 2
            dy = -1 if math.cos(angle) < 0 else 1
            x = rect.x + dx * math.cos(angle) - dy * math.sin(angle)
            y = rect.y + dx * math.sin(angle) + dy * math.cos(angle)
            assert (x, y) == pytest.approx(pose.muzzle)
            assert kw["angle"] == pytest.approx(-math.degrees(angle))


def test_menu_label_bounds_and_reduced_effects(window, monkeypatch):
    from game import TelaMenu
    from arcade_style import lettering
    menu = TelaMenu()
    window.show_view(menu)
    for b in menu.ui.buttons:
        scale = 2 if len(b.label) > 12 else 3
        tex = lettering(b.label, scale, (224, 210, 170), "plain")
        assert 43 + tex.width <= b.box[2] - 10
        assert tex.height <= b.box[3]
    times = []
    monkeypatch.setattr(menu.scene, "draw", lambda t: times.append(t))
    menu.ui.time = 4
    window.reduced_effects = True
    menu.on_draw()
    assert times == [0]
    window.reduced_effects = False


def test_about_keeps_required_authorship_and_individual_avatar(window, monkeypatch):
    import game
    view = game.TelaSobre()
    window.show_view(view)
    messages = []
    monkeypatch.setattr(game, "center", lambda message, *args, **kwargs: messages.append(message))
    view.on_draw()
    assert any("Vitor" in message for message in messages)
    assert view.avatar.texture.size == (96, 128)
    assert view.avatar.bottom > 365


def test_v5b_ui_assets_preloaded_and_shop_keeps_economy(window, monkeypatch):
    from game import TelaMenu, TelaLoja
    assert {"ammo", "armor", "repair", "crosshair"} <= window.ui_assets.keys()
    shop = TelaLoja(TelaJogo())
    window.show_view(shop)
    wallet = shop.game.run.wallet
    monkeypatch.setattr(arcade, "load_texture", lambda *a, **k: pytest.fail("Texture loaded during draw"))
    shop.ui.time = 1
    shop.on_draw()
    shop.game.draw_hud()
    assert shop.game.run.wallet == wallet
    for b in shop.ui.buttons:
        x, y, w, h = b.box
        assert 0 <= x < x+w <= 960 and 0 <= y < y+h <= 640


def test_v5b_hud_points_tag_does_not_cover_score(window, monkeypatch):
    from arcade_style import lettering
    game = TelaJogo()
    window.show_view(game)
    labels = {}
    monkeypatch.setattr(game.hud, "draw", lambda key, value, x, y, *a: labels.update({key: (value, x, y)}))
    game.draw_hud()
    score_width = lettering("000000", 3, (224, 210, 170), "plain").width
    assert labels["scoretag"][1] >= 20 + score_width + 4
    assert labels["coins"][0] == f"INSIGNIAS {game.collected:02d}/{game.total_coins:02d}"


def test_mine_is_shootable_and_detonates_once(window, monkeypatch):
    from game import Bullet
    from world_fx import Hazard
    game = TelaJogo()
    window.show_view(game)
    game.ballistic.clear()
    game.enemies.clear()
    game.hazards.clear()
    game.shootable_mines.clear()
    mine = Hazard(300, "mine")
    game.hazards.append(mine)
    game.shootable_mines.append(mine)
    explosions = []
    monkeypatch.setattr(game, "explode", lambda *a, **k: explosions.append(a))
    game.bullets.append(Bullet(220, 103, 160, 0))
    game.update_projectiles(1/60)
    assert mine.exploded and mine not in game.hazards and len(explosions) == 1
    assert not mine.tick(2, 3, game.player)


def test_boss_arena_is_clear_and_camera_frames_whole_screen(window):
    from campaign import Campaign
    run = Campaign()
    run.stage = 3
    game = TelaJogo(run)
    window.show_view(game)
    assert game.boss.hp == 460
    assert all(b.right <= 3040 for b in game.blocks if b.bottom > 96)
    game.player.center_x = 3120
    game.on_update(1/60)
    assert game.boss_introduced and game.camera_center() == 3520
    assert list(game.enemies) == [game.boss]


def test_menu_bomb_finishes_before_action(window):
    from game import TelaMenu
    menu = TelaMenu()
    window.show_view(menu)
    calls = []
    menu.ui.buttons[0].action = lambda: calls.append(True)
    menu.ui.trigger("play")
    assert menu.ui.pending[0] == .85
    for _ in range(30):
        menu.on_update(1/60)
    assert menu.ui.shot and not calls
    for _ in range(25):
        menu.on_update(1/60)
    assert calls == [True]


def test_enemy_bullet_speed_gets_exact_point_45_increment(window):
    from game import Enemy
    game = TelaJogo()
    window.show_view(game)
    game.enemies.clear()
    game.ballistic.clear()
    enemy = Enemy(450, 150, "guard", 0, 350, 550)
    enemy.speed = 0
    enemy.direction = -1
    enemy.shot_clock = 0
    game.player.position = (140, 150)
    game.enemies.append(enemy)
    for _ in range(40):
        game.update_enemy_attacks(1/60)
    import math
    bullet = game.hostile[0]
    assert math.hypot(bullet.change_x, bullet.change_y) == pytest.approx(3.45)


def test_insignias_keep_school_points_and_rebalanced_wallet(window):
    game = TelaJogo()
    window.show_view(game)
    game.coins.clear()
    game.enemies.clear()
    game.hazards.clear()
    game.player.position = (200, 130)
    wallet = game.run.wallet
    game.add_coin(200, 130)
    game.on_update(1/60)
    assert game.run.score == 1 and game.run.wallet == wallet + 1
    game.add_coin(*game.player.position, special=True)
    game.on_update(1/60)
    assert game.run.score == 6 and game.run.wallet == wallet + 6


def test_boss_ground_charge_attack_is_telegraphed_and_shootable(window):
    from campaign import Campaign
    run = Campaign()
    run.stage = 3
    game = TelaJogo(run)
    window.show_view(game)
    game.player.position = (3300, 131)
    game.boss_introduced = True
    for enemy in list(game.enemies):
        if enemy is not game.boss:
            enemy.remove_from_sprite_lists()
    boss = game.boss
    boss.direction = -1
    boss.shot_clock = 0
    boss.aim_time = .65
    boss.volley = 3
    before = len(game.shootable_mines)
    game.update_enemy_attacks(1/60)
    assert boss.volley == 4 and len(game.shootable_mines) == before + 3
    assert all(m.fuse == 1.2 for m in list(game.shootable_mines)[-3:])


def test_menu_music_loop_stops_on_navigation(window, monkeypatch):
    from game import TelaMenu, TelaOpcoes
    class Player:
        paused = False
        deleted = False
        def pause(self): self.paused = True
        def delete(self): self.deleted = True
    player = Player()
    calls = []
    monkeypatch.setattr(arcade, "play_sound", lambda *a, **k: (calls.append(k), player)[1])
    window.audio.muted = False
    window.audio.sounds["march"] = object()
    menu = TelaMenu()
    window.show_view(menu)
    assert calls[-1]["loop"] and window.audio.music_player is player
    window.show_view(TelaOpcoes())
    assert player.paused and player.deleted and window.audio.music_player is None
    window.audio.muted = True


def test_enemy_mirrored_frames_are_reused(window):
    from sprite_assets import texture
    assert texture("fighter-walk", .1, flip=True) is texture("fighter-walk", .1, flip=True)
    assert texture("boss", .3, flip=True) is texture("boss", .3, flip=True)


def test_guard_stops_to_aim_with_planted_feet(window):
    from game import Enemy
    from sprite_assets import texture
    game = TelaJogo()
    window.show_view(game)
    guard = Enemy(450, 130, "guard", 0, 300, 600)
    guard.aim_time = .3
    guard.direction = -1
    guard.shot_clock = 1
    old_x = guard.center_x
    guard.tick(1/60, game.player)
    assert guard.center_x == old_x
    assert guard.texture is texture("fighter-aim", guard.anim_age, flip=True)


def test_visible_hostile_sprite_and_rifle_muzzle(window):
    from game import Enemy, Bullet
    from combat import draw_projectile
    from sprite_assets import texture
    game = TelaJogo()
    window.show_view(game)
    guard = Enemy(450, 130, "guard", 0)
    guard.direction = -1
    assert guard.shot_origin == (418, 144)
    alpha = texture("hostile-tracer").image.getchannel("A")
    assert alpha.getextrema()[1] == 255
    calls = []
    import combat
    from unittest.mock import patch
    with patch("sprite_assets.draw", side_effect=lambda *args, **kwargs: calls.append(args)):
        draw_projectile(Bullet(300, 144, -3.45, hostile=True))
    assert calls[0][0] == "hostile-tracer" and calls[0][3:5] == (32, 12)


def test_boss_aim_is_stable_without_camera_shake_or_recoil(window):
    from campaign import Campaign
    run = Campaign()
    run.stage = 3
    game = TelaJogo(run)
    window.show_view(game)
    game.boss_introduced = True
    game.player.position = (3300, 130)
    game.mouse_aim = True
    # Pointer close to body used to flip the pivot based on the previous angle.
    game.mouse = (265, 133)
    game.camera_shake = (4, -4)
    angles = []
    for _ in range(8):
        game.aim()
        angles.append(game.aim_angle)
    assert max(angles) - min(angles) < .00001
    game.fire()
    assert game.recoil == 0


def test_letterbox_mouse_coordinates_match_logical_view(window):
    viewport = window.content_viewport(1920, 1080)
    assert viewport.width == 1620 and viewport.height == 1080
    assert viewport.left == 150
    assert window.logical_mouse(960, 540, viewport) == (480, 320)


def test_scaled_menu_click_reaches_correct_button(window):
    from game import TelaMenu, TelaOpcoes
    window.set_size(1280, 800)
    try:
        menu = TelaMenu()
        window.show_view(menu)
        box = window.content_viewport(window.width, window.height)
        button = next(b for b in menu.ui.buttons if b.id == "options")
        x, y, _, _ = button.box
        menu.on_mouse_press(box.left + (x+20)*box.width/960,
                            box.bottom + (y+20)*box.height/640,
                            arcade.MOUSE_BUTTON_LEFT, 0)
        assert menu.ui.pending
        for _ in range(55):
            menu.on_update(1/60)
        assert isinstance(window.current_view, TelaOpcoes)
        assert window.current_view.camera.viewport == box
    finally:
        window.set_size(960, 640)
        window.fit_view()
