import random

def computer(x):
    global Times
    low = 1
    high = x
    feedback = ""
    answer = int(input("Input your number which is right: "))
    Times = 0
    guess = random.randint(1, x)
    print(guess)
    while guess != answer:
        if answer > guess:
            feedback = "l"
            low = guess + 1
            guess = random.randint(low,high)
        elif answer < guess:
            feedback = "h"
            high = guess - 1
            guess = random.randint(low,high)
        Times += 1
        print(guess)


computer(10)
print(f"You didn't get that for {Times} times")

