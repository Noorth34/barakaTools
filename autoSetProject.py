# coding:utf-8

__author__ = "Gabriel Vidal"

import pymel.core as pm
import pymel.core.system as pms
import maya.cmds as cmds
import os
import maya.OpenMaya as om


def checkWorkspace(limit=10):

	workspace = None
	scenePath = cmds.file(q=True, sn=True)
	dir = os.path.dirname(scenePath)

	for i in range(limit):
		if "workspace.mel" in os.listdir(dir):
			workspace = dir
			break
		else:
			dir = os.path.dirname(dir)

	return workspace


def setProject():

	workspace = checkWorkspace()

	if workspace:
		pm.mel.setProject(workspace)
		print("Project set to : {}".format(workspace))
		cmds.inViewMessage( amg='Project Changed to: \n <hl>' + workspace + '</hl>.', pos='topCenter', fade=True )


def main():
	setProject()
	

