import logging
import unittest
import sys
import os.path
from unittest.mock import MagicMock

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from requestOn.request_service import RequestService
from requestOn.logs import Logs


class RequestServiceTest(unittest.TestCase):

    def setUp(self):
        self.log = Logs()
        self.request = RequestService(api_name='API Name', logs=self.log)

    def expectedEndpoints(self):
        return ['http://www.github.com', 'http://www.google.com', 'http://www.circleci.com']

    def test_should_add_a_endpoint_list(self):
        expected_endpoints = self.expectedEndpoints()
        self.request.addEndpoints(expected_endpoints)
        actual_endpoints = self.request.getEndpointList()
        self.assertEqual(expected_endpoints, actual_endpoints)

    def test_call_a_endpoint_list(self):
        self.request.addEndpoints(self.expectedEndpoints())
        self.log.logger.info = MagicMock()

        actual_responses = self.request.start()

        self.assertEqual(200, actual_responses[0])
        self.assertEqual(200, actual_responses[1])
        self.assertEqual(200, actual_responses[2])
        self.assertTrue(self.log.logger.info.called)

    def test_call_a_endpoint_list_with_broken_url(self):
        endpoints = self.expectedEndpoints()
        endpoints[1] = 'https://www.facebook.com/Idontknow?_rdr'
        self.request.addEndpoints(endpoints)
        self.log.logger.info = MagicMock()
        self.log.logger.error = MagicMock()
        actual_responses = self.request.start()

        self.assertEqual(200, actual_responses[0])
        self.assertEqual(404, actual_responses[1])
        self.assertEqual(200, actual_responses[2])

        self.assertTrue(self.log.logger.info)
        self.assertTrue(self.log.logger.error.called)

    def test_should_treat_correctly_when_a_invalid_url_is_passed(self):
        self.request.addEndpoint('test')
        expected_response_endpoint = 0
        self.log.logger.error = MagicMock()

        actual_responses = self.request.start()

        self.assertEqual(expected_response_endpoint, actual_responses[0])
        self.assertTrue(self.log.logger.error.called)


class LogsTest(unittest.TestCase):

    def setUp(self):
        self.log = Logs()

    def test_info_log(self):
        self.log.logger.info = MagicMock()
        self.log.info('https://www.google.com  --- code response:  200')
        self.log.logger.info.assert_called_once_with(
            'Calling endpoint: https://www.google.com  --- code response:  200')

    def test_error_status_code_log(self):
        self.log.logger.error = MagicMock()
        self.log.error_status_code('400')
        self.log.logger.error.assert_called_once_with('Error 400')

    def test_general_error_log(self):
        self.log.logger.error = MagicMock()
        self.log.general_error('Crazy error')
        self.log.logger.error.assert_called_once_with('Undefined Error: Crazy error')

    def test_extra_info_log(self):
        self.log.logger.info = MagicMock()
        self.log.extra_info('Crazy extra info')
        self.log.logger.info.assert_called_once_with('Extra information: Crazy extra info')

    def test_write_file(self):
        filename = 'test_log_file.txt'
        logging.FileHandler = MagicMock()
        self.log.logger.addHandler = MagicMock()
        self.log.write_file(filename)
        logging.FileHandler.assert_called_once_with(filename)
        self.log.logger.addHandler.assert_called_once_with(logging.FileHandler(filename))

if __name__ == '__main__':
    unittest.main()
