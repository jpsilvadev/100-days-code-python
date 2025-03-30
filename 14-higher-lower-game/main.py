import random
import os
from game_data import data
from art import logo, vs


score = 0
print(logo)


option_a = random.choice(data)
option_b = random.choice(data)

# avoid duplicate draw
while option_b == option_a:
    option_b = random.choice(data)


while True:
    print(
        f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}"
    )

    print(vs)

    print(
        f"Compare B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}"
    )

    choice = input("Who has more followers? Type 'A' or 'B': ")
    correct_answer = (
        "A" if option_a["follower_count"] > option_b["follower_count"] else "B"
    )

    os.system("clear")
    print(logo)

    option_a = option_b
    option_b = random.choice(data)
    while option_b == option_a:
        option_b = random.choice(data)

    if choice == correct_answer:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break
