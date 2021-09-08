"""Counting letters in a string."""

__author__ = "730433261"


# Begin your solution here...
letter: str = str(input("What letter do you want to search for?: "))
word: str = str(input("Enter a word: "))

i: int = 0
result: int = 0
while i < len(word):
    if word[i] == letter:
        result = result + 1
    i = i + 1

print("Count: " + str(result))