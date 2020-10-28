# coding:utf-8

import maya.cmds as cmds

def get():

	return cmds.ls(sl=True, ap=True)
