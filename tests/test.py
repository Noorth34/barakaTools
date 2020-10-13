from constants import *
import os
reload(constants)

path = ROOT_PATH + "/asset_logs.json" 
path = path.replace("/", "\\")
print(path)
with open(path, "w+") as f:
	f.close()

os.system("attrib +h {}".format(path))
"""
path = ROOT_PATH + "/testfile.txt"
with open(path, "a") as f:
	f.write("\nI'm a new line !")
	f.close()
"""