#coding:utf-8

from PySide2.QtWidgets import QApplication, QWidget, QDialog, QLabel, QHBoxLayout, QVBoxLayout, QCheckBox, QGroupBox, QPushButton, QMessageBox
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


	def initMainDialog(self):

		VBoxMainButtons = QVBoxLayout(self)

		autorigButton = QPushButton("Autorig", self)
		autorigButton.setIcon( QIcon(BARAKA_ICONS_PATH + "/burger.png") )
		autorigButton.clicked.connect(self.openManager)
		autorigButton.setToolTip("This is the autorig tool box")
		VBoxMainButtons.addWidget(autorigButton)

		managerButton = QPushButton("Manager", self)
		managerButton.setIcon( QIcon(BARAKA_ICONS_PATH + "/coca.png") )
		managerButton.clicked.connect(self.printHello)
		VBoxMainButtons.addWidget(managerButton)

		helpButton = QPushButton("Help", self)
		helpButton.setIcon( QIcon(BARAKA_ICONS_PATH + "/help.png") )
		helpButton.clicked.connect(self.printHello)
		VBoxMainButtons.addWidget(helpButton)
	

	def initManagerDialog(self):

		self.managerDialog = QDialog(self)
		self.managerDialog.setWindowTitle("BrkAutorig")
		self.managerDialog.setWindowIcon(QIcon( BARAKA_ICONS_PATH + "/burger.png") )
		self.managerDialog.setGeometry(600, 400, 225, 0)
		self.managerDialog.setMinimumSize(225, 200)
		self.managerDialog.setMaximumSize(600, 500)

		VBoxAutorigButtons = QVBoxLayout(self.managerDialog)
		ribbonButton = QPushButton("Ribbonize", self.managerDialog)
		VBoxAutorigButtons.addWidget(ribbonButton)

	def openManager(self):

		self.managerDialog.show()


	def printHello(self):
		print(__file__)




		
		