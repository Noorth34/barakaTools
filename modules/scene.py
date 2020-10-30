# coding:utf-8

import pymel.core.system as pms
import maya.cmds as cmds
import modules.path as Path
import modules.file as File
import modules.directory as Dir
import modules.selection as Sel
from constants import *

reload(Sel)


def save(type):

    return pms.saveFile(type=type)


def saveAs(dest):

    return pms.saveAs(dest)


def exportSelection(dest, type):

    return pms.exportSelected(dest, type=type)


def edit():

    scene = cmds.file(q=True, sn=True)
    edit = incrementIndex(scene)
    return pms.saveAs(edit)


def publish(selection = []):
    
    # Variables

    scene = getScene() #../maya/scenes/edit/geo/........

    asset = getAsset(scene)
    state = getState(scene)
    type = getType(scene)
    index = getIndex(scene)

    shortSceneName = File.getShortFileName(scene)
    stateChangedScene = shortSceneName.replace("_E_", "_P_")
    stateChangedSceneNoIndex = stateChangedScene.replace("_" + index, "")
    dirBackup = createDirBackup()
    dirPublish = scene.replace("/edit/", "/publish/").replace(shortSceneName, "")

    fullBackupScenePath = dirBackup + "/" + stateChangedScene
    fullPublishScenePath = dirPublish + "/" + stateChangedSceneNoIndex

    # Securities

    if not selection:
        selection = Sel.get()
        if not selection:
            cmds.error("Select the TOP group before publish.")

    if len(selection) != 1:
        cmds.error("Multiple selection. Just select the TOP group for publish.")

    if not "TOP_" in selection[0]:
        cmds.error("Bad selection. Please select the TOP group for publish.")

    exportSelection(fullBackupScenePath, "mayaAscii")
    print("Asset backup : {}".format(fullBackupScenePath))
    exportSelection(fullPublishScenePath, "mayaAscii")
    print("Asset published : {}".format(fullPublishScenePath))
    

def createDirBackup(scene=None):

    if scene is None:
        scene = cmds.file(q=True, sn=True)

    publishDir = File.getParent(scene).replace("/edit/", "/publish/")

    if not "backup" in Dir.getChildren(publishDir):
        backup = Dir.createDir(publishDir, name="backup")
        print("Directory 'backup' created : {}".format(backup))
        return backup
    else:
        return publishDir + "/backup"

def incrementIndex(scene):

    if not scene:
        scene = pms.sceneName()
    scene = Path.deleteExtension(scene)

    currentIndex = scene.split("/")[-1].split("_")[-1]
    newIndex = str(int(currentIndex) + 1)
    newIndex = newIndex.zfill(4)

    scene = scene.replace(currentIndex, newIndex)
    scene = Path.addExtension(scene, ".ma")
    return scene

def getScene():

    return cmds.file(q=True, sn=True)

def getAsset(scene):

    return scene.split("/")[-1].split("_")[0]

def getState(scene):

    return scene.split("/")[-1].split("_")[-3]

def getType(scene):

    return scene.split("/")[-1].split("_")[-2]

def getIndex(scene):

    sceneWithNoExt = Path.deleteExtension(scene)
    return sceneWithNoExt.split("/")[-1].split("_")[-1]

def createCharacter(name):

    char = PIPELINE_CHARACTERS + "/{}".format(name)
    Dir.copyTo(TEMPLATE_ASSET_DIRS, char)

    initScene = char + "/maya/scenes/edit/geo/{}_E_geo_0001.ma".format(name)
    File.copyTo(TEMPLATE_ASSET_SCENE, initScene)

    return char


def createSet(name):

    set = PIPELINE_SETS + "/{}".format(name)
    Dir.copyTo(TEMPLATE_ASSET_DIRS, set)

    initScene = set + "/maya/scenes/edit/geo/{}_E_geo_0001.ma".format(name)
    File.copyTo(TEMPLATE_ASSET_SCENE, initScene)

    return set


def createProp(name):

    prop = PIPELINE_PROPS + "/{}".format(name)
    Dir.copyTo(TEMPLATE_ASSET_DIRS, prop)

    initScene = prop + "/maya/scenes/edit/geo/{}_E_geo_0001.ma".format(name)
    File.copyTo(TEMPLATE_ASSET_SCENE, initScene)

    return prop
