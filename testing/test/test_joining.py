import unittest
from string_operations import joining_names

class TestJoiningNames(unittest.TestCase):

    def test_joining_names(self):
        self.assertEqual(joining_names(["name1", "name2", "name3"]), "name1name2name3")


if __name__ == '__main__':
    unittest.main()