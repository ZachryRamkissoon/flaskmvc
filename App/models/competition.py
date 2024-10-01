from App.database import db

class Competition(db.Model):
    competition_id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.admin_id"), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    results = db.relationship('Result', backref=db.backref('competition'), lazy=True)

    def _init_(self, organizer_id, name, description):
        self.admin_id = admin_id
        self.name = name
        self.description = description

    def get_json(self):
        return{
            'competition_id:': self.competition_id,
            'name': self.name,
            "description": self.description
        }
