"""Examples of using lists in a simple 'game'."""


from random import randint

rolls: list[int] = list()  # constructor like str(10)
counter: int = 0
sum: int = 0
while len(rolls) < 5000:
    while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
        rolls.append(randint(1, 6))

    # print(rolls)

    # Remove an item from the list by its index ("pop")
    rolls.pop(len(rolls) - 1)
    # print(rolls)

    # Sum the values of our rolls!
    i: int = 0
    while i < len(rolls):
        sum = sum + rolls[i]
        i = i + 1
    counter = counter + 1
print(rolls)
print(f"Total score: {sum}")
print(counter)
print(len(rolls))
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)

# # Access an individual item
# print(rolls[0])
# print(rolls[1])

# # Access the length of a list (number of items)
# print(len(rolls))

# # Access the last item of a list
# last_index: int = len(rolls) - 1
# # print(rolls[len(rolls) - 1])
# print(rolls[last_index])