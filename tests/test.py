import unittest
import sys
import os.path
from unittest.mock import patch

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from checkit.request_service import RequestService
from checkit.logs import Logs


class RequestServiceTest(unittest.TestCase):
    def setUp(self):
        api_name = 'API Name'
        self.request = RequestService(api_name)

    def expectedEndpoints(self):
        return ['http://www.github.com', 'http://www.google.com', 'http://www.circleci.com']

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

    def test_should_add_a_endpoint_list(self):
        expected_endpoints = self.expectedEndpoints()
        self.request.addEndpoints(expected_endpoints)
        actual_endpoints = self.request.getEndpointList()
        self.assertEqual(expected_endpoints, actual_endpoints)

    def test_call_a_endpoint_list(self):
        self.request.addEndpoints(self.expectedEndpoints())
        actual_responses = self.request.start()
        self.assertEqual([200, 200, 200], actual_responses)

    def test_call_a_endpoint_list_with_broken_url(self):
        endpoints = self.expectedEndpoints()
        endpoints[1] = 'https://www.facebook.com/Idontknow?_rdr'
        self.request.addEndpoints(endpoints)
        actual_responses = self.request.start()
        self.assertEqual([200, 404, 200], actual_responses)


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
        mock_logging.error.assert_called_once_with('Crazy error')

    @patch('checkit.logs.Logs.logger')
    def test_extra_info_log(self, mock_logging):
        Logs.extra_info('Crazy extra info')
        self.assertTrue(mock_logging.info.called)
        mock_logging.info.assert_called_once_with('Extra information: Crazy extra info')

if __name__ == '__main__':
    unittest.main()
