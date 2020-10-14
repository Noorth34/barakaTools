#coding:utf-8

import json
import os
import pymel.core.system as pms

class File():
	"""
	Class for file management
	"""
	def __init__(self, path):
		self.path = path

	def setHidden(self):

		backSlashPath = self.path.replace("/", "\\")
		os.system( "attrib +h {}".format(backSlashPath) )


	def setVisible(self):

		backSlashPath = self.path.replace("/", "\\")
		os.system( "attrib -h {}".format(backSlashPath) )


class Scene():
	"""
	Class for maya scene management
	"""
	def __init__(self):

		self.scene = pms.sceneName()


	def getLongSceneName(self):

		return self.scene

	def getShortSceneName(self):

		return self.scene.split("/")[-1]

	def getNoExtensionShortSceneName(self):

		return self.scene.getShortSceneName().split(".")[0]

	def saveScene(self, type):

		return pms.saveFile(type= type)

	def saveSceneAs(self, dest):

		return pms.saveAs(dest)

	def exportSelection(self, dest, type):

		return pms.exportSelected(dest, type= type)


class Asset():
	"""
	"""
	def __init__(self):
		
		self.elements = ["asset", "state", "type", "index"]

		
		#self.asset = self.elements[0]
		#self.state = self.elements[1]
		#self.type = self.elements[2]
		#self.index = self.elements[-1]

	def getFullAssetName(self):

		return "_".join(self.elements)

	def setAsset(self, name):

		self.elements[0] = name

	def setState(self, state):

		self.elements[1] = state

	def setType(self, type):

		self.elements[2] = type

	def setIndex(self, index):
		
		self.elements[3] = index


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

	def setIndex(self):
		"""
		"""






class Commit():
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