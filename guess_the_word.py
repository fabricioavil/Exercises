import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

new_game = None

while new_game != "n":
    # pick one word randomly from the sequence
    word = random.choice(WORDS)
    # create a variable to use later to see if the guess is correct

    # start the game
    print(
    """
             Welcome to Guess the WORD!
            
    """
    )
    print("The word has:", len(word) , "letters.\n")

    for i in range(5):
        letter = input("Guess a letter: ")
        while len(letter) > 1 or letter == "":
            letter = input("Guess a letter: ")
        if letter not in word:
            print("The word doesn't have this letter.")
        elif letter in word:
            print("The word has this letter.")
        else:
            print("What did you do? I couldn't find a reason!")
    guess = input("\nWhat is your guess for the word? ")
    if guess == word:
        print("\nThat's it! You guessed it!")
    else:
        print("\nYou didn't accept, the word was:", word)

    new_game = input("\nDo you want to play again? (y|n) ")
    new_game = new_game[0].lower()
    
input("\n\nPress the enter key to exit.")