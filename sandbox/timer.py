import time
i: float = 1
h: int = 0
while i < 2:
    print(h)
    time.sleep(i)
    h += 1
    i *= .5