# coding:utf-8

from configparser import ConfigParser

BARAKA_PATH = __file__.split("\\")[0]
BARAKA_CONFIG_PATH = BARAKA_PATH + "/config.ini"
BARAKA_ICONS_PATH = BARAKA_PATH + "/icons"
BARAKA_STYLESHEETS_PATH = BARAKA_PATH + "/qt/stylesheets"
BARAKA_IMAGES_PATH = BARAKA_PATH + "/qt/images"
BARAKA_RESSOURCES_PATH = BARAKA_PATH + "/ressources"

BARAKA_TEMP_PATH = BARAKA_PATH + "/.temp"

TEMPLATE_ASSET_DIRS = BARAKA_RESSOURCES_PATH + "/_template_workspace_asset"
TEMPLATE_ASSET_SCENE = BARAKA_RESSOURCES_PATH + "/asset_state_type_index.ma"
ASSET_TYPES = {
    "Modeling": "mod",
    "Rigging": "rig",
    "Animation": "anim",
    "Lookdev": "lookdev",
    "Lighting": "lighting"
}

# Pipeline paths
config = ConfigParser()
config.read(BARAKA_PATH + "/config.ini")

global PIPELINE_ROOT_PATH
global PIPELINE_CHARACTERS
global PIPELINE_PROPS
global PIPELINE_SETS

PIPELINE_ROOT_PATH = config["PATHS"]["rootPath"]
# "//gandalf/3D4_20_21/barakafrites/04_asset"

PIPELINE_CHARACTERS = PIPELINE_ROOT_PATH + "/character"
PIPELINE_FX = PIPELINE_ROOT_PATH + "/FX"
PIPELINE_PROPS = PIPELINE_ROOT_PATH + "/prop"
PIPELINE_SETS = PIPELINE_ROOT_PATH + "/set"

PIPELINE_ASSET_PUBLISH = "/scenes/publish"

def refreshConst():
	PIPELINE_CHARACTERS = PIPELINE_ROOT_PATH + "/character"
	PIPELINE_PROPS = PIPELINE_ROOT_PATH + "/prop"
	PIPELINE_SETS = PIPELINE_ROOT_PATH + "/set"
	print("constants refreshed.")

# create Const class with self to have a dynamic object to modify