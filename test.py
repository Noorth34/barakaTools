from configparser import ConfigParser

config = ConfigParser()
config.read("D:/Documents/Programmation/Python/Projets/barakaTools/config.ini")
config.set("PATHS", "rootPath", "hello")
with open("D:/Documents/Programmation/Python/Projets/barakaTools/config.ini", "wb") as f:
	config.write(f)
	
import constants as const
reload(const)

const.PIPELINE_ROOT_PATH

const.PIPELINE_ROOT_PATH = "hello"
config.set("PATHS", "rootPath", "hello")
with open("D:/Documents/Programmation/Python/Projets/barakaTools/config.ini", "wb") as f:
	config.write(f)