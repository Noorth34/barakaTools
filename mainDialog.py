#coding:utf-8

from PySide2.QtWidgets import QApplication, QMenuBar, QAction, QWidget, QDialog, QLabel, QHBoxLayout, QVBoxLayout, QCheckBox, QGroupBox, QPushButton, QMessageBox
from PySide2.QtGui import QIcon
from constants import *

class MainDialogInstance(QWidget):
	"""
	"""
	def __init__(self):
		"""
		"""
		super(MainDialogInstance, self).__init__()

		self.setWindowTitle("BrkTools")
		self.setWindowIcon(QIcon( BARAKA_ICONS_PATH + "/frites.png") )
		self.setGeometry(600, 400, 225, 0)
		self.setMinimumSize(225, 200)
		self.setMaximumSize(600, 500)

		self.initMainDialog()
		self.initManagerDialog()
		self.createMainMenuBar()


	def initMainDialog(self):

		mainButtonsVBox = QVBoxLayout(self)
		self.setLayout(mainButtonsVBox)

		autorigButton = QPushButton("Autorig", self)
		autorigButton.setIcon( QIcon(BARAKA_ICONS_PATH + "/burger.png") )
		autorigButton.clicked.connect(self.openManager)
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
	

	def initManagerDialog(self):

		self.managerDialog = QDialog(self)
		self.managerDialog.setWindowTitle("BrkAutorig")
		self.managerDialog.setWindowIcon(QIcon( BARAKA_ICONS_PATH + "/burger.png") )
		self.managerDialog.setGeometry(600, 400, 225, 0)
		self.managerDialog.setMinimumSize(225, 200)
		self.managerDialog.setMaximumSize(600, 500)

		autorigButtonsVBox = QVBoxLayout(self.managerDialog)

		ribbonButton = QPushButton("Ribbonize", self.managerDialog)
		ribbonButton.clicked.connect(self.printSomething)
		autorigButtonsVBox.addWidget(ribbonButton)
		

	def createMainMenuBar(self):
		mainMenu = QMenuBar(self)
		fileMenu = mainMenu.addMenu("File")
		printAction = QAction("Print Hello", self)
		printAction.triggered.connect(self.printSomething)
		fileMenu.addAction(printAction)



	def openManager(self):

		self.managerDialog.show()


	def printSomething(self):
		print("Hello")




		
		