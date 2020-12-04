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
		
duplicata = cmds.duplicate(sel, returnRootsOnly=False, rc=True, upstreamNodes=True)

# rename ALL nodes ; both DAG and DG nodes
renamed_duplicata = []
for node in duplicata:
	renamed_node = cmds.rename(node, node.replace("_L", "_R").rstrip("1"))
	renamed_duplicata.append(renamed_node)

# Save constraint structure

constraints_list = []

for node in renamed_duplicata:
	if cmds.objectType(node) in ["parentConstraint", "orientConstraint", "scaleConstraint", "aimConstraint"]:
		constraints_list.append(node)

constraint = {}
for constr in constraints_list:
	
	constraint[constr] = {}
	constraint[constr]["type"] = cmds.objectType(constr)
	
	id = 0
	constraint[constr]["source"] = None
	while not constraint[constr]["source"]:
		constraint[constr]["source"] = cmds.listConnections(constr+".target[{}].targetParentMatrix".format(id), s=True, d=False)
		id += 1
	
	constraint[constr]["source"] = constraint[constr]["source"][0]
	
	dest_tx = cmds.listConnections("{}.constraintTranslateX".format(constr), s=False, d=True)[0]
	dest_ty = cmds.listConnections("{}.constraintTranslateY".format(constr), s=False, d=True)[0]
	dest_tz = cmds.listConnections("{}.constraintTranslateZ".format(constr), s=False, d=True)[0]
	
	dest_rx = cmds.listConnections("{}.constraintRotateX".format(constr), s=False, d=True)[0]
	dest_ry = cmds.listConnections("{}.constraintRotateY".format(constr), s=False, d=True)[0]
	dest_rz = cmds.listConnections("{}.constraintRotateZ".format(constr), s=False, d=True)[0]

	if dest_tx == dest_ty and dest_ty == dest_tz:
		constraint[constr]["destination"] = dest_tx
	elif dest_rx == dest_ry and dest_ry == dest_rz:
		constraint[constr]["destination"] = dest_rx
	
	offset_tr = cmds.getAttr("{}.target[0].targetOffsetTranslate".format(constr))[0]
	offset_rot = cmds.getAttr("{}.target[0].targetOffsetRotate".format(constr))[0]
	
	if offset_tr == (0, 0, 0) and offset_rot == (0, 0, 0):
		constraint[constr]["maintain_offset"] = False
	else:
		constraint[constr]["maintain_offset"] = True

	cmds.delete(constr)


# Work only with DAG nodes
cmds.select(renamed_duplicata[0:len(sel)], hierarchy=True)
dagNodes_list = cmds.ls(sl=True, shapes=False)

# filter shapes because maya sucks
for id, node in enumerate(dagNodes_list):
	if cmds.objectType(node, isType="nurbsCurve") == True:
		dagNodes_list.pop(id)

dagParent = {}

for node in dagNodes_list:
	parent = cmds.listRelatives(node, parent=True)[0]
	dagParent[node] = parent

for node in dagNodes_list:
	cmds.parent(node, world=True)

for node in dagNodes_list:
	pos_x, pos_y, pos_z = cmds.xform(node, q=True, t=True)
	rot_x, rot_y, rot_z = cmds.xform(node, q=True, ro=True)
	global_move = cmds.createNode("transform", n="temp_mirror")
	cmds.xform(global_move, t=[pos_x, pos_y, pos_z])
	cmds.parent(node, global_move)
	cmds.xform(global_move, t=[-pos_x, pos_y, pos_z])
	cmds.xform(global_move, ro=[0, 180, 180])
	cmds.parent(node, w=True)
	cmds.delete(global_move)

for node in dagNodes_list:
	cmds.parent(node, dagParent[node])

# redo constraints
for i in constraints_list:
	if constraint[i]["type"] == "parentConstraint":
		cmds.parentConstraint(constraint[i]["source"], constraint[i]["destination"], mo= constraint[i]["maintain_offset"])
	
	elif constraint[i]["type"] == "orientConstraint":
		cmds.orientConstraint(constraint[i]["source"], constraint[i]["destination"], mo= constraint[i]["maintain_offset"])
	
	elif constraint[i]["type"] == "scaleConstraint":
		cmds.scaleConstraint(constraint[i]["source"], constraint[i]["destination"], mo= constraint[i]["maintain_offset"])
	
	# elif constraint[i]["type"] == "aimConstraint":
	# 	cmds.aimConstraint(constraint[i]["source"], constraint[i]["destination"], mo= constraint[i]["maintain_offset"])


# MIRROR POSITION AND ROTATION

def mirror_object(objects_list=[], axis="x"):

	if not objects_list:
		cmds.error("Any objects passed for mirror.")

	if objects_list not type(list):
		objects = list(objects)

	for obj in objects_list:
		pos_x, pos_y, pos_z = cmds.xform(obj, q=True, t=True)
		rot_x, rot_y, rot_z = cmds.xform(obj, q=True, ro=True)

		global_move = cmds.createNode("transform", n="temp_mirror")
		
		cmds.xform(global_move, t=[pos_x, pos_y, pos_z])
		cmds.parent(obj, global_move)

		if axis == "x":
			cmds.xform(global_move, t=[(-1)*pos_x, pos_y, pos_z])
			cmds.xform(global_move, ro=[0, 180, 180])

		if axis == "y":
			cmds.xform(global_move, t=[pos_x, (-1)*pos_y, pos_z])
			cmds.xform(global_move, ro=[180, 0, 180])

		if axis == "z":
			cmds.xform(global_move, t=[pos_x, pos_y, (-1)*pos_z])
			cmds.xform(global_move, ro=[180, 180, 0])

		cmds.parent(obj, w=True)
		cmds.delete(global_move)

# MIRROR SHAPES

def mirror_curve_shape(sel=[])
	
	if sel not type(list):
		cmds.error("{} passed. Must pass selection list".format(type(sel)))

	if not sel:
		sel = cmds.ls(sl=True, ap=True)

	if not sel:
		cmds.error("Any selection. Please select curves")

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



def hook_legacy():
	sel = cmds.ls(sl=True, ap=True)

	hook = cmds.createNode("transform", n= "hook_{}_for_{}".format( sel[0], sel[-1] ) )
	cmds.setAttr("{}.useOutlinerColor".format(hook), 1)
	cmds.setAttr("{}.outlinerColorR".format(hook), 0)
	cmds.setAttr("{}.outlinerColorG".format(hook), 1)
	cmds.setAttr("{}.outlinerColorB".format(hook), 1)

	cmds.parentConstraint(sel[0], hook, mo=False)
	cmds.scaleConstraint(sel[0], hook, mo=False)

	parent = cmds.listRelatives(sel[-1], parent=True, path=True)

	cmds.parent(sel[-1], hook)

	if parent:
		parent = parent[0]
		cmds.parent(hook, parent)
	else:
		pass