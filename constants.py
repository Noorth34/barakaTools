#coding:utf-8

import socket

ROOT_PATH = "//gandalf/3D4_20_21/barakafrites/04_asset"

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

