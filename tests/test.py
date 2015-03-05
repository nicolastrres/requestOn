import logging
import unittest
import sys
import os.path
from unittest.mock import MagicMock

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from checkit.request_service import RequestService
from checkit.logs import Logs


class RequestServiceTest(unittest.TestCase):
    def setUp(self):
        self.request = RequestService()
        self.log = Logs()

    def test_valid_url(self):
        url = 'http://www.google.com'
        message = 'Calling endpoint: ' + url + " --- code response:" + str(200)
        self.log.logger.info = MagicMock()

        response = self.request.get_code(url, self.log)

        self.log.logger.info.assert_called_with(message)
        self.assertEqual(response, 200)

    def test_not_found(self):
        self.log.logger.error = MagicMock()

        response = self.request.get_code('http://www.github.com/sdksdjflskjflskjflsdkjflskdjfsfds', self.log)
        self.log.logger.error.assert_called_with('Error %s' % 404)
        self.assertEqual(response, 404)

    def test_invalid_url(self):
        self.log.logger.error = MagicMock()

        response = self.request.get_code('test', self.log)

        self.log.logger.error.assert_called_with('Undefined Error: ' + response[0])
        self.assertEqual(response[0], "unknown url type: 'test'")


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
