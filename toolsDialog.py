#coding:utf-8

from PySide2.QtWidgets import QApplication, QWidget, QDialog, QLabel, QHBoxLayout, QVBoxLayout, QCheckBox, QGroupBox, QPushButton, QMessageBox
from PySide2.QtGui import QIcon
from constants import *

class BarakaToolsDialogInstance(QWidget):
	"""
	"""
	def __init__(self, parent = None):
		"""
		"""
		super(BarakaToolsDialogInstance, self).__init__(parent)

		self.setWindowTitle("BrkTools")
		self.setWindowIcon(QIcon( BARAKA_PATH + "/icons/frites.png") )
		self.setGeometry(600, 400, 225, 0)
		self.setMinimumSize(225, 200)
		self.setMaximumSize(600, 500)
		
		

		vbox = QVBoxLayout(self)

		autorigButton = QPushButton("Autorig", self)
		autorigButton.clicked.connect(self.quitApp)
		vbox.addWidget(autorigButton)
		autorigButton.setToolTip("This is the autorig tool box")

		managerButton = QPushButton("Manager", self)
		managerButton.clicked.connect(self.quitApp)
		vbox.addWidget(managerButton)

		helpButton = QPushButton("Help", self)
		helpButton.clicked.connect(self.quitApp)
		vbox.addWidget(helpButton)

		hbox = QHBoxLayout(self)
		vbox.addLayout(hbox)
		checkLabel = QLabel("This is a checkbox", self)
		check = QCheckBox(self)
		hbox.addWidget(check)
		hbox.addWidget(checkLabel)
		


	def printHello(self):
		print(__file__)


	def quitApp(self):
		userInfo = QMessageBox.question(self, "Confirmation", "Do you really want to quit ?",
										QMessageBox.Yes | QMessageBox.No)

		if userInfo == QMessageBox.Yes:
			app.quit()
		



		
		