"""A random integer test."""

from random import randint

rannum: int = int(randint(0, 100))
counter: int = 1
rannum2: int = int(randint(0, 100))

while rannum != rannum2:
    rannum = randint(1, 100)
    print(str(counter) + " " + str(rannum) + " " + str(rannum2))  
    counter = counter + 1

percent: float = float(1 / counter * 100)
percent2: float = float(percent * 100.0)
percent3: int = int(percent2 // 1)
percent4: float = float(percent3 / 100)

print("It took " + str(counter) + (" times to guess the right number, which was " + str(rannum2) + "."))
print("It guessed right " + str(percent4) + "%" + " of the time.")