# Create a class 
# Create a constructor for the 6 inputs
#           question
#           choice_a
#           choice_b
#           choice_c
#           choice_d
#           correct_answer
#   create a method to get the user input
#   write the given inputs to the file
# Create another constructor for continuation of the program
#   set a file name where the code will be saved
# Create a method for the main loop to happen
#       use while True
#       ask if the user wants another question or if the user wants to end the program
# Allow the user to know that the code is ready
# Create an object that is the instance of the class
# Call the program

class QuestionItems:
    def __init__(self):
        self.question = ""
        self.choice_a = ""
        self.choice_b = ""
        self.choice_c = ""
        self.choice_d = ""
        self.correct_answer = ""

    def get_user_input(self):
        self.question = input("Enter your desired question: ").capitalize()
        self.choice_a = input("Enter choice letter a: ")
        self.choice_b = input("Enter choice letter b: ")
        self.choice_c = input("Enter choice letter c: ")
        self.choice_d = input("Enter choice letter d: ")
        self.correct_answer = input("Which letter is correct among the choices a, b, c, and d?: ")

    def write_file(self, file):
        file.write("Question: " + self.question + "\n")
        file.write("a.): " + self.choice_a + "\n")
        file.write("b.): " + self.choice_b + "\n")
        file.write("c.): " + self.choice_c + "\n")
        file.write("d.): " + self.choice_d + "\n")
        file.write("correct answer: " + self.correct_answer + "\n")
        print(" ")

class Assessment:
    def __init__(self):
        self.filename = "Questionnaire.txt"

    def quiz(self):
        with open(self.filename, "a") as file:
            while True:
                question = QuestionItems()
                question.get_user_input()
                question.write_file(file)

                continuity = input("Do you want to add another question? (y/n): ")
                if continuity.lower() != 'y':
                    break

        print("Your question(s) and choice(s) as well as the right answer has been added to the file")
        print("Your questionnaire is now ready!")

test = Assessment()
test.quiz()