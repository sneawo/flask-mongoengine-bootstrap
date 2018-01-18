import os


MONGODB_SETTINGS = [
    {
        "ALIAS": "default",
        "DB":    os.environ.get('MONGODB_DB', 'db'),
        "HOST": os.environ.get('MONGODB_HOST', 'db'),
        "PORT": int(os.environ.get('MONGODB_PORT', 27017)),
        "USERNAME": os.environ.get('MONGODB_USERNAME', ''),
        "PASSWORD": os.environ.get('MONGODB_PASSWORD', ''),
        "MAXPOOLSIZE": int(os.environ.get('MONGODB_MAXPOOLSIZE', 30))
    }
]


class Config(object):
    SECRET_KEY = '\xf5\x9e\x80\xedh\x076I \xe28\xb0pyM\xf2\x95\xa2u\xc8\xb7\x1a\xec\xb3'

    APP_NAME = 'APP_NAME'
    PREFERRED_URL_SCHEME = os.environ.get('URL_SCHEME', 'http')

    MONGODB_SETTINGS = MONGODB_SETTINGS


class TestingConfig(Config):
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    TESTING = True
    MONGODB_SETTINGS = [dict(settings, **{'DB': 'db_test'}) for settings in MONGODB_SETTINGS]
