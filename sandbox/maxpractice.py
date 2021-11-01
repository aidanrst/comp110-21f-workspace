
def main() -> None:
    """Main."""  
    print(max([1, 2, 11, 4, 3, 5, 7, 1, 4, 8, 6]))


def max(input: list[int]) -> int:
    """A function that returns the greatest integer in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    maximum: int = 0
    i: int = 0
    while i < len(input):    
        if maximum < input[i]:
            maximum = input[i]
        i += 1
    return maximum


if __name__ == "__main__":
    main()