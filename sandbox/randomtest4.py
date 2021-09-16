"""A random integer test 4."""

from random import randint

rannum: int = int(randint(0, 100))
counter: int = 1
rannum2: int = int(randint(0, 100))
i: int = 0
finalcount: int = 0
finalpercent: float = 0.00
attempt: int = 0

while i < 1000000:
    while rannum != rannum2:
        rannum = randint(1, 100) 
        counter = counter + 1

    percent: float = float(1 / counter * 100)
    percent2: float = float(((percent * 100) // 1) / 100)

    i = i + 1

    finalcount = finalcount + counter
    finalpercent = finalpercent + percent2

    rannum: int = int(randint(0, 100))
    counter: int = 1
    rannum2: int = int(randint(0, 100))
    attempt = attempt + 1
    # print(attempt)
finalpercent2: float = float(((finalpercent * 100) // 1) / 100)
print(finalcount)
print(finalpercent2)
avg: float = float(finalcount / 1000000)
avgp: float = float(finalpercent / 1000000)
print(avg)
print(avgp)
print("Done!")