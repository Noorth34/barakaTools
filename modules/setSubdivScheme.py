# coding: utf-8

# Author: Gabriel Vidal

###
# Script to set on selected meshes the rman subdiv_scheme attr on "Catmull-Clark"
###

import sys
import maya.cmds as cmds

sel = cmds.ls(sl=True, ap=True)

for i in sel:
	shape = cmds.listRelatives(i, shapes=True, path=True)[0]
	if cmds.objectType( , isType="mesh"):
		try:
			cmds.setAttr("{}.rman_subdivScheme".format(shape), 1)
		except:
			sys.stderr("No RMAN attributes found. Please load RMAN plugin and assign a shader on object.")
