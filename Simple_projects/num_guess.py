# Number guessing game

import random
secret = random.randrange(1, 101)
guess = 0
tries = 0

while guess != secret:
    guess = int( input("Make a guess between 1 and 100: ") )
    tries += 1
    if guess > secret:
        print ("Guess too high")
    elif guess < secret:
        print ("Guess too low")
    else:
        print ("Guess is correct!")

print ("Total number of tries: " + str(tries))