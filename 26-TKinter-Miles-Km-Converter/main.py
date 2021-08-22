from tkinter import *
# GUI program with tkinter


# Function for button clicked
def converter():
    """To get text input when clicking on button
        called by command arg of tkinter.Button(command=function)"""
    # input.get() to save the text entered
    miles = input.get()
    km = round(float(miles) * 1.609344)
    # config the label with new text
    label_result.config(text=km)


# window
window = Tk()
window.title("Mile to km Converter")
window.minsize(width=300, height=150)
# padding
window.config(padx=20, pady=20)

# Entry / Input
input = Entry(width=8)
input.grid(column=1, row=0)


# Label
label_mile = Label(text= "Miles", font= ("Arial", 15, "bold"))
label_mile.grid(column=2, row=0)
label_mile.config(padx=10, pady=10)
label_equal = Label(text="is equal to", font=("Arial", 15, "bold"))
label_equal.grid(column=0, row=1)
label_km = Label(text="Km", font=("Arial", 15, "bold"))
label_km.grid(column=2, row=1)
label_result = Label(text="0", font= ("Arial", 15, "bold"))
label_result.grid(column=1, row=1)

# button
# command= calls the function button_click
button = Button(text="Calculate", font= ("Arial", 10, "bold"), command=converter)
button.grid(column=1, row=2)


# Keep the window open
window.mainloop()