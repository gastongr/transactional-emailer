from flask import Flask
from flask_restful import Api

from resources.transactional_email import TransactionalEmail, TransactionalEmailList
from resources.email_template import EmailTemplate, EmailTemplateList
from resources.user import User, UserList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(TransactionalEmail, '/transactional-emails/<string:id>')
api.add_resource(TransactionalEmailList, '/transactional-emails/')

api.add_resource(EmailTemplate, '/email-templates/<string:id>')
api.add_resource(EmailTemplateList, '/email-templates/')

api.add_resource(User, '/users/<string:id>')
api.add_resource(UserList, '/users/')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
