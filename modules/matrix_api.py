# Script API de connexion de Matrices en Parent avec Offset
# Connexion entre un Objet nommé Master et un nommé Slave

from maya.api.OpenMaya import *


sel = MGlobal.getActiveSelectionList() # return MSelectionList object


Master = MMatrix( cmds.getAttr('{}.wm[0]'.format(sel.getSelectionStrings()[0]) ) )
Slave = MMatrix( cmds.getAttr('{}.wm[0]'.format(sel.getSelectionStrings()[-1]) ) )


Offset = MTransformationMatrix(Slave * Master.inverse()).asMatrix()

# Creation du Mult Matrix avec connexion de l'Offset

MultMatX = cmds.createNode('multMatrix', name = "MultMatX")

cmds.setAttr(MultMatX + '.i[0]', Offset, type='matrix')
cmds.connectAttr('{}.matrix'.format(sel.getSelectionStrings()[0]), MultMatX + '.i[1]')

# Creation et Connexion du Decompose Matrix

DecMatX = cmds.createNode('decomposeMatrix', name = "DecMatX")

cmds.connectAttr(MultMatX + '.matrixSum', DecMatX + '.inputMatrix')
cmds.connectAttr(DecMatX + '.outputTranslate', '{}.t'.format(sel.getSelectionStrings()[-1]))
cmds.connectAttr(DecMatX + '.outputRotate', '{}.r'.format(sel.getSelectionStrings()[-1]))