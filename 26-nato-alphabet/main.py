"""Bravo Delta Sierra"""

import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")


code_dic = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    letters = list(word)
    try:
        result = [code_dic[letter] for letter in letters]
    except KeyError:
        print("Sorry, only letters in the alphabet.")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()
