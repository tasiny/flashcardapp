from tkinter import *
from tkinter import messagebox
import pandas
import random
import time

# Constants
BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("french_words.csv")
FONT = ("Arial", 24, "bold")
# Syntax for grabbing a word: data["English"][0] == "part"


def timer(count):
    if count > 0:
        window.after(1000, timer, count - 1)
    elif count == 0:
        # my_label.config(text=data["English"][random_number], font=FONT)
        my_label.grid(row=0, column=1)


def start_app():
    random_number = random.randint(0, 100)
    my_label.config(text=data["French"][random_number], font=FONT)
    my_label.grid(row=0, column=1)
    timer(2)


# Canvas
window = Tk()
window.title("Flashy")
window.wm_minsize(width=900, height=600)
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
back_img = PhotoImage(file="card_back.png")
front_img = PhotoImage(file="card_front.png")
right_img = PhotoImage(file="right.png")
wrong_img = PhotoImage(file="wrong.png")
canvas = Canvas(highlightthickness=0, width=800, height=530, bg=BACKGROUND_COLOR)
# back_card = canvas.create_image(400, 265, image=back_img)
# BUTTONS
wrong_button = Button(bg=BACKGROUND_COLOR, fg=BACKGROUND_COLOR, image=wrong_img, highlightthickness=0)
wrong_button.grid(padx=60, row=1, column=1, sticky=W)
right_button = Button(command=start_app, bg=BACKGROUND_COLOR, fg=BACKGROUND_COLOR, image=right_img, highlightthickness=0)
right_button.grid(padx=200, row=1, column=1, sticky=E)
canvas_image = canvas.create_image(400, 265, image=front_img)
canvas.grid(row=0, columnspan=2)
my_label = Label()

timer(3)
window.mainloop()
