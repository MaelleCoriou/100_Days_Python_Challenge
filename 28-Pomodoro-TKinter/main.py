from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # after_cancel using the variable timer saving the time when stopped
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
# Function when button clicked start timer

def start_timer():
    """ updates canvas with count_down function """
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # round minutes, keep the first digit until the superior one
    minutes = math.floor(count / 60)
    # get the remaining seconds
    seconds = count % 60
    # Dynamique typing to use str with int
    if seconds < 10:
        seconds = f"0{seconds}"
    # Methode to change canvas text canvas.intemconfig(variable, text=)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        # Execute a command after a time delay in milliseconds ms
        timer = window.after(1000, count_down, count - 1)
    else:
        # Restart timer
        start_timer()
        mark = ""
        # Add check symbols for each work session to check label text
        for turns in range(math.floor(reps / 2)):
            mark += "✔"
        label_check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)

# Actual size of the png image set up
canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(text="start", font=(FONT_NAME, 10, "bold"), bg="white", relief="flat", command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="reset", font=(FONT_NAME, 10, "bold"), bg="white", relief="flat", command=reset_timer)
button_reset.grid(column=2, row=2)

label_timer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=0)

label_check = Label(font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
label_check.grid(column=1, row=2)
window.mainloop()
