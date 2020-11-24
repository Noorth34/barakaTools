# coding:utf-8

# real mirror script

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