"""Tests for functions in Exercise 6."""

__author__ = "730433261"

import pytest

from exercises.ex06.dictionaries import invert, favorite_color, count


def test_invert_empty_dictionary() -> None:
    """A test function that tests an empty dictionary."""
    xs = {}
    assert invert(xs) == {}


def test_invert_unique_values() -> None:
    """A test function that tests a dictionary with unique keys and values."""
    xs = {'race': 'car', 'working': 'hardly', 'did': 'they'}
    assert invert(xs) == {'car': 'race', 'hardly': 'working', 'they': 'did'}


def test_invert_key_error() -> None:
    """A test function that results in a key error."""
    with pytest.raises(KeyError):
        xs = {'a': 'z', 'b': 'z', 'c': 'x'}
        invert(xs)


def test_favorite_color_empty_dictionary() -> None:
    """A test function that tests an empty dictionary."""
    ys = {}
    assert favorite_color(ys) == ""


def test_favorite_color_three_way_tie() -> None:
    """A test function that tests a dictionary with a three way tie."""
    ys = {"Mark": "purple", "Marc": "yellow", "Ezri": "red", "Kris": "red", "Carc": "blue", "Czri": "yellow", "Cris": "blue"}
    assert favorite_color(ys) == "yellow"


def test_favorite_color_red() -> None:
    """A test function that tests a dictionary with red as the most frequent value."""
    ys = {"Marc": "yellow", "Ezri": "red", "Kris": "blue", "Carc": "red", "Czri": "yellow", "Cris": "red"}
    assert favorite_color(ys) == "red"


def test_count_empty_list() -> None:
    """A test function that tests an empty list."""
    zs: list[str] = []
    assert count(zs) == {}


def test_count_long_list() -> None:
    """A test function that tests a long list."""
    zs: list[str] = ["Marc", "yellow", "Ezri", "blue", "Kris", "blue", "Marc", "red", "Ezri", "yellow", "blue", "blue", "Ezri"]
    assert count(zs) == {'Marc': 2, 'yellow': 2, 'Ezri': 3, 'blue': 4, 'Kris': 1, 'red': 1}


def test_count_unique_list() -> None:
    """A test function that tests a list where each value appears only once."""
    zs: list[str] = ["Marc", "yellow", "Ezri", "red", "Kris", "blue", "Mark", "purple", "Ezra", "green", "Chris", "orange"]
    assert count(zs) == {'Marc': 1, 'yellow': 1, 'Ezri': 1, 'red': 1, 'Kris': 1, 'blue': 1, 'Mark': 1, 'purple': 1, 'Ezra': 1, 'green': 1, 'Chris': 1, 'orange': 1}