import random

myNum = random.randint(1, 20)
print("I am thinking a number between 1 to 20")

for guesses in range(1, 6):
    print("Take a guess")
    guess = input()
    check = guess.isnumeric()

    if check == False:
        print("enter integer")

    if int(guess) < myNum:
        print("Your guess is too low")
    elif int(guess) > myNum:
        print("Your guess is too high")
    else:
        break

if int(guess) == myNum:
    print("You guessed right in " + str(guesses) + " guesses")
else:
    print("You are not able to guess in 5 chance")
