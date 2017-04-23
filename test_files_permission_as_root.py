"""
Test suite for files permissions checks as root user.
"""
import unittest
import os
from constants import Constants
from utility import Utility

log = Utility.Logtst.logger_init('Test files permission as root user.')


class FilePermissionsAsRoot(unittest.TestCase):
    """First test class."""

    @classmethod
    def setUpClass(cls):
        log.info('Permissions tests as root')
        os.chdir(Constants.nfs_dir.client)
        cls.file_names = Constants.lists.file_names
        # expected results
        cls.expected_result_read = [True, True, True, True, True, True, True]
        cls.expected_result_write = [True, True, True, True, True, True, True]
        # Asign expected results to file names
        cls.expected_result_read_dict = dict(zip(cls.file_names, cls.expected_result_read))
        cls.expected_result_write_dict = dict(zip(cls.file_names, cls.expected_result_write))

    def testFileCreationIsSuccess(self):
        """Test if file exists"""
        log.info(self.testFileCreationIsSuccess.__name__)
        for file_name in Utility.gen(self.file_names):
            excode = os.path.isfile(file_name)
            if (excode):
                Utility.Logtst.debug_log(log, 'File {} exist: Yes'.format(file_name))
            else:
                Utility.Logtst.debug_log(log, 'File {} exist: No'.format(file_name))
                raise EOFError('No such file {}'.format(file_name))

    def testReadFiles(self):
        """Test if read from file is allowed"""
        log.info(self.testReadFiles.__name__)
        for file_name in Utility.gen(self.file_names):
            try:
                f = open(file_name, 'r')
                f.close()
                actual_result = True
            except:
                actual_result = False
            if (actual_result == self.expected_result_read_dict[file_name]):
                Utility.Logtst.debug_log(log, 'Reading file {} : Success'.format(file_name))
            else:
                Utility.Logtst.debug_log(log, 'Reading file {} : Failure'.format(file_name))
                raise EOFError('Permission denied for file {}'.format(file_name))

    def testWriteFiles(self):
        """Test if write in file is allowed"""
        log.info(self.testWriteFiles.__name__)
        for file_name in Utility.gen(self.file_names):
            try:
                f = open(file_name, 'w+')
                f.close()
                actual_result = True
            except IOError:
                actual_result = False
            if (actual_result == self.expected_result_write_dict[file_name]):
                Utility.Logtst.debug_log(log, 'Writing into file {} : Success'.format(file_name))
            else:
                Utility.Logtst.debug_log(log, 'Writing into file {} : Failure'.format(file_name))
                raise EOFError('Permission denied for file {}'.format(file_name))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FilePermissionsAsRoot)
    unittest.TextTestRunner(verbosity=2).run(suite)
