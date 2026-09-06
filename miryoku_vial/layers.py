"""Miryoku layers, adapted for the Bad Wings V2 (36-key split).

Each layer is a flat list of 36 QMK/Vial keycode strings, in the same
slot order as ``miryoku_vial.layout.KEY_POSITIONS``. The non-alpha
layers (Nav, Mouse, Media, Num, Sym, Fun) reproduce the official
Miryoku reference behaviour: content lives on the hand opposite the
thumb key that activates the layer, the "active" hand's other thumb
keys are inert (``KC_NO``), and its home row exposes held modifiers
(GUI/Alt/Ctrl/Shift) so the two layers can be chorded (e.g. Nav + Ctrl
for word-wise navigation).

The base layer uses QWERTY alphas with home row mods (GUI/Alt/Ctrl/
Shift on the pinky/ring/middle/index columns), intended to be typed
with the OS keyboard layout set to "US International" so dead keys
remain available for accented characters. Swap ``BASE_QWERTY_US_INTL``
for another alpha set (e.g. Colemak-DH) to experiment with layouts --
that's a good next exercise for this project.

Thumb layer-tap layout (same on both hands, matches Miryoku's
reference thumb assignment):

    left:  Media/Esc | Nav/Space | Mouse/Tab
    right: Fun/Del    | Num/Bspc  | Sym/Enter
"""

NUM = "KC_NO"

# Layer indices, referenced by the LTn() layer-tap keycodes below.
BASE, NAV, MOUSE, MEDIA, NUMPAD, SYM, FUN = range(7)

LAYER_NAMES = ["Base", "Nav", "Mouse", "Media", "Num", "Sym", "Fun"]

BASE_QWERTY_US_INTL: list[str] = [
    # left top row (pinky -> inner)
    "KC_Q", "KC_W", "KC_E", "KC_R", "KC_T",
    # right top row (inner -> pinky)
    "KC_Y", "KC_U", "KC_I", "KC_O", "KC_P",
    # left home row (pinky -> inner), GACS home row mods
    "LGUI_T(KC_A)", "LALT_T(KC_S)", "LCTL_T(KC_D)", "LSFT_T(KC_F)", "KC_G",
    # right home row (inner -> pinky), mirrored home row mods
    "KC_H", "RSFT_T(KC_J)", "RCTL_T(KC_K)", "RALT_T(KC_L)", "RGUI_T(KC_SCOLON)",
    # left bottom row (pinky -> inner)
    "KC_Z", "KC_X", "KC_C", "KC_V", "KC_B",
    # right bottom row (inner -> pinky)
    "KC_N", "KC_M", "KC_COMMA", "KC_DOT", "KC_SLASH",
    # left thumbs: Media(Esc), Nav(Space), Mouse(Tab)
    "LT3(KC_ESCAPE)", "LT1(KC_SPACE)", "LT2(KC_TAB)",
    # right thumbs: Fun(Del), Num(Bspc), Sym(Enter)
    "LT6(KC_DELETE)", "LT4(KC_BSPACE)", "LT5(KC_ENTER)",
]

NAV_LAYER: list[str] = [
    NUM, NUM, NUM, NUM, NUM,
    "KC_AGIN", "KC_PSTE", "KC_COPY", "KC_CUT", "KC_UNDO",
    "KC_LGUI", "KC_LALT", "KC_LCTRL", "KC_LSHIFT", NUM,
    "KC_CAPSLOCK", "KC_LEFT", "KC_DOWN", "KC_UP", "KC_RIGHT",
    NUM, NUM, NUM, NUM, NUM,
    "KC_INSERT", "KC_HOME", "KC_PGDOWN", "KC_PGUP", "KC_END",
    NUM, NUM, NUM,
    "KC_DELETE", "KC_BSPACE", "KC_ENTER",
]

