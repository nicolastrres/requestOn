import logging
import unittest
from unittest.mock import MagicMock
from requestOn.logs import Logs


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
