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


# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_pw():
    # Get entries inputs info
    website = input_website.get()
    try:
        with open("data.json", "r") as f:
            # reading file to get old data as dic
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Website Search",
                            message=f"No info registered yet.")
    else:
        website_check = ""

        for (key, value) in data.items():
            if key == website.capitalize() or key == website.upper() or key == website.lower():
                website_check += f"Email: {data[key]['email']},\nPassword: {data[key]['password']}"
                messagebox.showinfo(title="Website Search",
                                    message=f"Website {key} registered.\n{website_check}\n")
        if len(website_check) == 0:
            messagebox.showinfo(title="Website Search", message="Website not found")

    # Other way tto get values :
    # if website in data:
    #    email = data[website]['email']
    #    password = data[website]['password']
    #    messagebox.showinfo(title="Website Search",
    #                        message=f"Email: {email}.\nPassword: {password}\n")


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
        try:
            # Entries to existing json file
            with open("data.json", "r") as f:
                # reading file to get old data as dic
                data = json.load(f)
        # If file doesn't exists
        except FileNotFoundError:
            with open("data.json", "w") as f:
                # create file
                json.dump(data_json, f, indent=4)
        # Update file with data
        else:
            # update data with adding new data
            data.update(data_json)

            with open("data.json", "w") as f:
                # save data to file
                json.dump(data, f, indent=4)
        # To do anyway
        finally:
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
input_website = Entry(width=35, relief="groove")
input_website.grid(column=1, row=1, columnspan=2, sticky=W)
# Get the cursor to the first input
input_website.focus()

input_email = Entry(width=35, relief="groove")
# Set up the email of the user, index 0 to insert text from the beginning or END to insert from the end
input_email.insert(0, user)
input_email.grid(column=1, row=2, columnspan=2, sticky=W + E)

input_password = Entry(width=35, relief="groove")
input_password.grid(column=1, row=3, sticky=W)

# Buttons
button_search = Button(text="Search", bg="white", width=14, relief="groove", bd=1, command=search_pw)
button_search.grid(column=2, row=1, sticky=E)

button_password = Button(text="Generate Password", bg="white", width=14, relief="groove", bd=1, command=create_password)
button_password.grid(column=2, row=3, sticky=E)

button_add = Button(text="Add", bg="white", bd=1, relief="groove", command=save_entry)
button_add.grid(column=1, row=4, columnspan=2, sticky=W + E)

window.mainloop()
