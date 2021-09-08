"""Repeating a beat in a loop."""

__author__ = "730433261"


# Begin your solution here...
beat: str = str(input("What beat do you want to repeat? ")) + " "
repeat: int = int(input("How many times do you want to repeat it? "))
repeatedbeat: str = ""
i: int = 0

if repeat <= 0:
    print("No beat...")
else:
    while i < repeat:
        repeatedbeat = repeatedbeat + beat
        i = i + 1

print(repeatedbeat)