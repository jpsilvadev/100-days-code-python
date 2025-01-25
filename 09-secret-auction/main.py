import os
from art import logo


def clearscreen():
    os.system("cls" if os.name == "nt" else "clear")


print(logo)
print("Welcome to the secret auction program.")

bids = {}
while True:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    clearscreen()

    if more_bidders != "yes":
        break

_max = float("-inf")
winner = ""


for k, v in bids.items():
    if v > _max:
        _max = v
        winner = k

print(f"The winner is {winner} with a bid of ${_max}.")
