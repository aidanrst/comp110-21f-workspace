"""An exercise in remainders and boolean logic."""

__author__ = "730433261"


# Begin your solution here...
num: int = int(input("Enter an int: "))

if num % 2 == 0 and num % 7 == 0:
    print("TAR HEELS")
else: 
    if num % 2 == 0:
        print("TAR")
    if num % 7 == 0:
        print("HEELS")
    if num % 2 != 0 and num % 7 != 0:
        print("CAROLINA")