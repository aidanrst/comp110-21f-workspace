"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730433261"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")

fortune: int = int(randint(1, 4))

if fortune < 2:
    print("Your lucky numbers are 04-16-38-10-05-20.")
else:
    if fortune < 3:
        print("Try our new seafood platter for only $5!")
    else:
        if fortune < 4:
            print("Your day will be halfway between the most mediocre and least mediocre days of your life.")
        else:
            print("Your day will be approximately 25% better than you thought it was going to be!")

print("Now, go spread positive vibes!")