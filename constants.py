"""
Variables for the script.
"""

class Constants():
    log_file_name = '/nfs_test_logs.log'

    class nfs_dir():
        server = '/mnt/public_nfs'
        client = '/mnt/nfs'
        script_on_client = '/tmp/nfs_testing'

    class ip():
        server = '192.168.182.2'
        client = '192.168.182.5'

    class User():
        sudoer = 'nikita'
        root = 'root'

    class lists():
        permissions = ['777', '770', '700', '444', '440', '400', '000']
        directory_names = ['d.{}'.format(item) for item in permissions]
        file_names = ['f.{}'.format(item) for item in permissions]

    class tests():
        file_permissions_root = 'test_files_permission_as_root.py'
        file_permissions_user = 'test_files_permission_as_user.py'
        directory_permissions_root = 'test_directory_permission_as_root.py'
        directory_permissions_user = 'test_directory_permission_as_user.py'
        transfer_logs = 'transfer_logs.py'
