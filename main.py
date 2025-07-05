#use to import random module for random word selection
import random

# Predefined word list
words = ["apple", "banana", "grape", "mango", "guava"]
word = random.choice(words)
guessed = ['_'] * len(word)
attempts = 6
guessed_letters = []
# Function to display the current state of the guessed word
print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

while attempts > 0 and '_' in guessed:
    print("Word:", ' '.join(guessed))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct!\n")
    else:
        attempts -= 1
        print(f"Incorrect! You have {attempts} attempts left.\n")

if '_' not in guessed:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("😢 Out of guesses! The word was:", word)
