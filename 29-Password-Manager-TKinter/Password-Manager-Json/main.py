import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

user = "user@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)
    password = "".join(password_list)

    # Shows the password in password field
    input_password.insert(0, password)
    # Automatically copies new password to be pasted somewhere else
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_entry():
    # Get entries inputs info
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()

    # Dic to keep track of empty fields
    inputs = {
        "Website": len(website),
        "Email": len(email),
        "Password": len(password)
    }

    # Dic for json file
    data_json = {
        website: {
            "email": email,
            "password": password
        }
    }

    # Get fields names
    message_error = ""

    for (key, value) in inputs.items():
        if value == 0:
            message_error += f"{key} "

    # Message error if empty field
    if len(message_error) > 0:
        messagebox.showerror(title="Missing Info", message=f"Empty field(s) {message_error}\nPlease check again.")
    else:
        # Entries to json file
        with open("data.json", "w") as f:
            json.dump(data_json, f)
            # Clear entries
            input_website.delete(0, END)
            input_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
# geometry("width_size x height_size + x_position + y_position")
window.geometry("490x370+300+100")
window.config(padx=20, pady=20, bg="white", highlightthickness=0)

# Image Canvas widget
img = PhotoImage(file="logo.png")
canvas = Canvas(height=220, width=220, bg="white", highlightthickness=0)
# 100,100 are coordinates x and y to center image in canvas
canvas.create_image(125, 100, image=img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ", bg="white")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ", bg="white")
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ", bg="white")
password_label.grid(column=0, row=3)

# Input entries
input_website = Entry()
input_website.grid(column=1, row=1, columnspan=2, sticky=W + E)
# Get the cursor to the first input
input_website.focus()

input_email = Entry()
# Set up the email of the user, index 0 to insert text from the beginning or END to insert from the end
input_email.insert(0, user)
input_email.grid(column=1, row=2, columnspan=2, sticky=W + E)

input_password = Entry(width=36)
input_password.grid(column=1, row=3)

# Buttons
button_password = Button(text="Generate Password", bg="white", width=14, relief="flat", command=create_password)
button_password.grid(column=2, row=3, sticky=E)

button_add = Button(text="Add", bg="white", command=save_entry)
button_add.grid(column=1, row=4, columnspan=2, sticky=W + E)

window.mainloop()
