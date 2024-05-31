import random

name = input("What is your name? ")
print("Good luck!!", name)

words = ['kritan', 'swikriti', 'saugat', 'python', 'pukar', 'water', 'kriti', 'kiran', 'geeks', 'board']
word = random.choice(words)

print("Guess the characters")

guesses = ''
turns = 12

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print("\nYou win!")
        print("The word is:", word)
        break

    print("\n")

    guess = input("Guess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong!")
        print("You have", turns, "more guesses")

        if turns == 0:
            print("You lose! Better luck next time.")