from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageColor
import pandas as pd
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CANVAS_COLOR = "#7a8c96"


class TriviaInterface:

    def __init__(self, quiz_brain: QuizBrain):
        # Call and initialize quiz_brain functions under self.quiz
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=20, bg=THEME_COLOR)

        # Image
        false_img = Image.open("images/false-2.png")
        # Resize the Image using resize method
        false_img = false_img.resize((100, 100), Image.ANTIALIAS)
        false_img = ImageTk.PhotoImage(false_img)

        true_img = Image.open("images/true-2.png")
        # Resize the Image using resize method
        true_img = true_img.resize((100, 100), Image.ANTIALIAS)
        true_img = ImageTk.PhotoImage(true_img)

        # Canvas
        self.canvas = Canvas(width=610, height=320, bg=CANVAS_COLOR, highlightthickness=0)
        self.question_text = self.canvas.create_text(305, 160,
                                                     width=608,
                                                     text="ok",
                                                     font=("Arial", 18, "bold"),
                                                     fill="IVORY")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=10)

        # Button
        self.button_ok = Button(image=true_img, relief="flat", bg=THEME_COLOR, command=self.button_true)
        self.button_ok.grid(column=0, row=3)

        self.button_no = Button(image=false_img, relief="flat", bg=THEME_COLOR, command=self.button_false)
        self.button_no.grid(column=1, row=3)

        # Label
        self.label_score = Label(text="Score:",
                                 bg=THEME_COLOR,
                                 font=("Arial", 12, "bold"),
                                 fg="IVORY")
        self.label_score.grid(column=1, row=0, sticky=W + E, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(self.canvas, bg=CANVAS_COLOR)
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text, text=q_text)
            self.label_score.configure(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}")
        else:
            self.canvas.itemconfigure(self.question_text,
                                      text=f"You've reached the end of the game.\nYour final score is {self.quiz.score}",
                                      justify="center")
            self.button_ok.config(state="disabled")
            self.button_no.config(state="disabled")
            self.label_score.configure(text="")

    def button_true(self):
        answer = self.quiz.check_answer("True")
        self.get_answer(answer)

    def button_false(self):
        answer = self.quiz.check_answer("False")
        self.get_answer(answer)

    def get_answer(self, answer):
        if answer:
            self.canvas.configure(self.canvas, bg="MEDIUMSEAGREEN")
            self.canvas.itemconfigure(self.question_text, text="😀\n\nYou got it right.\nIt's True!")
        else:
            self.canvas.configure(self.canvas, bg="darkorange")
            self.canvas.itemconfigure(self.question_text, text="😩\n\nIt's False!")
        self.window.after(1000, func=self.get_next_question)


