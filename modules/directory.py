# coding:utf-8

import os
import shutil
from modules.path import Path

class Directory():

    def __init__(self):
        pass

    @staticmethod
    def isDir(func):
        def inside(path, *args):
            if Path.isDir(path) is False:
                raise TypeError("This path doesn't refer to a directory")
                return
            func(path, *args)
        return inside

    @staticmethod
    def create(path, name="_New_Dir"):

        path = path + "/" + name
        os.mkdir(path)
        return path

    @staticmethod
    def getChildren(path):

        return os.listdir(path)


    @isDir
    @staticmethod
    def copy(src, dest):

        return shutil.copytree(src, dest)


    @isDir
    @staticmethod
    def move(src, dest):

        return shutil.move(src, dest)


    @isDir
    @staticmethod
    def delete(path):

        return shutil.rmtree(path)


    @isDir
    @staticmethod
    def getShortName(path):

        return path.split("/")[-1]


    @isDir
    @staticmethod
    def getParent(path):

        return os.path.dirname(path)


    @isDir
    @staticmethod
    def getRecursiveParent(path, iteration=1):

        temp = None
        for i in range(iteration):
            temp = getParent(path)
            path = temp

        parent = path
        return parent


    @isDir
    @staticmethod
    def setHidden(path):

        backSlashPath = Path.convertSlashToBackslash(path)
        os.system("attrib +h {}".format(backSlashPath))


    @isDir
    @staticmethod
    def setVisible(path):

        backSlashPath = Path.convertSlashToBackslash(path)
        os.system("attrib -h {}".format(backSlashPath))
