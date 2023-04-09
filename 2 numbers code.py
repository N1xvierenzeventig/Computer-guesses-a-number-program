import random

def computer(x):
    global Times
    global answer
    global guess
    low = 1
    high = x
    feedback = ""
    answer = int(input("Input your number which is right: "))
    Times = 1
    Available_guesses = 5
    guess = random.randint(1, x)
    print(guess)
    while guess != answer and Available_guesses != 1:
        if answer > guess:
            feedback = "l"
            low = guess + 1
            Available_guesses -= 1
            guess = random.randint(low,high)
        elif answer < guess:
            feedback = "h"
            high = guess - 1
            Available_guesses -= 1
            guess = random.randint(low,high)
            Times += 1
        print(guess)


computer(199)
if answer == guess:
    print(f"You won and used your chance for {Times} times, congrats!!!")
elif answer != guess:
    print(f"You've lost the game and used your chance for {Times + 1}")
