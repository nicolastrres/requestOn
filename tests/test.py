import unittest
import sys
import os.path
import inspect

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from checkit.request_service import RequestService



class RequestServiceTest(unittest.TestCase):
    def setUp(self):
        self.request = RequestService()

    def test_service_available(self):
        response = self.request.getcode("http://www.google.com")
        self.assertEqual(response, 200)

    def test_not_found(self):
        response = self.request.getcode('http://www.github.com/sdksdjflskjflskjflsdkjflskdjfsfds')
        self.assertEqual(response, 404)

if __name__ == '__main__':
    unittest.main()
