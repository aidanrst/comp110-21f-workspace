"""A Gambling Game."""

__author__ = "730433261"

import time
from random import randint 

DF1: str = '\U00002680'
DF2: str = '\U00002681'
DF3: str = '\U00002682'
DF4: str = '\U00002683'
DF5: str = '\U00002684'
DF6: str = '\U00002685'

print(DF1 + " " + DF2 + " " + DF3 + " " + DF4 + " " + DF5 + " " + DF6)
time.sleep(.2)
print("Get ready to roll!")
points: int = 200
player: str = ""


def main() -> None:
    """Main."""
    greet()
    game()


def greet() -> None:
    """Greets the player."""
    global player
    print("You step off the bus. $100 to your name. Nothing to lose. Well, not much.")
    print("You aren't getting calls back after interviews, you don't have anywhere to go.")
    print("Maybe today will be your lucky day. After all, the flashing neon sign that says \"Win Big!\" wouldn't lie to you, would it?")
    print("You walk in the double doors. The casino matches your money. 200 chips. $200. Not for free of course.")
    print("You do have to pay it back. And if you lose, you have to take out a loan.")
    print("And I don't have to tell you that casinos are not a great place to take loans from.")
    print("As you're considering the choices that led you to this moment, a stranger calls out to you.")
    print("Hey, pal! What do they call you?")
    player = str(input(""))
    print(f"{player}, huh? Wouldn't have named my kid that, but to each their own.")
    print("Seems like a nice guy.")
    print("He continues..")


def game() -> None:
    """Begins the game."""
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
        another_try()
    if play != "Yes" and play != "yes" and play != "No" and play != "no":
        print("You trying to be funny? I'm not laughing.")
        another_try()


def betting() -> int:
    """Estaablishes what the player has to gain and/or lose."""
    print("How much you wanna bet?")
    print(">Enter a number:")
    bet: int = int(input(""))
    if bet <= 0:
        print("You trying to be funny? I'm not laughing.")
        another_try()
    if bet > points:
        print(f"Where's that money coming from, bud? I see you only got {points} chips.")
        print(">Enter a number:")
        bet: int = int(input("")) 
        if bet > points:
            print("You trying to be funny? I'm not laughing.")
            another_try()
    if bet <= (.2 * points) and bet > 0:
        print("Don't be a coward. Let's see you raise that bet.")
        print(">Yes")
        print(">No")
        print(">Walk away")
        raise_bet = input("")
        if raise_bet == "Walk away" or raise_bet == "walk away":
            print("So that's how it's gonna be. Have a good day.")
            another_try()
            quit()
        if raise_bet == "Yes" or raise_bet == "yes":
            bet = int(input("Love to hear it. What's your new bet? "))
            if bet <= 0 or bet > points:
                print("You trying to be funny? I'm not laughing.")
                another_try()
            if bet > (.2 * points) and bet < points:
                print("Alright then. Let's play.")
                return bet
            if bet <= (.2 * points) and bet > 0:
                print("So you're one of those. Whatever. Let's play.")
                return bet
        if raise_bet == "No" or raise_bet == "no":
            print("Heh. Fair enough. I can admire someone who sticks to their guns.")
            return bet
        if raise_bet != "Yes" and raise_bet != "yes" and raise_bet != "No" and raise_bet != "no" and raise_bet != "Walk away" and raise_bet != "walk away":
            print("You trying to be funny? I'm not laughing.")
            another_try()
    if bet == points:
        print("All in, huh? I like your confidence. Wonder if it will pay off.")
        return bet
    if bet > (.2 * points) and bet != points and bet < points: 
        print("Sounds good. Let's play.")
        return bet
    return bet


