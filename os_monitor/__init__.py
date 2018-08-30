# -*- coding: utf-8 -*-
#
#
# Author Harold.Duan
# This module is os monitor script.

import sys

import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
from os_monitor import OS_Monitor 

if __name__ == '__main__':
    monitor = OS_Monitor()
    # monitor.get_cpu()
    monitor.get_disks()
    pass