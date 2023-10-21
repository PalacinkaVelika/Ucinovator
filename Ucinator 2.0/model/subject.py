from view.consoleControl import ConsoleControl
from model.database import Database

class Subject:
    def __init__(self, name, teacher, description, test_file_name):
        self.name = name
        self.teacher = teacher
        self.description = description
        self.test_file_name = test_file_name
        self.tasks_answered = []

    def save_subject(self):
        task_data = []
        for task in self.tasks_answered:
            task_data.append({
                "question" : task.question,
                "answer" : task.answer,
                "correct" : task.correct,
                "student_answer" : task.student_answer
            })

        subject_data =  {
            "name": self.name,
            "teacher": self.teacher,
            "description": self.description,
            "test_file_name": self.test_file_name,
            "tasks_answered": task_data
        }
        Database().save_subject(subject_data)