import unittest
import sys
import os.path
from unittest.mock import patch

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from checkit.request_service import RequestService
from checkit.logs import Logs


class RequestServiceTest(unittest.TestCase):
    def setUp(self):
        self.request = RequestService()

    @patch('checkit.logs.Logs.logger')
    def test_valid_url(self, mock_logging):
        response = self.request.get_code('http://www.google.com')
        self.assertTrue(mock_logging.info.called)
        self.assertEqual(response, 200)

    @patch('checkit.logs.Logs.logger')
    def test_not_found(self, mock_logging):
        response = self.request.get_code('http://www.github.com/sdksdjflskjflskjflsdkjflskdjfsfds')
        self.assertTrue(mock_logging.error.called)
        self.assertEqual(response, 404)

    @patch('checkit.logs.Logs.logger')
    def test_invalid_url(self, mock_logging):
        response = self.request.get_code('test')
        self.assertTrue(mock_logging.error.called)
        self.assertEqual(response[0], "unknown url type: 'test'")


class LogsTest(unittest.TestCase):
    @patch('checkit.logs.Logs.logger')
    def test_info_log(self, mock_logging):
        Logs.info('https://www.google.com  --- code response:  200')
        self.assertTrue(mock_logging.info.called)
        mock_logging.info.assert_called_once_with('Calling endpoint: https://www.google.com  --- code response:  200')

    @patch('checkit.logs.Logs.logger')
    def test_error_status_code_log(self, mock_logging):
        Logs.error_status_code('400')
        self.assertTrue(mock_logging.error.called)
        mock_logging.error.assert_called_once_with('Error 400')

    @patch('checkit.logs.Logs.logger')
    def test_general_error_log(self, mock_logging):
        Logs.general_error('Crazy error')
        self.assertTrue(mock_logging.error.called)
        mock_logging.error.assert_called_once_with('Undefined Error: Crazy error')

    @patch('checkit.logs.Logs.logger')
    def test_extra_info_log(self, mock_logging):
        Logs.extra_info('Crazy extra info')
        self.assertTrue(mock_logging.info.called)
        mock_logging.info.assert_called_once_with('Extra information: Crazy extra info')

if __name__ == '__main__':
    unittest.main()
