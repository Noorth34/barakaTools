# coding:utf-8

from maya import cmds


class FacialRibbonMatrix():

	def __init__(self, name="ASSET_ribbon_PART"):
		self.sel = cmds.ls(sl=True, ap=True)[0]
		self.surface = cmds.listRelatives( self.sel,
										   shapes=True,
										   path=True )[0]

		self.NAME = name
		self.spans = spans = { "U" : int( cmds.getAttr( "{}.spansUV".format(self.surface) )[0][0] ),
							   "V" : int( cmds.getAttr( "{}.spansUV".format(self.surface) )[0][-1] ) }

		self.direction = None
		self.other = None

		self.rivets = None
		self.binds = None
		self.point_on_surface_infos = None
		self.four_by_four_matrices = None
		self.decompose_matrices = None

		self.driver_joints = None
		self.offset_driver_joints = None

		self.grp_binds = None
		self.grp_driver_joints = None


	def compute(self, numControls, direction="U"):
		self._delete()

		self.direction = direction

		if self.direction == "U":
			self.other = "V"
		elif self.direction =="V":
			self.other = "U"

		self._rebuild_surface()

		self.rivets = self._create_rivets()
		self.binds = self._create_binds()
		self.point_on_surface_infos = self._create_point_on_surface_infos()
		self.four_by_four_matrices = self._create_four_by_four_matrices()
		self.decompose_matrices = self._create_decompose_matrices()


		self._parent_binds_to_rivets()

		self._connect_surface_to_point_on_surface_infos()
		self._connect_point_on_surface_infos_to_four_by_four_matrices()
		self._connect_four_by_four_matrices_to_decompose_matrices()
		self._connect_decompose_matrices_to_rivets()
		self._set_rivets_position()

		self.driver_joints = self._create_driver_joints(numControls)
		self._set_driver_joints_position_on_surface()
		self.skin_cluster = self._skin_surface()

		self.grp_binds = self._organize_binds()
		self.grp_driver_joints = self._organize_driver_joints()

		self.offset_driver_joints = self._offset_driver_joints()


	def _rebuild_surface(self):
		if self.direction == "U":
			degreeU = 3
			degreeV = 1
			spanU = self.spans[self.direction]
			spanV = self.spans[self.other]
		elif self.direction == "V":
			degreeU = 1
			degreeV = 3
			spanU = self.spans[self.other]
			spanV = self.spans[self.direction]

		cmds.rebuildSurface( self.surface,
							 degreeU = degreeU,
							 degreeV = degreeV,
							 spansU = spanU,
							 spansV = spanV,
							 constructionHistory = False )


	def _gen_name_with_index(self, id, depth=2):
		return "{}_{}".format( self.NAME, str(id).zfill(depth) )


	def _create_rivets(self):
		rivets = [ cmds.spaceLocator( name="rivet_{}".format( self._gen_name_with_index(id+1) ) )[0]
					 for id in range(self.spans[self.direction]) ]
		return rivets


	def _create_binds(self):
		binds = [ cmds.createNode("joint", name= "bind_{}".format( self._gen_name_with_index(id+1) ) )
				  for id in range(self.spans[self.direction]) ]
		return binds


	def _create_point_on_surface_infos(self):
		pt_surf_infos = [ cmds.createNode("pointOnSurfaceInfo",
						   name="ptOnSurfInfo_{}".format(self._gen_name_with_index(id+1) ) )
						   for id in range(self.spans[self.direction]) ]
		return pt_surf_infos


	def _create_four_by_four_matrices(self):
		four_by_four_matrices = [ cmds.createNode("fourByFourMatrix",
								  name = "fbfMatrix_{}".format(self._gen_name_with_index(id+1) ) )
								  for id in range(self.spans[self.direction]) ]
		return four_by_four_matrices


	def _create_decompose_matrices(self):
		decompose_matrices = [ cmds.createNode("decomposeMatrix",
							   name="dMatrix_{}".format(self._gen_name_with_index(id+1) ) )
							   for id in range(self.spans[self.direction]) ]
		return decompose_matrices


	def _create_driver_joints(self, numControls):
		driver_joints = [ cmds.createNode( "joint",
						  n="drivJnt_{}".format(self._gen_name_with_index(id+1), ) )
						  for id in range(numControls) ]
		return driver_joints


	def _organize_binds(self):
		if not self.grp_binds:
			grp = cmds.createNode( "transform",
						n="binds_{}".format(self.NAME) )
			cmds.parent(self.rivets, grp)
			return grp
		else:
			cmds.parent(self.rivets, self.grp_binds)
			return self.grp_binds


	def _organize_driver_joints(self):
		if not self.grp_driver_joints:
			grp = cmds.createNode( "transform",
						n="drivJnts_{}".format(self.NAME) )

			cmds.parent(self.driver_joints, grp)
			return grp
		else:
			cmds.parent(self.driver_joints, self.grp_driver_joints)
			return self.grp_driver_joints


	def _offset_driver_joints(self):
		off_driv_jnts = [ cmds.createNode("transform",
						  n="{}_offset".format(jnt) )
						  for jnt in self.driver_joints ]

		for id, offset in enumerate(off_driv_jnts):
			cmds.matchTransform(offset, self.driver_joints[id])
			cmds.parent(self.driver_joints[id], offset)
			cmds.parent(offset, self.grp_driver_joints)

		return off_driv_jnts


	def _parent_binds_to_rivets(self):
		for bind, riv in zip(self.binds, self.rivets):
			cmds.parent(bind, riv)


	def _connect_surface_to_point_on_surface_infos(self):
		for pt_surf_info in self.point_on_surface_infos:
			cmds.connectAttr( "{}.worldSpace[0]".format(self.surface),
							  "{}.inputSurface".format(pt_surf_info) )


	def _connect_point_on_surface_infos_to_four_by_four_matrices(self):
		for pt_surf_info, fbf in zip(self.point_on_surface_infos, self.four_by_four_matrices):
			# normals
			cmds.connectAttr("{}.normalX".format(pt_surf_info),
							 "{}.in00".format(fbf))

			cmds.connectAttr("{}.normalY".format(pt_surf_info),
							 "{}.in01".format(fbf))

			cmds.connectAttr("{}.normalZ".format(pt_surf_info),
							 "{}.in02".format(fbf))

			# tangent {direction}
			cmds.connectAttr("{}.tangent{}x".format(pt_surf_info, self.direction),
							 "{}.in10".format(fbf))

			cmds.connectAttr("{}.tangent{}y".format(pt_surf_info, self.direction),
							 "{}.in11".format(fbf))

			cmds.connectAttr("{}.tangent{}z".format(pt_surf_info, self.direction),
							 "{}.in12".format(fbf))

			# tangent {other}
			cmds.connectAttr("{}.tangent{}x".format(pt_surf_info, self.other),
							 "{}.in20".format(fbf))

			cmds.connectAttr("{}.tangent{}y".format(pt_surf_info, self.other),
							 "{}.in21".format(fbf))

			cmds.connectAttr("{}.tangent{}z".format(pt_surf_info, self.other),
							 "{}.in22".format(fbf))

			# position
			cmds.connectAttr("{}.positionX".format(pt_surf_info),
							 "{}.in30".format(fbf))

			cmds.connectAttr("{}.positionY".format(pt_surf_info),
							 "{}.in31".format(fbf))

			cmds.connectAttr("{}.positionZ".format(pt_surf_info),
							 "{}.in32".format(fbf))


	def _connect_four_by_four_matrices_to_decompose_matrices(self):
		for fbf, d_matrix in zip(self.four_by_four_matrices, self.decompose_matrices):
			cmds.connectAttr( "{}.output".format(fbf),
							  "{}.inputMatrix".format(d_matrix) )


	def _connect_decompose_matrices_to_rivets(self):
		for d_matrix, riv in zip(self.decompose_matrices, self.rivets):
			cmds.connectAttr( "{}.outputRotate".format(d_matrix),
							  "{}.rotate".format(riv) )

			cmds.connectAttr( "{}.outputTranslate".format(d_matrix),
							  "{}.translate".format(riv) )


	def _set_rivets_position(self):
		paramU = None
		paramV = None

		for id, pt_surf_info in enumerate(self.point_on_surface_infos):
			if self.direction == "U":
				paramU = (id + 0.5) / 10.0
				paramV = 0.5
			elif self.direction == "V":
				paramU = 0.5
				paramV = (id + 0.5) / 10.0

			cmds.setAttr("{}.turnOnPercentage".format(pt_surf_info), 1)
			cmds.setAttr("{}.parameterU".format(pt_surf_info), paramU)
			cmds.setAttr("{}.parameterV".format(pt_surf_info), paramV)


	def _set_driver_joints_position_on_surface(self):
		for id, jnt in enumerate(self.driver_joints):
			if self.direction == "U":
				paramU = 1.0 / (len(self.driver_joints)-1) * id
				paramV = 0.5
			elif self.direction == "V":
				paramU = 0.5
				paramV = 1.0 / (len(self.driver_joints)-1) * id

			temp_pci = cmds.createNode("pointOnSurfaceInfo",
										n="temp_ptSurfInfo")

			cmds.setAttr("{}.turnOnPercentage".format(temp_pci), 1)

			cmds.setAttr( "{}.parameterU".format(temp_pci),
						  paramU)

			cmds.setAttr( "{}.parameterV".format(temp_pci),
						  paramV)

			cmds.connectAttr( "{}.worldSpace[0]".format(self.surface),
							  "{}.inputSurface".format(temp_pci) )

			pos = cmds.getAttr("{}.position".format(temp_pci))[0]
			cmds.xform(jnt, t=pos, a=True)
			cmds.delete(temp_pci)


	def _skin_surface(self):
		sk_clus = cmds.skinCluster(self.driver_joints, self.sel, tsb=True)


	def _delete(self):
		self._unbind_surface()
		self._delete_driver_joints()
		self._delete_decompose_matrices()
		self._delete_four_by_four_matrices()
		self._delete_point_on_surface_infos()
		self._delete_binds()
		self._delete_rivets()


	def _delete_rivets(self):
		if hasattr(self, "rivets"):
			if self.rivets:
				try:
					cmds.delete(self.rivets)
				except ValueError:
					cmds.warning("Rivets nodes have already been deleted.")
					pass
		self.rivets = None


	def _delete_binds(self):
		if hasattr(self, "binds"):
			if self.binds:
				try:
					cmds.delete(self.binds)
				except ValueError:
					cmds.warning("Binds nodes have already been deleted.")
					pass
		self.binds = None


	def _delete_point_on_surface_infos(self):
		if hasattr(self, "point_on_surface_infos"):
			if self.point_on_surface_infos:
				try:
					cmds.delete(self.point_on_surface_infos)
				except ValueError:
					cmds.warning("ptOnSurfInfo nodes have already been deleted.")
					pass
		self.point_on_surface_infos = None


	def _delete_four_by_four_matrices(self):
		if hasattr(self, "four_by_four_matrices"):
			if self.four_by_four_matrices:
				try:
					cmds.delete(self.four_by_four_matrices)
				except ValueError:
					cmds.warning("fbfMatrix nodes have already been deleted.")
					pass
		self.four_by_four_matrices = None


	def _delete_decompose_matrices(self):
		if hasattr(self, "decompose_matrices"):
			if self.decompose_matrices:
				try:
					cmds.delete(self.decompose_matrices)
				except ValueError:
					cmds.warning("dMatrix nodes have already been deleted.")
					pass
		self.decompose_matrices = None


	def _delete_driver_joints(self):
		if hasattr(self, "driver_joints"):
			if self.driver_joints:
				try:
					cmds.delete(self.driver_joints)
				except ValueError:
					cmds.warning("drivJnts nodes have already been deleted.")
					pass
		self.driver_joints = None


	def _unbind_surface(self):
		if hasattr(self, "skin_cluster"):
			if self.skin_cluster:
				cmds.skinCluster(self.skinCluster, edit=True, unbind=True)

"""
		self.grp_binds = self._organize_binds()
		self.grp_driver_joints = self._organize_driver_joints()

		self.offset_driver_joints = self._offset_driver_joints()
"""

	def _delete_grp_binds(self):
		if hasattr(self, "grp_binds"):
			if self.grp_binds:
				try:
					cmds.delete(self.grp_binds)
				except ValueError:
					cmds.warning("Binds Group has already been deleted.")
					pass
		self.grp_binds = None


	def _delete_grp_driver_joints(self):
		if hasattr(self, "grp_driver_joints"):
			if self.grp_driver_joints:
				try:
					cmds.delete(self.grp_driver_joints)
				except ValueError:
					cmds.warning("Driver Joints Group has already been deleted.")
					pass
		self.grp_driver_joints = None