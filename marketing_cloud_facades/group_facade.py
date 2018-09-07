from flask import current_app as app
import ET_Client
import os

class GroupFacade():

    def __init__(self):
        client_config = {
            "clientid":          app.config['FUELSDK_CLIENT_ID'],
            "clientsecret":      app.config['FUELSDK_CLIENT_SECRET'],
            "appsignature":      app.config['FUELSDK_APP_SIGNATURE'],
            "defaultwsdl":       app.config['FUELSDK_DEFAULT_WSDL'],
            "authenticationurl": app.config['FUELSDK_AUTH_URL']
        }
        self.auth_stub = ET_Client.ET_Client(False, True, client_config)

    def get_groups(self):
        groups = ET_Client.ET_Group()
        groups.auth_stub = self.auth_stub
        groups.props = ["ID", "Name"]
        return groups.get()
