"""Exercise 06 - Dictionary Functions."""

__author__ = "730433261"


def invert(xs: dict[str, str]) -> dict[str, str]:
    """A function that inverts the keys and the values of a dictionary."""
    inverted: dict[str, str] = dict()
    for key in xs:
        inverted[xs[key]] = key
    if len(inverted) < len(xs):
        raise KeyError("KeyError")
    return inverted


def favorite_color(ys: dict[str, str]) -> str:
    """A function that returns the most frequent string value in a dictionary."""
    color_count: dict[str, int] = dict()
    fav: str = ""
    for key in ys:
        if ys[key] in color_count:
            color_count[ys[key]] += 1
        else:
            color_count[ys[key]] = 1
        if len(color_count) == 1:
            fav = ys[key]
    for key in color_count:
        if color_count[fav] < color_count[key]:
            fav = key
    return fav


def count(zs: list[str]) -> dict[str, int]:
    """A function that returns the frequencies of items in a list."""
    freq: dict[str, int] = dict()
    for item in zs:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1  
    return freq