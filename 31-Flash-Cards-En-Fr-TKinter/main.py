from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from random import choice
import pandas as pd
import os

BACKGROUND_COLOR = "#B1DDC6"
DATA = pd.read_csv("data/french_words.csv")
# Recors to get the value
to_learn = DATA.to_dict(orient="records")
word = {}


# ---------------------------- Flash Card ----------------------------- #


def card():
    """ random choice of word, timer of 4 sec to flip card
        with flip_car() function to get translated word """
    global word, flip_timer, to_learn
    # Doesn't show the translation after clicking
    window.after_cancel(flip_timer)
    word = choice(to_learn)
    canvas.itemconfig(canvas_image, image=img_front)
    canvas.itemconfigure(line_language, text="French", fill="black")
    canvas.itemconfigure(line_word, text=word["French"], fill="black")
    # Updates card to the English translation after 3 sec if no click button
    flip_timer = window.after(4000, func=flip_card)


def ok():
    """Removes known words from to_learn dic when ok button clicked and
        flips another card calling card() function, if to_learn file is
        empty: end() function called"""
    global to_learn, word, flip_timer, DATA
    try:
        to_learn.remove(word)
        new_list = pd.DataFrame(to_learn)
        card()
    except (IndexError, ValueError, AttributeError):
        end()
    finally:
        new_list.to_csv("data/to_learn.csv", sep=",", index=False)


def end():
    """When all words are known, to_learn list updated with Data file, canvas card
        updated with goodbye message"""
    global to_learn, word, flip_timer, DATA

    if len(to_learn) == 0:
        window.after_cancel(flip_timer)
        to_learn = DATA
        os.remove("data/to_learn.csv")
        canvas.itemconfig(canvas_image, image=img_front)
        canvas.itemconfigure(line_language, text="", fill="black")
        canvas.itemconfigure(line_word, text=f"Well done!\nYou know {len(DATA)} words!", font=35, fill="black")


def flip_card():
    """ Gets the English translation of the current card calling word dic variable """
    canvas.itemconfig(canvas_image, image=img_back)
    canvas.itemconfigure(line_language, text="English", fill="white"),
    canvas.itemconfigure(line_word, text=word["English"], fill="white")


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(4000, func=flip_card)

# Image
img_front = Image.open("images/card_front.png")
# Resize the Image using resize method
img_front = img_front.resize((610, 320), Image.ANTIALIAS)
img_front = ImageTk.PhotoImage(img_front)

img_back = Image.open("images/card_back.png")
# Resize the Image using resize method
img_back = img_back.resize((610, 320), Image.ANTIALIAS)
img_back = ImageTk.PhotoImage(img_back)

img_no = Image.open("images/wrong.png")
# Resize the Image using resize method
img_no = img_no.resize((80, 80), Image.ANTIALIAS)
img_no = ImageTk.PhotoImage(img_no)

img_yes = Image.open("images/right.png")
# Resize the Image using resize method
img_yes = img_yes.resize((80, 80), Image.ANTIALIAS)
img_yes = ImageTk.PhotoImage(img_yes)

# Canvas
canvas = Canvas(width=610, height=320)
canvas_image = canvas.create_image(305, 160, image=img_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
line_language = canvas.create_text(305, 70, text="", font=("Arial", 30, "italic"))
line_word = canvas.create_text(305, 200, text="", font=("Arial", 50, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Button / calling end() function
button_ok = Button(image=img_yes, relief="flat", bg=BACKGROUND_COLOR, command=ok)
button_ok.grid(column=0, row=2)
# Button / calling card() function
button_no = Button(image=img_no, relief="flat", bg=BACKGROUND_COLOR, command=card)
button_no.grid(column=1, row=2)

# To have the proper set up when starting the program
card()

window.mainloop()
