import tempfile
import unittest

from requestOn.request_service import RequestService
from unittest.mock import patch


class RequestServiceTest(unittest.TestCase):
    def setUp(self):
        self.request = RequestService()

    def expectedEndpoints(self):
        return ['http://www.github.com', 'http://www.google.com', 'http://www.circleci.com']

    def test_should_add_a_endpoint_list(self):
        expected_endpoints = self.expectedEndpoints()
        self.request.add_endpoints(expected_endpoints)
        actual_endpoints = self.request.get_endpointList()
        self.assertEqual(expected_endpoints, actual_endpoints)

    def test_call_a_endpoint_list(self):
        self.request.add_endpoints(self.expectedEndpoints())

        actual_responses = self.request.call_endpoints()

        self.assertEqual(200, actual_responses[0])
        self.assertEqual(200, actual_responses[1])
        self.assertEqual(200, actual_responses[2])

    @patch("builtins.print")
    def test_call_a_endpoint_list_with_broken_url(self, mock_print):
        endpoints = self.expectedEndpoints()
        endpoints[1] = 'https://www.facebook.com/Idontknow?_rdr'
        self.request.add_endpoints(endpoints)
        actual_responses = self.request.call_endpoints()

        self.assertEqual(200, actual_responses[0])
        self.assertEqual(404, actual_responses[1])
        self.assertEqual(200, actual_responses[2])

    @patch("builtins.print")
    def test_should_treat_correctly_when_a_invalid_url_is_passed(self, mock_print):
        self.request.add_endpoint('test')

        actual_responses = self.request.call_endpoints()

        self.assertEqual(0, len(actual_responses))

    def test_should_get_endpoints_from_file(self):
        data = 'https://google.com'
        with tempfile.NamedTemporaryFile() as tempf:
            tempf.write(bytes(data, 'UTF-8'))
            tempf.flush()
            self.request.read_endpoints_from_file(tempf.name)

        self.assertEqual([data], self.request.get_endpointList())
