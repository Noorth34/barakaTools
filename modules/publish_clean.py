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
					- holes in faces
					- holes in geometry
					- UVs

cmds.polyInfo
cmds.polyClean

"""
from math import trunc
from maya import cmds
from pymel.core.general import MeshFace, MeshEdge

######### TO DEBUG
def check_geo_transforms(geo):

	transform = cmds.listRelatives(geo, parent=True, path=True)[0]
	
	translates = cmds.xform(transform, q=True, translation=True)
	rotates = cmds.xform(transform, q=True, rotation=True)
	scales = cmds.xform(transform, q=True, scale=True, relative=True)
	
	for t, r, s in zip(translates, rotates, scales):
		if t != 0 or r != 0 or s != 1:
			cmds.warning("Object ''{}'' has transforms. Please freeze transforms before publish.".format(transform))
			return 1


def check_geo_pivot(geo):

	transform = cmds.listRelatives(geo, parent=True, path=True)[0]
	current_pivot = cmds.xform(transform, q=True, pivots=True, ws=True)[0:3]

	bbox = cmds.xform(transform, q=True, bb=True)
	bbox_min = bbox[0:3]
	bbox_max = bbox[3:]

	bbox_center = []
	for min, max in zip(bbox_min, bbox_max):
		average = (min+max)/2
		bbox_center.append(average) 

	if current_pivot != bbox_center:
		cmds.warning("''{}'' pivot is at Babelwed. Please center pivot each geometry before publish.".format(transform))


def check_geo_history(geo):
	# history
	history = cmds.listConnections(geo, connections=True, destination=False) # get input connections
	
	if history:
		cmds.warning("''{}'' has a construction history. Please delete history for each geometry before publish.".format(geo))
		return 1
######### TO DEBUG 

def check_holes_in_geometry(geo):

	faces = MeshFace(geo)
	
	faces_around_hole = []
	for face in faces:
		if len(face.connectedFaces()) == 3 and len(face.connectedEdges()) == 8:
			faces_around_hole.append(str(face))

	if len(faces_around_hole):
		cmds.select(faces_around_hole, add=True)
		cmds.warning("''{}'' geometry is opened. Please close all geometries before publish.".format(geo))
		return 1


def check_holed_faces(geo):

	faces = MeshFace(geo)
	holed_faces = [str(face) for face in faces if face.isHoled()]

	if holed_faces:
		cmds.warning("All those faces are holed: \n [{}] \n Please cleanup that shit.".format( ", ".join( holed_faces ) ) )
		cmds.select(holed_faces, add=True)
		return 1


def check_lamina_faces(geo):

	faces = MeshFace(geo)
	lamina_faces = [str(face) for face in faces if face.isLamina()]

	if lamina_faces:
		cmds.warning("All those faces are holed: \n [{}] \n Please cleanup that shit.".format( ", ".join( lamina_faces ) ) )
		cmds.select(lamina_faces, add=True)
		return 1


def check_faces_with_more_4_sides(geo):

	faces = MeshFace(geo)
	non_conform_faces = [str(face) for face in faces if len(face.getEdges()) < 3 or len(face.getEdges()) > 4]

	if non_conform_faces:
		cmds.select(non_conform_faces, add=True)
		cmds.warning("''{}'' have faces with more than 4 sides or less than 3 sides. Please retopoly geometries with quads (or tris...)".format(geo))
		return 1


def check_non_manifold_components(geo):

	non_manifold_edges = cmds.polyInfo(geo, nonManifoldEdges=True)
	non_manifold_vertices = cmds.polyInfo(geo, nonManifoldVertices=True)

	if non_manifold_vertices or non_manifold_edges:
		cmds.warning("All those edges are non-manifold: \n [{}] \n Please cleanup that shit.".format( ", ".join( non_manifold_edges ) ))
		cmds.warning("All those vertices are non-manifold: \n [{}] \n Please cleanup that shit.".format( ", ".join( non_manifold_vertices ) ))
		cmds.select(non_manifold_edges, add=True)
		cmds.select(non_manifold_vertices, add=True)
		return 1


def check_non_manifold_uvs(geo):
	# UVs bugs
	non_manifold_uvs = cmds.polyInfo(geo, nonManifoldUVs=True)
	non_manifold_uv_edges = cmds.polyInfo(geo, nonManifoldUVEdges=True)

	if non_manifold_uvs:
		cmds.warning("All those UVs are non-manifold: \n [{}] \n Please cleanup that shit.".format( ", ".join( non_manifold_uvs ) ))
		cmds.select(non_manifold_uvs, add=True)

	if non_manifold_uv_edges:
		cmds.warning("All those UV edges are non-manifold: \n [{}] \n Please cleanup that shit.".format( ", ".join( non_manifold_uv_edges ) ))
		cmds.select(non_manifold_uvs_edges, add=True)
		return 1


def check_geo(geo):

	exceptions = [

	check_holed_faces(geo),
	check_holes_in_geometry(geo),
	check_lamina_faces(geo),
	check_faces_with_more_4_sides(geo),
	check_non_manifold_components(geo),
	check_non_manifold_uvs(geo),
	check_geo_transforms(geo),
	check_geo_pivot(geo),
	check_geo_history(geo)
	
	]

	if 1 in exceptions:
		cmds.warning("''{}'' cannot be published.".format(geo))

