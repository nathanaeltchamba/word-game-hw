import random


def instructions():
    print("See if you can figure out the missing word is in the blanks below. You have 7 guesses!")

instructions()

words = ["hardware", "software", "tuples", "coding", "dictionary", "lists", "march", "library", "june", "certification"]

print(random.choice(words))

word = random.choice(words)



errors_left = 7

guesses = []

done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        
        else:
            print("_", end=" ")

    print("")

    guess = input(f"Allowed Errors Left {errors_left}, Next Guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word:
        errors_left -= 1
        if errors_left == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"You found the word! It was {word}!")
else:
    print(f"Game Over! The word was {word}!")


