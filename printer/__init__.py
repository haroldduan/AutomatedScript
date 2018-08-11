# -*- coding: utf-8 -*-
# Copyright 2018, AVATech
#
# Author Harold.Duan
# This module is windows print script.

import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
# sys.path.append('../printer')
from printer import Printer

if __name__ == '__main__':
    printer = Printer()
    printer.run()
    pass
