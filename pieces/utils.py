def is_pos_in_bounds(pos: int) -> bool:
    """checks that pos is inside board bounds"""
    if pos < 11:
        return False

    if pos > 88:
        return False

    if pos % 10 > 8:
        return False

    if pos % 10 < 1:
        return False

    return True
