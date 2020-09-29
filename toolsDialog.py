#coding:utf-8

from PySide2.QtWidgets import QApplication, QWidget, QDialog, QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton, QMessageBox
from PySide2.QtGui import QIcon

class BarakaToolsDialogInstance(QWidget):
	"""
	"""
	def __init__(self, parent = None):
		"""
		"""
		super(BarakaToolsDialogInstance, self).__init__(parent)

		self.setWindowTitle("BrkTools")
		self.setGeometry(600, 400, 225, 300)
		self.setMinimumSize(225, 200)
		self.setMaximumSize(300, 500)

		quitMessage = QMessageBox()

		vbox = QVBoxLayout(self)

		autorigButton = QPushButton("Autorig", self)
		autorigButton.clicked.connect(self.quitApp)
		vbox.addWidget(autorigButton)

		managerButton = QPushButton("Manager", self)
		managerButton.clicked.connect(self.quitApp)
		vbox.addWidget(managerButton)

		helpButton = QPushButton("Help", self)
		helpButton.clicked.connect(self.quitApp)
		vbox.addWidget(helpButton)


	def printHello(self):
		print("hello")


	def quitApp(self):
		userInfo = QMessageBox.question(self, "Confirmation", "Do you really want to quit ?",
										QMessageBox.Yes | QMessageBox.No)

		if userInfo == QMessageBox.Yes:
			app.quit()
		



		
		