# coding:utf-8

# real mirror script

# 1) duplicate special ( world | input graph)

# 2) unparent offsets to world

# 3) create a null for each offset

# 4) match Translate each null on his respective offset

# 5) *(-1) translate X on each null

# 6) rotation 180° on Y and Z axis on each null

# 7) unparent offsets and reparent them correctly

# 8) reorient CTRLS' shapes

#  /|\
# / ! \  *(-1) translate X on each null joint
#
sel = cmds.ls(sl=True, ap=True)

duplicata = cmds.duplicate(sel, returnRootsOnly=True, upstreamNodes=True)

for id, module in enumerate(duplicata):
	# rename nodes
	for child in cmds.listRelatives(module, ad=True, path=True):
		cmds.rename(child, child.split("|")[-1].replace("_L_", "_R_"))
	renamed_module = cmds.rename(module, sel[id].replace("_L_", "_R_"))

	# do mirror
	parents_list = []
	offsets_list = []
	for child in cmds.listRelatives(renamed_module, ad=True, path=True):
		
		if cmds.objectType(child, isType="joint") and child.startswith("null"):
			pos_x, pos_y, pos_z = cmds.xform(child, q=True, t=True)
			cmds.xform(child, t=[-pos_x, pos_y, pos_z])
			
		if cmds.objectType(child, isType="transform") and child.endswith("_offset"):
			parent = cmds.listRelatives(child, parent=True, path=True)
			child = cmds.parent(child, world=True)
			
			pos_x, pos_y, pos_z = cmds.xform(child, q=True, t=True)
			rot_x, rot_y, rot_z = cmds.xform(child, q=True, ro=True)
			global_move = cmds.createNode("transform", n="temp_mirror")
			cmds.xform(global_move, t=[pos_x, pos_y, pos_z])
			cmds.parent(child, global_move)
			cmds.xform(global_move, t=[-pos_x, pos_y, pos_z])
			cmds.xform(global_move, ro=[0, 180, 180])
			cmds.parent(child, w=True)
			cmds.delete(global_move)
	
			parents_list.append(parent[0])
			offsets_list.append(child[0])
			
	for offset, parent in zip(offsets_list, parents_list):
		cmds.parent(offset, parent)




sel = cmds.ls(sl=True, ap=True)

for i in sel:
	pos_x, pos_y, pos_z = cmds.xform(i, q=True, t=True)
	rot_x, rot_y, rot_z = cmds.xform(i, q=True, ro=True)
	
	
	global_move = cmds.createNode("transform", n="temp")
	
	cmds.xform(global_move, t=[pos_x, pos_y, pos_z])
	
	cmds.parent(i, global_move)
	
	cmds.xform(global_move, t=[-pos_x, pos_y, pos_z])
	
	cmds.xform(global_move, ro=[0, 180, 0])
	cmds.parent(i, w=True)
	
	rot_x, rot_y, rot_z = cmds.xform(i, q=True, ro=True)
	
	cmds.xform(i, ro=[-rot_x, -rot_y, rot_z])
	
	cmds.delete(global_move)

	#hello