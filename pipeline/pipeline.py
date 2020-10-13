#coding:utf-8

import json
import pymel.core as pm

class File:
	"""
	Functions for files management
	"""

class Path:
	"""
	Functions for path management
	"""

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