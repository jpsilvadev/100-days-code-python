from art import logo


def caesar(text, shift, direction):
    output_text = ""

    if direction == "decode":
        shift *= -1
    for char in text:
        if char not in alphabet:
            output_text += char
        else:
            shift_char = (alphabet.index(char) + shift) % len(alphabet)
            output_text += alphabet[shift_char]

    return output_text


alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

print(logo)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction not in ["encode", "decode"]:
        print("Choose 'encode' or 'decode' to proceed.")
        break

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    out_text = caesar(text, shift, direction)
    print(f"Here's the {direction}d result: {out_text}")

    if input("Type 'yes' if you want to go again. Otherwise type 'no'\n") != "yes":
        break
