#coding:utf-8

from PySide2.QtWidgets import QApplication, QMainWindow, QMenuBar, QAction, QWidget, QDialog, QLabel, QHBoxLayout, QVBoxLayout, QCheckBox, QGroupBox, QPushButton, QMessageBox
from PySide2.QtGui import QIcon
from constants import *
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance


def getMayaMainWindow():
	omui.MQtUtil.mainWindow()    
	ptr = omui.MQtUtil.mainWindow()    
	widget = wrapInstance(long(ptr), QWidget)
	return widget


class MainDialogInstance(QDialog):
	"""
	"""
	def __init__(self):
		"""
		"""
		super(MainDialogInstance, self).__init__(getMayaMainWindow())

		self.setWindowTitle("Baraka Tools")
		self.setWindowIcon(QIcon( BARAKA_ICONS_PATH + "/frites.png") )
		self.setGeometry(600, 400, 225, 0)
		self.setMinimumSize(225, 200)
		self.setMaximumSize(600, 500)

		self.initMainDialog()
		self.initAutorigDialog()
		self.createMainMenuBar()


	def initMainDialog(self):

		mainButtonsVBox = QVBoxLayout(self)
		self.setLayout(mainButtonsVBox)

		autorigButton = QPushButton("Autorig", self)
		autorigButton.setIcon( QIcon(BARAKA_ICONS_PATH + "/burger.png") )
		autorigButton.clicked.connect(self.openAutorigDialog)
		autorigButton.setToolTip("This is the autorig tool box")
		mainButtonsVBox.addWidget(autorigButton)

		managerButton = QPushButton("Manager", self)
		managerButton.setIcon( QIcon(BARAKA_ICONS_PATH + "/coca.png") )
		managerButton.clicked.connect(self.printSomething)
		mainButtonsVBox.addWidget(managerButton)

		helpButton = QPushButton("Help", self)
		helpButton.setIcon( QIcon(BARAKA_ICONS_PATH + "/help.png") )
		helpButton.clicked.connect(self.printSomething)
		mainButtonsVBox.addWidget(helpButton)
	

	def initAutorigDialog(self):

		self.autorigDialog = QDialog(self)
		self.autorigDialog.setWindowTitle("Autorig")
		self.autorigDialog.setWindowIcon(QIcon( BARAKA_ICONS_PATH + "/burger.png") )
		self.autorigDialog.setGeometry(600, 400, 225, 0)
		self.autorigDialog.setMinimumSize(225, 200)
		self.autorigDialog.setMaximumSize(600, 500)

		autorigButtonsVBox = QVBoxLayout(self.autorigDialog)

		limbButton = QPushButton("Limb", self.autorigDialog)
		limbButton.clicked.connect(self.printSomething)
		autorigButtonsVBox.addWidget(limbButton)

		eyeButton = QPushButton("Eye", self.autorigDialog)
		eyeButton.clicked.connect(self.printSomething)
		autorigButtonsVBox.addWidget(eyeButton)

		utilsButton = QPushButton("Utils", self.autorigDialog)
		utilsButton.clicked.connect(self.printSomething)
		autorigButtonsVBox.addWidget(utilsButton)


	def initManagerDialog(self):

		self.managerDialog = QDialog(self)
		self.managerDialog.setWindowTitle("Manager")
		self.managerDialog.setWindowIcon(QIcon( BARAKA_ICONS_PATH + "/coca.png") )
		self.managerDialog.setGeometry(600, 400, 225, 0)
		self.managerDialog.setMinimumSize(225, 200)
		self.managerDialog.setMaximumSize(600, 500)

		

	def createMainMenuBar(self):

		mainMenu = QMenuBar(self)
		fileMenu = mainMenu.addMenu("File")
		printAction = QAction("Print Hello", self)
		printAction.triggered.connect(self.printSomething)
		fileMenu.addAction(printAction)



	def openAutorigDialog(self):

		self.autorigDialog.show()


	def printSomething(self):
		print("Hey buddy")




		
		