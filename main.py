#coding:utf-8

"""
"""
import sys
import mainDialog
import autorig.autorigDialog
import constants
from PySide2.QtWidgets import QApplication


reload(mainDialog)
reload(constants)
#reload(autorig.autorigDialog)
#reload(manager.managerDialog)


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


	mainWidget = mainDialog.MainDialogInstance()
	mainWidget.show()
	mainApp.exec_()
