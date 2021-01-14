# coding:utf-8

from configparser import ConfigParser
from modules.path import Path


BARAKA_PATH = Path.convert_backslash_to_slash( __file__.split("\\")[0] )
BARAKA_CONFIG_PATH = BARAKA_PATH + "/config.ini"
BARAKA_ICONS_PATH = BARAKA_PATH + "/icons"
BARAKA_STYLESHEETS_PATH = BARAKA_PATH + "/qt/stylesheets"
BARAKA_IMAGES_PATH = BARAKA_PATH + "/qt/images"
BARAKA_RESSOURCES_PATH = BARAKA_PATH + "/ressources"


BARAKA_TEMP_PATH = BARAKA_PATH + "/.temp"


TEMPLATE_ASSET_DIRS = BARAKA_RESSOURCES_PATH + "/_template_workspace_asset"
TEMPLATE_SET_DIRS = BARAKA_RESSOURCES_PATH + "/_template_workspace_set"
TEMPLATE_SEQUENCE_DIRS = BARAKA_RESSOURCES_PATH + "/_template_workspace_sequence"
TEMPLATE_SHOT_DIRS = BARAKA_RESSOURCES_PATH + "/_template_workspace_shot"
TEMPLATE_ASSET_SCENE = BARAKA_RESSOURCES_PATH + "/asset_state_type_index.ma"
TEMPLATE_LOG = BARAKA_RESSOURCES_PATH + "/_template_log.json"
ASSET_TYPES = {
    "Modeling": "mod",
    "Rigging": "rig",
    "Animation": "anim",
    "Lookdev": "lookdev",
    "Lighting": "lighting"
}

config = ConfigParser()
config.read(BARAKA_CONFIG_PATH)

FILE_TO_IGNORE_LIST = config["PIPELINE"]["ignore"]


PIPELINE_ROOT_PATH = config["PATH"]["root"]

PIPELINE_ASSET_PATH = PIPELINE_ROOT_PATH + "/04_asset"
PIPELINE_CHARACTERS = PIPELINE_ASSET_PATH + "/character"
PIPELINE_FX = PIPELINE_ASSET_PATH + "/FX"
PIPELINE_PROPS = PIPELINE_ASSET_PATH + "/prop"
PIPELINE_SETS = PIPELINE_ASSET_PATH + "/set"


PIPELINE_SHOT_PATH = PIPELINE_ROOT_PATH + "/05_shot"


