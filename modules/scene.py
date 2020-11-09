# coding:utf-8

import pymel.core.system as pms
import maya.cmds as cmds
from path import Path
from file import File
from directory import Directory
from selection import Selection
import constants as const
from functools import partial

class Scene():
    def __init__(self):
        pass

    def checkSelection(func, obj=None, type=None, msg="Any selection. Please select something"):
        def wrapper(*args, **kwargs):
            sel = Selection.get()
            if obj:
                if not sel:
                    cmds.error("Any selection. Please select {}".format(obj))
                for i in sel:
                    if not obj in i:
                        cmds.error("Bad selection. Please select {}".format(obj))
            if type:
                for i in sel:
                    if cmds.objectType( cmds.listRelatives(i) ) != type:
                        cmds.error("Selected objects are not {}".format(type))
            if not sel:
                cmds.error(msg)
            return func(*args, **kwargs)
        return wrapper
        
    # @staticmethod
    # @partial(checkSelection, obj="TOP")
    # def _printStuff():
    #     print("GOOD !")

    @staticmethod
    def import_(scene):

        return pms.importFile(scene)

    @staticmethod
    def reference(scene):

        return pms.createReference(scene)

    @staticmethod
    def open_(scene):

        return pms.openFile(scene)

    @staticmethod
    def save(type):

        return str( pms.saveFile(type=type) )

    @staticmethod
    def saveAs(dest):

        return str( pms.saveAs(dest) )

    @staticmethod
    def exportSelection(dest, type):

        return str( pms.exportSelected(dest, type=type) )

    @staticmethod
    def edit():

        scene = Scene.getScene()
        edit = Scene.incrementIndex(scene)
        cmds.inViewMessage(amg='Asset edited: \n <hl>' + edit + '</hl>.', pos='topCenter', fade=True)
        return Scene.saveAs(edit)

    @staticmethod
    @partial(checkSelection, type="mesh", msg="Select geo before publish")
    def alembicExport(file, start=1, end=1):

        toExport = " ".join( cmds.ls(sl=True, long=True, ap=True) )

        abcFIle = None
        # //gandalf/3d4_20_21/barakafrites/04_asset/character/patatax/maya/scenes/edit/geo/patatax_E_geo_0001.ma
        # //gandalf/3d4_20_21/barakafrites/04_asset/character/patatax/maya/cache/patatax_P_geo_0001.abc
        if "/04_asset/" and "/geo/" in file:
            abcFile = file.replace("/scenes/edit/geo", "/cache/alembic").replace("_E_", "_P_").replace(".ma", ".abc")
        # //gandalf/3d4_20_21/barakafrites/05_shot/shotTest/maya/scenes/edit/anim/patatax_E_anim_0001.ma
        # //gandalf/3d4_20_21/barakafrites/05_shot/shotTest/maya/cache/patatax_E_anim_0001.abc
        if "/05_shot/" and "/anim/" in file:
            abcFile = file.replace("/scenes/edit/anim", "/cache/alembic").replace("_E_", "_P_").replace(".ma", ".abc")
         
        command = "-frameRange {} {} -autoSubd -uvWrite -worldSpace -root {} -file {}".format(start, end, toExport, abcFile)

        cmds.AbcExport(j = command)

    @staticmethod
    @checkSelection
    def publish(selection=[]):

        # Variables

        scene = Scene.getScene()  # ../maya/scenes/edit/geo/........

        asset = Scene.getAsset(scene)
        state = Scene.getState(scene)
        type = Scene.getType(scene)
        index = Scene.getIndex(scene)

        shortSceneName = File.getShortName(scene)
        stateChangedScene = shortSceneName.replace("_E_", "_P_")
        stateChangedSceneNoIndex = stateChangedScene.replace("_" + index, "")
        dirBackup = Scene.createDirBackup()
        dirPublish = scene.replace("/edit/", "/publish/").replace(shortSceneName, "")

        fullBackupScenePath = dirBackup + "/" + stateChangedScene
        fullPublishScenePath = dirPublish + "/" + stateChangedSceneNoIndex

        # Securities

        # if not selection:
        #     selection = Selection.get()
        #     if not selection:
        #         cmds.error("Select geo before publish.")

        # if len(selection) != 1:
        #     cmds.error(
        #         "Multiple selection. Just select the TOP_GROUP (or simple geo) for publish.")

        # if not "TOP_" in selection[0]:
        #     cmds.error("Bad selection. Please select the TOP_GROUP (or simple geo) for publish.")

        Scene.exportSelection(fullBackupScenePath, "mayaAscii")
        print("Asset backup : {}".format(fullBackupScenePath))
        Scene.exportSelection(fullPublishScenePath, "mayaAscii")
        print("Asset published : {}".format(fullPublishScenePath))

        cmds.inViewMessage(amg='Asset published: \n <hl>' + fullPublishScenePath + '</hl>. \n Publish backup: \n <hl>' + fullBackupScenePath + '</hl>.', pos='topCenter', fade=True)

    @staticmethod
    def createDirBackup(scene=None):

        if scene is None:
            scene = Scene.getScene()

        publishDir = File.getParent(scene).replace("/edit/", "/publish/")

        if not "backup" in Directory.getChildren(publishDir):
            backup = Directory.create(publishDir, name="backup")
            print("Directory 'backup' created : {}".format(backup))
            return backup
        else:
            return publishDir + "/backup"

    @staticmethod
    def incrementIndex(scene):

        if not scene:
            scene = Scene.getScene()
        scene = Path.deleteExtension(scene)

        currentIndex = scene.split("/")[-1].split("_")[-1]
        newIndex = str(int(currentIndex) + 1)
        newIndex = newIndex.zfill(4)

        scene = scene.replace(currentIndex, newIndex)
        scene = Path.addExtension(scene, ".ma")
        return scene

    @staticmethod
    def getScene():

        return str( pms.sceneName() )

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

        char = const.PIPELINE_CHARACTERS + "/{}".format(name)
        Directory.copy(const.TEMPLATE_ASSET_DIRS, char)

        initScene = char + "/maya/scenes/edit/geo/{}_E_geo_0001.ma".format(name)
        File.copy(const.TEMPLATE_ASSET_SCENE, initScene)

        return char

    @staticmethod
    def createSet(name):

        set = const.PIPELINE_SETS + "/{}".format(name)
        Directory.copy(const.TEMPLATE_SET_DIRS, set)

        initScene = set + "/maya/scenes/edit/geo/{}_E_geo_0001.ma".format(name)
        File.copy(const.TEMPLATE_ASSET_SCENE, initScene)

        return set

    @staticmethod
    def createProp(name):

        prop = const.PIPELINE_PROPS + "/{}".format(name)
        Directory.copy(const.TEMPLATE_ASSET_DIRS, prop)

        initScene = prop + "/maya/scenes/edit/geo/{}_E_geo_0001.ma".format(name)
        File.copy(const.TEMPLATE_ASSET_SCENE, initScene)

        return prop

    @staticmethod
    def createItem(name, set):

        parentSet = const.PIPELINE_SETS + "/{}".format(set)
        item = parentSet + "/maya/scenes/edit/geo/items/{}_E_geo_0001.ma".format(name)
        File.copy(const.TEMPLATE_ASSET_SCENE, item)

        return item

