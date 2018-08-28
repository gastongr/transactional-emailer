from flask_restful import Resource, reqparse
from models.user import UserModel

class User(Resource):

    def get(self, id):
        user = UserModel.find_by_id(id)
        if user:
            return user.json()
        return {'message': 'Resource not found'}, 404

    def delete(self, id):
        user = UserModel.find_by_id(id)
        if user:
            user.delete()
            return {'message': 'User deleted.'}
        return {'message': 'User not found.'}, 404

    def put(self, id):
        data = UserList.parser.parse_args()

        user = UserModel.find_by_id(id)
        if not user:
            return {'message': "User with id '{}' was not found.".format(id)}, 400

        user.email = data['email']
        user.save()

        return user.json()

class UserList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'email',
        type=str,
        required=True,
        help="email field is required on the request body!"
    )

    def get(self):
        return {'items': list(map(lambda x: x.json(), UserModel.query.all()))}

    def post(self):
        data = UserList.parser.parse_args()

        user = UserModel.find_by_email(data['email'])
        if user:
            return {'message': "A user with the email '{}' already exists.".format(data['email'])}, 400

        new_user = UserModel(data['email'])

        try:
            new_user.save()
        except:
            return {"message": "An error occurred inserting the user."}, 500

        return new_user.json(), 201
