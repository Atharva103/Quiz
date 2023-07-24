#_______________________________________________________________________________
#Name: Atharva Lokhande
#Purpose: Task
#Task: 5
#Author: atharva
#created: 21-07-23
#_______________________________________________________________________________

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("600x400")

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Berlin", "Paris", "Madrid"],
                "answer": "Paris"
            },
            {
                "question": "What is the largest mammal in the world?",
                "options": ["Elephant", "Blue Whale", "Giraffe", "Lion"],
                "answer": "Blue Whale"
            },
            {
                "question": "What is 2 + 2?",
                "options": ["3", "4", "5", "6"],
                "answer": "4"
            },
            {
                "question": "What is the symbol for water?",
                "options": ["H2O", "CO2", "O2", "NaCl"],
                "answer": "H2O"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Jupiter", "Saturn", "Neptune", "Mars"],
                "answer": "Jupiter"
            },
            {
                "question": "Which famous comet has an orbital period of about 76 years?",
                "options": ["Halley's Comet", "Comet McNaught", "Comet ISON", "Comet Hale-Bopp"],
                "answer": "Halley's Comet"
            },
            {
                "question": "What is the name of the galaxy that contains our solar system?",
                "options": ["Andromeda Galaxy", "Sombrero Galaxy", "Milky Way Galaxy", "Triangulum Galaxy"],
                "answer": "Milky Way Galaxy"
            },
            {
                "question": "What is the first planet in our solar system?",
                "options": ["Mercury", "Venus", "Earth", "Mars"],
                "answer": "Mercury"
            },
        ]

        self.current_question = 0
        self.score = 0

        self.label_welcome = tk.Label(root, text="Welcome to the Quiz Game!", font=("Arial", 20, "bold"), pady=10)
        self.label_rules = tk.Label(root, text="Rules:\nAnswer the following questions by selecting the correct option.", font=("Arial", 12))

        self.start_button = tk.Button(root, text="Start Quiz", command=self.start_quiz, font=("Arial", 14, "bold"), bg="blue", fg="white")

        self.label_welcome.pack()
        self.label_rules.pack(pady=10)
        self.start_button.pack(pady=10)

    def start_quiz(self):
        self.start_button.pack_forget()
        self.label_welcome.pack_forget()
        self.label_rules.pack_forget()
        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=10)
        random.shuffle(self.questions)
        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            question = question_data["question"]
            options = question_data["options"]
            answer = question_data["answer"]

            self.current_question += 1

            question_frame = tk.Frame(self.root)
            question_frame.pack(pady=20)

            label_question = tk.Label(question_frame, text=question, font=("Arial", 16, "bold"), pady=10)
            label_question.pack()

            var_answer = tk.StringVar()
            var_answer.set("")

            for i in range(4):
                radio_option = ttk.Radiobutton(question_frame, text=options[i], variable=var_answer, value=options[i], style="TRadiobutton")
                radio_option.pack(anchor=tk.W, padx=20, pady=5)

            button_submit = tk.Button(question_frame, text="Submit", command=lambda: self.submit_answer(question_frame, var_answer.get(), answer), font=("Arial", 14, "bold"), bg="blue", fg="white")
            button_submit.pack(pady=10)

        else:
            self.show_final_results()

    def submit_answer(self, question_frame, user_answer, correct_answer):
        question_frame.pack_forget()
        feedback_text = ""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            feedback_text = "Correct!"
        else:
            feedback_text = f"Incorrect! The correct answer is: {correct_answer}"
        self.feedback_label.config(text=feedback_text)
        self.load_question()

    def show_final_results(self):
        self.feedback_label.pack_forget()
        final_score_label = tk.Label(self.root, text=f"Your Final Score: {self.score}/{len(self.questions)}", font=("Arial", 16, "bold"), pady=10)
        final_score_label.pack()

        if self.score == len(self.questions):
            message = "Congratulations! You answered all questions correctly."
        else:
            message = "Good effort! Keep practicing to improve your score."

        final_message_label = tk.Label(self.root, text=message, font=("Arial", 12))
        final_message_label.pack(pady=10)

        play_again_button = tk.Button(self.root, text="Play Again", command=self.reset_game, font=("Arial", 14, "bold"), bg="blue", fg="white")
        play_again_button.pack(pady=10)

    def reset_game(self):
        self.current_question = 0
        self.score = 0

        for widget in self.root.winfo_children():
            widget.pack_forget()

        self.label_welcome.pack()
        self.label_rules.pack()
        self.start_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    quiz_game = QuizGame(root)
    root.mainloop()
