class Task:
    # Má v sobě zadání, výsledek, bool jestli byl dobře splněn(defaultně False), odpověď od studenta
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.correct = False
        self.student_answer = "Unanswered"
