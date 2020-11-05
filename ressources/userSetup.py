import maya.cmds as cmds
import sys
from maya import utils
import autoSetProject



def sublimeConnect():
	# Close ports if they were already open under another configuration
	try:
	    cmds.commandPort(name=":7001", close=True)
	except:
	    cmds.warning('Could not close port 7001 (maybe it is not opened yet...)')
	try:
	    cmds.commandPort(name=":7002", close=True)
	except:
	    cmds.warning('Could not close port 7002 (maybe it is not opened yet...)')

	# Open new ports
	cmds.commandPort(name=":7001", sourceType="mel")
	cmds.commandPort(name=":7002", sourceType="python")

try:
	sys.path.append("D:/Documents/Programmation/Python/Projets/barakaTools")
	sys.path.append("D:/Documents/Programmation/Python/Projets/barakaTools/Lib/site-packages")
	sys.path.append("D:/Documents/Programmation/Python/Projets/barakaTools/modules")
except:
	pass

try:
	sys.path.append("C:/Users/{}/Documents/maya/2020/scripts/barakaTools".format(os.environ['username']))
	sys.path.append("C:/Users/{}/Documents/maya/2020/scripts/barakaTools/Lib/site-packages".format(os.environ['username']))
	sys.path.append("C:/Users/{}/Documents/maya/2020/scripts/barakaTools/modules".format(os.environ['username']))
except:
	pass

sublimeConnect()

cmds.evalDeferred(autoSetProject.main)