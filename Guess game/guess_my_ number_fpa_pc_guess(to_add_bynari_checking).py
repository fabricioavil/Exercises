# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random  

print("\n\n\tWelcome to 'Guess My Number 2'!")
print("\nYou will think of a number between 1 and 100,")
print("and this program will try to guess it in as few attempts as possible.\n")

input("Press enter when you are ready")


# set the initial values
the_number = random.randint(1,100)
print("\nHis first attempt is {0}".format(the_number))
feedback = str(input("Is it correct? (yes | more | less) ").lower())
while not (feedback == "yes" or feedback == "more" or feedback == "less"):
	feedback = str(input("Is it correct? (yes | more | less) ").lower())
tries = 1

# guessing loop
while feedback != "yes":
	if tries < 10:
	    if feedback == "more":
	        tries += 1
	        the_number = random.randint(1,100)
	        print("His next try is:", the_number)
	        feedback = str(input("Is it correct? (yes | more | less) ").lower())
	        while not (feedback == "yes" or feedback == "more" or feedback == "less"):
	        	feedback = str(input("Is it correct? (yes | more | less) ").lower())
	    elif feedback == "less":
	        tries += 1
	        the_number = random.randint(1,100)
	        print("His next try is:", the_number)
	        feedback = str(input("Is it correct? (yes | more | less) ").lower())
	        while not (feedback == "yes" or feedback == "more" or feedback == "less"):
	        	feedback = str(input("Is it correct? (yes | more | less) ").lower())
	else:
		print("\nIt doesn't have more attempt remaining. You won!")
		break
if feedback == "yes":
	print("\nThe program guessed your number! The number was {0}! You lost!".format(the_number))
	print("And it only took", tries, "tries!")
input("\nPress the enter key to exit.")