import os
from model.student import Student

class ConsoleControl:

    @staticmethod
    def welcome_phase (subjects):
        clear_console()
        print("0 - choose student")
        for num, subject in enumerate(subjects):
            print(f"{num+1} - Stats for {subject['name']} (Teacher: {subject['teacher']})")
        #User input
        while True:
            user_input = input("Select student number: ")
            if user_input.isdigit() and int(user_input) <= len(subjects) and int(user_input) >= 0:
                if int(user_input) == 0:
                    return "play"
                else:
                    return subjects[int(user_input)-1]
            else:
                print("Please write a correct number.")

    @staticmethod
    def student_phase (students):
        clear_console()
        print("0 - New student")
        for num, student in enumerate(students):
            print(f"{num + 1} - {student['name']} {student['class_name']}")
        #User input
        while True:
            user_input = input("Select student number: ")
            if user_input.isdigit() and int(user_input) <= len(students) and int(user_input) >= 0:
                if int(user_input) == 0:
                    return "new"
                else:
                    return students[int(user_input)-1] # Vrať to logic classe ať se o to postará
            else:
                print("Please write a correct number.")
            
    @staticmethod
    def student_create ():
        clear_console()
        name = ""
        class_name = ""
        input_message = "Write student name: "  # Initial input message

        # User input
        while True:
            user_input = input(input_message)
            if user_input != "" and name == "":
                name = user_input
                input_message = "Write student class: "  # Change the input message
            elif user_input != "" and class_name == "":
                class_name = user_input
                return Student(name, class_name)
            else:
                print("Please write a correct input.")

    @staticmethod
    def subject_phase (subjects):
        clear_console()
        for num, subject in enumerate(subjects):
            print(f"{num} - {subject['name']} (Teacher: {subject['teacher']})")
        #User input
        while True:
            user_input = input("Select subject number: ")
            if user_input.isdigit() and int(user_input) <= len(subjects) and int(user_input) >= 0:
                return subjects[int(user_input)] # Vrať to logic classe ať se o to postará
            else:
                print("Please write a correct number.")

    @staticmethod
    def test_phase (question):
        clear_console()
        print(f"Question: {question.question}")
        #User input
        while True:
            user_input = input("Answer: ")
            return user_input
        
    @staticmethod    
    def test_statistic(answers, mark):
        clear_console()
        print("_________________________")
        print("TEST RESULT")
        print("_________________________")
        for task in answers:
            print(f"Question: {task.question}")
            print(f"Student answered: {task.student_answer}")
            print(f"Correct answer: {task.answer}")
            print("[correct]" if task.correct else "[incorrect]")
            print("----------------------------")
        print(f"Mark: {mark.value} ({mark.description})")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')