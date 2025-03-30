"""Password manager module"""
import json
import random
from tkinter import *
from tkinter import messagebox

import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """Generate user password and automatically copy it to clipboard"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters)
                        for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols)
                        for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers)
                        for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    """Save password to data.txt file"""

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or password == "":
        messagebox.showinfo(title="Password Manager",
                            message="I found empty fields, please fill them out.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new_data dict
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    try:
        with open("data.json", "r") as data_file:
            # reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Password Manager",
                            message="No data file found. Create one by adding a new password.")
    else:
        try:
            messagebox.showinfo(title="Password Manager", message=f"Website: \
{data[website_entry.get()]['email']}\n Password: {data[website_entry.get()]['password']}")
        except KeyError:
            messagebox.showinfo(
                title="Password Manager", message="No details for the website in the data file.")
# ---------------------------- UI SETUP ------------------------------- #


# create root window
root = Tk()
root.title("Password Manager")
root.config(padx=20, pady=20)
# Create canvas
canvas = Canvas(width=150, height=150)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1)

# Create Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Create Entries
website_entry = Entry(width=29)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=3)
email_entry.insert(0, string="youremail@gmail.com")

password_entry = Entry(width=29)
password_entry.grid(row=3, column=1)

# Create Buttons

generate_password = Button(text="Generate Password",
                           width=16, command=generate_password)
generate_password.grid(row=3, column=3)

add = Button(text="Add", width=42, command=save_password)
add.grid(row=4, column=1, columnspan=3)

search = Button(text="Search", width=16, command=find_password)
search.grid(row=1, column=3)

root.mainloop()
