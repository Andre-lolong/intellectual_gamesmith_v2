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