# coding:utf-8

from maya import cmds
from maya import mel


class AdvancedEyeRig():


	def __init__(self, name, numControls=5):
		self.NAME = "_".join( name.split("_")[0:-1] ).rstrip("_")
		self.SIDE = name.split("_")[-1]
		
		self.sel = cmds.ls(sl=True, ap=True)

		self.curve = self.sel[0]
		self.crv_shape = AdvancedEyeRig.get_curve_shape(self.curve)
		self.spans = AdvancedEyeRig.get_curve_spans(self.crv_shape)
		self._delete_curve_history()
		
		self.eye = self.sel[-1]
		self.eye_center = AdvancedEyeRig.create_loc_obj_center(self.eye)

		self.point_on_curve_infos = []
		self.locators = []
		self.bones = []
		self.grp_locators = None
		self.grp_bones = None
		self.grp_driver_joints = None


	def compute(self, numControls=3):
		self._delete_point_on_curve_infos()
		self._delete_locators()
		self._delete_bones()
		self._delete_driver_joints()

		for id in range(self.spans):
			name = self._generate_name_with_index( (id+1) )

			pt_crv_info = self._create_point_on_curve_info(name)
			loc = self._create_loc(name)
			bone = self._create_bone(name)

			self._connect_loc_to_curve(loc, pt_crv_info)
			self._set_loc_position_on_curve(pt_crv_info, id)
			self._set_bone_position(bone, loc)

			self.point_on_curve_infos.append(pt_crv_info)
			self.locators.append(loc)
			self.bones.append(bone)
		
		self.driver_joints = self._create_driver_joints(numControls)
		self._set_driver_joint_position_on_curve()
		self.sk_clus_curve = cmds.skinCluster(self.driver_joints, self.curve, tsb=True)

		self.grp_locators = self._organize_locators()
		self.grp_bones = self._organize_bones()
		self.grp_driver_joints = self._organize_driver_joints()


	def _organize_locators(self):
		if not self.grp_locators:
			grp = cmds.createNode( "transform", n="locs_{}_{}".format(self.NAME, self.SIDE) )
			cmds.parent(self.locators, grp)
			return grp
		else:
			cmds.parent(self.locators, self.grp_locators)
			return self.grp_locators


	def _organize_bones(self):
		if not self.grp_bones:
			grp = cmds.createNode( "transform", n="binds_{}_{}".format(self.NAME, self.SIDE) )

			for bone in self.bones:
				cmds.parent(bone["base"], grp)
			return grp
		else:
			for bone in self.bones:
				cmds.parent(bone["base"], self.grp_bones)
			return self.grp_bones


	def _organize_driver_joints(self):
		if not self.grp_driver_joints:
			grp = cmds.createNode( "transform", n="drivJnts_{}_{}".format(self.NAME, self.SIDE) )
			cmds.parent(self.driver_joints, grp)
			return grp
		else:
			cmds.parent(self.driver_joints, self.grp_driver_joints)
			return self.grp_driver_joints


	def _generate_name_with_index(self, id, depth=2):
		return "{}_{}_{}".format(self.NAME, str(id).zfill(depth), self.SIDE)


	def _create_point_on_curve_info(self, name):
		return cmds.createNode( "pointOnCurveInfo",
								n="ptCrvInfo_{}".format(name) )


	def _create_loc(self, name):
		return cmds.spaceLocator( n="loc_{}".format(name) )[0]


	def _create_bone(self, name):
		cmds.select(clear=True)
		bone = AdvancedEyeRig.create_bone(name)
		return bone


	def _create_driver_joints(self, numControls):
		driver_joints = []
		for id in range(numControls):
			jnt = cmds.createNode( "joint",
									n="drivJnt_{}".format(self._generate_name_with_index(id+1) ) )
			driver_joints.append(jnt)
		return driver_joints


	def _connect_loc_to_curve(self, loc, pt_crv_info):
		cmds.connectAttr( "{}.worldSpace[0]".format(self.crv_shape),
						  "{}.inputCurve".format(pt_crv_info) )

		cmds.connectAttr( "{}.position".format(pt_crv_info),
						  "{}.translate".format(loc) )


	def _set_driver_joint_position_on_curve(self):
		for id, jnt in enumerate(self.driver_joints):
			temp_pci = self._create_point_on_curve_info("temp_ptCrvInfo")
			cmds.setAttr("{}.turnOnPercentage".format(temp_pci), 1)
			cmds.setAttr( "{}.parameter".format(temp_pci), (1.0 / (len(self.driver_joints)-1) )*id )

			cmds.connectAttr( "{}.worldSpace[0]".format(self.curve),
							  "{}.inputCurve".format(temp_pci) )

			pos = cmds.getAttr("{}.position".format(temp_pci))[0]
			print(pos)
			cmds.xform(jnt, t=pos, a=True)

			cmds.delete(temp_pci)


	def _set_loc_position_on_curve(self, pt_crv_info, id):
		cmds.setAttr("{}.turnOnPercentage".format(pt_crv_info), 1)
		cmds.setAttr( "{}.parameter".format(pt_crv_info), 0.1*id )


	def _set_bone_position(self, bone, loc):
		cmds.matchTransform(bone["base"], self.eye_center)
		cmds.aimConstraint(loc, bone["base"])
		cmds.matchTransform(bone["bind"], loc, pos=True)


	def _delete_curve_history(self):
		cmds.delete(self.curve, constructionHistory=True)


	def _delete_point_on_curve_infos(self):
		if hasattr(self, "point_on_curve_infos"):
			cmds.delete(self.point_on_curve_infos)
		self.point_on_curve_infos = []


	def _delete_locators(self):
		if hasattr(self, "locators"):
			cmds.delete(self.locators)
		self.locators = []


	def _delete_bones(self):
		if hasattr(self, "bones"):
			for bone in self.bones:
				cmds.delete(bone["base"])
		self.bones = []


	def _delete_driver_joints(self):
		if hasattr(self, "driver_joints"):
			cmds.delete(self.driver_joints)
		self.driver_joints = []


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
			spans = int( cmds.getAttr( "{}.spans".format(curveShape) ) + 1 )
			return spans


	@staticmethod
	def create_bone(name):
		base_joint = cmds.joint( n="baseJnt_{}".format(name) )
		bind_joint = cmds.joint( n="bind_{}".format(name), position=(1,0,0) )
		bone = {"base" : base_joint, "bind" : bind_joint}
		return bone