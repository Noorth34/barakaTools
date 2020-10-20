#coding:utf-8

import json
import os
import shutil
import pymel.core.system as pms
import modules.path as Path
reload(Path)



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
	
	def getSceneName(self):

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



		