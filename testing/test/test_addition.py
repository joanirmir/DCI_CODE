import unittest
from math_operations import add

class TestAddition(unittest.TestCase):
    pass

    def test_add(self):
        self.assertEqual(add(2, 2), 4)


if __name__ == '__main__':
    unittest.main()