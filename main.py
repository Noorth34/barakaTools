#coding:utf-8

"""
"""
import mainDialog
from PySide2.QtWidgets import QApplication


reload(mainDialog)

# OPTIMISATION: voir si le code du Dialog principal ne serait pas mieux directement dans le main.py

if __name__ == "__main__":
		
	app = QApplication.instance()
	widget = mainDialog.BarakaToolsDialogInstance()
	widget.show()
	app.exec_()


