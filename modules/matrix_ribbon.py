# coding:utf-8

import maya.cmds as cmds

name = "limb"
length = 5
ribbon = cmds.nurbsPlane(name="ribb_{}".format(name), axis=[0,1,0], degree=3, lengthRatio=length, patchesU=1, patchesV=5)[0]

# rebuild ribbon (make U linear, keep V cubic)

for i in range(length):
	loc = cmds.spaceLocator(name="rivet_{}_01".format(name))[0]
	point_on_surface_info = cmds.createNode("pointOnSurfaceInfo", name="ptOnSurfInfo_{}".format(name))
	vector_product = cmds.createNode("vectorProduct", name="vecProd_{}".format(name))
	four_by_four_matrix = cmds.createNode("fourByFourMatrix", name = "fbfMatrix_{}".format(name))
	decompose_matrix = cmds.createNode("decomposeMatrix", name="dMatrix_{}".format(name))

	# insert joint here

	# Make connection system
	cmds.connectAttr("{}.worldSpace[0]".format(ribbon), "{}.inputSurface".format(point_on_surface_info))

	cmds.connectAttr("{}.normal".format(point_on_surface_info), "{}.input1".format(vector_product))
	cmds.connectAttr("{}.tangentV".format(point_on_surface_info), "{}.input2".format(vector_product))

	cmds.connectAttr("{}.normalX".format(point_on_surface_info), "{}.in00".format(four_by_four_matrix))
	cmds.connectAttr("{}.normalY".format(point_on_surface_info), "{}.in01".format(four_by_four_matrix))
	cmds.connectAttr("{}.normalZ".format(point_on_surface_info), "{}.in02".format(four_by_four_matrix))

	cmds.connectAttr("{}.tangentVx".format(point_on_surface_info), "{}.in10".format(four_by_four_matrix))
	cmds.connectAttr("{}.tangentVy".format(point_on_surface_info), "{}.in11".format(four_by_four_matrix))
	cmds.connectAttr("{}.tangentVz".format(point_on_surface_info), "{}.in12".format(four_by_four_matrix))

	cmds.connectAttr("{}.outputX".format(vector_product), "{}.in20".format(four_by_four_matrix))
	cmds.connectAttr("{}.outputY".format(vector_product), "{}.in21".format(four_by_four_matrix))
	cmds.connectAttr("{}.outputZ".format(vector_product), "{}.in22".format(four_by_four_matrix))

	cmds.connectAttr("{}.positionX".format(point_on_surface_info), "{}.in30".format(four_by_four_matrix))
	cmds.connectAttr("{}.positionY".format(point_on_surface_info), "{}.in31".format(four_by_four_matrix))
	cmds.connectAttr("{}.positionZ".format(point_on_surface_info), "{}.in32".format(four_by_four_matrix))

	cmds.connectAttr("{}.output".format(four_by_four_matrix), "{}.inputMatrix".format(decompose_matrix))

	cmds.connectAttr("{}.outputRotate".format(decompose_matrix), "{}.rotate".format(loc))
	cmds.connectAttr("{}.outputTranslate".format(decompose_matrix), "{}.translate".format(loc))


	# Set up U, V parameters for spacing rivet on ribbon
	ratio = 1.0/length
	paramV = ratio*(i+1) - 0.1  
	cmds.setAttr("{}.turnOnPercentage".format(point_on_surface_info), 1)
	cmds.setAttr("{}.parameterU".format(point_on_surface_info), 0.5)
	cmds.setAttr("{}.parameterV".format(point_on_surface_info), paramV)

