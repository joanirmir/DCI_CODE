import unittest
from math_operations import subtraction

class TestSubtraction(unittest.TestCase):
    def test_subtraction(self):
        self.assertEqual(subtraction(2, 2), 0)


if __name__ == '__main__':
    unittest.main()