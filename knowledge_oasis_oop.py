# My previous assignment which is the assignment 10 is already in OOP so I will just copy that and paste here
# Pseudocode
#CLASS KnowledgeOasis
#  CONSTRUCTOR(root)
#    #SET self.root TO root
#    #SET window title TO "Knowledge Oasis"
#    #LOAD questions FROM "Questionnaire.txt" using load_questions method
#    #SET self.current_question_index TO 0
#    #SET self.score TO 0
#    #CREATE a StringVar called self.user_answer
#    #CREATE a Label called self.feedback_label with empty text and pack it
#
#    #IF no questions loaded
#    #  #SHOW error message "No questions found in the file."
#    #  #DESTROY self.root
#    #  #RETURN
#    #END IF
#
#    #RANDOMIZE the order of questions:
#    #SHUFFLE the self.questions list
#
#    #CREATE a Label called self.question_label with wrapping and left justification and pack it
#    #CREATE an empty list called self.radio_buttons
#    #FOR i FROM 0 TO 3
#    #  #CREATE a Radiobutton
#    #  #SET text to character 'a' + i followed by a parenthesis and space
#    #  #SET variable to self.user_answer
#    #  #SET value to character 'a' + i
#    #  #SET command to self.check_answer
#    #  #ADD the Radiobutton to self.radio_buttons list
#    #  #PACK the Radiobutton with left alignment and padding
#    #END FOR
#
#    #CREATE a Button called self.next_button
#    #  #SET text to "Next Question"
#    #  #SET command to self.next_question
#    #  #SET state to DISABLED
#    #  #PACK the Button with padding
#    #
#    #CALL self.load_current_question()
#
#  METHOD load_questions(filename)
#    #TRY
#    #  #OPEN filename in read mode AS file
#    #  #READ all lines from file into a list called lines
#    #  #CREATE an empty list called questions
#    #  #SET i TO 0
#    #  #WHILE i IS less than the number of lines
#    #    #IF the line at index i STARTS WITH "Question:"
#    #      #EXTRACT the question text
#    #      #EXTRACT answer choice 'a'
#    #      #EXTRACT answer choice 'b'
#    #      #EXTRACT answer choice 'c'
#    #      #EXTRACT answer choice 'd'
#    #      #EXTRACT the correct answer (convert to lowercase)
#    #      #CREATE a dictionary for the question with:
#    #        #"question": question text
#    #        #"choices": a dictionary of choices {'a': choice_a, 'b': choice_b, 'c': choice_c, 'd': choice_d}
#    #        #"correct": correct answer
#    #      #ADD the question dictionary to the questions list
#    #      #INCREMENT i BY 6
#    #    #ELSE
#    #      #INCREMENT i BY 1
#    #    #END IF
#    #  #END WHILE
#    #  #RETURN questions
#    #CATCH FileNotFoundError
#    #  #SHOW error message "The file '{filename}' was not found."
#    #  #RETURN an empty list
#    #CATCH other exceptions AS e
#    #  #SHOW error message "An error occurred while loading questions: {e}"
#    #  #RETURN an empty list
#    #END TRY
#
#  METHOD load_current_question()
#    #IF self.current_question_index IS less than the number of questions
#    #  #GET the question data at self.current_question_index
#    #  #SET the text of self.question_label to the question text
#    #  #GET the list of choices from the question data
#    #  #FOR i FROM 0 TO 3
#    #    #SET the text of the Radiobutton at index i to character 'a' + i followed by a parenthesis and the corresponding choice
#    #    #SET the state of the Radiobutton at index i to NORMAL
#    #  #END FOR
#    #  #SET self.user_answer to None (to deselect any previous choice)
#    #  #SET the text of self.feedback_label to "" (clear previous feedback)
#    #  #SET the state of self.next_button to DISABLED
#    #  #SET the text of self.next_button to "Next Question"
#    #  #SET the command of each Radiobutton to self.check_answer
#    #ELSE
#    #  #CALL self.show_results()
#    #END IF
#
#  METHOD check_answer()
#    #GET the selected answer from self.user_answer
#    #IF a selected answer exists
#    #  #GET the correct answer for the current question
#    #  #IF selected answer IS equal to correct answer
#    #    #SET the text of self.feedback_label to "You are CORRECT! MABUHAY!" with green color
#    #    #INCREMENT self.score
#    #  #ELSE
#    #    #SET the text of self.feedback_label to "I am afraid you are WRONG! The correct answer was: {correct answer}" with red color
#    #  #END IF
#    #  #FOR each button in self.radio_buttons
#    #    #SET the state of the button to DISABLED
#    #    #SET the command of the button to None
#    #  #END FOR
#    #  #SET the state of self.next_button to NORMAL
#    #END IF
#
#  METHOD next_question()
#    #INCREMENT self.current_question_index
#    #CALL self.load_current_question()
#
#  METHOD show_results()
#    #SHOW info message "Quiz Finished" with text "Your final score is: {self.score} / {number of questions}"
#    #DESTROY self.root
#END CLASS
#
#IF the script is run directly
#  #CREATE a main window called root
#  #CREATE an instance of KnowledgeOasis with root
#  #START the Tkinter event loop
#END IF

