#coding:utf-8

import os
import shutil
import modules.path as Path


def createInnerFile(parent, file="_New_File"):

		with open(parent + "/" + file, "w+") as f:
			f.close()
		

def createInnerDir(parent, dir="_New_Directory"):

	return os.mkdir(parent + "/" + dir)


def copyFileTo(src=None, dest=None):

	return shutil.copy(src, dest)


def moveFileTo(src=None, dest=None):

	return shutil.move(src, dest)


def delete(path=None):

	return os.remove(path)


def getShortFileName(file):

	return file.split("/")[-1]


def setHidden(file):

	backSlashPath = Path.convertSlashToBackslash(file)
	os.system( "attrib +h {}".format(backSlashPath) )


def setVisible(file):

	backSlashPath = Path.convertSlashToBackslash(file)
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