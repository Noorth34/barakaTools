# coding:utf-8

import pymel.core as pm
import pymel.core.system as pms
import maya.cmds as cmds
import os
import maya.OpenMaya as om


def checkWorkspace(limit=10):

	workspace = None
	scenePath = str( pms.sceneName() )
	dir = os.path.dirname(scenePath)

	try:
		for i in range(limit):
			if "workspace.mel" in os.listdir(dir):
				workspace = dir
				break
			else:
				dir = os.path.dirname(dir)
	except:
		cmds.warning("No workspace.mel found in hierarchy. Project set to default.")
		workspace = "C:/Users/{}/Documents/maya/projects/default".format(os.environ['username'])

	return workspace


def setProject():

	workspace = checkWorkspace()

	if workspace:
		pm.mel.setProject(workspace)
		print("Project set to : {}".format(workspace))
		cmds.inViewMessage( amg='Project Changed to: \n <hl>' + workspace + '</hl>.', pos='topCenter', fade=True )


def main():
	setProject()
	

