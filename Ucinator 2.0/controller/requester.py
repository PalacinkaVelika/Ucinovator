import numexpr as ne
import re
from view.consoleControl import ConsoleControl
from model.database import Database
from model.task import Task
from model.student import Student
from model.subject import Subject
from model.questionMaker import QuestionMaker
from model.sessionData import SessionData

class Requester:
    # hlavní práce sem prostě (zpracování dat a tak)
    
    def __init__(self):
      self.session = SessionData()
      self.welcome_phase()

    def welcome_phase(self):
        input = ConsoleControl().welcome_phase(Database().fetch_subjects())
        if input == "play":
            self.choose_student(ConsoleControl().student_phase(Database().fetch_students()))
        else:
            self.subject_stats(input)

    def choose_student(self, student):
        if student == "new":
            self.create_student()
        else:
            self.session.studentActive = Student(student["name"], student["class_name"])
            self.choose_subject() # subject phase

    def create_student(self):
        student = ConsoleControl().student_create()
        self.session.studentActive = student
        self.session.studentActive.save_student() # Vytvořil jsem nového, takže ho rovnou uložím
        self.choose_subject() # subject phase

    def choose_subject(self):
        subject = ConsoleControl.subject_phase(Database().fetch_subjects())
        self.session.subjectActive = Subject(subject["name"], subject["teacher"], subject["description"], subject["test_file_name"])
        self.test_phase_init()

    def test_phase_init(self):
        self.session.question_pool = QuestionMaker().generate_questions(5,self.session.subjectActive.test_file_name) #vyrob otázky (jsou rovnou zamíchané takže mohu projíždět po indexech)
        self.test_questioning()
        
    def test_questioning(self):
        #Došly otázky?
        if self.new_question() == None:
            self.session.end_session()
            return
        #User answer
        task = self.session.question_pool[self.session.question_idx-1]
        answer = ConsoleControl.test_phase(task)
        task.student_answer = answer
        task.correct = self.check_answer(answer) 
        self.session.subjectActive.tasks_answered.append(task) #Ulož příklad do session - subject
        self.test_questioning() #další otázka
        

    def new_question(self):
        if self.session.question_idx < len(self.session.question_pool):
            current_question = self.session.question_pool[self.session.question_idx]
            self.session.question_idx += 1 
            return current_question
        else:
            return None  # Došly otázky

    def check_answer(self, answer):
        if self.session.question_idx > 0 and self.session.question_idx <= len(self.session.question_pool):
            correct_answer = self.session.question_pool[self.session.question_idx-1].answer
            try:
                # Attempt to evaluate the input as a mathematical expression
                result = ne.evaluate(answer)
                if result == correct_answer:
                    return True  # Správně
                else:
                    return False  # Špatně
            except Exception as e:
                print("Not a valid number or expression:", e)
                return False
        else:
            return False
    
    # Vyhážu z textu čísla
    def simplify_question(self, question):
        return ''.join(char for char in question if not char.isdigit())
    
    # Vyhážu z textu +-*/
    def remove_symbols(self, question):
        return re.sub(r'[/*\-+]', '', question)
    
    def subject_stats(self, subj):
        question_groups = {}
        #Pro každou otázku
        for task in subj["tasks_answered"]:
            question = task["question"] #Otázka
            simplified_question = self.simplify_question(question) # Odeber čísla
            simplified_question = self.remove_symbols(simplified_question) # Odeber operátory
            correct = "correct" if task["correct"] else "incorrect"     # Jestli je correct True -> dosaď correct jinak incorrect
            if simplified_question in question_groups:
                question_groups[simplified_question].append(correct)
            else:
                question_groups[simplified_question] = [correct]
        for simplified_question, correct_values in question_groups.items():
            # Calculate the percentage of "correct" values
            total_values = len(correct_values)
            if total_values > 0:
                correct_count = correct_values.count("correct")
                percent = (correct_count / total_values) * 100

            print(f"Simplified Question: {simplified_question}")
            print(f"Succes rate: {percent}%")
            print(f"Answers: {correct_values}")




    
            
    

