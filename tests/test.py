import unittest
from checkit.request_service import RequestService

class RequestServiceTest(unittest.TestCase):
    def test_service_available(self):
        request = RequestService
        response = RequestService.getcode('http://www.google.com')
        self.assertEqual(response, 200)


if __name__ == '__main__':
    unittest.main()
