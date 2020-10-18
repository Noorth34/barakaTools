#coding:utf-8


PIPELINE_ROOT_PATH = "//gandalf/3D4_20_21/barakafrites/04_asset"

BARAKA_PATH = __file__.split("\\")[0]

BARAKA_ICONS_PATH = BARAKA_PATH + "/icons"

BARAKA_STYLESHEETS_PATH = BARAKA_PATH + "/qt/stylesheets"
BARAKA_IMAGES_PATH = BARAKA_PATH + "/qt/images"

ASSET_TYPES = {
	"Modeling" : "mod", 
	"Rigging" : "rig", 
	"Animation" : "anim", 
	"Lookdev" : "lookdev",
	"Lighting" : "lighting"
}

# Pipeline paths
PIPELINE_CHARACTERS = PIPELINE_ROOT_PATH + "/character"
PIPELINE_FX = PIPELINE_ROOT_PATH + "/FX" 
PIPELINE_PROPS = PIPELINE_ROOT_PATH + "/prop"
PIPELINE_SETS = PIPELINE_ROOT_PATH + "/set"	

