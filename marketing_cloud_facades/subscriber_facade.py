from flask import current_app as app
import ET_Client
import uuid
import os

class SubscriberFacade():

    def __init__(self):
        client_config = {
            "clientid":          app.config['FUELSDK_CLIENT_ID'],
            "clientsecret":      app.config['FUELSDK_CLIENT_SECRET'],
            "appsignature":      app.config['FUELSDK_APP_SIGNATURE'],
            "defaultwsdl":       app.config['FUELSDK_DEFAULT_WSDL'],
            "authenticationurl": app.config['FUELSDK_AUTH_URL']
        }
        self.auth_stub = ET_Client.ET_Client(False, True, client_config)

    def get_subscribers(self):
        subscribers = ET_Client.ET_Subscriber()
        subscribers.auth_stub = self.auth_stub
        subscribers.props = ["ID", "EmailAddress", "Status"]
        return subscribers.get()
