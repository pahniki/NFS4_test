"""
Logs transering class. Is the last stage of all script module working process.
If logs transfer action passed without error will self clean working space for client pc
"""

from utility import Utility
from constants import Constants
import os

log = Utility.Logtst.logger_init('Logs transfer.')


def transfer_logs():
    logfiles_list = list()
    self_log_path = Utility.where_am_i() + Constants.log_file_name
    remote_host = Constants.User.root + '@' + Constants.ip.server + \
                  ':' + Constants.nfs_dir.script_on_client
    logfiles_list.append(self_log_path)

    logfile = '/var/log/messages'
    try:
        excode = os.path.isfile(logfile)
        if (excode):
            logfiles_list.append(logfile)
    except:
        Utility.Logtst.debug_log(log, 'can\'t get a {} file'.format(logfile))
    logfile = '/var/log/syslog'
    try:
        excode = os.path.isfile(logfile)
        if (excode):
            logfiles_list.append(logfile)
    except:
        Utility.Logtst.debug_log(log, 'can\'t get a {} file'.format(logfile))
    logfile = '/var/log/kern.log'
    try:
        excode = os.path.isfile(logfile)
        if (excode):
            logfiles_list.append(logfile)
    except:
        Utility.Logtst.debug_log(log, 'can\'t get a {} file'.format(logfile))
    print logfiles_list
    rsync_cmd = ['rsync', '-rP'] + logfiles_list + [remote_host, ]
    out_msg, err_msg, exitcode = Utility.subpr_cmd(rsync_cmd)
    Utility.Logtst.info_log(log, out_msg + err_msg)
    if (not exitcode):
        Utility.cleanWorkSpace()


transfer_logs()
