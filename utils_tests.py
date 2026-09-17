import unittest
from utils import utils

class TestUtils(unittest.TestCase):

    def test_reverse_int(self):
        self.assertEqual(utils.reversed(41), 14)
        print()

    def test_reverse_str(self):
        with self.assertRaises(TypeError):
            utils.reversed("41")

    def test_reverse_float(self):
        with self.assertRaises(TypeError):
            utils.reversed(41.50)

    def test_formatter_int(self):
         self.assertEqual(utils.formatter(10), ("1010", "12"))

    @unittest.expectedFailure
    def test_formatter_str(self):
        with self.assertRaises(TypeError):
            utils.reversed("41")
   
    @unittest.expectedFailure
    def test_formatter_float(self):
        with self.assertRaises(TypeError):
            utils.reversed(41.50)

test = TestUtils()
test.test_reverse_int()
test.test_reverse_float()
test.test_reverse_str()
test.test_formatter_float()
test.test_formatter_str()
test.test_formatter_int()
