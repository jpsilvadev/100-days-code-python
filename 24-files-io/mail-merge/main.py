with open("./input/names/invited_names.txt", "r") as guests:
    guest_names = guests.read().splitlines()

with open("./input/letters/starting_letter.txt") as template:
    model_template = template.read()

for name in guest_names:
    with open(f"./output/letter_for_{name}.txt", "w") as letter:
        model_name = model_template.replace("[name]", name)
        file = letter.write(model_name)
