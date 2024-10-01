from App.models import Competition
from App.database import db

def create_competition(admin_id, name, description):
    new_competition = Competition(admin_id = admin_id, name = name, description = description)
    db.session.add(new_competition)
    db.session.commit()
    return new_competition

def get_competition(id):
    return Competition.query.get(id)

def get_competition_by_admin(id):
    return Competition.query.filter_by(admin_id = admin.id).all()

def get_all_competitions():
    return Competition.query.all()

def get_all_competitions_json():
    competitions = Competition.query.all()
    if not competition:
        return []
    competitions = [competition.get_json() for competition in competitions]
    print(competitions)