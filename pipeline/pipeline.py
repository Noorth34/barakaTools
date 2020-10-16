#coding:utf-8

import json
import os
import pymel.core.system as pms


class Path(object):
	"""
	Functions for path management
	"""
	def __init__(self, path):

		self.path = path

	def convertSlashToBackslash(self):

		self.path = self.path.replace("/", "\\")
		return self.path

	def convertBackslashToSlash(self):

		self.path = self.path.replace("\\", "/")
		return self.path

	def addExtension(self, ext):

		self.path = self.path + ext
		return self.path

	def deleteExtension(self):

		ext = "." + self.path.split(".")[-1]

		self.path = self.path.replace(ext, "")
		return self.path


	def getParent(self, path=None):
		
		if path is None:
			path = self.path

		return os.path.dirname(path)


	def getRecursiveParent(self, path=None, iteration=1):

		if path is None:
			path = self.path

		temp = None
		for i in range(iteration):
			temp = self.getParent(path)
			path = temp

		parent = path
		return parent


	def listChildren(self, path=None):

		if path is None:
			path = self.path
		
		return os.listdir(path)


	def isDir(self, path=None):

		if path is None:
			path = self.path

		return os.path.isdir(path)


	def isFile(self, path=None):
		
		if path is None:
			path = self.path

		return os.path.isfile(path)



class File(Path):
	"""
	Class for file management
	"""
	def __init__(self, path):
		super(File, self).__init__(path)


	def setHidden(self):

		backSlashPath = self.convertSlashToBackslash()
		os.system( "attrib +h {}".format(backSlashPath) )


	def setVisible(self):

		backSlashPath = self.convertSlashToBackslash()
		os.system( "attrib -h {}".format(backSlashPath) )


	def isHidden(self):
		pass


	def isVisible(self):
		pass


	def copyFileTo(self):
		pass


	def moveFileTo(self):
		pass


	def deleteFile(self):
		pass
		





class Scene(File):
	"""
	Class for maya scene management
	"""
	def __init__(self, path):
		super(Scene, self).__init__(path)

		self.asset = "asset"
		self.state = "state"
		self.type = "type"
		self.index = "index"


	def save(self, type):

		return pms.saveFile(type= type)

	def saveAs(self, dest):

		return pms.saveAs(dest)

	def exportSelection(self, dest, type):

		return pms.exportSelected(dest, type= type)

	def edit(self):
		pass


	# Setters
	
	def setAsset(self, name):

		self.asset = name

	def setState(self, state):

		self.state = state

	def setType(self, type):

		self.type= type

	def setIndex(self, index):
		
		self.index = index


	# Getters
	
	def getFullAssetName(self):

		return "{}_{}_{}_{}".format(self.asset, self.state, self.type, self.index)
	

	def getAsset(self):

		return self.asset
		
	def getState(self):

		return self.state

	def getType(self):

		return self.type

	def getIndex(self):

		return self.index



class Commit:
	"""
	Functions for JSON management 

	--> create commits and update logs
	"""
	def writeJson(data, filename="commits.json"):

		with open(filename, "w") as f:
			json.dump(data, f, indent=4)


	def commit():

		with open("commits.json") as f:
		
			data = json.load(f)
			temp = data["logs"]
			temp.append(commit)

		writeJson(data)