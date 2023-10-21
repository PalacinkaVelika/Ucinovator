import random, re
import numexpr as ne
from model.database import Database
from model.task import Task


class QuestionMaker:
    # Vezme si data z XML a zpracuje je třeba do slovníku 
    def __init__(self):
        self.db = Database()

    def generate_questions(self, num_of_questions, test_name):
        questions = self.db.fetch_questions(test_name) #vše z db
        num_of_questions = min(num_of_questions, len(questions)) #Pokud žádáš víc otázek než máme tak dodej maximum
        questions = self.random_questions(num_of_questions, questions) #random výběr
        question_final = []
        #Generace otázky
        for question_name, question_data in questions.items():
            otazka = self.randomizace(question_data)
            question_final.append(otazka)
        return question_final

    #Randomizuje proměnné podle předpisů v jsonu
    def randomizace(self, otazka):
        replacements = {}
        pattern = r'\{(.*?)\}'  # Use single curly braces {} in the pattern
        text = otazka["text"]
        calculation = otazka["answer"]
        
        matches = re.findall(pattern, text) + re.findall(pattern, calculation)
        for match in matches:
            if match in otazka:
                if otazka[match]["type"] == "number":
                    replacement = random.randint(int(otazka[match]["min"]), int(otazka[match]["max"]))
                elif otazka[match]["type"] == "operation":
                    replacement = random.choice(otazka[match]["values"])
                replacements[f"{{{match}}}"] = str(replacement)  # Use double curly braces to match {x}
        for key, value in replacements.items():
            text = text.replace(key, value)
            calculation = calculation.replace(key, value)
        answer = float(ne.evaluate(calculation)) # eval je velký ne e danger zone 
        return Task(text, answer)
                        
    
    def random_questions(self, num_questions, questions):
        question_names = list(questions.keys())
        random.shuffle(question_names)
        selected_questions = {}
        for i in range(num_questions):
            question_name = question_names[i]
            selected_questions[question_name] = questions[question_name]
        return selected_questions