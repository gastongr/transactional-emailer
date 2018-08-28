from db import db

class EmailTemplateModel(db.Model):
    __tablename__ = 'email_templates'

    id = db.Column(db.Integer, primary_key=True)
    transaction_name = db.Column(db.String(80), unique=True)
    email_body = db.Column(db.String(1024))
    email_subject = db.Column(db.String(254))

    def __init__(self, transaction_name, email_body, email_subject):
        self.transaction_name = transaction_name
        self.email_body = email_body
        self.email_subject = email_subject

    def json(self):
        return {'id': self.id, 'transaction_name': self.transaction_name, 'email_body': self.email_body, 'email_subject': self.email_subject}

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_transaction_name(cls, _transaction_name):
        return cls.query.filter_by(transaction_name=_transaction_name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
