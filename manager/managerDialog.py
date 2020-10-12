#coing:utf-8

from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from constants import *

class ManagerDialogInstance(QTabWidget):

	def __init__(self):

		QTabWidget.__init__(self)
		self.setWindowTitle("Manager")
		self.setWindowIcon(QIcon( BARAKA_ICONS_PATH + "/coca.png") )
		self.setGeometry(600, 400, 225, 0)
		self.setMinimumSize(225, 200)
		self.setMaximumSize(600, 500)

		self.initTabs()
		

	def initTabs(self):
		
		self.tabManager = QWidget()
		self.tabPublisher = QWidget()

		self.addTab(self.tabManager, "Manager")
		self.addTab(self.tabPublisher, "Publisher")



	def open(self):
		self.show()