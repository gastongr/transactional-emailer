from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), unique=True)
    token = db.Column(db.String(27))
    transactional_emails = db.relationship('TransactionalEmailModel', lazy='dynamic')

    def __init__(self, email, token):
        self.email = email
        self.token = token

    def json(self):
        return {'id': self.id, 'email': self.email, 'token': self.token}

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_email(cls, _email):
        return cls.query.filter_by(email=_email).first()

    @classmethod
    def find_all(cls):
        return cls.query.filter_by(id=_id).first()
