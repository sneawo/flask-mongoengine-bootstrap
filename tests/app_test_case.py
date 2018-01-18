import logging
from unittest import TestCase

from app.bootstrap import init_app, mongo


logging.disable(logging.CRITICAL)


class AppTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = init_app(config_obj='app.config.TestingConfig')

    def drop_mongo_collections(self):
        with self.app.app_context():
            mongo.connection['default'].drop_database(self.app.config['MONGODB_SETTINGS'][0]['DB'])

    def setUp(self):
        self.client = self.app.test_client()
        self.context = self.app.test_request_context()
        self.context.push()
        self.drop_mongo_collections()

    def tearDown(self):
        self.context.pop()
        self.drop_mongo_collections()
