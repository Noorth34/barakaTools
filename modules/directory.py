#coding:utf-8

import os
import shutil
import modules.path as Path


def createDir(path, name="_New_Dir"):

	path = path + "/" + name
	os.mkdir(path)
	return path


def getChildren(path):
	
	return os.listdir(path)