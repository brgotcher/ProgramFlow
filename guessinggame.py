import random

highest = 10
answer = random.randint(1, highest)
print(answer)   # TODO: remove after testing

guess = ""
print("Please guess number between 1 and {}: ".format(highest))
while guess != answer:
    guess = int(input())
    if guess == 0:
        print("quitter!")
        break
    elif guess == answer:
        print("Correct!")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:   # guess must be greater than answer
            print("Please guess lower")


