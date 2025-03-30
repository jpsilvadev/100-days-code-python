"""Flash Cards App"""

import random
import time
from tkinter import *

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


def generate_word():
    """Generate a random word to display in flash card"""
    global current_card, flip_timer
    root.after_cancel(flip_timer)
    current_card = random.choice(words_dict)
    card_front.itemconfig(
        card_front_text_word, text=current_card["French"], fill="black"
    )
    card_front.itemconfig(card_front_text_lang, text="French", fill="black")
    card_front.itemconfig(card_front_image, image=card_front_img)
    flip_timer = root.after(3000, func=flip_card)


def flip_card():
    """Flip the card to english"""
    global current_card
    card_front.itemconfig(card_front_text_lang, text="English", fill="white")
    card_front.itemconfig(
        card_front_text_word, text=current_card["English"], fill="white"
    )
    card_front.itemconfig(card_front_image, image=card_back_img)


def knows_card():
    global current_card
    words_dict.remove(current_card)
    dict_to_frame = pd.DataFrame(words_dict)
    dict_to_frame.to_csv("data/words_to_learn.csv", index=False)
    generate_word()


# read in data
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
    words_dict = df.to_dict(orient="records")
else:
    words_dict = df.to_dict(orient="records")


# Create root window
root = Tk()
root.title("Flashly")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = root.after(3000, func=flip_card)


# create canvas
card_front = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_front_image = card_front.create_image(400, 263, image=card_front_img)
card_front.grid(row=0, column=0, columnspan=2)

card_front_text_lang = card_front.create_text(
    400, 150, text="lang", font=("Ariel", 40, "italic")
)

card_front_text_word = card_front.create_text(
    400, 263, text="word", font=("Ariel", 60, "bold")
)

# flip card
card_back_img = PhotoImage(file="images/card_back.png")


# create buttons
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_word)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_image, highlightthickness=0, command=knows_card)
right_button.grid(row=1, column=1)

generate_word()

root.mainloop()
