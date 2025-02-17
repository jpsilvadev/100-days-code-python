import random
import os
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_card_score(cards):
    # dealt blackjack
    if len(cards) == 2 and sum(cards) == 21:
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Dealer won with blackjack!"
    elif user_score == 0:
        return "You won with blackjack!"
    elif user_score > 21:
        return "Bust. You lose!"
    elif computer_score > 21:
        return "Dealer Bust. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def blackjack():
    print(logo)
    user_cards = []
    computer_cards = []

    user_score = None
    computer_score = None

    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_card_score(user_cards)
        computer_score = calculate_card_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_draw = input("Would you like to draw another card? Type yes or no: ").lower()
            if should_draw == "yes":
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_card_score(computer_cards)



    print(f"Your final hand: {user_cards}")
    print(f"Dealer's final hand: {computer_cards}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type yes or no: ") == "yes":
    os.system("clear")
    blackjack()
    