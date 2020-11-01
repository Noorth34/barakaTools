# coding:utf-8

import os
import shutil
from modules.path import Path

class Directory():

    def __init__(self):
        pass

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

    @staticmethod
    @isDir
    def copy(src, dest):

        return shutil.copytree(src, dest)


    @staticmethod
    @isDir
    def move(src, dest):

        return shutil.move(src, dest)


    @staticmethod
    @isDir
    def delete(path):

        return shutil.rmtree(path)


    @staticmethod
    @isDir
    def getShortName(path):

        return path.split("/")[-1]


    @staticmethod
    @isDir
    def getParent(path):

        return os.path.dirname(path)


    @staticmethod
    @isDir
    def getRecursiveParent(path, iteration=1):

        temp = None
        for i in range(iteration):
            temp = getParent(path)
            path = temp

        parent = path
        return parent


    @staticmethod
    @isDir
    def setHidden(path):

        backSlashPath = Path.convertSlashToBackslash(path)
        os.system("attrib +h {}".format(backSlashPath))


    @staticmethod
    @isDir
    def setVisible(path):

        backSlashPath = Path.convertSlashToBackslash(path)
        os.system("attrib -h {}".format(backSlashPath))
