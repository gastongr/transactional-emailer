from flask import current_app as app
import ET_Client
import uuid
import os

class DataExtensionFacade():

    def __init__(self):
        client_config = {
            "clientid":          app.config['FUELSDK_CLIENT_ID'],
            "clientsecret":      app.config['FUELSDK_CLIENT_SECRET'],
            "appsignature":      app.config['FUELSDK_APP_SIGNATURE'],
            "defaultwsdl":       app.config['FUELSDK_DEFAULT_WSDL'],
            "authenticationurl": app.config['FUELSDK_AUTH_URL']
        }
        self.auth_stub = ET_Client.ET_Client(False, True, client_config)


    def get_data_extension_by_name(self, name):
        de = ET_Client.ET_DataExtension()
        de.auth_stub = self.auth_stub
        de.props = ["CustomerKey", "Name"]
        de.search_filter = {'Property' : 'Name', 'SimpleOperator' : 'like', 'Value' : name}
        return de.get()

    def get_data_extension_by_customer_key(self, data_extension_customer_key):
        de = ET_Client.ET_DataExtension()
        de.auth_stub = self.auth_stub
        de.props = ["CustomerKey", "Name"]
        de.search_filter = {'Property' : 'CustomerKey', 'SimpleOperator' : 'like', 'Value' : data_extension_customer_key}
        return de.get()

    def get_fields_from_data_extension(self, data_extension_customer_key):
        dec = ET_Client.ET_DataExtension_Column()
        dec.auth_stub = self.auth_stub
        dec.props = ["Name"]
        dec.search_filter = {'Property' : 'CustomerKey','SimpleOperator' : 'like', 'Value' : data_extension_customer_key}
        return dec.get()

    def add_row_to_data_extension(self, data_extension_name, fields_dictionary):
        der = ET_Client.ET_DataExtension_Row()
        der.auth_stub = self.auth_stub
        der.Name = data_extension_name
        der.props = fields_dictionary
        return der.post()

    def get_all_rows_from_data_extension(self, data_extension_customer_key, fields_list):
        der = ET_Client.ET_DataExtension_Row()
        der.auth_stub = self.auth_stub
        der.CustomerKey = data_extension_customer_key
        der.props = fields_list
        return der.get()
