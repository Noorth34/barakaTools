# coding : utf-8

import json
import constants as const
from modules.file import File
from modules.scene import Scene
from os.path import exists
from datetime import datetime, date


def write_json(data, filename=""):
	with open(filename, "w") as f:
		json.dump(data, f, sort_keys=True, indent=2)


def commit(message, filename):

	if not exists(filename):
		File.copy(const.TEMPLATE_LOG, filename)

	if exists(filename):
		with open(filename) as f:
			
			data = json.load(f)
			temp = data["logs"]
			temp.append({"0_Date": str(date.today().strftime("%d/%m/%Y")),
						 "1_Time" : str(datetime.now().time().strftime("%H:%M:%S")),
						 "2_Version" : Scene.get_name().split("/")[-1],
						 "3_Commit" : message})

		write_json(data, filename)