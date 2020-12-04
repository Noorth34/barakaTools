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

    def check_selection(func, obj=None, type=None, msg="Any selection. Please select something"):
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
    def import_scene(scene):

        return pms.importFile(scene, force=True,)

    @staticmethod
    def reference_scene(scene):

        return pms.createReference(scene, force=True, defaultNamespace=True)

    @staticmethod
    def open_scene(scene):

        return pms.openFile(scene, force=True)

    @staticmethod
    def save(type):

        return str( pms.saveFile(type=type) )

    @staticmethod
    def save_as(dest):

        return str( pms.saveAs(dest) )

    @staticmethod
    def export_selection(dest, type):

        return str( pms.exportSelected(dest, type=type) )

    @staticmethod
    def edit():

        scene = Scene.get_name()
        edit = Scene.increment_index(scene)
        cmds.inViewMessage(amg='Asset edited: \n <hl>' + edit + '</hl>.', pos='topCenter', fade=True)
        return Scene.save_as(edit)

    @staticmethod
    @partial(check_selection, type="mesh", msg="Select geo before publish")
    def alembic_export(file, start=1, end=1):

        to_export = " ".join( cmds.ls(sl=True, long=True, ap=True) )

        abc_file = None
        # //gandalf/3d4_20_21/barakafrites/04_asset/character/patatax/maya/scenes/edit/geo/patatax_E_geo_0001.ma
        # //gandalf/3d4_20_21/barakafrites/04_asset/character/patatax/maya/cache/patatax_P_geo_0001.abc
        if "/04_asset/" and "/geo/" in file:
            abc_file = file.replace("/scenes/edit/geo", "/cache/alembic").replace("_E_", "_P_").replace(".ma", ".abc")
        # //gandalf/3d4_20_21/barakafrites/05_shot/shotTest/maya/scenes/edit/anim/patatax_E_anim_0001.ma
        # //gandalf/3d4_20_21/barakafrites/05_shot/shotTest/maya/cache/patatax_E_anim_0001.abc
        if "/05_shot/" and "/anim/" in file:
            abc_file = file.replace("/scenes/edit/anim", "/cache/alembic").replace("_E_", "_P_").replace(".ma", ".abc")
         
        command = "-frameRange {} {} -autoSubd -uvWrite -worldSpace -root {} -file {}".format(start, end, to_export, abc_file)

        cmds.AbcExport(j = command)

    @staticmethod
    @check_selection
    def publish(selection=[]):

        # Variables

        scene = Scene.get_name()  # ../maya/scenes/edit/geo/........

        asset = Scene.get_asset(scene)
        state = Scene.get_state(scene)
        type = Scene.get_type(scene)
        index = Scene.get_index(scene)

        scene_name = File.get_short_name(scene)
        state_changed_scene = scene_name.replace("_E_", "_P_")
        state_changed_scene_no_index = state_changed_scene.replace("_" + index, "")

        if "/items/" in scene:
            dir_backup = Scene.create_dir_backup(item=True)
            dir_publish = scene.replace("/edit/", "/publish/").replace("/{}/".format(asset), "").replace(scene_name, "")

            full_backup_scene_path = dir_backup + "/" + asset + "/" + state_changed_scene
            full_publish_scene_path = dir_publish + "/" + state_changed_scene_no_index

        else:
            dir_backup = Scene.create_dir_backup()

            dir_publish = scene.replace("/edit/", "/publish/").replace(scene_name, "")

            full_backup_scene_path = dir_backup + "/" + state_changed_scene
            full_publish_scene_path = dir_publish + "/" + state_changed_scene_no_index

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

        Scene.export_selection(full_backup_scene_path, "mayaAscii")
        print("Asset backup : {}".format(full_backup_scene_path))
        Scene.export_selection(full_publish_scene_path, "mayaAscii")
        print("Asset published : {}".format(full_publish_scene_path))

        # Alembic
        # Scene.alembicExport(scene)
        
        cmds.inViewMessage(amg='Asset published: \n <hl>' + full_publish_scene_path + '</hl>. \n Publish backup: \n <hl>' + full_backup_scene_path + '</hl>.', pos='topCenter', fade=True)

    @staticmethod
    def create_dir_backup(scene=None, item=False):

        if scene is None:
            scene = Scene.get_name()
        
        asset = Scene.get_asset(scene)

        if item == True:
            publish_dir = File.get_parent(scene).replace("/edit/", "/publish/").replace("/{}".format(asset), "")
        else:
            publish_dir = File.get_parent(scene).replace("/edit/", "/publish/")

        if not "backup" in Directory.get_children(publish_dir):
            backup = Directory.create(publish_dir, name="backup")
            print("Directory 'backup' created : {}".format(backup))
            return backup
        else:
            return publish_dir + "/backup"

    @staticmethod
    def increment_index(scene):

        if not scene:
            scene = Scene.get_name()
        scene = Path.delete_extension(scene)

        current_index = scene.split("/")[-1].split("_")[-1]
        new_index = str(int(current_index) + 1)
        new_index = new_index.zfill(4)

        scene = scene.replace(current_index, new_index)
        scene = Path.add_extension(scene, ".ma")
        return scene

    @staticmethod
    def get_name():

        return str( pms.sceneName() )

    @staticmethod
    def get_asset(scene):

        return scene.split("/")[-1].split("_")[0]

    @staticmethod
    def get_state(scene):

        return scene.split("/")[-1].split("_")[-3]

    @staticmethod
    def get_type(scene):

        return scene.split("/")[-1].split("_")[-2]

    @staticmethod
    def get_index(scene):

        scene_with_no_ext = Path.delete_extension(scene)
        return scene_with_no_ext.split("/")[-1].split("_")[-1]

    @staticmethod
    def create_character(name):

        char = const.PIPELINE_CHARACTERS + "/{}".format(name)
        Directory.copy(const.TEMPLATE_ASSET_DIRS, char)

        # init_scene = char + "/maya/scenes/edit/geo/{}_E_geo_0001.ma".format(name)
        dir_edit = "{}/maya/scenes/edit".format(char)

        for dir in Directory.get_children(dir_edit):
            init_scene = "{}_E_{}_0001.ma".format(name, dir)
            File.copy(const.TEMPLATE_ASSET_SCENE, "{}/{}/{}".format(dir_edit, dir, init_scene))

        return char

    @staticmethod
    def create_set(name):

        set = const.PIPELINE_SETS + "/{}".format(name)
        Directory.copy(const.TEMPLATE_SET_DIRS, set)

        dir_edit = "{}/maya/scenes/edit".format(set)

        for dir in Directory.get_children(dir_edit):
            init_scene = "{}_E_{}_0001.ma".format(name, dir)
            File.copy(const.TEMPLATE_ASSET_SCENE, "{}/{}/{}".format(dir_edit, dir, init_scene))

        return set

    @staticmethod
    def create_prop(name):

        prop = const.PIPELINE_PROPS + "/{}".format(name)
        Directory.copy(const.TEMPLATE_ASSET_DIRS, prop)

        dir_edit = "{}/maya/scenes/edit".format(prop)

        for dir in Directory.get_children(dir_edit):
            init_scene = "{}_E_{}_0001.ma".format(name, dir)
            File.copy(const.TEMPLATE_ASSET_SCENE, "{}/{}/{}".format(dir_edit, dir, init_scene))

        return prop

    @staticmethod
    def create_item(name, set):

        parent_set = const.PIPELINE_SETS + "/{}".format(set)
        items_path = parent_set + "/maya/scenes/edit/geo/items/"
        item_folder = Directory.create(items_path, name=name)
        # {}_E_geo_0001.ma".format(name)"
        File.copy(const.TEMPLATE_ASSET_SCENE, "{}/{}_E_geo_0001.ma".format(item_folder, name))

        return item_folder


    @staticmethod
    def create_sequence(name):

        seq_path = const.PIPELINE_SHOT_PATH + "/" + name
        Directory.copy(const.TEMPLATE_SEQUENCE_DIRS, seq_path)

        for folder in Directory.get_children("{}/master/maya/scenes".format(seq_path)):
            File.copy(const.TEMPLATE_ASSET_SCENE, "{}/master/maya/scenes/{}/{}_{}_0001.ma".format(seq_path, folder, name, folder))

        return seq_path


    @staticmethod
    def create_shot(name, seq):

        shot_path = const.PIPELINE_SHOT_PATH + "/{}/{}".format(seq, name)
        Directory.copy(const.TEMPLATE_SHOT_DIRS, shot_path)

        scenes_folder = "{}/maya/scenes/".format(shot_path)

        for folder in Directory.get_children(scenes_folder):
            init_scene = "{}_{}_0001.ma".format(name, folder)
            File.copy( const.TEMPLATE_ASSET_SCENE, "{}/{}/{}".format(scenes_folder, folder, init_scene) )

        return shot_path