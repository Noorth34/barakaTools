#coding:utf-8

import os
import shutil
import modules.path as Path
reload(Path)


def isFile(func):
	def inside(path, *args):
		if Path.isFile(path) is False:
			raise TypeError("This path doesn't refer to a file")
			return
		func(path, *args)
	return inside


def createFile(path, name="_New_File"):

	path = path + "/" + name
	with open(path, "w+") as f:
		f.close()
	return path


@isFile
def copyTo(src=None, dest=None):

	return shutil.copy(src, dest)

@isFile
def moveTo(src=None, dest=None):

	return shutil.move(src, dest)


@isFile
def delete(path=None):

	return os.remove(path)

@isFile
def getShortFileName(path):

	return path.split("/")[-1]

@isFile
def getParent(path):

	return os.path.dirname(path)

@isFile
def getRecursiveParent(path, iteration=1):

	temp = None
	for i in range(iteration):
		temp = getParent(path)
		path = temp

	parent = path
	return parent

@isFile
def setHidden(path):

	backSlashPath = Path.convertSlashToBackslash(path)
	os.system( "attrib +h {}".format(backSlashPath) )

@isFile
def setVisible(path):

	backSlashPath = Path.convertSlashToBackslash(path)
	os.system( "attrib -h {}".format(backSlashPath) )

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