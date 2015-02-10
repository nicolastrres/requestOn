import unittest
import sys
import os.path
from unittest.mock import patch

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from checkit.request_service import RequestService


class RequestServiceTest(unittest.TestCase):
    def setUp(self):
        self.request = RequestService()

    @patch('CHECKIT.logs.logging')
    def test_valid_url(self, mock_logging):
        response = self.request.getcode("http://www.google.com")
        self.assertTrue(mock_logging.info.called)
        self.assertEqual(response, 200)

    @patch('CHECKIT.logs.logging')
    def test_not_found(self, mock_logging):
        response = self.request.getcode('http://www.github.com/sdksdjflskjflskjflsdkjflskdjfsfds')
        self.assertTrue(mock_logging.error.called)
        self.assertEqual(response, 404)

    @patch('CHECKIT.logs.logging')
    def test_invalid_url(self, mock_logging):
        response = self.request.getcode('test')
        self.assertTrue(mock_logging.error.called)
        self.assertEqual(response[0], "unknown url type: 'test'")

if __name__ == '__main__':
    unittest.main()