##### I copied my previous code since it is already in OOP ###
### I fixed the previous mistake, which is the single letter variable ###

import tkinter as tk
from tkinter import messagebox
import random

class KnowledgeOasis:
    def __init__(self, root):
        self.root = root
        self.root.title("Knowledge Oasis")
        self.questions = self.load_questions("Questionnaire.txt")
        self.current_question_index = 0
        self.score = 0
        self.user_answer = tk.StringVar()
        self.feedback_label = tk.Label(root, text="")
        self.feedback_label.pack(pady=5)

        if not self.questions:
            messagebox.showerror("Error", "No questions found in the file.")
            self.root.destroy()
            return
        
        random.shuffle(self.questions)

        self.question_label = tk.Label(root, text="", wraplength=400, justify="left")
        self.question_label.pack(pady=10)

        self.radio_buttons = []
        for i in range(4):
            radio = tk.Radiobutton(root, text="", variable=self.user_answer, value=chr(ord('a') + i), command=self.check_answer)
            self.radio_buttons.append(radio)
            radio.pack(anchor="w", padx=20)

        self.next_button = tk.Button(root, text="Next Question", command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=10)

        self.load_current_question()

    def load_questions(self, filename):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()

            questions = []
            i = 0
            while  i < len(lines):
                if lines[i].startswith("Question:"):
                    question = lines[i].strip().replace("Question: ", "")
                    choice_a = lines[i+1].strip().replace("a.): ", "")
                    choice_b = lines[i+2].strip().replace("b.): ", "")
                    choice_c = lines[i+3].strip().replace("c.): ", "")
                    choice_d = lines[i+4].strip().replace("d.): ", "")
                    correct = lines[i+5].strip().replace("correct answer: ", "").lower()
                    questions.append({
                        "question": question,
                        "choices": {"a": choice_a, "b": choice_b, "c": choice_c, "d": choice_d},
                        "correct": correct
                    })
                    i += 6
                else:
                    i += 1
            return questions
        except FileNotFoundError:
            messagebox.showerror("Error", f"The file '{filename}' was not found.")
            return []
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while loading questions: {str(e)}")
            return []
        
    def load_current_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data["question"])

            choices = list(question_data["choices"].values())
            for i, button in enumerate(self.radio_buttons):
                button.config(text=f"{chr(ord('a') + i)}) {choices[i]}", state=tk.NORMAL)
            self.user_answer.set(None)
            self.feedback_label.config(text="") 
            self.next_button.config(state=tk.DISABLED, text="Next Question", command=self.next_question)
            for button in self.radio_buttons:
                button.config(command=self.check_answer) 
        else:
            self.show_results()

    def check_answer(self):
        selected_answer = self.user_answer.get()
        if selected_answer:
            correct_answer = self.questions[self.current_question_index]["correct"]
            if selected_answer == correct_answer:
                self.feedback_label.config(text="You are CORRECT! MABUHAY!", fg="green")
                self.score += 1
            else:
                self.feedback_label.config(text=f"I am afraid you are WRONG! The correct answer was: {correct_answer}", fg="red")

            for button in self.radio_buttons:
                button.config(state=tk.DISABLED, command=None)

            self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question_index += 1
        self.load_current_question()

    def show_results(self):
        messagebox.showinfo("Quiz Finished", f"Your final score is: {self.score}/{len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = KnowledgeOasis(root)
    root.mainloop()