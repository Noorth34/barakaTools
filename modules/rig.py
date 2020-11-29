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
# MIRROR RIG MODULES
sel = cmds.ls(sl=True, ap=True)
cmds.select(cl=True)

duplicata = cmds.duplicate(sel, returnRootsOnly=False, rc=True, upstreamNodes=True)

renamed_duplicata = []
for node in duplicata:
	renamed_node = cmds.rename(node, node.replace("_L", "_R").rstrip("1"))
	renamed_duplicata.append(renamed_node)

for id, module in enumerate(renamed_duplicata[0:len(sel)]):

	# do mirror
	parents_list = []
	offsets_list = []
	for child in cmds.listRelatives(renamed_duplicata[id], ad=True, path=True):
		
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
	
	pos_x, pos_y, pos_z = cmds.xform(module, q=True, t=True)
	rot_x, rot_y, rot_z = cmds.xform(module, q=True, ro=True)
	global_move = cmds.createNode("transform", n="temp_mirror")
	cmds.xform(global_move, t=[pos_x, pos_y, pos_z])
	cmds.parent(module, global_move)
	cmds.xform(global_move, t=[-pos_x, pos_y, pos_z])
	cmds.xform(global_move, ro=[0, 180, 180])
	cmds.parent(module, w=True)
	cmds.delete(global_move)
		
	for offset, parent in zip(offsets_list, parents_list):
		cmds.parent(offset, parent)


# MIRROR SHAPES
sel = cmds.ls(sl=True, ap=True)

for transform in sel:
	shapes_list = cmds.listRelatives(transform, shapes=True, path=True)
	for shape in shapes_list:
		if cmds.objectType(shape, isType="nurbsCurve"):
			cv_number = cmds.getAttr("{}.spans".format(shape))
			for id in range(cv_number):
				cv_x = cmds.getAttr("{}.controlPoints[{}].xValue".format(shape, id))
				cv_y = cmds.getAttr("{}.controlPoints[{}].yValue".format(shape, id))
				cv_z = cmds.getAttr("{}.controlPoints[{}].zValue".format(shape, id))
				cmds.setAttr("{}.controlPoints[{}].xValue".format(shape, id), cv_x)
				cmds.setAttr("{}.controlPoints[{}].yValue".format(shape, id), (-1)*cv_y)
				cmds.setAttr("{}.controlPoints[{}].zValue".format(shape, id), (-1)*cv_z)