"""
Test suite for file permissions checks as common user.
"""
import unittest
import subprocess, os
from constants import Constants
from utility import Utility
from test_files_permission_as_root import FilePermissionsAsRoot

log = Utility.Logtst.logger_init('Test files permission as common user.')


class FilePermissionsAsCommonUser(FilePermissionsAsRoot):
    @classmethod
    def setUpClass(cls):
        log.info('Permissions tests as common user')
        os.chdir(Constants.nfs_dir.client)
        cls.file_names = Constants.lists.file_names
        # expected results
        cls.expected_result_read = [True, False, False, True, False, False, False]
        cls.expected_result_write = [True, False, False, False, False, False, False]
        # Asign expected results to file names
        cls.expected_result_read_dict = dict(zip(cls.file_names, cls.expected_result_read))
        cls.expected_result_write_dict = dict(zip(cls.file_names, cls.expected_result_write))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FilePermissionsAsCommonUser)
    unittest.TextTestRunner(verbosity=2).run(suite)
