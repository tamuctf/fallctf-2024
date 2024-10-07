from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Submission(db.Model):
    __tablename__ = 'submissions'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(256), nullable=False)

    def get_submission(id):
        submission = Submission.query.filter_by(id=id).first()
        if submission == None:
            return ""
        return submission.message
