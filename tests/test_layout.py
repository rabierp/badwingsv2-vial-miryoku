from miryoku_vial.layout import KEY_POSITIONS, MATRIX_COLS, MATRIX_ROWS, build_matrix


def test_key_positions_are_unique_and_in_bounds():
    assert len(KEY_POSITIONS) == 36
    assert len(set(KEY_POSITIONS)) == 36
    for row, col in KEY_POSITIONS:
        assert 0 <= row < MATRIX_ROWS
        assert 0 <= col < MATRIX_COLS


def test_build_matrix_shape_and_unused_cells():
    keys = [f"KC_{i}" for i in range(36)]
    grid = build_matrix(keys)

    assert len(grid) == MATRIX_ROWS
    assert all(len(row) == MATRIX_COLS for row in grid)

    # These four cells have no switch on the Bad Wings V2 (each half's
    # thumb column only carries 3 of its 5 rows).
    for row, col in [(0, 3), (1, 3), (0, 7), (1, 7)]:
        assert grid[row][col] == -1


def test_build_matrix_places_each_key_at_its_matrix_position():
    keys = [f"KC_{i}" for i in range(36)]
    grid = build_matrix(keys)

    for idx, (row, col) in enumerate(KEY_POSITIONS):
        assert grid[row][col] == f"KC_{idx}"


def test_build_matrix_rejects_wrong_length():
    try:
        build_matrix(["KC_A"])
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for wrong-length key list")
