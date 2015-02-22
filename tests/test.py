import unittest
import sys
import os.path
from unittest.mock import patch

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from checkit.response_endpoint import ResponseEndpoint
from checkit.request_service import RequestService
from checkit.logs import Logs

# from testfixtures.comparison import register
# from testfixtures import compare
#
# def compare_response_endpoint_objects(self, obj1, obj2):
#         if obj1.code == obj2.code and obj1.data == obj2.data:
#             return
#
#         return 'Obj1 different of Obj2'
#
# register(ResponseEndpoint, compare_response_endpoint_objects)


class RequestServiceTest(unittest.TestCase):
    def setUp(self):
        api_name = 'API Name'
        self.request = RequestService(api_name)

    def expectedEndpoints(self):
        return ['http://www.github.com', 'http://www.google.com', 'http://www.circleci.com']

    def test_should_add_a_endpoint_list(self):
        expected_endpoints = self.expectedEndpoints()
        self.request.addEndpoints(expected_endpoints)
        actual_endpoints = self.request.getEndpointList()
        self.assertEqual(expected_endpoints, actual_endpoints)

    @patch('checkit.logs.Logs.logger')
    def test_call_a_endpoint_list(self, mock_logging):
        self.request.addEndpoints(self.expectedEndpoints())
        actual_responses = self.request.start()
        self.assertEqual(200, actual_responses[0].code)
        self.assertEqual(200, actual_responses[1].code)
        self.assertEqual(200, actual_responses[2].code)
        self.assertTrue(mock_logging.info.called)

    @patch('checkit.logs.Logs.logger')
    def test_call_a_endpoint_list_with_broken_url(self, mock_logging):
        endpoints = self.expectedEndpoints()
        endpoints[1] = 'https://www.facebook.com/Idontknow?_rdr'
        self.request.addEndpoints(endpoints)
        actual_responses = self.request.start()
        self.assertEqual(200, actual_responses[0].code)
        self.assertEqual(404, actual_responses[1].code)
        self.assertEqual(200, actual_responses[2].code)
        self.assertTrue(mock_logging.info.called)
        self.assertTrue(mock_logging.error.called)

    @patch('checkit.logs.Logs.logger')
    def test_should_treat_correctly_when_a_invalid_url_is_passed(self, mock_logging):
        self.request.addEndpoint('test')
        actual_responses = self.request.start()
        expected_response_endpoint = ResponseEndpoint(0, '')
        self.assertEqual(expected_response_endpoint.code, actual_responses[0].code)
        self.assertEqual("unknown url type: 'test'", actual_responses[0].data[0])
        self.assertTrue(mock_logging.error.called)

    @patch('checkit.logs.Logs.logger')
    def test_call_a_endpoint_list_and_retrieve_data(self, mock_logging):
        self.request.addEndpoint('http://www.google.com')
        actual_responses = self.request.start()
        expected_response_endpoint = ResponseEndpoint(200, '')
        # compare(expected_response_endpoint, actual_responses[0])
        self.assertEqual(expected_response_endpoint.code, actual_responses[0].code)
        self.assertEqual(expected_response_endpoint.data, actual_responses[0].data)
        self.assertTrue(mock_logging.info.called)


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
