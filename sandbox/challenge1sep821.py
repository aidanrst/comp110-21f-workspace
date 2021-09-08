"""Challenge Question #1."""
# A < 25, 25 <= B < 50, 50 <= D < 75, 75 <= C
choice: int = int(input("Enter a number: "))

if choice < 50:
    if choice < 25:
        print("A")
    else:
        print("B")
else:
    if choice < 75:
        print("D")
    else:
        print("C")
