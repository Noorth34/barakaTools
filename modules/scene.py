#coding:utf-8

import pymel.core.system as pms
import modules.path as Path
import modules.file as File
from constants import *

_asset = "asset"
_state = "state"
_type = "type"
_index = "index"


def save(type):

	return pms.saveFile(type= type)


def saveAs(dest):

	return pms.saveAs(dest)


def exportSelection(dest, type):

	return pms.exportSelected(dest, type= type)


def edit():
	pass


def publish():
	pass


def createCharacter(name):

	pass

