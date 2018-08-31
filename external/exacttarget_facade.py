from flask import current_app as app
import ET_Client
import uuid
import os

class ExactTargetFacade():

    def __init__(self):
        client_config = {
            "clientid":          app.config['FUELSDK_CLIENT_ID'],
            "clientsecret":      app.config['FUELSDK_CLIENT_SECRET'],
            "appsignature":      app.config['FUELSDK_APP_SIGNATURE'],
            "defaultwsdl":       app.config['FUELSDK_DEFAULT_WSDL'],
            "authenticationurl": app.config['FUELSDK_AUTH_URL']
        }
        self.auth_stub = ET_Client.ET_Client(False, True, client_config)

    def get_triggered_send_definitions(self):
        try:
            # Get all TriggeredSendDefinitions
            print('>>> Get all TriggeredSendDefinitions')
            getTS = ET_Client.ET_TriggeredSend()
            getTS.auth_stub = self.auth_stub
            getTS.props = ["CustomerKey", "Name", "TriggeredSendStatus"]
            getResponse = getTS.get()
            print('Retrieve Status: ' + str(getResponse.status))
            print('Code: ' + str(getResponse.code))
            print('Message: ' + str(getResponse.message))
            print('MoreResults: ' + str(getResponse.more_results))
            print('Results Count: ' + str(len(getResponse.results)))
            #print 'Results: ' + str(getResponse.results)
        except Exception as e:
            print('Caught exception: ' + e.message)
            print(e)

    def pause_triggered_send(self, name):
        try:
            # Specify the name of a TriggeredSend that was setuprint for testing
            # Do not use a production Triggered Send Definition

            NameOfTestTS = "TEXTEXT"

            # Pause a TriggeredSend

            print('>>> Pause a TriggeredSend')
            patchTrig = ET_Client.ET_TriggeredSend()
            patchTrig.auth_stub = self.auth_stub
            patchTrig.props = {"CustomerKey" : NameOfTestTS, "TriggeredSendStatus" :"Inactive"}
            patchResponse = patchTrig.patch()
            print('Patch Status: ' + str(patchResponse.status))
            print('Code: ' + str(patchResponse.code))
            print('Message: ' + str(patchResponse.message))
            print('Result Count: ' + str(len(patchResponse.results)))
            print('Results: ' + str(patchResponse.results))
        except Exception as e:
            print('Caught exception: ' + e.message)
            print(e)

    def retrieve_triggered_send(self):
        try:
            NameOfTestTS = "TEXTEXT"

            # Retrieve Single TriggeredSend
            print('>>> Retrieve Single TriggeredSend')
            getTS = ET_Client.ET_TriggeredSend()
            getTS.auth_stub = self.auth_stub
            getTS.props = ["CustomerKey", "Name", "TriggeredSendStatus"]
            getTS.search_filter = {'Property' : 'CustomerKey','SimpleOperator' : 'equals','Value' : NameOfTestTS}
            getResponse = getTS.get()
            print('Retrieve Status: ' + str(getResponse.status))
            print('Code: ' + str(getResponse.code))
            print('Message: ' + str(getResponse.message))
            print('MoreResults: ' + str(getResponse.more_results))
            print('Results Count: ' + str(len(getResponse.results)))
            print('Results: ' + str(getResponse.results))
        except Exception as e:
            print('Caught exception: ' + e.message)
            print(e)

    def send_triggered_send(self):
        try:
            NameOfTestTS = "TEXTEXT"

            # Start a TriggeredSend by setting to Active
            print('>>> Start a TriggeredSend by setting to Active')
            patchTrig = ET_Client.ET_TriggeredSend()
            patchTrig.auth_stub = self.auth_stub
            patchTrig.props = {"CustomerKey" : NameOfTestTS, "TriggeredSendStatus" :"Active"}
            patchResponse = patchTrig.patch()
            print('Patch Status: ' + str(patchResponse.status))
            print('Code: ' + str(patchResponse.code))
            print('Message: ' + str(patchResponse.message))
            print('Result Count: ' + str(len(patchResponse.results)))
            print('Results: ' + str(patchResponse.results))
        except Exception as e:
            print('Caught exception: ' + e.message)
            print(e)

    def send_email_with_triggered_send(self):
        try:
            NameOfTestTS = "TEXTEXT"

            # Send an email with TriggeredSend
            print('>>> Send an email with TriggeredSend')
            sendTrig = ET_Client.ET_TriggeredSend()
            sendTrig.auth_stub = self.auth_stub
            sendTrig.props = {"CustomerKey" : NameOfTestTS}
            sendTrig.subscribers = [{"EmailAddress":"testing@bh.exacttarget.com", "SubscriberKey" : "testing@bh.exacttarget.com"}]
            sendResponse = sendTrig.send()
            print('Send Status: ' + str(sendResponse.status))
            print('Code: ' + str(sendResponse.code))
            print('Message: ' + str(sendResponse.message))
            print('Result Count: ' + str(len(sendResponse.results)))
            print('Results: ' + str(sendResponse.results))
        except Exception as e:
            print('Caught exception: ' + e.message)
            print(e)

    def create_triggered_send_deffinition(self):
        try:
            # Generate a unique identifier for the TriggeredSend customer key since they cannot be re-used even after deleted
            TSNameForCreateThenDelete = str(uuid.uuid4())

            # Create a TriggeredSend Definition
            print('>>> Create a TriggeredSend Definition')
            postTrig = ET_Client.ET_TriggeredSend()
            postTrig.auth_stub = self.auth_stub
            postTrig.props = {'CustomerKey' : TSNameForCreateThenDelete,'Name' : TSNameForCreateThenDelete, 'Email' : {"ID":"3113962"}, "SendClassification": {"CustomerKey": "2240"}}
            postResponse = postTrig.post()
            print('Post Status: ' + str(postResponse.status))
            print('Code: ' + str(postResponse.code))
            print('Message: ' + str(postResponse.message))
            print('Result Count: ' + str(len(postResponse.results)))
            print('Results: ' + str(postResponse.results))
        except Exception as e:
            print('Caught exception: ' + e.message)
            print(e)

    def delete_triggered_send_deffinition(self):
        try:
            # Delete a TriggeredSend Definition
            print('>>> Delete a TriggeredSend Definition ')
            deleteTrig = ET_Client.ET_TriggeredSend()
            deleteTrig.auth_stub = self.auth_stub
            deleteTrig.props = {'CustomerKey' : TSNameForCreateThenDelete}
            deleteResponse = deleteTrig.delete()
            print('Delete Status: ' + str(deleteResponse.status))
            print('Code: ' + str(deleteResponse.code))
            print('Message: ' + str(deleteResponse.message))
            print('Result Count: ' + str(len(deleteResponse.results)))
            print('Results: ' + str(deleteResponse.results))

        except Exception as e:
            print('Caught exception: ' + e.message)
            print(e)
