# coding:utf-8

"""
#################################
Function to prevent bad publish.
#################################

• check nomenclature

• check geometries :
					- transforms (0, 0, 0)
					- pivot (center pivot / world)
					- History
					- non 4-edges face
					- non-manifolds
					- lamina-faces
					- holes
					- UVs

cmds.polyInfo
cmds.polyClean

"""

from maya import cmds
from pymel.core.general import MeshFace


def check_geo_transforms(geo):

	transform = cmds.listRelatives(geo, parent=True, path=True)
	
	translates = cmds.xform(transform, q=True, translation=True)
	rotates = cmds.xform(transform, q=True, rotation=True)
	scales = cmds.xform(transform, q=True, scale=True)
	
	for t, r, s in zip(translates, rotates, scales):
		if t != 0 or r != 0 or s != 1:
			cmds.error("Object has transforms. Please freeze transforms before publish.")
			
	cmds.warning("Object's transforms are clean.")


def check_geo_pivot():

	parent = cmds.listRelatives(geo, parent=True, path=True)[0]
	
	geo_bbox = cmds.xform(cmds.ls(sl=True, ap=True), q=True, bb=True)

	bbox_min = geo_bbox[0:3]
	bbox_max = geo_bbox[3:]
	
	bbox_center = []
	for min, max in zip(bbox_min, bbox_max):
		average = (min + max)/2.0
		bbox_center.append(average)
	
	current_pivot = cmds.getAttr("{}.rotatePivot".format(parent))
	
	if current_pivot != bbox_center:
		cmds.error("Object pivot is at Babelwed. Please center pivot each geometry before publish.")


def check_geo_history(geo):
	# history
	history = cmds.listConnections(geo, connections=True, destination=False) # get input connections
	
	if history:
		cmds.error("Geometries have a construction history. Please delete history for each geometry before publish.")
	
	cmds.warning("Geometries' construction history are clean.")


def check_geo_shape(geo):

	# holes
	faces = MeshFace(geo)

	holed_faces = [str(holed_face) for holed_face in faces if face.isHoled()]

	if holed_faces:
		print("All those faces are holed: \n [{}] \n Please cleanup that shit.".format( ", ".join( holed_faces ) ) )

	# lamina faces
	lamina_faces = [str(lamina_face) for lamina_face in faces if face.isLamina()]

	if lamina_faces:
		print("All those faces are holed: \n [{}] \n Please cleanup that shit.".format( ", ".join( lamina_faces ) ) )

	# non manifold
	non_manifold_edges = cmds.polyInfo(geo, nonManifoldEdges=True)
	non_manifold_vertices = cmds.polyInfo(geo, nonManifoldVertices=True)

	# UVs bugs
	non_manifold_uvs = cmds.polyInfo(geo, nonManifoldUVs=True)
	non_manifold_uv_edges = cmds.polyInfo(geo, nonManifoldUVEdges=True)
