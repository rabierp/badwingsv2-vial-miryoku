"""Physical/matrix layout of the Bad Wings V2 keyboard.

The Bad Wings V2 (Hazel's Garage) is a 36-key unibody split keyboard
using QMK's community layout ``split_3x5_3`` (3 rows x 5 columns per
half + 3 thumb keys per half). The matrix positions below are taken
verbatim from the upstream QMK keyboard definition
(``keyboards/hazel/bad_wings/keyboard.json``, layout
``LAYOUT_split_3x5_3``), so they match what the real firmware expects.

``KEY_POSITIONS`` lists the 36 logical key slots in the same order as
the ``LAYOUT_split_3x5_3`` macro arguments:

    idx  0- 4: left  finger row 1 (top),    pinky -> inner
    idx  5- 9: right finger row 1 (top),    inner -> pinky
    idx 10-14: left  finger row 2 (home),   pinky -> inner
    idx 15-19: right finger row 2 (home),   inner -> pinky
    idx 20-24: left  finger row 3 (bottom), pinky -> inner
    idx 25-29: right finger row 3 (bottom), inner -> pinky
    idx 30-32: left  thumb cluster,  outer -> inner (closest to center)
    idx 33-35: right thumb cluster,  inner -> outer (closest to center)

Each entry is the ``(matrix_row, matrix_col)`` pair scanned by the
firmware for that slot.
"""

MATRIX_ROWS = 5
MATRIX_COLS = 8

KEY_POSITIONS: list[tuple[int, int]] = [
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
    (4, 4), (3, 4), (2, 4), (1, 4), (0, 4),
    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
    (4, 5), (3, 5), (2, 5), (1, 5), (0, 5),
    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
    (4, 6), (3, 6), (2, 6), (1, 6), (0, 6),
    (2, 3), (3, 3), (4, 3),
    (4, 7), (3, 7), (2, 7),
]

assert len(KEY_POSITIONS) == 36


def build_matrix(keys: list[str]) -> list[list[str | int]]:
    """Place 36 keycodes (in ``KEY_POSITIONS`` order) onto a full
    ``MATRIX_ROWS`` x ``MATRIX_COLS`` grid, filling unused cells with
    ``-1`` the way Vial's ``.vil`` layout arrays expect.
    """
    if len(keys) != len(KEY_POSITIONS):
        raise ValueError(f"expected {len(KEY_POSITIONS)} keys, got {len(keys)}")

    grid: list[list[str | int]] = [[-1] * MATRIX_COLS for _ in range(MATRIX_ROWS)]
    for (row, col), keycode in zip(KEY_POSITIONS, keys):
        grid[row][col] = keycode
    return grid
