import random

highest = 50
answer = random.randint(1, highest)
print(answer)   # TODO: remove after testing

guess = 0
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
            print("Please guess higher or enter '0' to quit")
        else:   # guess must be greater than answer
            print("Please guess lower or enter '0' to quit")

