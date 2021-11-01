"""Tests for functions in Exercise 5."""

__author__ = "730433261"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty_list() -> None:
    """A test function that tests an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_only_odds() -> None:
    """A test function that tests a list with only odd items."""
    xs: list[int] = [1, 5, 7, 9, 11]
    assert only_evens(xs) == []


def test_only_evens_repeated_items_and_negatives() -> None:
    """A test function that adds repeated items and negatives into the mix."""
    xs: list[int] = [-6, -5, -4, 0, 1, 2, 2, 5, 7, 8, 8, 9]
    assert only_evens(xs) == [-6, -4, 0, 2, 2, 8, 8]


def test_sub_empty_list() -> None:
    """A test function that tests an empty list."""
    ys: list[int] = list()
    start: int = 2
    end: int = 5
    assert sub(ys, start, end) == []


def test_sub_large_set() -> None:
    """A test function that uses a large set of items."""
    ys: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start: int = 3
    end: int = 9
    assert sub(ys, start, end) == [3, 4, 5, 6, 7, 8]

    
def test_sub_small_set() -> None:
    """A test function that uses a small set of items."""
    ys: list[int] = [5, 2, 4, 8, 14, 24, 3, 3, 2, 77, 35, 5, 6]
    start: int = 4
    end: int = 8
    assert sub(ys, start, end) == [14, 24, 3, 3]


def test_concat_empty_lists() -> None:
    """A test function that tests empty lists."""
    first: list[int] = list()
    second: list[int] = list()
    assert concat(first, second) == []


def test_concat_long_list_with_repeat() -> None:
    """A test function that tests longer lists with repeated items."""
    first: list[int] = [0, 1, 2, 3, 4, 5]
    second: list[int] = [5, 6, 7, 8, 9, 10]
    assert concat(first, second) == [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]


def test_concat_short_list_negatives() -> None:
    """A test function that tests shorter lists that have negatives."""
    first: list[int] = [-5, -7, 2]
    second: list[int] = [0, -2, 9]
    assert concat(first, second) == [-5, -7, 2, 0, -2, 9]