"""An example of a while loop statement."""

counter: float = 1
maximum: float = float(input("Count up to but not including what?"))
while counter < maximum:
    counter_squared: float = counter ** 2.0
    print("The square of " + str(counter) + " is " + str(counter_squared))
    counter = counter + 1 / counter

print("Done!")