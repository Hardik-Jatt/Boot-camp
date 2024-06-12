import tkinter as tk
from tkinter import messagebox

class Quiz:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quiz")
        self.questions = [
            {"question": "What is the capital of France?", "answers": ["Paris", "London", "Berlin"], "correct": 0},
            {"question": "What is the largest planet in our solar system?", "answers": ["Earth", "Saturn", "Jupiter"], "correct": 2},
            {"question": "What is the smallest country in the world?", "answers": ["Vatican City", "Monaco", "Nauru"], "correct": 0}
        ]
        self.current_question = 0
        self.score = 0
        self.question_label = tk.Label(self.window, text=self.questions[self.current_question]["question"])
        self.question_label.pack()
        self.answer_buttons = []
        for i, answer in enumerate(self.questions[self.current_question]["answers"]):
            button = tk.Button(self.window, text=answer, command=lambda answer=i: self.check_answer(answer))
            button.pack()
            self.answer_buttons.append(button)
        self.next_button = tk.Button(self.window, text="Next", command=self.next_question)
        self.next_button.pack()
        self.window.mainloop()

    def check_answer(self, answer):
        if answer == self.questions[self.current_question]["correct"]:
            self.score += 1
            messagebox.showinfo("Correct", "Correct answer!")
        else:
            messagebox.showerror("Incorrect", "Incorrect answer. The correct answer is " + self.questions[self.current_question]["answers"][self.questions[self.current_question]["correct"]])
        self.next_question()

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question]["question"])
            for i, button in enumerate(self.answer_buttons):
                button.config(text=self.questions[self.current_question]["answers"][i])
        else:
            messagebox.showinfo("Quiz Over", f"Quiz over. Your score is {self.score} out of {len(self.questions)}")

Quiz()