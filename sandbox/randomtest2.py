"""A random integer test 2."""

from random import randint

rannum: int = int(randint(0, 100))
counter: int = 1
rannum2: int = int(randint(0, 100))
i: int = 0
first: int = 0
second: int = 0
third: int = 0
fourth: int = 0
fifth: int = 0
sixth: int = 0
seventh: int = 0
eighth: int = 0
ninth: int = 0
tenth: int = 0
while i < 10:
    while rannum != rannum2:
        rannum = randint(1, 100)
        # print(str(counter) + " " + str(rannum) + " " + str(rannum2))  
        counter = counter + 1

    percent: float = float(1 / counter * 100)
    percent2: float = float(percent * 100.0)
    percent3: int = int(percent2 // 1)
    percent4: float = float(percent3 / 100)

    print("It took " + str(counter) + (" times to guess the right number, which was " + str(rannum2) + "."))
    print("It guessed right " + str(percent4) + "%" + " of the time.")
    
    if i == 0:
        first: int = counter
        firstp: float = percent4
    if i == 1:
        second: int = counter
        secondp: float = percent4
    if i == 2:
        third: int = counter
        thirdp: float = percent4
    if i == 3:
        fourth: int = counter
        fourthp: float = percent4
    if i == 4:
        fifth: int = counter
        fifthp: float = percent4
    if i == 5:
        sixth: int = counter
        sixthp: float = percent4
    if i == 6:
        seventh: int = counter
        seventhp: float = percent4
    if i == 7:
        eighth: int = counter
        eighthp: float = percent4
    if i == 8:
        ninth: int = counter
        ninthp: float = percent4
    if i == 9:
        tenth: int = counter
        tenthp: float = percent4 
    i = i + 1
    rannum: int = int(randint(0, 100))
    counter: int = 1
    rannum2: int = int(randint(0, 100))

avg: float = float((first + second + third + fourth + fifth + sixth + seventh + eighth + ninth + tenth) / 10)
print(avg)