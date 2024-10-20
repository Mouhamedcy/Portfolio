import tkinter as tk
from tkinter import messagebox
import random

# Liste de questions et réponses
questions = [
    {
        "question": "Quelle est la capitale de la France ?",
        "options": ["A) Paris", "B) Londres", "C) Berlin", "D) Madrid"],
        "answer": "A"
    },
    {
        "question": "Quel est le plus grand océan du monde ?",
        "options": ["A) Atlantique", "B) Indien", "C) Pacifique", "D) Arctique"],
        "answer": "C"
    },
    {
        "question": "Qui a écrit 'Roméo et Juliette' ?",
        "options": ["A) Victor Hugo", "B) William Shakespeare", "C) Charles Dickens", "D) Molière"],
        "answer": "B"
    },
   
]

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Interactif")
        self.score = 0
        self.question_index = 0
        self.time_limit = 10
        self.remaining_time = self.time_limit

        # Widgets de l'interface
        self.question_label = tk.Label(master, text="", wraplength=400)
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()
        self.option_buttons = []
        for _ in range(4):
            button = tk.Radiobutton(master, text="", variable=self.var, value="")
            button.pack(anchor='w')
            self.option_buttons.append(button)

        self.timer_label = tk.Label(master, text="")
        self.timer_label.pack(pady=20)

        self.next_button = tk.Button(master, text="Suivant", command=self.next_question, state="disabled")
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        if self.question_index < len(questions):
            question = questions[self.question_index]
            self.question_label.config(text=question["question"])
            for i, option in enumerate(question["options"]):
                self.option_buttons[i].config(text=option, value=option[0])
            self.var.set(None)
            self.next_button.config(state="disabled")
            self.remaining_time = self.time_limit
            self.update_timer()
        else:
            self.end_quiz()

    def update_timer(self):
        if self.remaining_time > 0:
            self.timer_label.config(text=f"Temps restant : {self.remaining_time} secondes")
            self.remaining_time -= 1
            self.master.after(1000, self.update_timer)
        else:
            self.check_answer()

    def check_answer(self):
        question = questions[self.question_index]
        if self.var.get() == question["answer"]:
            self.score += 1
            messagebox.showinfo("Résultat", "Correct !")
        else:
            messagebox.showinfo("Résultat", f"Incorrect. La bonne réponse était {question['answer']}.")
        self.next_button.config(state="normal")

    def next_question(self):
        self.question_index += 1
        self.load_question()

    def end_quiz(self):
        messagebox.showinfo("Quiz Terminé", f"Votre score final est {self.score} sur {len(questions)}.")
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
