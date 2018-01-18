from app.models import RequestLog
from tests.app_test_case import AppTestCase


class GetApiTests(AppTestCase):

    def test_get(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)

    def test_create(self):
        response = self.client.post('/', headers={'request-id': 'test-id'})
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, RequestLog.objects.count())
        self.assertEqual('test-id', RequestLog.objects[0].request_id)
