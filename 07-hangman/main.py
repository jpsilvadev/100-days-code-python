import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

lives = 6

chosen_word = random.choice(word_list)

display = ["_" for _ in range(len(chosen_word))]

while lives > 0 and "_" in display:
    print(
        f"****************************{lives}/6 LIVES LEFT****************************"
    )
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    if lives == 0:
        print(
            f"***********************IT WAS {chosen_word}! YOU LOSE**********************"
        )
        print(stages[lives])
        break

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    print("".join(display))

    if "_" not in display:
        print("****************************YOU WIN****************************")
    print(stages[lives])
