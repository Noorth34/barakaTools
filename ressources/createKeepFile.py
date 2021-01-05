# coding: utf-8

import os

path = "C:\\Users\\g.vidal\\Documents\\maya\\2020\\scripts\\barakaTools\\ressources\\_template_workspace_shot"

for root, dirs, files in os.walk(path):
	for dir in dirs:
		f = open(root + "/" + dir + "/" + ".keep", "a+")
		os.system("attrib +h {}".format(root + "/" + dir + "/" + ".keep"))

print("0")