MOUSE_LAYER: list[str] = [
    NUM, NUM, NUM, NUM, NUM,
    "KC_AGIN", "KC_PSTE", "KC_COPY", "KC_CUT", "KC_UNDO",
    "KC_LGUI", "KC_LALT", "KC_LCTRL", "KC_LSHIFT", NUM,
    NUM, "KC_MS_L", "KC_MS_D", "KC_MS_U", "KC_MS_R",
    NUM, NUM, NUM, NUM, NUM,
    NUM, "KC_WH_L", "KC_WH_D", "KC_WH_U", "KC_WH_R",
    NUM, NUM, NUM,
    "KC_BTN3", "KC_BTN1", "KC_BTN2",
]

MEDIA_LAYER: list[str] = [
    NUM, NUM, NUM, NUM, NUM,
    NUM, NUM, NUM, NUM, NUM,
    "KC_LGUI", "KC_LALT", "KC_LCTRL", "KC_LSHIFT", NUM,
    NUM, "KC_MPRV", "KC_VOLD", "KC_VOLU", "KC_MNXT",
    NUM, NUM, NUM, NUM, NUM,
    NUM, NUM, NUM, NUM, NUM,
    NUM, NUM, NUM,
    "KC_MUTE", "KC_MPLY", "KC_MSTP",
]

NUM_LAYER: list[str] = [
    "KC_LBRACKET", "KC_7", "KC_8", "KC_9", "KC_RBRACKET",
    NUM, NUM, NUM, NUM, NUM,
    "KC_SCOLON", "KC_4", "KC_5", "KC_6", "KC_EQUAL",
    NUM, "KC_RSHIFT", "KC_RCTRL", "KC_RALT", "KC_RGUI",
    "KC_GRAVE", "KC_1", "KC_2", "KC_3", "KC_BSLASH",
    NUM, NUM, NUM, NUM, NUM,
    "KC_DOT", "KC_0", "KC_MINUS",
    NUM, NUM, NUM,
]

SYM_LAYER: list[str] = [
    "LSFT(KC_LBRACKET)", "LSFT(KC_7)", "LSFT(KC_8)", "LSFT(KC_9)", "LSFT(KC_RBRACKET)",
    NUM, NUM, NUM, NUM, NUM,
    "LSFT(KC_SCOLON)", "LSFT(KC_4)", "LSFT(KC_5)", "LSFT(KC_6)", "LSFT(KC_EQUAL)",
    NUM, "KC_RSHIFT", "KC_RCTRL", "KC_RALT", "KC_RGUI",
    "LSFT(KC_GRAVE)", "LSFT(KC_1)", "LSFT(KC_2)", "LSFT(KC_3)", "LSFT(KC_BSLASH)",
    NUM, NUM, NUM, NUM, NUM,
    "LSFT(KC_9)", "LSFT(KC_0)", "LSFT(KC_MINUS)",
    NUM, NUM, NUM,
]

FUN_LAYER: list[str] = [
    "KC_F12", "KC_F7", "KC_F8", "KC_F9", "KC_PSCREEN",
    NUM, NUM, NUM, NUM, NUM,
    "KC_F11", "KC_F4", "KC_F5", "KC_F6", "KC_SCROLLLOCK",
    NUM, "KC_RSHIFT", "KC_RCTRL", "KC_RALT", "KC_RGUI",
    "KC_F10", "KC_F1", "KC_F2", "KC_F3", "KC_PAUSE",
    NUM, NUM, NUM, NUM, NUM,
    NUM, "KC_SPACE", "KC_TAB",
    NUM, NUM, NUM,
]

MIRYOKU_LAYERS: list[list[str]] = [
    BASE_QWERTY_US_INTL,
    NAV_LAYER,
    MOUSE_LAYER,
    MEDIA_LAYER,
    NUM_LAYER,
    SYM_LAYER,
    FUN_LAYER,
]

for _name, _layer in zip(LAYER_NAMES, MIRYOKU_LAYERS):
    assert len(_layer) == 36, f"{_name} layer must have 36 keys, got {len(_layer)}"
