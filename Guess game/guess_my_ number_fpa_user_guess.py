# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random  

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1, 2)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop
while guess != the_number:
	if tries < 10:
	    if guess < the_number:
	        print("Higher...")
	        tries += 1
	        guess = int(input("Take a guess: "))
	    elif guess > the_number:
	        print("Lower...")
	        tries += 1
	        guess = int(input("Take a guess: "))
	else:
		print("\nYou don't have more attempt remaining.")
		break
if guess == the_number:
	print("\nYou guessed it! The number was {0}!".format(the_number))
	print("And it only took you", tries, "tries!")
input("\nPress the enter key to exit.")