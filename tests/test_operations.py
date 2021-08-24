import operations as op
import unittest

class TestClass(unittest.TestCase):

    def test_two_power_6(self):
        assert op.two_power(6) == 64
    
    def test_two_power_10(self):
        value = op.two_power(10)
        self.assertEqual(value, 1024)

    def test_truncate(self):
        assert op.truncate(9, 2) == 4
