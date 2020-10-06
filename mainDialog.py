#coding:utf-8

from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from barakaTools.autorig.autorigDialog import *
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
		super(MainDialogInstance, self).__init__()

		self.autorigDialog = AutorigDialogInstance()
		self.managerDialog = ManagerDialogInstance()

		self.setWindowTitle("Baraka Tools")
		self.setWindowIcon(QIcon( BARAKA_ICONS_PATH + "/frites.png") )
		self.setGeometry(600, 400, 225, 0)
		self.setFixedSize(200, 280)

		self.initUI()
		self.createMainMenuBar()


	def initUI(self):

		mainButtonsVBox = QVBoxLayout(self)
		self.setLayout(mainButtonsVBox)

		autorigButton = QPushButton("Autorig", self)
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


	def createMainMenuBar(self):

		mainMenu = QMenuBar(self)
		fileMenu = mainMenu.addMenu("File")
		printAction = QAction("Print Hello", self)
		printAction.triggered.connect(self.printSomething)
		fileMenu.addAction(printAction)


	def printSomething(self):
		print("Hey buddy")



class AutorigDialogInstance(QDialog):
	def __init__(self):
		super(AutorigDialogInstance, self).__init__()

		self.setWindowTitle("Autorig")
		self.setWindowIcon(QIcon( BARAKA_ICONS_PATH + "/burger.png") )
		self.setGeometry(800, 500, 225, 0)
		self.setMinimumSize(225, 200)
		self.setMaximumSize(600, 500)

		self.initUI()


	def initUI(self):
		self.autorigTabWidget = QTabWidget()
		
		limbWidget = QWidget()
		eyesWidget = QWidget()
		utilsWidget = QWidget()
		
		autorigVBox = QGridLayout()
		autorigVBox.addWidget(limbWidget)
		autorigVBox.addWidget(limbWidget)
		autorigVBox.addWidget(utilsWidget)

		self.autorigTabWidget.addTab(limbWidget, "Limb")
		self.autorigTabWidget.addTab(eyesWidget, "Eyes")
		self.autorigTabWidget.addTab(utilsWidget, "Utils")


	def open(self):
		self.autorigTabWidget.show()
		
		



class ManagerDialogInstance(QWidget):
	def __init__(self):
		super(ManagerDialogInstance, self).__init__()
		self.setWindowTitle("Manager")
		self.setWindowIcon(QIcon( BARAKA_ICONS_PATH + "/coca.png") )
		self.setGeometry(600, 400, 225, 0)
		self.setMinimumSize(225, 200)
		self.setMaximumSize(600, 500)


	def initManagerDialog(self):
		pass

	def open(self):
		self.show()