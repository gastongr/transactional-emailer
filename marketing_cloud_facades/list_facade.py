from flask import current_app as app
import ET_Client
import uuid
import os

class ListFacade():

    def __init__(self):
        client_config = {
            "clientid":          app.config['FUELSDK_CLIENT_ID'],
            "clientsecret":      app.config['FUELSDK_CLIENT_SECRET'],
            "appsignature":      app.config['FUELSDK_APP_SIGNATURE'],
            "defaultwsdl":       app.config['FUELSDK_DEFAULT_WSDL'],
            "authenticationurl": app.config['FUELSDK_AUTH_URL']
        }
        self.auth_stub = ET_Client.ET_Client(False, True, client_config)

    def get_lists(self):
        lists = ET_Client.ET_List()
        lists.auth_stub = self.auth_stub
        lists.props = ["ID","ListName","Description","Category","Type"]
        return lists.get()

    def get_list_by_name(self, name):
        lists = ET_Client.ET_List()
        lists.auth_stub = self.auth_stub
        lists.search_filter = {'Property' : 'ListName', 'SimpleOperator' : 'like', 'Value' : name}
        lists.props = ["ID","PartnerKey","CreatedDate","ModifiedDate","Client.ID","Client.PartnerClientKey","ListName","Description","Category","Type","CustomerKey","ListClassification","AutomatedEmail.ID"]
        return lists.get()
