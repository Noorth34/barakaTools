# coding:utf-8

import os
import shutil
from modules.path import Path

class Directory():

    def __init__(self):
        pass

    def is_dir(func):
        def wrapper(path, *args):
            if Path.is_dir(path) is False:
                raise TypeError("This path doesn't refer to a directory")
                return
            func(path, *args)
        return wrapper

    @staticmethod
    def create(path, name="_New_Dir"):

        path = path + "/" + name
        os.mkdir(path)
        return path

    @staticmethod
    def get_children(path):

        return os.listdir(path)

    @staticmethod
    @is_dir
    def copy(src, dest):

        return shutil.copytree(src, dest)


    @staticmethod
    @is_dir
    def move(src, dest):

        return shutil.move(src, dest)


    @staticmethod
    @is_dir
    def delete(path):

        return shutil.rmtree(path)


    @staticmethod
    @is_dir
    def get_short_name(path):

        return path.split("/")[-1]


    @staticmethod
    @is_dir
    def get_parent(path):

        return os.path.dirname(path)


    @staticmethod
    @is_dir
    def get_recursive_parent(path, iteration=1):

        temp = None
        for i in range(iteration):
            temp = get_parent(path)
            path = temp

        parent = path
        return parent


    @staticmethod
    @is_dir
    def set_hidden(path):

        back_slash_path = Path.convert_slash_to_backslash(path)
        os.system("attrib +h {}".format(back_slash_path))


    @staticmethod
    @is_dir
    def set_visible(path):

        back_slash_path = Path.convert_slash_to_backslash(path)
        os.system("attrib -h {}".format(back_slash_path))
