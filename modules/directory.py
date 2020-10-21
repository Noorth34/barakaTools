# coding:utf-8

import os
import shutil
import modules.path as Path


def isDir(func):
    def inside(path, *args):
        if Path.isDir(path) is False:
            raise TypeError("This path doesn't refer to a directory")
            return
        func(path, *args)
    return inside


def createDir(path, name="_New_Dir"):

    path = path + "/" + name
    os.mkdir(path)
    return path


def getChildren(path):

    return os.listdir(path)


@isDir
def copyTo(src=None, dest=None):

    return shutil.copy(src, dest)


@isDir
def moveTo(src=None, dest=None):

    return shutil.move(src, dest)


@isDir
def delete(path):

    return shutil.rmtree(path)


@isDir
def getShortDirName(path):

    return path.split("/")[-1]


@isDir
def getParent(path):

    return os.path.dirname(path)


@isDir
def getRecursiveParent(path, iteration=1):

    temp = None
    for i in range(iteration):
        temp = getParent(path)
        path = temp

    parent = path
    return parent


@isDir
def setHidden(path):

    backSlashPath = Path.convertSlashToBackslash(path)
    os.system("attrib +h {}".format(backSlashPath))


@isDir
def setVisible(path):

    backSlashPath = Path.convertSlashToBackslash(path)
    os.system("attrib -h {}".format(backSlashPath))
