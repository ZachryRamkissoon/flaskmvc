from App.models import Result, Competition
from App.database import db
import csv

def import_results(competition_id, file):
    with open(file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            student_id, score = row
            result = Result(student_id = student_id, competition_id = competition_id, score = float(score))
            db.session.add(result)
    db.session.commit()
    print("Results imported.")

def get_student_results(id):
    return Result.query.filter_by(student_id = id).all()

def get_competition_results(id):
    return Result.query.filter_by(competition_id = id).all()

def get_all_results():
    return Result.query.all()
