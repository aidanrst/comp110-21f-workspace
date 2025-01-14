"""Utility functions."""

__author__ = "730433261"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Returns only the first n values of each column."""
    head_dict: dict[str, list[str]] = {}
    for column in column_table:
        if n > len(column_table[column]):
            n = len(column_table[column])
        n_values: list[str] = []
        for i in range(n):
            n_values.append(column_table[column][i])
        head_dict[column] = n_values

    return head_dict


def select(column_table: dict[str, list[str]], columns_list: list[str]) -> dict[str, list[str]]:
    """Returns only a specified subset of columns."""
    select_dict: dict[str, list[str]] = {}
    for column in columns_list:
        select_dict[column] = column_table[column]
        
    return select_dict


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two column-based tables."""
    concat_dict: dict[str, list[str]] = {}
    for column in table_1:
        concat_dict[column] = table_1[column]
    for column in table_2:
        if column not in concat_dict:
            concat_dict[column] = table_2[column]
        else:
            concat_dict[column] += table_2[column]

    return concat_dict


def count(xs: list[str]) -> dict[str, int]:
    """Counts the frequencies of values in a list."""
    count_dict: dict[str, int] = {}
    for value in xs:
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1

    return count_dict