# -*- coding: utf-8 -*-

import os
from os import path
import inspect
import sys
import logging
import json
import win32api
import win32ui
import win32con
import win32print
import tempfile

class Printer(object):
    ''' Windows print service class '''

    def __init__(self):
        self.__logger = self.__get_logger()
        self.__config = self.__init_config()
        # self.__get_files()
        pass

    def __init_config(self):
        ''' Init print service configurations '''
        try:
            result = self.__get_data_by_json(
                path.join(path.dirname(__file__), 'config.json'))
            return result
        except Exception, e:
            self.__logger.exception(e.message)
        pass

    def __get_data_by_json(self, file):
        ''' Get data by json file '''
        try:
            with open(file, 'r') as f:
                configs = json.load(f)
                return configs
        except Exception, e:
            self.__logger.exception(e.message)

    def __get_logger(self):
        ''' Get logging Logger instance '''
        try:
            logger = logging.getLogger('[print_log')
            this_file = inspect.getfile(inspect.currentframe())
            dirpath = path.abspath(path.dirname(this_file))
            folder_path = path.join(dirpath, 'LOG')
            if not path.exists(folder_path):
                os.makedirs(folder_path)
            handler = logging.FileHandler(
                path.join(folder_path, 'print_log.log'))
            formatter = logging.Formatter(
                '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
            return logger
        except Exception, e:
            print(e.message)

    def __get_files(self):
        try:
            if self.__config:
                cur_path = self.__config["dir_path"] if self.__config["dir_path"] else \
                    os.path.abspath(os.path.dirname(__file__))
                print cur_path
                all_files = os.listdir(cur_path)
                exts = self.__config["file_exts_in"]
                names = self.__config["file_name_in"]
                # prefixs = map(lambda x: os.path.splitext(x)[0],all_files)
                # suffixs = map(lambda x: os.path.splitext(x)[1],all_files)
                temp = filter(lambda f: True if not exts else os.path.splitext(f)[
                              1] in exts, all_files)
                files = filter(lambda f: True if not names else os.path.splitext(f)[
                               0] in names, temp)
                return files
            pass
        except Exception as e:
            raise e
        pass

    def __print(self):
        try:
            print_files = self.__get_files()
            if print_files:
                for f in print_files:
                    temp = path.join(self.__config["dir_path"], f)
                    win32api.ShellExecute(
                        0, 'print', temp, win32print.GetDefaultPrinterW(), ".", 0)
                    # win32api.ShellExecute(
                    #     0, 'print', f, win32print.GetDefaultPrinterW(), ".", 0)
            pass
        except Exception as e:
            raise e
        pass

    def run(self):
        try:
            self.__print()
            pass
        except Exception as e:
            raise e
        pass

# class Filer(object):
#     ''' Windows file operator class '''

#     def __init__(self):

#         pass


