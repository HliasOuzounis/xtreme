# ---------------- Iterables ---------------- #


def lexicographically_smaller(a, b):
    """
    Check if iterable a is lexicographically smaller than b
    """
    for ai, bi in zip(a, b):
        if ai > bi:
            return False
        if ai < bi:
            return True

    return len(a) <= len(b)