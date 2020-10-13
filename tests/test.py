from constants import *
from pipeline.pipeline import File 
reload(constants)
reload(pipeline.pipeline)

path = ROOT_PATH + "/asset_logs.json" 
print(path)
with open(path, "w+") as f:
	f.close()

logFile = File(path)
logFile.setHidden()
"""
path = ROOT_PATH + "/testfile.txt"
with open(path, "a") as f:
	f.write("\nI'm a new line !")
	f.close()
"""