from campaign import Campaign, WEAPONS


def test_requested_arsenal_and_profiles():
    assert set(WEAPONS) == {"glock", "ak", "minigun"}
    g, a, m = (WEAPONS[k] for k in ("glock", "ak", "minigun"))
    assert g.movement > a.movement > m.movement
    assert m.interval < a.interval < g.interval
    assert a.damage > m.damage >= g.damage
    assert m.price > a.price > g.price
    assert a.speed > g.speed and a.spread == 0


def test_upgrades_belong_to_equipped_gun_and_minigun_has_no_rate():
    run = Campaign()
    run.wallet = 5000
    assert run.buy("damage")[0]
    assert run.damage_level == 1
    assert run.buy("ak")[0] and run.damage_level == 0
    assert run.buy("rate")[0]
    assert run.rate_level == 1
    assert run.equip("glock") and run.damage_level == 1 and run.rate_level == 0
    assert run.buy("minigun")[0]
    wallet = run.wallet
    assert not run.buy("rate")[0] and run.wallet == wallet


def test_starting_wallet_cannot_purchase_upgrades_and_prices_grow():
    run = Campaign()
    assert not run.buy("damage")[0]
    run.wallet = 1000
    before = run.price("damage")
    assert run.buy("damage")[0]
    assert run.price("damage") > before


def test_generated_animation_contracts_and_transparency():
    import json
    from pathlib import Path
    from PIL import Image
    base = Path(__file__).resolve().parents[1] / "assets/sprites"
    registry = json.loads((base / "sprites.json").read_text())
    for name, spec in registry.items():
        with Image.open(base / spec.get("file", name + ".png")) as image:
            w, h = spec["size"]
            assert image.mode == "RGBA"
            assert image.size == (w * spec["count"], h)
            if not spec.get("opaque", False):
                assert image.getchannel("A").getextrema()[0] == 0
            for i in range(spec["count"]):
                bbox = image.crop((i*w, 0, (i+1)*w, h)).getchannel("A").getbbox()
                if i in spec.get("empty_frames", []):
                    assert bbox is None
                else:
                    assert bbox, (name, i)
    for name in ("insignia", "mine", "jerrycan", "emitter", "boss", "drone"):
        assert registry[name]["count"] == 8


def test_local_march_and_weapon_audio_are_real_pcm():
    import wave
    from pathlib import Path
    base = Path(__file__).resolve().parents[1] / "assets/audio"
    for name in ("menu-march", "shot-glock", "shot-minigun"):
        with wave.open(str(base / (name + ".wav"))) as sound:
            assert sound.getsampwidth() == 2 and sound.getframerate() == 22050
            assert sound.getnframes() >= 1400
            if name == "menu-march":
                assert sound.getnframes() / sound.getframerate() == 16


def test_fighter_states_have_real_seven_frame_cycles():
    import json
    from pathlib import Path
    registry = json.loads((Path(__file__).resolve().parents[1] / "assets/sprites/sprites.json").read_text())
    for state in ("idle", "walk", "aim", "fire"):
        assert registry["fighter-" + state]["count"] == 7
