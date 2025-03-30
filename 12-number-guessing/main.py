import random
from art import logo


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


if difficulty == "easy":
    LIVES = 10
else:
    LIVES = 5

num_to_guess = random.randint(1, 100)

while True:
    print(f"You have {LIVES} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == num_to_guess:
        print(f"You got it! The answer was {num_to_guess}.")
        break
    elif guess < num_to_guess:
        print("Too low.\nGuess again.")
    else:
        print("Too high.\nGuess again.")
    LIVES -= 1
    if LIVES < 1:
        print(f"You've run out of guesses. The number was {num_to_guess}.")
        break
