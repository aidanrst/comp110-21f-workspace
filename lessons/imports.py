"""Examples of importing Python."""


from lessons import helpers

# Alias a module / imported name as another anme
from lessons import helpers as hp

# Import names defined globally in a module
from lessons.helpers import powerful, THE_ANSWER


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))  # or hp.powerful
    print(f"The answer: {hp.THE_ANSWER}")  # or helpers.THE_ANSWER
    print(powerful(2, 4))
    print(THE_ANSWER)


if __name__ == "__main__":
    main()