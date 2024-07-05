import random
rn = random.randint(0,100)
Guess = 111
while Guess != rn:
    print()
    Guess = (input("Guess a number 0-100: "))
    if Guess == rn:
        print("You Won!")
        break
    elif Guess == "Give up":
        break
    elif int(Guess) > rn:
        print()
        print("Lower")
    elif int(Guess) < rn:
        print()
        print("Higher")
print("The number was", rn)
