import unittest
from my_module import rm
import os
import mock


# no mocking test
# class RmTestCase(unittest.TestCase):
#     def test_rm(self):
#         # create a file
#         open('somefile.txt', 'a')
#         # try to delete it
#         rm('somefile.txt')
#         # check file if still exist
#         self.assertFalse(os.path.isfile('/somefile.txt'), 'failed to remove the file')

# if __name__== '__main__':
#     unittest.main()


# mocking test

class RmTestCase(unittest.TestCase):
    # in the following like mock will simulate os library in myModule
    @mock.patch('my_module.os')
    def test_rm(self, mock_os):
        rm("somefile1.txt")
        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("somefile1.txt")

if __name__ == '__main__':
    unittest.main()