#coding:utf-8

from PySide2 import QtCore, QtGui, QtWidgets

class BarakaToolsDialogInstance(QtWidgets.QWidget):
	"""
	"""
	def __init__(self, parent = None):
		"""
		"""
		super(BarakaToolsDialogInstance, self).__init__(parent)

		self.setWindowTitle("BrkTools")
		self.setGeometry(600, 400, 225, 300)
		self.setMinimumSize(100, 200)
		self.setMaximumSize(300, 500)

		button = QtWidgets.QPushButton("Hello", self)
		

		#self.buttonsNames = ["Manager", "Autorig"]
		#self.buttons = []
		#for name in self.buttonsNames:
		#	button = QtWidgets.QPushButton()
		



		
		