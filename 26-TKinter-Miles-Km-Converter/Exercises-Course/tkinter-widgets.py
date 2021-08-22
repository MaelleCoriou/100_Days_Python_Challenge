from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

#------------------------------------------------------------------------------------#
# Function for button clicked
def button_click():
    """To get text input when clicking on button
        called by command arg of tkinter.Button(command=function)"""
    # input.get() to save the text entered
    new_text = input.get()
    # update and config label with new_text from input
    label.config(text=new_text)

# window
window = Tk()
window.title("Convertisseur")
window.minsize(width=500, height=300)
# padding
window.config(padx=20, pady=20)

# Label
label = Label(text= "Label", font= ("Arial", 24, "bold"))
# .pack() to show the label in the window
# .pack(side="bottom" or "right" or "left" or "top", expand=True or False)
# label.pack()
# .place() to show the label to a precise coordinate
# label.place(y=0, x=0)
# .grid() to show the label with grid info, defined with other widget grids
label.grid(column=0, row=0)
# button.grid(column=1, row=1)
# input.grid(column=2, row=2)
# grid and pack can't be mixed

# # Modify label:
# label["text"] = "New text"
# # or:
# label.config(text="New text")


# button
# command= calls the function button_click
button = Button(text="Ok", command=button_click)
button.grid(column=1, row=1)

new_button = Button(text="New button", command=button_click)
new_button.grid(column=2, row=0)

# Entry / Input
input = Entry(width=10)
input.grid(column=3, row=2)

# Keep the window open
window.mainloop()


