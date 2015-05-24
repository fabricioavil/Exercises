# Guess My Number 2
#
# The user picks a random number between 1 and 100
# The program tries to guess it and the user lets
# the program know if the guess is correct or not.

import random  

print("\n\n\tWelcome to 'Guess My Number 2'!")
print("\nYou will think of a number between 1 and 100,")
print("and this program will try to guess it in as few attempts as possible.\n")

input("Press enter when you are ready")


# set the initial values
the_number = random.randint(1,100)
print("\nThe program first attempt is {0}".format(the_number))

feedback = str(input("Is it correct? (yes|no) ").lower())
while not (feedback == "yes" or feedback == "no"):
	feedback = str(input("Is it correct? (yes|no) ").lower())

tries = 1
previous_numbers = []

# guessing loop
while feedback != "yes":
	if tries < 10:
		tries += 1
		the_number = random.randint(1,100)
		while the_number in previous_numbers:
			the_number = random.randint(1,100)
		previous_numbers.append(the_number)
		print("The program next try is:", the_number)
		feedback = str(input("Is it correct? (yes|no) ").lower())
		while not (feedback == "yes" or feedback == "no"):
			feedback = str(input("Is it correct? (yes|no) ").lower())
	else:
		print("\nThe program doesn't have more attempt remaining. You won!")
		break
if feedback == "yes":
	print("\nThe program guessed your number! The number was {0}! You lost!".format(the_number))
	print("And it only took", tries, "tries!")
input("\nPress the enter key to exit.")