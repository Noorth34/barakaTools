#coding:utf-8

import os
import shutil

def createFile(path, name="_New_File"):

	path = path + "/" + name
	with open(path, "w+") as f:
		f.close()
	return path


def createDir(path, name="_New_Dir"):

	path = path + "/" + name
	os.mkdir(path)
	return path


def getParent(path):

	return os.path.dirname(path)


def getRecursiveParent(path, iteration=1):

	temp = None
	for i in range(iteration):
		temp = getParent(path)
		path = temp

	parent = path
	return parent


def getChildren(path):
	
	return os.listdir(path)


def isDir(path):

	return os.path.isdir(path)


def isFile(path):

	return os.path.isfile(path)


def convertSlashToBackslash(path):

	path = path.replace("/", "\\")
	return path


def convertBackslashToSlash(path):

	path = path.replace("\\", "/")
	return path


def addExtension(path, ext):

	path = path + ext
	return path


def deleteExtension(path):

	ext = "." + path.split(".")[-1]

	path = path.replace(ext, "")
	return path