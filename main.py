#coding:utf-8

"""
"""
import sys
import launcher
import autorig.autorigDialog
import manager.managerDialog
import constants
from PySide2.QtWidgets import QApplication


reload(launcher)
reload(constants)
reload(autorig.autorigDialog)
reload(manager.managerDialog)


if __name__ == "__main__":
	
	global mainWidget

	try:
		mainWidget.close()
	except:
		pass		
	
	try:
		mainApp = QApplication(sys.argv)
	except:
		mainApp = QApplication.instance()


	mainWidget = launcher.LauncherInstance()
	mainWidget.show()
	mainApp.exec_()
