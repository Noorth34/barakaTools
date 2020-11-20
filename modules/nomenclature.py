# coding:utf-8


from maya import cmds


class Nomenclature():

	def __init__(self):

		self.dict_nomenclature = {

								"transform" : ['TOP_', 'grp_', 'hook_', '_offset', 'cstr_', 'master_', 'msh_', 'geo_', 'lookdev_', 'dressing', 'layout_', 'set_'],

								"locator" : ['loc_'],

								"nurbsSurface" : ['surf_', 'ribbon_'],

								"joint" : ['jnt_', 'bind_', 'drivJnt_', 'bone_'],

								"nurbsCurve" : ['ctrl_', 'crv_', 'crvWire_', 'crvBind_'],

								"curveInfo" : ['crvInfo_'],

								"multiplyDivide" : ['mult_', 'div_', 'pow_', 'sqrt_'],

								"multDoubleLinear" : ['mdl_'],

								"plusMinusAverage" : ['plusMinAv_'],

								"condition" : ['cond_'],

								"multMatrix" : ['mMatrix_'],

								"decomposeMatrix" : ['dMatrix_'],

								"fourByFourMatrix" : ['fbfMatrix_'],

								"ikHandle" : ['ik_'],

								"ikSplineHandle" : ['ikSpline_'],

								"ikEffector" : ['effec_'],

								"blendshape" : ['bshp_'],

								"wrap" : ['wrap_'],

								"twist" : ['twist_'],

								"wire" : ['wire_'],

								"sine" : ['sine_'],

								"deltaMush" : ['dMush_'],

								"tension" : ['tension_'],

								"skinCluster" : ['skinCluster_'],

								"cluster" : ['clus_'],

								"follicle" : ['fol_'],

								}


		self.nodes_list = cmds.ls(ap=True)
		self.to_rename = []


	def check(self):

		for node in self.nodes_list:
			type = cmds.objectType(node)

			if type in list(self.dict_nomenclature.keys()):
				for prefix in self.dict_nomenclature[type]:
					if not prefix in node:
						self.to_rename.append(node)
	

	def select_nodes_to_rename(self):

		cmds.select(self.to_rename, add=True)
