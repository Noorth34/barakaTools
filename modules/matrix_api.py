# coding:utf-8 

# Script API de connexion de Matrices en Parent avec Offset
# Connexion entre un Objet nommé Master et un nommé Slave

from maya.api.OpenMaya import *
from maya import cmds

def constraint(type="parent", offset=True):

	sel = MGlobal.getActiveSelectionList() # return MSelectionList object


	master = MMatrix( cmds.getAttr('{}.worldMatrix[0]'.format(sel.getSelectionStrings()[0]) ) )
	slave = MMatrix( cmds.getAttr('{}.worldMatrix[0]'.format(sel.getSelectionStrings()[-1]) ) )


	mMatrix = cmds.createNode('multMatrix', name = "mMatrix_{}_{}".format(sel.getSelectionStrings()[-1], type))

	if offset is True:
		offset = MTransformationMatrix(slave * master.inverse()).asMatrix()

		# connexion de l'Offset

		cmds.setAttr(mMatrix + '.i[0]', offset, type='matrix')
	cmds.connectAttr('{}.matrix'.format(sel.getSelectionStrings()[0]), mMatrix + '.i[1]')

	# Creation et Connexion du Decompose Matrix

	dMatrix = cmds.createNode('decomposeMatrix', name = "dMatrix_{}_{}".format(sel.getSelectionStrings()[-1], type))
	cmds.connectAttr(mMatrix + '.matrixSum', dMatrix + '.inputMatrix')

	# null_indicator = cmds.createNode('transform', n="{}_{}".format(sel.getSelectionStrings()[-1], type))
	# cmds.parent(null_indicator, sel.getSelectionStrings()[-1])

	if type == "parent":
		cmds.connectAttr(dMatrix + '.outputTranslate', '{}.translate'.format(sel.getSelectionStrings()[-1]))
		cmds.connectAttr(dMatrix + '.outputRotate', '{}.rotate'.format(sel.getSelectionStrings()[-1]))

	if type == "point":
		cmds.connectAttr(dMatrix + '.outputTranslate', '{}.translate'.format(sel.getSelectionStrings()[-1]))

	if type == "orient":
		cmds.connectAttr(dMatrix + '.outputRotate', '{}.rotate'.format(sel.getSelectionStrings()[-1]))

	if type == "scale":
		cmds.connectAttr(dMatrix + '.outputScale', '{}.scale'.format(sel.getSelectionStrings()[-1]))


