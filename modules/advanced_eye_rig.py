# coding:utf-8

from maya import cmds


class AdvancedEyeRig():

	def __init__(self, name, numControls=5):
		self.NAME = "_".join( name.split("_")[0:-1] ).rstrip("_")
		self.SIDE = name.split("_")[-1]

		sel = cmds.ls(sl=True, ap=True)
		self.curve = sel[0]
		self.crv_shape = AdvancedEyeRig.get_curve_shape(self.curve)
		self.spans = AdvancedEyeRig.get_curve_spans(self.crv_shape)
		
		self.eye = cmds.ls(sl=True, ap=True)[-1]
		self.eye_center = AdvancedEyeRig.create_loc_obj_center(self.eye)

		self.wire = cmds.duplicate( self.curve, n="crvWire_{}_{}".format(self.NAME, self.SIDE) )
		cmds.rebuildCurve(self.wire, spans=numControls)


	def compute(self):
		for id in range(self.spans):
			name = "{}_{}_{}".format(self.NAME, str(id+1).zfill(2), self.SIDE)

			pt_crv_info = self._create_point_on_curve_info(name)
			loc = self._create_loc(name)
			bone = self._create_bone(name)

			self._delete_curve_history()
			self._connect_loc_to_curve(loc, pt_crv_info)
			self._set_loc_position_on_curve(pt_crv_info, id)
			self._set_bone_position(bone, loc)


	def _delete_curve_history(self):
		cmds.delete(self.curve, constructionHistory=True)


	def _create_point_on_curve_info(self, name):
		return cmds.createNode( "pointOnCurveInfo",
								n="ptCrvInfo_{}".format(name) )


	def _create_loc(self, name):
		return cmds.spaceLocator( n="loc_{}".format(name) )[0]


	def _connect_loc_to_curve(self, loc, pt_crv_info):
		cmds.connectAttr( "{}.worldSpace[0]".format(self.crv_shape), "{}.inputCurve".format(pt_crv_info) )
		cmds.connectAttr( "{}.position".format(pt_crv_info), "{}.translate".format(loc) )


	def _set_loc_position_on_curve(self, pt_crv_info, id):
		cmds.setAttr("{}.turnOnPercentage".format(pt_crv_info), 1)
		cmds.setAttr("{}.parameter".format(pt_crv_info), 0.1*(id+1))


	def _create_bone(self, name):
		cmds.select(clear=True)
		bone = AdvancedEyeRig.create_bone(name)
		return bone


	def _set_bone_position(self, bone, loc):
		cmds.matchTransform(bone["base"], self.eye_center)
		cmds.aimConstraint(loc, bone["base"])
		cmds.matchTransform(bone["bind"], loc, pos=True)


	@staticmethod
	def create_loc_obj_center(object):
		if cmds.objectType(object, isType="transform"):
			loc = cmds.spaceLocator(n="loc_{}_center".format(object))[0]
			cmds.matchTransform(loc, object, pos=True)
			return loc


	@staticmethod
	def get_curve_shape(curve):
		shape = cmds.listRelatives(curve, shapes=True, path=True)[0]
		return shape


	@staticmethod
	def get_curve_spans(curveShape):
		if cmds.objectType(curveShape, isType="nurbsCurve"):
			return cmds.getAttr( "{}.spans".format(curveShape) )


	@staticmethod
	def create_bone(name):
		base_joint = cmds.joint( n="baseJnt_{}".format(name) )
		bind_joint = cmds.joint( n="bind_{}".format(name), position=(1,0,0) )
		bone = {"base" : base_joint, "bind" : bind_joint}
		return bone