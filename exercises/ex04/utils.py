"""Exercise 4- List Utility Functions."""

__author__ = "730433261"


def main() -> None:
    """Main."""  
    print(all([1, 1, 1, 1, 1, 1], 1))
    print(all([], 1))
    print(is_equal([3, 4, 4], [3, 4, 4, 1]))
    print(max([1, 2, 11, 4, 3, 5, 7, 1, 4, 8, 6]))


def all(haystack: list[int], needle: int) -> bool:
    """Return True if only needles are found in the haystack, False otherwise."""
    i: int = 0
    if len(haystack) == 0:
        return False

    while i < len(haystack):
        item: int = haystack[i]
        if item != needle:
            return False
        i += 1
    
    return True


def is_equal(butter: list[int], toast: list[int],) -> bool:
    """Return True if only butter and toast are the same, False otherwise."""
    i: int = 0
    a: list[int]
    if len(butter) != len(toast):
        return False
    if len(butter) <= len(toast):
        a = butter
    else:
        a = toast
    while i < len(a):
        spread: int = butter[i]
        bread: int = toast[i]
        if spread != bread:
            return False
        i += 1
    
    return True


def max(input: list[int]) -> int:
    """A function that returns the greatest integer in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    maximum: int = input[i] - 1
    while i < len(input):    
        if maximum < input[i]:
        
            maximum = input[i]
        i += 1
    return maximum


if __name__ == "__main__":
    main()