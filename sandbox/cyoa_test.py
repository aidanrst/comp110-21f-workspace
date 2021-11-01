"""project test."""

points: int = 100

# choices are Yes No Walk_Away
raise_bet: str
bet: int = int(input("How much you wanna bet? "))
if bet <= (.2 * points):
    print("Don't be a coward. Let's see you raise that bet.")
    print(">Yes")
    print(">No")
    raise_bet = input("")
    if raise_bet == "Yes" or raise_bet == "yes":
        bet = int(input("Love to hear it. What's your new bet? "))
        if bet <= (.2 * points):
            print("So you're one of those. Whatever. Let's play.")
    if raise_bet == "No" or raise_bet == "no":
        print("Heh. I can admire someone who sticks to their guns.")
    if raise_bet != "Yes" and raise_bet != "yes" and raise_bet != "No" and raise_bet != "no":
        print("You trying to be funny? I'm not laughing.")
if bet == points:
    print("All in, huh? I like your confidence. Wonder if it will pay off.")
if bet >= (.2 * points) and bet != points: 
    print("Sounds good. Let's play.")