def roll_dice() -> None:
    """Gambles for the player."""
    global points
    i: int = 0
    roll: int
    player_result: int = 0
    bet = betting()
    runchance: int = (randint(0, 100))
    while i < 6:
        roll = randint(1, 6)
        if roll == 1:
            print(DF1)
        if roll == 2:
            print(DF2)
        if roll == 3:
            print(DF3)
        if roll == 4:
            print(DF4)
        if roll == 5:
            print(DF5)
        if roll == 6:
            print(DF6)
        i = i + 1
        time.sleep(.3)
        player_result = player_result + roll
    if player_result < 18:
        print(f"Only {player_result}, I guess luck isn't on your side.")
    if player_result == 18:
        print(f"{player_result}! Right down the middle. As good odds as any, I guess.")
    if player_result > 18:
        print(f"Someone's lucky. {player_result} is gonna be pretty hard to beat.")
    print("")
    time.sleep(.7)
    print("Well, it's my turn now.")
    time.sleep(.5)
    h: int = 0
    roll2: int 
    opponent_result: int = 0
    while h < 5:
        roll2 = randint(1, 6)
        if roll2 == 1:
            print(DF1)
        if roll2 == 2:
            print(DF2)
        if roll2 == 3:
            print(DF3)
        if roll2 == 4:
            print(DF4)
        if roll2 == 5:
            print(DF5)
        if roll2 == 6:
            print(DF6)
        h = h + 1
        time.sleep(.3)
        opponent_result = opponent_result + roll2
    if opponent_result < player_result:
        if player_result - opponent_result <= 6:
            print("C'mon. I got this.")
        if player_result - opponent_result > 6:
            print("Well. You've already won. Still gonna make me roll this?")
            print("Of course you are.")
    if opponent_result >= player_result:
        print("You know, I don't even need to roll this one, but I'm going to anyway, just for posterity.")
    time.sleep(.3)
    roll2 = randint(1, 6)
    if roll2 == 1:
        print(DF1)
    if roll2 == 2:
        print(DF2)
    if roll2 == 3:
        print(DF3)
    if roll2 == 4:
        print(DF4)
    if roll2 == 5:
        print(DF5)
    if roll2 == 6:
        print(DF6)
    opponent_result = opponent_result + roll2
    if opponent_result > player_result:
        if opponent_result - player_result >= 7:
            print(f"Ha! {opponent_result} to {player_result} - not even close! Hand it over.")
        if opponent_result - player_result < 7 and opponent_result - player_result > 3:
            print(f"{opponent_result} to {player_result}. Not bad, but you still lost.")
        if opponent_result - player_result <= 3:
            print(f"Heh, so close... but not quite. {opponent_result} to {player_result} - I almost feel bad taking from you. Almost.")
        points = points - bet
        print(points)
    if opponent_result < player_result:
        if player_result - opponent_result >= 7:
            print(f"Wow. {opponent_result} to {player_result}. I guess lady luck isn't smiling on me today.")
        if player_result - opponent_result < 7 and player_result - opponent_result > 3:
            print(f"{opponent_result} to {player_result}. Fair game. Here's what you've earned.")
        if player_result - opponent_result <= 3:
            print(f"Agh- so close! {opponent_result} to {player_result} - beat me by the skin of your teeth.")
        points = points + bet
        print(points)
    if opponent_result == player_result:
        print(f"What are the chances! {opponent_result} to {player_result}. Let's try again.")
        roll_dice()
    print("Good game.")
    print("Do you wanna play again?")
    print(">Yes")
    print(">Cash out")
    print(">Run")
    play_again: str = input("")
    if play_again == "yes" or play_again == "Yes":
        print("Love to see it.")
        roll_dice()
    if play_again == "Run" or play_again == "run":
        print("Your quick thinking has bought you valuable time. No one is prepared for your next move.")
        print("But that's by no means a guarantee. They do have measures against this sort of thing. Here goes nothing.")
        time.sleep(1)
        print("...")
        time.sleep(1)
        if runchance <= 35:
            print("You were there, then you weren't. The staff kick themselves for not saving your ID. You're officially an outlaw.")
            print("Nothing to your name, but also no debt. You can build from here, if you so desire.")
            another_try()
        if runchance > 35:
            print("You barely made it 5 steps before they tackled you to the ground.") 
            print("Not only do you have nothing, not only are you in debt, but now you also face jailtime.")
            print("Congratulations")    
            another_try()
    if play_again == "Cash out" or play_again == "cash out":
        if points > 200:
            print(f"Today was your lucky day, you made out with ${points - 100}.")
            another_try()
        if points == 200:
            print(f"You came in with ${points - 100} and you left with ${points - 100}. Nothing gained, nothing lost; but at least you left with your dignity.")
            another_try()
        if points < 200 and points > 100:
            print(f"Well, there's no easy way to put this- you lost. You can still afford to pay back the casino, so that's good, but you're only left with ${points-100}")
            another_try()
        if points == 100:
            print(f"You're left with ${points-100}. Nothing.")
        if points < 100:
            print(f"You've only got {points}. If you leave now, you'll be in debt to the casino. They are not known for their generous interest rates.")
            print("Or..")
            print("You could run. It's a risk- and you'd be left with nothing. But at least you wouldn't be in debt.")
            print(">Yes")
            print(">No")
            run1: str = input("")
            if run1 == "yes" or run1 == "Yes":
                print("You wasted valuable seconds considering your options. Others have noticed the look.")
                print("After all, they are looking out for it. Here goes nothing.")
                time.sleep(1)
                print("...")
                time.sleep(1)
                if runchance <= 10:
                    print("Somehow, you've just barely made it. You've got nothing, but at least you aren't in the negatives.")
                    another_try()
                if runchance > 10:
                    print("You barely made it 5 steps before they tackled you to the ground.") 
                    print("Not only do you have nothing, not only are you in debt, but now you also face jailtime.")
                    print("Congratulations")    
                    another_try()
            if run1 == "no" or run1 == "No":
                print("Probably the wise decision. You kick yourself for even considering the option. You're not the main character here.")
                print("You gambled, you lost, you pay the price.")
                another_try()


def another_try() -> None:
    """Asks the player if they want to try again."""
    print("GAME OVER")
    print("Do you want to try again?")
    global points
    points = 200
    try_again: str = str(input(""))
    if try_again == "yes" or try_again == "Yes":
        main()
    else:
        print(f"Hope you had fun, {player}!")
        exit()


if __name__ == "__main__":
    main()