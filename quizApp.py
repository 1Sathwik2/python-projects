import tkinter as tk
from tkinter import messagebox

class quizapp:
    def __init__(self):
        #self is used for accessing instance(obj) variables & to distinguish themselves from local,global 
        self.window = tk.Tk()
        self.window.title("Quiz app")
        self.quizinfo = [
           {
              "question": "Which country first landed rover on moon south pole? ", 
              "options": ["India", "USA", "China", "Russia"],
              "correct_option": 0
           },
           {
              "question": "Which airpods am I using? ", 
              "options": ["zebronics", "noise", "boat", "Boult"],
              "correct_option": 2
           },
           {
              "question": "How much money does films generate in India(In in Billion Dollars)? ", 
              "options": ["1", "2", "3", "4"],
              "correct_option": 1
           }
           ]
        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(self.window, text="")
        self.question_label.pack()

        self.options_frame = tk.Frame(self.window)
        self.options_frame.pack()

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.options_frame, text="", width=30, command= lambda i=i : self.check_answer(i))
            button.pack(pady=5) # padding in y-axis
            self.option_buttons.append(button)

        self.next_question_button = tk.Button(self.window, text="Next Question", width=30, command= self.next_question)
        self.next_question_button.pack(pady=10)

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index == len(self.quizinfo):
            messagebox.showinfo("Game Over", "Your Score is "+str(self.score))
            self.window.quit()
        else:
            self.load_question()


    def check_answer(self, chosen_option):
         question_data = self.quizinfo[self.current_question_index]
         answer = question_data["correct_option"]
         if chosen_option == answer:
             self.score = self.score + 1
             messagebox.showinfo("Correct", "Your answer is correct")
         else:
             messagebox.showinfo("Incorrect", "Your answer is Incorrect")

    def load_question(self):
        question_data = self.quizinfo[self.current_question_index]
        self.question_label.config(text = question_data["question"])
        options = question_data["options"]
        for i in range(4):
            self.option_buttons[i].config(text = options[i])
        


        
        

    def run(self):
        self.load_question()
        self.window.mainloop()


quizinstance = quizapp()
quizinstance.run()
