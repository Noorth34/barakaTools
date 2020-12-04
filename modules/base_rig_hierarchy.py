# coding:utf-8


import maya.cmds as cmds


asset = input("name")

main_group = cmds.createNode("transform", name="rig_{}".format(asset))

elements_list = ["globalMove", "blendShape", "extraNodes"]
gl_move_list = ["ctrls", "joints", "iks"]
xtra_list = ["to_show", "to_hide"]

for element in elements_list:
	el = cmds.createNode("transform", name="{}_{}".format(element, asset))
	cmds.parent(el, main_group)

	if element == "globalMove":
		for i in gl_move_list:
			sub = cmds.createNode("transform", name="{}_{}".format(i, asset))
			cmds.parent(sub, el)

	if element == "extraNodes":
		for i in xtra_list:
			sub = cmds.createNode("transform", name="{}_{}_{}".format(element, asset, i))
			cmds.parent(sub, el)
