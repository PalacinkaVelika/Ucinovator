from model.gameState import GameState
from model.mark import Mark
from view.consoleControl import ConsoleControl

class SessionData:

    # hlavní práce sem prostě (zpracování dat a tak)
    def __init__(self):
        self.gameState = GameState.STUDENTchoice
        self.studentActive = None
        self.subjectActive = None #test
        self.question_pool = None
        self.question_idx = 0

    def give_mark (self):
        for task in self.subjectActive.tasks_answered:
            max = len(self.subjectActive.tasks_answered)
            score = 0
            if task.correct:
                score += 1
        percentage = (score / max) * 100
        if percentage > 80:
            mark = Mark("1", self.subjectActive.name, "Good job!")
        elif percentage > 60:
            mark = Mark("2", self.subjectActive.name, "Almost perfect, you can do better.")
        elif percentage > 40:
            mark = Mark("3", self.subjectActive.name, "Not bad, but try harder.")
        elif percentage > 20:
            mark = Mark("4", self.subjectActive.name, "You must improve, unless you want to fail the class...")
        else:
            mark = Mark("5", self.subjectActive.name, "You are done. Fired. Do not show your face at the laundry again.")
        self.studentActive.marks.append(mark)

    def end_session(self):
        self.give_mark()
        ConsoleControl.test_statistic(self.subjectActive.tasks_answered, self.studentActive.marks[-1]) 
        self.save_all()

    def save_all(self):
        self.studentActive.save_student()
        self.subjectActive.save_subject()
