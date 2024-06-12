import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock, Paper, Scissors")
        self.player_choice = tk.StringVar()
        self.player_choice.set("Choose an option")
        self.player_label = tk.Label(self.window, text="Choose an option:")
        self.player_label.pack()
        self.rock_button = tk.Button(self.window, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.pack()
        self.paper_button = tk.Button(self.window, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.pack()
        self.scissors_button = tk.Button(self.window, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.pack()
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()
        self.window.mainloop()

    def play(self, choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        if choice == computer_choice:
            self.result_label.config(text="Tie!")
        elif (choice == "rock" and computer_choice == "scissors") or (choice == "paper" and computer_choice == "rock") or (choice == "scissors" and computer_choice == "paper"):
            self.result_label.config(text="You win!")
        else:
            self.result_label.config(text="You lose!")

RockPaperScissors()