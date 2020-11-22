#-*- coding:utf-8 -*-

"""
Limb Autorig
"""
import maya.cmds as cmds
import ZFunctions
reload(ZFunctions)
		
# Create Asset Hierarchy
hierarchy = ZFunctions.createRigScene("toto")
ZFunctions.createSuffix(hierarchy, "01")

# Limb Elements creation
locs = cmds.ls(sl=True)
curves = ZFunctions.createCurveFromLocs(locs=locs, name=['Crv_Arm_L', 'Crv_Forearm_L'], deg = 3, numSpans = 1, multiCurves=True)
bones = ZFunctions.createJointsFromLocs(orient="xyz", rotationAxis="xdown", locs=locs)
forearmJoints = ZFunctions.createJointsChain(6, "Bind_Forearm_L", 2)
armJoints = ZFunctions.createJointsChain(6, "Bind_Arm_L", 2)

ZFunctions.moveJointsOnCurve(armJoints, curves[0], orient="xyz", rotationAxis="xdown")
ZFunctions.moveJointsOnCurve(forearmJoints, curves[-1], orient="xyz", rotationAxis="xdown")

# Create main IkHandle
ikHandleArm = cmds.ikHandle( n='Ik_Arm_L', sj=bones[0], ee=bones[-1] )

# Then ikSplines for twists & bends
ikSplineHandleArm = cmds.ikHandle( n='Ik_Spline_Arm_L', sj=armJoints[0], ee=armJoints[-1], ccv=False, curve = curves[0], solver = 'ikSplineSolver' )
ikSplineHandleForearm = cmds.ikHandle( n='Ik_Spline_Forearm_L', sj=forearmJoints[0], ee=forearmJoints[-1], ccv=False, curve = curves[-1], solver = 'ikSplineSolver' )

# Rename iks effectors
effectors = ZFunctions.renameEffectors()

# Parenting in Hierarchy

cmds.parent(armJoints[0], bones[0])
cmds.parent(curves[0], bones[0])
cmds.parent(forearmJoints[0], bones[1])
cmds.parent(curves[-1], bones[1])