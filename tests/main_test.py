from unittest import mock
from request_service import RequestService
from test_base import TestBase
import unittest


class MainTest(unittest.TestCase):
    
    def test_start_should_be_called_with_array(self):
        requestService = RequestService()
        requestService.start = mock.Mock()
        
        requestService.start.assert_called_once(url="http://www.google.com")
        
if __name__ == '__main__':
    unittest.main()
