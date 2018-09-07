from flask_restful import Resource, reqparse
from models.user import UserModel
from marketing_cloud_facades.data_extension_facade import DataExtensionFacade

class UserExport(Resource):


    def post(self):
        try:
            users = UserModel.query.all()
            for user in users:
                self.export_user_data(user)
        except Exception as e:
            return {"message": "An error occurred while exporting the data: {}".format(e.message)}, 500

        return {"status": "Export OK"}, 200

    def export_user_data(self, user):
        data_extension_facade = DataExtensionFacade()
        export_result = data_extension_facade.add_row_to_data_extension("ED8A3266-CB62-405D-A96B-C4EFC569868B", {"TOKEN": user.token, "EMAIL": user.email})

        if not export_result.status:
            raise Exception(str(export_result.message))
