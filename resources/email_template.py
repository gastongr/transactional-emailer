from flask_restful import Resource, reqparse
from models.email_template import EmailTemplateModel

class EmailTemplate(Resource):
    def get(self, id):
        email_template = EmailTemplateModel.find_by_id(id)
        if email_template:
            return email_template.json()
        return {'message': 'Resource not found'}, 404

    def delete(self, id):
        email_template = EmailTemplateModel.find_by_id(id)
        if email_template:
            email_template.delete()
            return {'message': 'Email Template deleted.'}
        return {'message': 'Email Template not found.'}, 404

    def put(self, id):
        data = EmailTemplateList.parser.parse_args()

        email_template = EmailTemplateModel.find_by_id(id)
        if not email_template:
            return {'message': "Email Template with id '{}' was not found.".format(id)}, 400

        email_template.transaction_name = data['transaction_name']
        email_template.email_subject = data['email_subject']
        email_template.email_body = data['email_body']
        email_template.save()

        return email_template.json()

class EmailTemplateList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'transaction_name',
        type=str,
        required=True,
        help="transaction_name field is required on the request body!"
    )
    parser.add_argument(
        'email_subject',
        type=str,
        required=True,
        help="email_subject field is required on the request body!"
    )
    parser.add_argument(
        'email_body',
        type=str,
        required=True,
        help="email_body field is required on the request body!"
    )

    def get(self):
        return {'items': list(map(lambda x: x.json(), EmailTemplateModel.query.all()))}

    def post(self):
        data = EmailTemplateList.parser.parse_args()

        email_template = EmailTemplateModel.find_by_transaction_name(data['transaction_name'])
        if email_template:
            return {'message': "An email template for the transaction '{}' already exists.".format(data['transaction_name'])}, 400

        new_email_template = EmailTemplateModel(data['transaction_name'], data['email_subject'], data['email_body'])

        try:
            new_email_template.save()
        except:
            return {"message": "An error occurred inserting the email template."}, 500

        return new_email_template.json(), 201
