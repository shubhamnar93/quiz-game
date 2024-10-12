THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizzUI:
    def __init__(self,quiz: QuizBrain):
        self.quiz=quiz
        self.window = Tk()
        self.window.title("quizzler")
        self.window.config(pady=20, padx=20)
        self.window.config(bg=THEME_COLOR)

        self.score = 0
        self.score_text = Label(text=f"score:{0}", bg=THEME_COLOR, fg='white', font=("Arial", 20))
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(width=400, height=200)
        self.text = self.canvas.create_text(200, 100, text='', width=350, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=10)

        correct_img = PhotoImage(file='./images/true.png')
        self.correct_button = Button(image=correct_img, highlightthickness=0, command=self.right_clicked)
        self.correct_button.grid(row=2, column=0)


        wrong_img = PhotoImage(file='./images/false.png')
        self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.wrong_clicked)
        self.wrong_button.grid(row=2, column=1)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg='white')

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="The End", font=('Arial',30,'bold'))
            self.correct_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def wrong_clicked(self):
        score=self.quiz.check_answer(user_answer='false')
        if score :
            self.canvas.config(bg='green')
            self.score += 1
            self.score_text.config(text=f'score: {self.score}')
            self.window.after(1000, self.get_question)

        else:
            self.canvas.config(bg='red')
            self.window.after(1000, self.get_question)


    def right_clicked(self):
        score=self.quiz.check_answer(user_answer='true')
        if score:
            self.canvas.config(bg='green')
            self.score += 1
            self.score_text.config(text=f'score: {self.score}')
            self.window.after(1000, self.get_question)

        else:
            self.canvas.config(bg='red')
            self.window.after(1000, self.get_question)





