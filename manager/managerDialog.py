#coding:utf-8

"""
"""

from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PySide2.QtGui import QIcon
from constants import *


class ManagerDialogInstance(QWidget):
	"""
	"""
	def __init__(self):
		"""
		"""
		super(ManagerDialogInstance,self).__init__()

		self.setWindowTitle("BrkAutorig")
		self.setWindowIcon(QIcon( BARAKA_ICONS_PATH + "/burger.png") )
		self.setGeometry(600, 400, 225, 0)
		self.setMinimumSize(225, 200)
		self.setMaximumSize(600, 500)

		VBoxAutorigButtons = QVBoxLayout(self)

		ribbonButton = QPushButton("Ribbonize", self)
		VBoxAutorigButtons.addWidget(ribbonButton)

	def show(self):
		self.show()


		