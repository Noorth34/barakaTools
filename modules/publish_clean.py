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

	transform = cmds.listRelatives(geo, parent=True, path=True)
	
	translates = cmds.xform(transform, q=True, translation=True)
	rotates = cmds.xform(transform, q=True, rotation=True)
	scales = cmds.xform(transform, q=True, scale=True, relative=True)
	
	for t, r, s in zip(translates, rotates, scales):
		if t != 0 or r != 0 or s != 1:
			cmds.error("Object has transforms. Please freeze transforms before publish.")
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
		cmds.error("Object pivot is at Babelwed. Please center pivot each geometry before publish.")


def check_geo_history(geo):
	# history
	history = cmds.listConnections(geo, connections=True, destination=False) # get input connections
	
	if history:
		cmds.error("Geometries have a construction history. Please delete history for each geometry before publish.")
		return 1
######### TO DEBUG 

def check_holes_in_geometry(geo):

	edges = MeshEdge(geo)
	non_two_faces_edges = [ str(edge) for edge in edges if len(edge.connectedFaces()) < 2 ]

	if non_two_faces_edges:
		cmds.select(non_two_faces_edges, add=True)
		cmds.warning("Some geometries are opened. Please close all geometries before publish.")
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


def check_non_4_sided_faces(geo):

	faces = MeshFace(geo)
	non_4_sided_faces = [str(face) for face in faces if len(face.connectedEdges()) % 2 == 1]

	if non_4_sided_faces:
		cmds.select(non_4_sided_faces, add=True)
		cmds.warning("Geometries have non-4-sided faces. Please retopoly geometries to have quads (or tris...)")
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

	if non_manifold_uvs or non_manifold_uv_edges:
		cmds.warning("All those UVs are non-manifold: \n [{}] \n Please cleanup that shit.".format( ", ".join( non_manifold_uvs ) ))
		cmds.warning("All those UV edges are non-manifold: \n [{}] \n Please cleanup that shit.".format( ", ".join( non_manifold_uv_edges ) ))
		cmds.select(non_manifold_edges, add=True)
		cmds.select(non_manifold_vertices, add=True)
		return 1


def check_geo_shape(geo):

	exceptions = [

	check_geo_transforms(geo),
	check_geo_pivot(geo),
	check_geo_history(geo),
	check_holed_faces(geo),
	check_holes_in_geometry(geo),
	check_lamina_faces(geo),
	check_non_4_sided_faces(geo),
	check_non_manifold_components(geo),
	check_non_manifold_uvs(geo)

	]

	if 1 in exceptions:
		cmds.error("Geometries cannot be published.")

