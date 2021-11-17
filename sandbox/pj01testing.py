p_data: dict[str, list[int]] = {"own_notes": [4, 7, 7, 6, 5], "ls_effective": [7, 6, 7, 7, 6]}


def row_based(xs: dict[str, list[int]]) -> list[dict[str, int]]:
    """DOCSTRING."""
    row_list: list[dict[str, int]] = []
    rows: dict[str, int] = {}
    i: int = 0
    for key in xs:
        for key2 in xs:
            if key2 != key:
                while i < len(xs[key]):
                    rows[key] = xs[key][i]
                    rows[key2] = xs[key2][i]
                    row_list.append(dict(rows))
                    i += 1
    print(row_list)
    return row_list


def filt_high(ys: list[dict[str, int]]) -> list[int]:
    """DOCSTRING."""
    f_list: list[int] = []
    for item in ys:
        if (item["own_notes"]) > 4:
            f_list.append(item["ls_effective"])
    return f_list


def filt_low(ys: list[dict[str, int]]) -> list[int]:
    """DOCSTRING."""
    f_list: list[int] = []
    for item in ys:
        if (item["own_notes"]) <= 4:
            f_list.append(item["ls_effective"])
    return f_list


def average_int(zs: list[int]) -> float:
    """DOCSTRING."""
    total: int = sum(zs)
    average: float = total / len(zs)
    return(average)


print((filt_high(row_based(p_data))))
print((filt_low(row_based(p_data))))