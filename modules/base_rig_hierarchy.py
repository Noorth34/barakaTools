# coding:utf-8


import maya.cmds as cmds


class RigHierarchy():

	def __init__(self, name):
		self.NAME = name
		self.rig_group = cmds.createNode( "transform",
										name="rig_{}".format(self.NAME) )

		self.main_groups_list = [ "globalMove", 
								  "blendShapes", 
								  "extraNodes" ]

		self.global_move_groups_list = [ "ctrls",
										 "joints",
										 "iks" ]

		self.extra_nodes_groups_list = [ "to_show",
										 "to_hide" ]


	def compute(self):
		self.main_groups = self._create_main_groups()
		self.global_move_groups = self._create_global_move_groups()
		self.extra_nodes_groups = self._create_extra_nodes_groups()

		cmds.parent(self.main_groups.values(), self.rig_group)
		cmds.parent(self.global_move_groups.values(), self.main_groups["globalMove"])
		cmds.parent(self.extra_nodes_groups.values(), self.main_groups["extraNodes"])


	def _create_main_groups(self):
		main_groups = [ cmds.createNode("transform",
						name="{}_{}".format(grp, self.NAME) )
						for grp in self.main_groups_list ]

		return { "globalMove" : main_groups[0],
				 "blendShapes" : main_groups[1],
				 "extraNodes" : main_groups[2] }


	def _create_global_move_groups(self):
		global_move_groups = [ cmds.createNode("transform",
							   name="{}_{}".format(grp, self.NAME) )
							   for grp in self.global_move_groups_list ]

		return { "ctrls" : global_move_groups[0],
				 "joints" : global_move_groups[1],
				 "iks" : global_move_groups[2] }


	def _create_extra_nodes_groups(self):
		extra_nodes_groups = [ cmds.createNode("transform",
							   name="extraNodes_{}_{}".format(self.NAME, grp) )
							   for grp in self.extra_nodes_groups_list ]

		return { "toShow" : extra_nodes_groups[0],
				 "toHide" : extra_nodes_groups[-1] }