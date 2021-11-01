"""Exercise 05 - More 'list' Utility Functions."""

__author__ = "730433261"


def only_evens(xs: list[int]) -> list[int]:
    """A function that returns the even items in a list."""
    i: int = 0
    evens: list[int] = list()
    while i < len(xs):
        if xs[i] % 2 == 0:
            evens.append(xs[i])
        i += 1
    return evens


def sub(ys: list[int], start: int, end: int) -> list[int]:
    """A function that returns a subset of a list."""
    sublist: list[int] = list()
    if len(ys) == 0 or start >= (len(ys) - 1) or end <= 0 or start >= end:
        return sublist
    if end > len(ys):
        end = len(ys)
    if start < 0:
        start = 0
    i: int = start
    while i < end:
        sublist.append(ys[i])
        i += 1
    return sublist


def concat(first: list[int], second: list[int]) -> list[int]:
    """A function that combines two lists."""
    combo: list[int] = list()
    i: int = 0
    while i < len(first):
        combo.append(first[i])
        i += 1
    h: int = 0
    while h < len(second):
        combo.append(second[h])
        h += 1
    return combo