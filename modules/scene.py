# coding:utf-8

import pymel.core.system as pms
import maya.cmds as cmds
from path import Path
from file import File
from directory import Directory
from selection import Selection
from constants import *


class Scene():
    def __init__(self):
        pass

    @staticmethod
    def save(type):

        return pms.saveFile(type=type)

    @staticmethod
    def saveAs(dest):

        return pms.saveAs(dest)

    @staticmethod
    def exportSelection(dest, type):

        return pms.exportSelected(dest, type=type)

    @staticmethod
    def edit():

        scene = getScene()
        edit = incrementIndex(scene)
        return pms.saveAs(edit)

    @staticmethod
    def publish(selection=[]):

        # Variables

        scene = getScene()  # ../maya/scenes/edit/geo/........

        asset = getAsset(scene)
        state = getState(scene)
        type = getType(scene)
        index = getIndex(scene)

        shortSceneName = File.getShortName(scene)
        stateChangedScene = shortSceneName.replace("_E_", "_P_")
        stateChangedSceneNoIndex = stateChangedScene.replace("_" + index, "")
        dirBackup = createDirBackup()
        dirPublish = scene.replace(
            "/edit/", "/publish/").replace(shortSceneName, "")

        fullBackupScenePath = dirBackup + "/" + stateChangedScene
        fullPublishScenePath = dirPublish + "/" + stateChangedSceneNoIndex

        # Securities

        if not selection:
            selection = Selection.get()
            if not selection:
                cmds.error("Select the TOP group before publish.")

        if len(selection) != 1:
            cmds.error(
                "Multiple selection. Just select the TOP group for publish.")

        if not "TOP_" in selection[0]:
            cmds.error(
                "Bad selection. Please select the TOP group for publish.")

        exportSelection(fullBackupScenePath, "mayaAscii")
        print("Asset backup : {}".format(fullBackupScenePath))
        exportSelection(fullPublishScenePath, "mayaAscii")
        print("Asset published : {}".format(fullPublishScenePath))

    @staticmethod
    def createDirBackup(scene=None):

        if scene is None:
            scene = getScene()

        publishDir = File.getParent(scene).replace("/edit/", "/publish/")

        if not "backup" in Dir.getChildren(publishDir):
            backup = Directory.create(publishDir, name="backup")
            print("Directory 'backup' created : {}".format(backup))
            return backup
        else:
            return publishDir + "/backup"

    @staticmethod
    def incrementIndex(scene):

        if not scene:
            scene = getScene()
        scene = Path.deleteExtension(scene)

        currentIndex = scene.split("/")[-1].split("_")[-1]
        newIndex = str(int(currentIndex) + 1)
        newIndex = newIndex.zfill(4)

        scene = scene.replace(currentIndex, newIndex)
        scene = Path.addExtension(scene, ".ma")
        return scene

    @staticmethod
    def getScene():

        return str(pms.sceneName())

    @staticmethod
    def getAsset(scene):

        return scene.split("/")[-1].split("_")[0]

    @staticmethod
    def getState(scene):

        return scene.split("/")[-1].split("_")[-3]

    @staticmethod
    def getType(scene):

        return scene.split("/")[-1].split("_")[-2]

    @staticmethod
    def getIndex(scene):

        sceneWithNoExt = Path.deleteExtension(scene)
        return sceneWithNoExt.split("/")[-1].split("_")[-1]

    @staticmethod
    def createCharacter(name):

        char = PIPELINE_CHARACTERS + "/{}".format(name)
        Directory.copy(TEMPLATE_ASSET_DIRS, char)

        initScene = char + \
            "/maya/scenes/edit/geo/{}_E_geo_0001.ma".format(name)
        File.copy(TEMPLATE_ASSET_SCENE, initScene)

        return char

    @staticmethod
    def createSet(name):

        set = PIPELINE_SETS + "/{}".format(name)
        Directory.copy(TEMPLATE_ASSET_DIRS, set)

        initScene = set + "/maya/scenes/edit/geo/{}_E_geo_0001.ma".format(name)
        File.copy(TEMPLATE_ASSET_SCENE, initScene)

        return set

    @staticmethod
    def createProp(name):

        prop = PIPELINE_PROPS + "/{}".format(name)
        Directory.copy(TEMPLATE_ASSET_DIRS, prop)

        initScene = prop + \
            "/maya/scenes/edit/geo/{}_E_geo_0001.ma".format(name)
        File.copy(TEMPLATE_ASSET_SCENE, initScene)

        return prop

