"""
Starter script. All test will be executed after running this one.
"""
from constants import Constants
import os, subprocess
from utility import Utility

log = Utility.Logtst.logger_init('Test runner.')


class TestRunner():
    @staticmethod
    def setUpModuleForFileWork():
        os.system('chmod 777 ' + Utility.where_am_i() + '/*')
        os.chdir(Constants.nfs_dir.server)
        permissions = Constants.lists.permissions
        for index, file_name in enumerate(Utility.gen(Constants.lists.file_names)):
            file_create_cmd = ['touch', file_name]
            subprocess.call(file_create_cmd)
            chmod_cmd = ['chmod', permissions[index], file_name]
            subprocess.call(chmod_cmd)

    @staticmethod
    def setUpModuleForDirectoryWork():
        os.chdir(Constants.nfs_dir.server)
        permissions = Constants.lists.permissions
        for index, directory in enumerate(Utility.gen(Constants.lists.directory_names)):
            direct_create_cmd = ['mkdir', directory]
            subprocess.call(direct_create_cmd)
            chmod_cmd = ['chmod', permissions[index], directory]
            subprocess.call(chmod_cmd)
            file_path = './' + directory + '/file'
            file_create_cmd = ['touch', file_path]
            subprocess.call(file_create_cmd)
            chmod_cmd = ['chmod', '777', file_path]
            subprocess.call(chmod_cmd)

    @staticmethod
    def tearDownModule():
        os.system('rm -rf ' + Constants.nfs_dir.server + '/*')

    @staticmethod
    def pass_script():
        remote_host = Constants.User.sudoer + '@' + Constants.ip.client + \
                      ':' + Constants.nfs_dir.script_on_client
        rsync_cmd = ['rsync', '-r', Utility.where_am_i() + '/', remote_host]
        out_msg, err_msg, exitcode = Utility.subpr_cmd(rsync_cmd)
        print out_msg, err_msg

    @staticmethod
    def setUpWrap(func):
        TestRunner.setUpModuleForFileWork()
        func()
        TestRunner.tearDownModule()

    @staticmethod
    def execute_permission_test_as_root(script_name):
        remoteclient = Constants.User.sudoer + '@' + Constants.ip.client
        script_path = Constants.nfs_dir.script_on_client + '/' + script_name
        python_cmd = '\"sudo python2.7 ' + script_path + '\"'
        subpr_cmd = ('ssh -t ' + remoteclient + ' ' + python_cmd)
        os.system(subpr_cmd)

    @staticmethod
    def execute_permission_test_as_user(script_name):
        remoteclient = Constants.User.sudoer + '@' + Constants.ip.client
        script_path = Constants.nfs_dir.script_on_client + '/' + script_name
        python_cmd = 'python2.7' + ' ' + script_path
        subpr_cmd = ['ssh', remoteclient, python_cmd]
        out_msg, err_msg, exitcode = Utility.subpr_cmd(subpr_cmd)
        print out_msg, err_msg

    @staticmethod
    def run_tests():
        # Execute file script for root
        TestRunner.setUpModuleForFileWork()
        TestRunner.execute_permission_test_as_root(
            Constants.tests.file_permissions_root)
        TestRunner.tearDownModule()
        # execute directory script for user
        TestRunner.setUpModuleForFileWork()
        TestRunner.execute_permission_test_as_user(
            Constants.tests.file_permissions_user)
        TestRunner.tearDownModule()
        # Execute directory script for root
        TestRunner.setUpModuleForDirectoryWork()
        TestRunner.execute_permission_test_as_root(
            Constants.tests.directory_permissions_root)
        TestRunner.tearDownModule()
        # execute directory script for user
        TestRunner.setUpModuleForDirectoryWork()
        TestRunner.execute_permission_test_as_user(
            Constants.tests.directory_permissions_user)
        TestRunner.tearDownModule()

    @staticmethod
    def transfer_logs():
        remoteclient = Constants.User.sudoer + '@' + Constants.ip.client
        script_path = Constants.nfs_dir.script_on_client + '/' + Constants.tests.transfer_logs
        python_cmd = 'python2.7' + ' ' + script_path
        subpr_cmd = ['ssh', remoteclient, python_cmd]
        out_msg, err_msg, exitcode = Utility.subpr_cmd(subpr_cmd)
        print out_msg, err_msg

    @staticmethod
    def result_transfer():
        """Final function in module will collect all valuable logs and tranfer it back"""
        try:
            TestRunner.transfer_logs()
            Utility.Logtst.debug_log(log, 'Logs where transfered to sever! Script successed!')
        except:
            Utility.Logtst.debug_log(log, 'Attention! Fail to transfer logs to server! HALP!')

    @staticmethod
    def main():
        TestRunner.pass_script()
        TestRunner.run_tests()
        TestRunner.result_transfer()


if __name__ == '__main__':
    log.info('Start test.')
    TestRunner.main()
