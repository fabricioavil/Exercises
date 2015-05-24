import random
import string


letters = ["a","b","c","d"]
new = ""

while len(new) < len(letters):
    for i in range(len(letters)):
        a = random.choice(letters)
        if a not in new:
            new += a

print(new)

input("\n\nPress the enter key to exit.")