"""Tkinter Pomodoro App"""

import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
my_timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global checkmarks
    """Stop the countdown and reset to Timer text"""
    global REPS
    root.after_cancel(my_timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark_label.config(text="", fg=GREEN)
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    """Start the timer"""
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    elif REPS % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    else:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    """Countdown system"""
    global my_timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        my_timer = root.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_runs = math.floor(REPS / 2)
        checkmarks = ""
        for _ in range(work_runs):
            checkmarks += "✔️"
        check_mark_label.config(text=checkmarks, fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
# Create root window
root = Tk()
root.title("Pomodoro")
root.config(padx=50, pady=50, bg=YELLOW)


# Create canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
# Adjusted to 102 to not chop image
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold")
)
canvas.grid(column=1, row=1)


# Create labels --> Timer and ✔️
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

check_mark_label = Label(fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=3)


# Create buttons --> Start and Reset
start_button = Button(text="Start", width=7, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=7, command=reset_timer)
reset_button.grid(column=2, row=2)


root.mainloop()
