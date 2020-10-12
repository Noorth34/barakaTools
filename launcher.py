#coding:utf-8

from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon, QPixmap, Qt
from autorig.autorigDialog import AutorigDialogInstance
from manager.managerDialog import ManagerDialogInstance
from constants import *
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance


def getMayaMainWindow():
	omui.MQtUtil.mainWindow()    
	ptr = omui.MQtUtil.mainWindow()    
	widget = wrapInstance(long(ptr), QWidget)
	return widget


class LauncherInstance(QDialog):
	"""
	"""
	def __init__(self):
		"""
		"""
		QDialog.__init__(self)

		self.autorigDialog = AutorigDialogInstance()
		self.managerDialog = ManagerDialogInstance()

		self.width = 200
		self.height = 300

		self.setWindowTitle("Brk Launcher")
		self.setWindowIcon(QIcon( BARAKA_ICONS_PATH + "/frites.png") )
		self.setGeometry(600, 400, 0, 0)
		self.setFixedSize(self.width, self.height)


		self.initUI()
		


	def initUI(self):

		image = QLabel()
		image.setPixmap( QPixmap(BARAKA_IMAGES_PATH + "/title.png") )
		image.setAlignment(Qt.AlignCenter)

		mainButtonsVBox = QVBoxLayout(self)
		mainButtonsVBox.addWidget(image)

		autorigButton = QPushButton("Autorigs", self)
		autorigButton.setIcon( QIcon(BARAKA_ICONS_PATH + "/burger.png") )
		autorigButton.clicked.connect(self.autorigDialog.open)
		autorigButton.setToolTip("This is the autorig tool box")
		mainButtonsVBox.addWidget(autorigButton)

		managerButton = QPushButton("Manager", self)
		managerButton.setIcon( QIcon(BARAKA_ICONS_PATH + "/coca.png") )
		managerButton.clicked.connect(self.managerDialog.open)
		mainButtonsVBox.addWidget(managerButton)

		helpButton = QPushButton("Help", self)
		helpButton.setIcon( QIcon(BARAKA_ICONS_PATH + "/help.png") )
		helpButton.clicked.connect(self.printSomething)
		mainButtonsVBox.addWidget(helpButton)


	def printSomething(self):

		print("Hey buddy")

