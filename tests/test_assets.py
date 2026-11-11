from pathlib import Path
import hashlib
from PIL import Image

BASE = Path(__file__).resolve().parents[1]


def test_commando_contract_and_original_preserved():
    with Image.open(BASE / "assets/sprites/player.png") as image:
        assert image.size == (960, 128) and image.mode == "RGBA"
        for i in range(10):
            frame = image.crop((i * 96, 0, (i + 1) * 96, 128))
            assert frame.getbbox() and frame.getpixel((0, 0))[3] == 0
    assert hashlib.sha256((BASE / "assets/player.png").read_bytes()).hexdigest() == (
        "e16e19b6a04f6c45d54b2060a5598a5751b68167ebb27894a91a3e4c00a9f333")


def test_asset_provenance_matches_integrated_bytes():
    import json
    manifest = json.loads((BASE / "assets/sources.json").read_text(encoding="utf-8"))
    for entry in manifest:
        assert entry["permission"] and entry["author"]
        assert hashlib.sha256((BASE / entry["integrated"]).read_bytes()).hexdigest() == entry["sha256"]


def test_crosshair_alpha_has_no_excess_padding():
    with Image.open(BASE / "assets/ui/crosshair.png") as image:
        assert image.mode == "RGBA" and image.size == (20, 20)
        assert image.getchannel("A").getbbox() == (0, 0, 20, 20)


def test_runtime_registry_does_not_depend_on_archived_assets():
    import json
    folder = BASE / "assets/sprites"
    registry = json.loads((folder / "sprites.json").read_text(encoding="utf-8"))
    for name, spec in registry.items():
        image = (folder / spec.get("file", name + ".png")).resolve()
        assert image.is_relative_to(folder.resolve()) and image.is_file()
    assert "beam" not in registry and "bullet" not in registry
