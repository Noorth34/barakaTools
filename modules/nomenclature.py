# coding:utf-8


from maya import cmds


class Nomenclature():

	def __init__(self):

		self.dict_nomenclature = {

								"camera" : ['cam_', 'persp', 'top', 'front', 'side'],

								"transform" : ['TOP_', 'grp_', 'hook_', '_offset', 'cstr_', 'master_', 'lookdev_', 'dressing', 'layout_', 'set_'],
								
								"mesh" : ['msh_', 'geo_', 'geoDriv_'],

								"locator" : ['loc_'],

								"nurbsSurface" : ['surf_', 'ribbon_'],

								"joint" : ['jnt_', 'bind_', 'drivJnt_', 'bone_', 'null_bind_', 'null_bone_'],

								"nurbsCurve" : ['ctrl_', 'crv_', 'crvWire_', 'crvBind_'],

								"curveInfo" : ['crvInfo_'],

								"multiplyDivide" : ['mult_', 'div_', 'pow_', 'sqrt_'],

								"multDoubleLinear" : ['mdl_'],

								"plusMinusAverage" : ['plusMinAv_'],

								"condition" : ['cond_'],

								"multMatrix" : ['mMatrix_'],

								"decomposeMatrix" : ['dMatrix_'],

								"fourByFourMatrix" : ['fbfMatrix_'],

								"ikHandle" : ['ik_', 'ikSpline_'],

								"ikEffector" : ['effec_'],

								"blendShape" : ['bshp_'],

								"nonLinear" : ['wrap_', 'twist_', 'wire_', 'sine_', 'squash_'],

								"wrap" : ['wrap_'],

								"deformTwist" : ['twist_'],

								"wire" : ['wire_'],

								"deformSine" : ['sine_'],

								"deformSquash" : ['squash_'],

								"deltaMush" : ['dMush_'],

								"tension" : ['tension_'],

								"skinCluster" : ['skinCluster_'],

								"cluster" : ['clus_'],

								"follicle" : ['fol_'],

								}


		self.nodes_list = cmds.ls(ap=True)
		self.to_rename = []


	def check(self):

		for type in list(self.dict_nomenclature.keys()):
			nodes_list = cmds.ls(exactType=type)
			
			if type == 'transform':
				
				for node in nodes_list:
					child = cmds.listRelatives(node, shapes=True)
				
					if child:
						child_type = cmds.objectType(child[0])
						
						match = 0
						for prefix in self.dict_nomenclature[child_type]:
							if prefix in node:
								match+=1
						if match == 0:
							self.to_rename.append(node)
			
			else:
				for node in nodes_list:
						
					match = 0
					for prefix in self.dict_nomenclature[type]:
						
						if prefix in node:
							match +=1
					if match == 0:
						self.to_rename.append(node)				
	

	def select_nodes_to_rename(self):

		cmds.select(self.to_rename, add=True)