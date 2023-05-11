import random
from tkinter import *
import pandas
from random import choice
import math

BACKGROUND_COLOR = "#B1DDC6"
timer = None

csv_data = pandas.read_csv("./data/french_words.csv")
data_records = csv_data.to_dict(orient="records")


def turn_card(word):
    card.itemconfig(lang_text, fill="white", text="English")
    card.itemconfig(word_text, fill="white", text=f"{word['English']}")
    card.itemconfig(canvas_image, image=card_back)


def count_down(count, word):
    global timer
    if count > 0:
        timer = window.after(1000, count_down, count - 1, word)
    else:
        turn_card(word)
        window.after_cancel(timer)


def right_click():
    global timer

    new_word = choice(data_records)
    card.itemconfig(lang_text, fill="black",text="French")
    card.itemconfig(word_text, fill="black", text=f"{new_word['French']}")
    card.itemconfig(canvas_image, image=card_front)
    if timer:
        window.after_cancel(timer)
    count_down(3, new_word)


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="./images/card_front.png", width=800, height=526)
card_back = PhotoImage(file="./images/card_back.png", width=800, height=526)
# creating a canvas
card = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas items
canvas_image = card.create_image(410, 263, image=card_front)
lang_text = card.create_text(400, 150, font=("Ariel", 40, "italic"))
word_text = card.create_text(400, 263, font=("Ariel", 60, "bold"))
# placing the canvas in the grid
card.grid(row=0, column=0, columnspan=2)
# cross button
cross_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=cross_image, borderwidth=0, highlightthickness=0, command=right_click)
wrong_button.grid(row=1, column=0)
# right button
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, borderwidth=0, highlightthickness=0, command=right_click)
right_button.grid(row=1, column=1)

right_click()

window.mainloop()
