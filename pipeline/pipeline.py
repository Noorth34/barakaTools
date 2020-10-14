#coding:utf-8

import json
import os
import pymel.core.system as pms


class Path():
	"""
	Functions for path management
	"""
	def __init__(self, path):

		self.path = path

	def convertSlashToBackslash(self):

		return self.path.replace("/", "\\")

	def convertBackslashToSlash(self):

		return self.path.replace("\\", "/")

	def addExtension(self, ext):

		self.path = self.path + ext
		return self.path

	def deleteExtension(self):

		ext = "." + self.path.split(".")[-1]

		self.path = self.path.replace(ext, "")
		return self.path


class File(Path):
	"""
	Class for file management
	"""
	def __init__(self, path):

		Path.__init__(self, path)

	def setHidden(self):

		backSlashPath = self.path.replace("/", "\\")
		os.system( "attrib +h {}".format(backSlashPath) )


	def setVisible(self):

		backSlashPath = self.path.replace("/", "\\")
		os.system( "attrib -h {}".format(backSlashPath) )



class Asset():
	"""
	"""
	def __init__(self):
		
		self.elements = ["asset", "state", "type", "index"]

	# Setters
	
	def setAsset(self, name):

		self.elements[0] = name

	def setState(self, state):

		self.elements[1] = state

	def setType(self, type):

		self.elements[2] = type

	def setIndex(self, index):
		
		self.elements[3] = index


	# Getters

	def getFullAssetName(self):

		return "_".join(self.elements)

	def getAsset(self):

		return self.elements[0]
		
	def getState(self):

		return self.elements[1]

	def getType(self):

		return self.elements[2]

	def getIndex(self):

		return self.elements[3]




class Scene():
	"""
	Class for maya scene management
	"""
	def __init__(self):

		pass


	def save(self, type):

		return pms.saveFile(type= type)

	def saveAs(self, dest):

		return pms.saveAs(dest)

	def exportSelection(self, dest, type):

		return pms.exportSelected(dest, type= type)

	def edit(self):
		"""
		"""





class Commit(File):
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