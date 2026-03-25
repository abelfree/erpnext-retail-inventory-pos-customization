def reorder_qty(actual_qty: float, reorder_level: float) -> int:
    return max(int(reorder_level - actual_qty), 1)


def test_reorder_qty():
    assert reorder_qty(3, 10) == 7
    assert reorder_qty(10, 10) == 1
