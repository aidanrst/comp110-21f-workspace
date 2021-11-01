# def favorite_color(ys: dict[str, str]) -> str:
#     """Function docstring."""
#     print(ys)
#     color_count: dict[str, int] = dict()
#     cl: list[str] = list()
#     counter: int = 0
#     for key in ys:
#         print(ys[key])
#         cl.append(ys[key])
#     print(counter)
#     print(cl)
#     print(color_count)
#     return "hello"


# def favorite_color(ys: dict[str, str]) -> str:
#     """Function docstring."""
#     print(ys)
#     color_count: dict[str, int] = dict()
#     counter: int = 0
#     for key in ys:
#         for key2 in ys:
#             if ys[key] == ys[key2]:
#                 counter += 1
#             color_count[ys[key]] = counter
#         counter = 0
#     print(counter)
#     print(color_count)
#     fav: str = ""
#     for key in color_count:
#         for key2 in color_count:
#             if color_count[key] != color_count[key2]:
#                 fav = str(key2)
#     print(fav)
#     return "hello"


def favorite_color(ys: dict[str, str]) -> str:
    """Function docstring."""
    print(ys)
    color_count: dict[str, int] = dict()
    counter: int = 0
    for key in ys:
        for key2 in ys:
            if ys[key] == ys[key2]:
                counter += 1
            color_count[ys[key]] = counter
        counter = 0
    print(counter)
    print(color_count)
    fav: str = ""
    for key in color_count:
        for key2 in color_count:
            if color_count[key] < color_count[key2]:
                fav = str(key2)
    print(fav)
    return "hello"


favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Carc": "red", "Czri": "yellow", "Cris": "blue"})
favorite_color({"Marc": "yellow", "Ezri": "red", "Kris": "red", "Carc": "red", "Czri": "yellow", "Cris": "blue"})
favorite_color({"Marc": "yelow", "Ezri": "red", "Kris": "blue", "Carc": "red", "Czri": "yellow", "Cris": "blue"})