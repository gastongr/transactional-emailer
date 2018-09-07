# Flask Core Settings
HOST  = '127.0.0.1'
PORT  = 5000
DEBUG = True

# Database Settings
SQLALCHEMY_DATABASE_URI        = 'sqlite:///data.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS           = True

# Fuel SDK Settings
FUELSDK_APP_SIGNATURE       = 'none'
FUELSDK_CLIENT_ID           = '###'
FUELSDK_CLIENT_SECRET       = '###'
FUELSDK_DEFAULT_WSDL        = 'https://webservice.exacttarget.com/etframework.wsdl'
FUELSDK_AUTH_URL            = 'https://auth.exacttargetapis.com/v1/requestToken?legacy=1'
