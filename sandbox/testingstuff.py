def game() -> None:
    global points
    global points
    play: str
    bet: int
    raise_bet: str
    print("You look like somebody who'd enjoy a little gambling. You interested?")
    print(">Yes")
    print(">No")
    play = input("")
    if play == "Yes" or play == "yes":
        print("Well let's get started.")
        roll_dice()
    if play == "No" or play == "no":
        print("Shame to hear. Have a good day.")
        print("GAME OVER")
    if play != "Yes" and play != "yes" and play != "No" and play != "no":
        print("You trying to be funny? I'm not laughing.")
        print("GAME OVER")