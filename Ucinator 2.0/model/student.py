import json
from model.database import Database

class Student:
    # Osobní údaje, známky a ukládání těch dat někam
    def __init__(self, name, class_name):
        self.name = name
        self.class_name = class_name
        self.marks = []

    def save_student(self):
        mark_data = []
        for mark in self.marks:
            mark_data.append({
                "value": mark.value,
                "subject": mark.subject,
                "description": mark.description
            })

        student_data = {
            "name": self.name,
            "class_name": self.class_name,
            "marks": mark_data  # Include the marks in the student data
        }
        Database().save_student(student_data)