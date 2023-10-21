import json
import os

class Database:

    #   Vím moc dobře, že by šlo ze všech fetch funkcí udělat jednu s parametrem, ale jsou zde inteligentní důvody hraničící s genialitou, kvůli kterým to zůstane takto!

    @staticmethod
    def fetch_questions(name):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(script_dir, f'../database/{name}.json')
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    
    @staticmethod
    def fetch_students():
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(script_dir, '../database/students.json')
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
     
    @staticmethod
    def save_student(student_data):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(script_dir, '../database/students.json')
        with open(json_file_path, "r") as json_file:
            students = json.load(json_file)
        existing_student_index = next((index for index, student in enumerate(students) if student["name"] == student_data["name"] and student["class_name"] == student_data["class_name"]), None)
        if existing_student_index is not None:
            existing_student = students[existing_student_index]
            if "marks" in existing_student:
                existing_student["marks"].extend(student_data.get("marks", []))
            else:
                existing_student["marks"] = student_data.get("marks", [])
        else:
            students.append(student_data)
        with open(json_file_path, "w") as json_file:
            json.dump(students, json_file, indent=4)

    @staticmethod
    def fetch_subjects():
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(script_dir, '../database/subjects.json')
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        return data

    @staticmethod
    def save_subject(subject_data):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(script_dir, '../database/subjects.json')
        with open(json_file_path, "r") as json_file:
            subjects = json.load(json_file)
        existing_subject_index = next((index for index, subject in enumerate(subjects) if subject["name"] == subject_data["name"]), None)
        if existing_subject_index is not None:
            existing_subject = subjects[existing_subject_index]
            if "tasks_answered" in existing_subject:
                existing_subject["tasks_answered"].extend(subject_data.get("tasks_answered", []))
            else:
                existing_subject["tasks_answered"] = subject_data.get("tasks_answered", [])
        else:
            subjects.append(subject_data)
        with open(json_file_path, "w") as json_file:
            json.dump(subjects, json_file, indent=4)

