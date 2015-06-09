import tempfile
import unittest

from requestOn.request_service import RequestService
from unittest.mock import patch


class RequestServiceTest(unittest.TestCase):

    def setUp(self):
        self.request = RequestService()
        self.expected_endpoints = ['http://www.github.com', 'http://www.google.com', 'http://www.circleci.com']

    def test_call_a_endpoint_list(self):
        self.request.endpoints = self.expected_endpoints

        actual_responses = self.request.call_endpoints()

        self.assertEqual(200, actual_responses[0])
        self.assertEqual(200, actual_responses[1])
        self.assertEqual(200, actual_responses[2])

    @patch("builtins.print")
    def test_call_a_endpoint_list_with_broken_url(self, mock_print):
        endpoints = self.expected_endpoints
        endpoints[1] = 'https://www.facebook.com/Idontknow?_rdr'
        self.request.endpoints = endpoints
        actual_responses = self.request.call_endpoints()

        self.assertEqual(200, actual_responses[0])
        self.assertEqual(404, actual_responses[1])
        self.assertEqual(200, actual_responses[2])

    @patch("builtins.print")
    def test_should_treat_correctly_when_a_invalid_url_is_passed(self, mock_print):
        self.request.endpoints.append('test')

        actual_responses = self.request.call_endpoints()

        self.assertEqual(0, len(actual_responses))

    def test_should_get_endpoints_from_file(self):
        data = 'https://google.com'
        with tempfile.NamedTemporaryFile() as tempf:
            tempf.write(bytes(data, 'UTF-8'))
            tempf.flush()
            self.request.read_endpoints_from_file(tempf.name)

        self.assertEqual([data], self.request.endpoints)
