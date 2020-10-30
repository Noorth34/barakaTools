# coding:utf-8

import os
import shutil

class Path():

    def __init__(self):
        pass

    @staticmethod
    def isDir(path):

        return os.path.isdir(path)

    @staticmethod    
    def isFile(path):

        return os.path.isfile(path)

    @staticmethod
    def convertSlashToBackslash(path):

        path = path.replace("/", "\\")
        return path

    @staticmethod
    def convertBackslashToSlash(path):

        path = path.replace("\\", "/")
        return path

    @staticmethod
    def addExtension(path, ext):

        path = path + ext
        return path

    @staticmethod
    def deleteExtension(path):

        ext = "." + path.split(".")[-1]

        path = path.replace(ext, "")
        return path
