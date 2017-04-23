"""
Test suite for directory permissions checks as common user.
"""
import unittest
import subprocess, os
from constants import Constants
from utility import Utility
from test_directory_permission_as_root import DirectoryPermissionsAsRoot

log = Utility.Logtst.logger_init('Test directory permission as common user.')


class FilePermissionsAsCommonUsert(DirectoryPermissionsAsRoot):
    @classmethod
    def setUpClass(cls):
        log.info('Permissions tests as user')
        os.chdir(Constants.nfs_dir.client)
        cls.directory_names = Constants.lists.directory_names
        # expected results
        cls.expected_result_read = [True, False, False, True, False, False, False]
        cls.expected_result_write = [True, False, False, False, False, False, False]
        # Asign expected results to dictionary names
        cls.directread_expres_dict = dict(zip(cls.directory_names,
                                              cls.expected_result_read))
        cls.directwrite_expres_dict = dict(zip(cls.directory_names,
                                               cls.expected_result_write))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FilePermissionsAsCommonUsert)
    unittest.TextTestRunner(verbosity=2).run(suite)
