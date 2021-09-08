"""Practice with if-then-else statements."""

# A < 25, 25 <= B < 50, 50 <= D <= 75, 75 < C

choice: int = int(input("Enter a number: "))

if choice < 50:
    if choice < 25:
        print("A")
    else:
        print("B")
else:
    if choice <= 75:
        print("D")
    else:
        print("C")
# OR
if choice < 25:
    print("A")
else:
    if choice < 50:
        print("B")
    else:
        if choice > 75:
            print("C")
        else:
            print("D")