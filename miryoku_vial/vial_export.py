"""Assemble a Vial ``.vil`` keymap document from Miryoku layers.

The ``.vil`` format is what Vial's GUI reads/writes via
``File > Load saved keymap`` / ``Download keymap``. Besides the
per-layer ``layout`` grids it carries a handful of other sections
(encoder layout, macros, tap dance, combos, key overrides, tuning
settings) that every Vial keyboard.json reserves a fixed number of
slots for, regardless of whether they're used. We leave those empty/
default here -- Vial ignores unused slots.

Two fields are keyboard/firmware specific and can't be guessed from
this repo alone:

* ``uid``: a 64-bit id baked into the compiled firmware's vial.json,
  used by Vial to check a saved keymap matches the keyboard it's
  loaded onto. Get the real value once from your own board via
  Vial's "Download keymap" and pass it with ``--uid`` (see README).
* ``vial_protocol`` / ``via_protocol``: bumped when Vial/VIA add
  protocol features; 6 and 9 match the Bad Wings V2's current
  (2024-era) vial-qmk fork and are a safe default.
"""

from __future__ import annotations

from .layers import MIRYOKU_LAYERS
from .layout import build_matrix

VIAL_PROTOCOL = 6
VIA_PROTOCOL = 9

# Vial reserves 16 layer slots for encoders/macros regardless of how
# many keymap layers are actually defined.
RESERVED_SLOTS = 16
TAP_DANCE_SLOTS = 32
COMBO_SLOTS = 32
KEY_OVERRIDE_SLOTS = 32


def _empty_tap_dance() -> list[str | int]:
    return ["KC_NO", "KC_NO", "KC_NO", "KC_NO", 200]


def _empty_key_override() -> dict:
    return {
        "trigger": "KC_NO",
        "replacement": "KC_NO",
        "layers": 65535,
        "trigger_mods": 0,
        "negative_mod_mask": 0,
        "suppressed_mods": 0,
        "options": 7,
    }


def build_vial_keymap(uid: int) -> dict:
    """Build the full Vial keymap document, ready to ``json.dump`` to
    a ``.vil`` file.
    """
    layout = [build_matrix(layer) for layer in MIRYOKU_LAYERS]

    return {
        "version": 1,
        "uid": uid,
        "layout": layout,
        "encoder_layout": [[] for _ in range(RESERVED_SLOTS)],
        "layout_options": -1,
        "macro": [[] for _ in range(RESERVED_SLOTS)],
        "vial_protocol": VIAL_PROTOCOL,
        "via_protocol": VIA_PROTOCOL,
        "tap_dance": [_empty_tap_dance() for _ in range(TAP_DANCE_SLOTS)],
        "combo": [["KC_NO"] * 5 for _ in range(COMBO_SLOTS)],
        "key_override": [_empty_key_override() for _ in range(KEY_OVERRIDE_SLOTS)],
        "settings": {},
    }
