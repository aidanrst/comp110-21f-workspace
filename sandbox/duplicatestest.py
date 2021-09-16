word: str = str(input("Enter a word: "))
result: int = 0

for a in word:
    for b in word:
        if a == b:
            result = result + 1
print(result)