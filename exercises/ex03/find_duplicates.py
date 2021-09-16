"""Finding duplicate letters in a word."""

__author__ = "730433261"

word: str = str(input("Enter a word: "))

i: int = 0
h: int
result: int = 0

while i < len(word):
    h = i
    while h >= 0:
        h = h - 1
        if word[h] == word[i]:
            result = result + 1  
    i = i + 1

if result > 1:
    print("Found Duplicate: True")
else:
    print("Found Duplicate: False")