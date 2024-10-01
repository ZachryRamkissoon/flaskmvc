from App.database import db

class Result(db.Model):
    result_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("user.student_id"), nullable=False)
    competition_id = db.Column(db.Integer, db.ForeignKey("competition.competition_id"), nullable=False)
    score = db.Column(db.Float, nullable=False)

    def _init_(self, student_id, competition_id, score):
        self.student_id = student_id
        self.competition_id = competition_id
        self.score = score
    
    def get_json(self):
        return{
            'student_id': self.student_id,
            'competition_id': self.competition_id,
            'score': self.score
        }