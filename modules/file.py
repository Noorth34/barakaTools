# coding:utf-8

import os
import shutil
from modules.path import Path

class File():

    def __init__(self):
        pass

    # @staticmethod
    def isFile(func):
        def inside(path, *args, **kwargs):
            if Path.isFile(path) is False:
                raise TypeError("This path doesn't refer to a file")
            return func(path, *args, **kwargs)
        return inside

    @staticmethod
    def create(path, name="_New_File"):

        path = path + "/" + name
        with open(path, "w+") as f:
            f.close()
        return path

    @staticmethod
    @isFile
    def copy(src, dest):

        return shutil.copy(src, dest)

    @staticmethod
    @isFile
    def move(src=None, dest=None):

        return shutil.move(src, dest)

    @staticmethod
    @isFile
    def delete(path=None):

        return os.remove(path)

    @staticmethod
    @isFile
    def getShortName(path):

        return path.split("/")[-1]

    @staticmethod
    @isFile
    def getParent(path):

        parent = os.path.dirname(path)
        return parent

    @staticmethod
    @isFile
    def getRecursiveParent(path, iteration=1):

        temp = None
        for i in range(iteration):
            temp = getParent(path)
            path = temp

        parent = path
        return parent

    @staticmethod
    @isFile
    def setHidden(path):

        backSlashPath = Path.convertSlashToBackslash(path)
        os.system("attrib +h {}".format(backSlashPath))

    @staticmethod
    @isFile
    def setVisible(path):

        backSlashPath = Path.convertSlashToBackslash(path)
        os.system("attrib -h {}".format(backSlashPath))


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
