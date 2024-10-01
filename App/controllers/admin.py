from App.models import Admin
from App.database import db

def create_admin(username, password):
    newuser = Admin(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_admin_by_username(username):
    return Admin.query.filter_by(username=username).first()

def get_admin(id):
    return Admin.query.get(id)

def get_all_admins():
    return Admin.query.all()

def get_all_admins_json():
    users = Admin.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_admin(id, username):
    user = get_admin(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None