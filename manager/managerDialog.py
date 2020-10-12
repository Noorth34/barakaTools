#coing:utf-8

from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from constants import *

class ManagerDialogInstance(QWidget):

	def __init__(self):

		QWidget.__init__(self)
		self.setWindowTitle("Manager")
		self.setWindowIcon(QIcon( BARAKA_ICONS_PATH + "/coca.png") )
		self.setGeometry(600, 400, 225, 0)
		self.setMinimumSize(225, 200)
		self.setMaximumSize(600, 500)


	def initManagerDialog(self):
		pass

	def open(self):
		self.show()