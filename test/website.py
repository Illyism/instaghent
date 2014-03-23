import unittest
from pyramid import testing

class PyramidTest(unittest.TestCase):
    def setUp(self):
    	request = testing.DummyRequest()
        self.config = testing.setUp(request=request)

    def tearDown(self):
        testing.tearDown()

if __name__ == '__main__':
	unittest.main()