# coding:utf-8

import maya.cmds as cmds

class Selection:

	def __init__(self):
		pass

	@staticmethod
	def get():

		return cmds.ls(sl=True, ap=True)
