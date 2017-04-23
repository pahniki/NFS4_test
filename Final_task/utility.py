from subprocess import PIPE, Popen
import os, sys
from constants import Constants


class Utility():
    """Utility class with useful for development methods"""

    @staticmethod
    def gen(some_obj):
        for item in some_obj:
            yield item

    @staticmethod
    def where_am_i():
        return os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def subpr_cmd(command):
        exec_cmd = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        out_msg, err_msg = exec_cmd.communicate()
        exitcode = exec_cmd.returncode

        return (out_msg, err_msg, exitcode)

    @staticmethod
    def decor_ssh_connection_decor(username):
        def ssh_connection_decorator(func):
            def wrapper():
                os.system('ssh ' + username + Constants.ip.server)
                func()
                os.system('exit')

            return wrapper

        return ssh_connection_decorator

    @staticmethod
    def cleanWorkSpace():
        os.system('rm -rf ' + Utility.where_am_i())

    class Logtst:
        '''
            Custom logger to store all rsync wrapper actions.
        '''

        @staticmethod
        def logger_init(some_str):
            ''' Initialise new logger '''
            import logging
            logger = logging.getLogger(some_str)
            logger.setLevel(logging.INFO)
            logger.setLevel(logging.DEBUG)
            handler = logging.FileHandler(Utility.where_am_i() + Constants.log_file_name)
            formatter = logging.Formatter('[%(asctime)s] - %(name)11s - %(levelname)6s : %(message)s',
                                          datefmt='%d-%m-%y %H:%M')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            consoleHandler = logging.StreamHandler(sys.stdout)
            logger.addHandler(consoleHandler)
            return logger

        @staticmethod
        def info_log(logger, infostr):
            ''' Log info message '''
            logger.info(infostr)

        @staticmethod
        def debug_log(logger, infostr):
            ''' Log debug message '''
            logger.debug(infostr)

        @staticmethod
        def error_msg(logger, err_msg, info_msg=''):
            """Universal error message.
                Allows u to post messages in both Debug and Info level of logger
                and exit program if needed.
                """
            if (info_msg):
                Utility.tstlog.info_log(logger, info_msg)
            if (err_msg):
                Utility.tstlog.debug_log(logger, err_msg)
