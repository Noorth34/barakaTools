# coding: utf-8

import os

path = "C:\\Users\\g.vidal\\Documents\\maya\\2020\\scripts\\barakaTools\\ressources\\_template_workspace_asset"

for dir in os.walk(path):
	with open(".keep", "w+") as file:
		file.close()

print("0")
