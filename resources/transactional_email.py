from flask_restful import Resource, reqparse
from models.transactional_email import TransactionalEmailModel
from models.email_template import EmailTemplateModel
from models.user import UserModel
import datetime

class TransactionalEmail(Resource):
    def get(self, id):
        transactional_email = TransactionalEmailModel.find_by_id(id)
        if transactional_email:
            return transactional_email.json()
        return {'message': 'Resource not found'}, 404

class TransactionalEmailList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('transaction_name',
        type=str,
        required=True,
        help="transaction_name field is required on the request body!"
    )
    parser.add_argument('user_id',
        type=int,
        required=True,
        help="user_id field is required on the request body!"
    )

    def get(self):
        return {'items': list(map(lambda x: x.json(), TransactionalEmailModel.query.all()))}

    def post(self):
        data = TransactionalEmailList.parser.parse_args()
        user = UserModel.find_by_id(data['user_id'])
        email_template = EmailTemplateModel.find_by_transaction_name(data['transaction_name'])

        if not user:
            return {'message': "User with id '{}' was not found.".format(data['user_id'])}, 400
        if not email_template:
            return {'message': "No email template configured for transaction '{}'.".format(data['transaction_name'])}, 400

        transactional_email = TransactionalEmailModel(datetime.datetime.now(), **data)

        try:
            transactional_email.save()
        except:
            return {"message": "An error occurred inserting the transactional email registry."}, 500

        return transactional_email.json(), 201
