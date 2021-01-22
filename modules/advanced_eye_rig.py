# coding:utf-8

from maya import cmds


class AdvancedEyeRig():

	def __init__(self, name):
		self.NAME = "_".join( name.split("_")[0:-1] ).rstrip("_")
		self.SIDE = name.split("_")[-1]
		self.curve = cmds.ls(sl=True, ap=True)[0]
		pass


	def compute(self):
		self.crv_shape = AdvancedEyeRig.get_curve_shape(self.curve)
		self.spans = AdvancedEyeRig.get_curve_spans(self.crv_shape)

		for id in range(self.spans):
			pt_crv_info = cmds.createNode( "pointOnCurveInfo",
											n="ptCrvInfo_{}_{}_{}".format(self.NAME, str(id+1).zfill(2), self.SIDE) )

			loc = cmds.spaceLocator( n="loc_{}_{}_{}".format(self.NAME, str(id+1).zfill(2), self.SIDE) )[0]

			cmds.connectAttr( "{}.worldSpace[0]".format(self.crv_shape), "{}.inputCurve".format(pt_crv_info) )
			cmds.connectAttr( "{}.position".format(pt_crv_info), "{}.translate".format(loc) )

			cmds.setAttr("{}.turnOnPercentage".format(pt_crv_info), 1)
			cmds.setAttr("{}.parameter".format(pt_crv_info), 0.1*(id+1))


	@staticmethod
	def get_curve_shape(curve):
		shape = cmds.listRelatives(curve, shapes=True, path=True)[0]
		return shape

	@staticmethod
	def get_curve_spans(curveShape):
		if cmds.objectType(curveShape, isType="nurbsCurve"):
			return cmds.getAttr( "{}.spans".format(curveShape) )