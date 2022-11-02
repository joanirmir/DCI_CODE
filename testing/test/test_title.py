import unittest
from string_operations import title

class TestTitle(unittest.TestCase):

    def test_title(self):
        self.assertEqual(title("hello", "world"), ("Hello", "World"))


if __name__ == '__main__':
    unittest.main()