# coding:utf-8

import os
import shutil

class Path():

    def __init__(self):
        pass

    @staticmethod
    def is_dir(path):

        return os.path.isdir(path)

    @staticmethod    
    def is_file(path):

        return os.path.isfile(path)

    @staticmethod
    def convert_slash_to_backslash(path):

        path = path.replace("/", "\\")
        return path

    @staticmethod
    def convert_backslash_to_slash(path):

        path = path.replace("\\", "/")
        return path

    @staticmethod
    def add_extension(path, ext):

        path = path + ext
        return path

    @staticmethod
    def delete_extension(path):

        ext = "." + path.split(".")[-1]

        path = path.replace(ext, "")
        return path
