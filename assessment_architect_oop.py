def quiz():
    with open("Questionnaire.txt", "a") as file:
         while True:
            # ask the question
            question = input("Enter your desired question: ").capitalize()
            # ask four possible answers (a, b, c, d)
            choice_a = input("Enter choice letter a: ")
            choice_b = input("Enter choice letter b: ")
            choice_c = input("Enter choice letter c: ")
            choice_d = input("Enter choice letter d: ")
            # ask the correct answer
            correct = input("Which letter is correct among the choices a, b, c, and d?: ")
            # write the inputs to file
            file.write("Question: " + question + "\n")
            file.write("a.): " + choice_a + "\n")
            file.write("b.): " + choice_b + "\n")
            file.write("c.): " + choice_c + "\n")
            file.write("d.): " + choice_d + "\n")
            file.write("correct answer: " + correct + "\n")
            print(" ")

            continunity = input("Do you want to add another question? (y/n): ")
            if continunity.lower() != "y":
                break       
        
    print("Your question(s) and choice(s) as well as the right answer has been added to the file")
    print("Your questionnaire is now ready!")
        
quiz()

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