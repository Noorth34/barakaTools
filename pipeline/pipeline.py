#coding:utf-8

import json
import os
import shutil
import pymel.core.system as pms
import modules.path as Path
reload(Path)



class PathString(object):
	"""
	Functions for path management
	"""
	def __init__(self, path):

		self.path = path


	def setPath(self, path):
		
		 self.path = path
		 return self.path


	def getPath(self):

		return self.path


	def createInnerFile(self, file="_New_File"):

		with open(self.path + "/" + file, "w+") as f:
			f.close()
		

	def createInnerDir(self, dir="_New_Directory"):

		return os.mkdir(self.path + "/" + dir)


	


class File(PathString):
	"""
	Class for file management
	"""
	def __init__(self, path):
		super(File, self).__init__(path)

		self.visibility = True
		
	def getLongFileName(self):

		return self.path

	def getShortFileName(self):

		return self.path.split("/")[-1]

	def setHidden(self):

		backSlashPath = self.convertSlashToBackslash()
		os.system( "attrib +h {}".format(backSlashPath) )
		self.visibility = False

	def setVisible(self):

		backSlashPath = self.convertSlashToBackslash()
		os.system( "attrib -h {}".format(backSlashPath) )
		self.visibility = True


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


	def copyFileTo(self, src=None, dest=None):
		
		if src is None:
			src = self.path

		if dest is None:
			dest = self.path

		return shutil.copy(src, dest)


	def moveFileTo(self, src=None, dest=None):
		
		if src is None:
			src = self.path

		if dest is None:
			dest = self.path

		return shutil.move(src, dest)


	def deleteFile(self, path=None):
		
		if path is None:
			path = self.path

		os.remove(path)





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



		