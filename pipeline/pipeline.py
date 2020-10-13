#coding:utf-8

import json
import os
import pymel.core as pm

class File():
	"""
	Functions for files management
	"""
	def __init__(self, path):
		self.path = path

	def setHidden(self):

		backSlashPath = self.path.replace("/", "\\")
		os.system( "attrib +h {}".format(backSlashPath) )


	def setVisible(self):

		backSlashPath = self.path.replace("/", "\\")
		os.system( "attrib -h {}".format(backSlashPath) )




class Path():
	"""
	Functions for path management
	"""
	def stringConvertSlash(src, dest):

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