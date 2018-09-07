from flask import current_app as app
import ET_Client
import uuid
import os

class TriggeredSendFacade():

    def __init__(self):
        client_config = {
            "clientid":          app.config['FUELSDK_CLIENT_ID'],
            "clientsecret":      app.config['FUELSDK_CLIENT_SECRET'],
            "appsignature":      app.config['FUELSDK_APP_SIGNATURE'],
            "defaultwsdl":       app.config['FUELSDK_DEFAULT_WSDL'],
            "authenticationurl": app.config['FUELSDK_AUTH_URL']
        }
        self.auth_stub = ET_Client.ET_Client(False, True, client_config)

    def get_triggered_send_definition(self, key):
        ts = ET_Client.ET_TriggeredSend()
        ts.auth_stub = self.auth_stub
        ts.props = ["CustomerKey", "Name", "TriggeredSendStatus"]
        ts.search_filter = {'Property' : 'CustomerKey', 'SimpleOperator' : 'equals', 'Value' : key}
        return ts.get()

    def get_triggered_send_definitions(self):
        ts = ET_Client.ET_TriggeredSend()
        ts.auth_stub = self.auth_stub
        ts.props = ["CustomerKey", "Name", "TriggeredSendStatus"]
        return ts.get()

    def create_triggered_send_definition(self, key):
        ts = ET_Client.ET_TriggeredSend()
        ts.auth_stub = self.auth_stub
        ts.props = {'CustomerKey' : key, 'Name' : key, 'Email' : {"ID":"3113962"}, "SendClassification": {"CustomerKey": "2240"}}
        return ts.post()

    def delete_triggered_send_definition(self, key):
        ts = ET_Client.ET_TriggeredSend()
        ts.auth_stub = self.auth_stub
        ts.props = {'CustomerKey' : key}
        return ts.delete()

    def pause_triggered_send_definition(self, key):
        ts = ET_Client.ET_TriggeredSend()
        ts.auth_stub = self.auth_stub
        ts.props = {"CustomerKey" : key, "TriggeredSendStatus" : "Inactive"}
        return ts.patch()

    def start_triggered_send_definition(self, key):
        ts = ET_Client.ET_TriggeredSend()
        ts.auth_stub = self.auth_stub
        ts.props = {"CustomerKey" key: , "TriggeredSendStatus" :"Active"}
        return ts.patch()

    def send_email(self, key, subscriber_email, subscriber_key):
        ts = ET_Client.ET_TriggeredSend()
        ts.auth_stub = self.auth_stub
        ts.props = {"CustomerKey" : key}
        ts.subscribers = [{"EmailAddress": subscriber_email, "SubscriberKey" : subscriber_key}]
        return ts.send()
