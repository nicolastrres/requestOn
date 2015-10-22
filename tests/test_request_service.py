import tempfile
import unittest
from requests import Response

from requestOn.request_service import RequestService
from unittest.mock import patch


class RequestServiceTest(unittest.TestCase):

    def setUp(self):
        self.request = RequestService()

    @patch('requests.get')
    def test_call_a_endpoint_list(self, mock_requests_get):
        response = Response()
        response.status_code = 200
        mock_requests_get.return_value = response
        self.request.endpoints = ['http://www.github.com']

        actual_responses = self.request.call_endpoints()

        self.assertEqual(200, actual_responses[0])

    @patch('requests.get')
    def test_call_a_endpoint_list_with_broken_url(self, mock_requests_get):
        response = Response()
        response.status_code = 404
        mock_requests_get.return_value = response
        self.request.endpoints = ['https://www.facebook.com/Idontknow?_rdr']

        actual_responses = self.request.call_endpoints()

        self.assertEqual(404, actual_responses[0])

    def test_should_treat_correctly_when_a_invalid_url_is_passed(self):
        self.request.endpoints = ['test']

        actual_responses = self.request.call_endpoints()

        self.assertEqual(0, len(actual_responses))

    def test_should_get_endpoints_from_file(self):
        data = 'https://google.com'
        with tempfile.NamedTemporaryFile() as tempf:
            tempf.write(bytes(data, 'UTF-8'))
            tempf.flush()
            self.request.read_endpoints_from_file(tempf.name)

        self.assertEqual([data], self.request.endpoints)
