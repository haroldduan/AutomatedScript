# -*- coding: utf-8 -*-


import os
from os import path
import inspect
import psutil
import logging
import jsonplus as json

class OS_Monitor(object):
    ''' OS monitor function class '''

    def __init__(self):
        self.__logger = self.__get_logger()
        pass
    
    def __get_logger(self):
        ''' Get logging Logger instance '''
        try:
            logger = logging.getLogger('[os_monitor_log')
            this_file = inspect.getfile(inspect.currentframe())
            dirpath = path.abspath(path.dirname(this_file))
            folder_path = path.join(dirpath, 'LOG')
            if not path.exists(folder_path):
                os.makedirs(folder_path)
            handler = logging.FileHandler(
                path.join(folder_path, 'os_monitor.log'))
            formatter = logging.Formatter(
                '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
            return logger
        except Exception, e:
            print e.message

    def __save_data_to_json(self,str_data):
        ''' Save data to json file '''
        try:
            print os.getcwd()
            # print str(str_data)
            print str_data
            with open('./data.json','w') as f:
                f.write(str_data)
            pass
        except Exception as e:
            self.__logger.exception(e)
        pass
    
    def get_cpu(self):
        ''' Get CPU info data '''
        try:
            cpu_info = psutil.cpu_times_percent()
            print str(cpu_info)
            print cpu_info
            pass
        except Exception as e:
            self.__logger.exception(e)
        pass
    
    def get_memory(self):
        ''' Get memory info data '''
        try:
            vir_memory = psutil.virtual_memory()
            print str(vir_memory)
            swap_memory = psutil.swap_memory()
            print str(swap_memory)
            pass
        except Exception as e:
            self.__logger.exception(e)
        pass

    def get_disks(self):
        ''' Get disks info data '''
        try:
            disk_partitions = psutil.disk_partitions()
            # print str(disk_partitions)
            # print json.dumps(disk_partitions,default=lambda obj: obj.__dic__)
            print json.dumps(disk_partitions)
            temp_str = json.dumps(disk_partitions)
            temp_obj = json.loads(temp_str)
            print str(temp_obj)
            self.__save_data_to_json(temp_str)
            pass
        except Exception as e:
            self.__logger.exception(e)
        pass

    def get_network(self):
        ''' Get CPU network data '''
        try:
            net_io_counters = psutil.net_io_counters()
            print str(net_io_counters)
            pass
        except Exception as e:
            self.__logger.exception(e)
        pass

    def get_process(self):
        ''' Get CPU process data '''
        try:
            pids = psutil.pids()
            print str(pids)
            pass
        except Exception as e:
            self.__logger.exception(e)
        pass

    pass