from tkinter import Entry, Button, Label, Tk

FONT = ("Arial", 10, "normal")


def convert_to_km():
    miles_to_km = round(float(miles_input.get()) * 1.609344, 3)
    km_out.config(text=miles_to_km)


# window
root = Tk()
root.title("Miles to Km Converter")
root.minsize(width=250, height=135)
root.config(padx=30, pady=20)

# equals to Label
equality = Label(text="is equal to", font=FONT)
equality.grid(column=0, row=1)
equality.config(padx=10, pady=10)

# Miles and Km labels
miles = Label(text="Miles", font=FONT)
miles.grid(column=2, row=0)
miles.config(padx=20)

km = Label(text="Km", font=FONT)
km.grid(column=2, row=1)
km.config(padx=20)

# Km output label
km_out = Label(text="0", font=FONT)
km_out.config(padx=10, pady=10)
km_out.grid(column=1, row=1)

# Miles Entry widget
miles_input = Entry(width=10, justify="center")
miles_input.grid(column=1, row=0)

# Calculate button
calculate = Button(text="Calculate", command=convert_to_km, font=FONT)
calculate.grid(column=1, row=3)


root.mainloop()
