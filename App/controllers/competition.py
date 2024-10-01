from App.models import Competition
from App.database import db

def create_competition(admin_id, name, date, description, results):
    newCompetition = Competition(admin_id = admin_id, name = name, date = date, description = description, results = results)
    db.session.add(newCompetition)
    db.session.commit()
    return newCompetition

def get_competition(id):
    return Competition.query.get(id)

def get_competition_by_admin(id):
    return Competition.query.filter_by(admin_id = admin.id).all()

