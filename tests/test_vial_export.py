from miryoku_vial.layers import LAYER_NAMES, MIRYOKU_LAYERS
from miryoku_vial.vial_export import (
    COMBO_SLOTS,
    KEY_OVERRIDE_SLOTS,
    RESERVED_SLOTS,
    TAP_DANCE_SLOTS,
    build_vial_keymap,
)


def test_all_layers_have_36_keys():
    for name, layer in zip(LAYER_NAMES, MIRYOKU_LAYERS):
        assert len(layer) == 36, name


def test_build_vial_keymap_structure():
    keymap = build_vial_keymap(uid=0x1234)

    assert keymap["uid"] == 0x1234
    assert keymap["version"] == 1
    assert len(keymap["layout"]) == len(MIRYOKU_LAYERS)
    for layer_grid in keymap["layout"]:
        assert len(layer_grid) == 5
        assert all(len(row) == 8 for row in layer_grid)

    assert len(keymap["encoder_layout"]) == RESERVED_SLOTS
    assert len(keymap["macro"]) == RESERVED_SLOTS
    assert len(keymap["tap_dance"]) == TAP_DANCE_SLOTS
    assert len(keymap["combo"]) == COMBO_SLOTS
    assert len(keymap["key_override"]) == KEY_OVERRIDE_SLOTS


def test_base_layer_thumb_keys_are_layer_taps():
    base_grid = build_vial_keymap(uid=0)["layout"][0]
    # left thumb cluster sits at matrix rows 2-4, col 3
    assert base_grid[2][3] == "LT3(KC_ESCAPE)"
    assert base_grid[3][3] == "LT1(KC_SPACE)"
    assert base_grid[4][3] == "LT2(KC_TAB)"
    # right thumb cluster sits at matrix rows 2-4, col 7
    assert base_grid[4][7] == "LT6(KC_DELETE)"
    assert base_grid[3][7] == "LT4(KC_BSPACE)"
    assert base_grid[2][7] == "LT5(KC_ENTER)"
