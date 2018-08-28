from db import db
from models.user import UserModel

class TransactionalEmailModel(db.Model):
    __tablename__ = 'transactional_emails'

    id = db.Column(db.Integer, primary_key=True)
    transaction_name = db.Column(db.String(80))
    transaction_datetime = db.Column(db.DateTime())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('UserModel')

    def __init__(self, transaction_datetime, transaction_name, user_id):
        self.transaction_datetime = transaction_datetime
        self.transaction_name = transaction_name
        self.user_id = user_id

    def json(self):
        return {'id': self.id, 'user_id': self.user_id, 'transaction_name': self.transaction_name, 'transaction_datetime': self.transaction_datetime.strftime("%Y-%m-%d %H:%M:%S")}

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
