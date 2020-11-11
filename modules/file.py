# coding:utf-8

import os
import shutil
from modules.path import Path

class File():

    def __init__(self):
        pass

    # @staticmethod
    def is_file(func):
        def wrapper(path, *args, **kwargs):
            if Path.is_file(path) is False:
                raise TypeError("This path doesn't refer to a file")
            return func(path, *args, **kwargs)
        return wrapper

    @staticmethod
    def create(path, name="_New_File"):

        path = path + "/" + name
        with open(path, "w+") as f:
            f.close()
        return path

    @staticmethod
    @is_file
    def copy(src, dest):

        return shutil.copy(src, dest)

    @staticmethod
    @is_file
    def move(src=None, dest=None):

        return shutil.move(src, dest)

    @staticmethod
    @is_file
    def delete(path=None):

        return os.remove(path)

    @staticmethod
    @is_file
    def get_short_name(path):

        return path.split("/")[-1]

    @staticmethod
    @is_file
    def get_parent(path):

        parent = os.path.dirname(path)
        return parent

    @staticmethod
    @is_file
    def get_recursive_parent(path, iteration=1):

        temp = None
        for i in range(iteration):
            temp = get_parent(path)
            path = temp

        parent = path
        return parent

    @staticmethod
    @is_file
    def set_hidden(path):

        back_slash_path = Path.convert_slash_to_backslash(path)
        os.system("attrib +h {}".format(back_slash_path))

    @staticmethod
    @is_file
    def set_visible(path):

        back_slash_path = Path.convert_slash_to_backslash(path)
        os.system("attrib -h {}".format(back_slash_path))


"""
def isHidden(self):

	if self.visibility is True:
		return False
	else:
		return True


def isVisible(self):
	
	if self.visibility is True:
		return True
	else:
		return False
"""
