"""
Test suite for directory permissions checks as root user.
"""
import unittest
import os
from constants import Constants
from utility import Utility

log = Utility.Logtst.logger_init('Test directory permission as root user.')


class DirectoryPermissionsAsRoot(unittest.TestCase):
    """First test class."""

    @classmethod
    def setUpClass(cls):
        log.info('Permissions tests as root')
        os.chdir(Constants.nfs_dir.client)
        cls.directory_names = Constants.lists.directory_names
        # expected results
        cls.expected_result_read = [True, True, True, True, True, True, True]
        cls.expected_result_write = [True, True, True, True, True, True, True]
        # Asign expected results to dictionary names
        cls.directread_expres_dict = dict(zip(cls.directory_names,
                                              cls.expected_result_read))
        cls.directwrite_expres_dict = dict(zip(cls.directory_names,
                                               cls.expected_result_write))

    def testDirectCreationIsSuccess(self):
        """Test if directory exists"""
        log.info(self.testDirectCreationIsSuccess.__name__)
        for directory in Utility.gen(self.directory_names):
            excode = os.path.isdir(directory)
            if (excode):
                Utility.Logtst.debug_log(log, 'Directory {} exist: Yes'.format(directory))
            else:
                Utility.Logtst.debug_log(log, 'Directory {} exist: No'.format(directory))
                raise EOFError('No such directory {}'.format(directory))

    def testReadDirect(self):
        """Test if directory is readable"""
        log.info(self.testReadDirect.__name__)
        for directory in Utility.gen(self.directory_names):
            # We are working with file in directory
            file_in_directory = directory + '/file'
            try:
                f = open(file_in_directory, 'r')
                f.close()
                actual_result = True
            except OSError:
                actual_result = False
            if (actual_result == self.directread_expres_dict[directory]):
                Utility.Logtst.debug_log(log, 'Reading directory {} : Success'.format(directory))
            else:
                Utility.Logtst.debug_log(log, 'Reading directory {} : Failure'.format(directory))
                raise EOFError('Permission denied for directory {}'.format(directory))

    def testWriteDirect(self):
        """Test if directory is writable"""
        log.info(self.testWriteDirect.__name__)
        for directory in Utility.gen(self.directory_names):
            # We are working with file in directory
            file_in_directory = directory + '/file'
            try:
                f = open(file_in_directory, 'w+')
                f.close()
                actual_result = True
            except:
                actual_result = False
            if (actual_result == self.directwrite_expres_dict[directory]):
                Utility.Logtst.debug_log(log, 'Writing into directory {} : Success'.format(directory))
            else:
                Utility.Logtst.debug_log(log, 'Writing into directory {} : Failure'.format(directory))
                raise EOFError('Permission denied for directory {}'.format(directory))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DirectoryPermissionsAsRoot)
    unittest.TextTestRunner(verbosity=2).run(suite)
