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
		self.setMinimumSize(225, 150)
		self.setMaximumSize(600, 500)

		self.initTabs()
		self.initPublisher()

	def initPublisher(self):

		self.layMain = QVBoxLayout(self.tabPublisher)
		self.layPublisher = QGridLayout()

		self.textfield = QLineEdit()
		self.textfield.setPlaceholderText("Asset name...")
		self.layMain.addWidget(self.textfield)

		self.layMain.layout().addLayout(self.layPublisher)
		editButton = QPushButton("Edit")
		publishButton = QPushButton("Publish")
		alembicCheckBox = QCheckBox("Is Alembic")

		self.layPublisher.addWidget(editButton, 0, 1)
		self.layPublisher.addWidget(publishButton, 0, 2)
		self.layPublisher.addWidget(alembicCheckBox, 1, 2)




	def initTabs(self):
		
		self.tabManager = QWidget()
		self.tabPublisher = QWidget()

		self.addTab(self.tabManager, "Manager")
		self.addTab(self.tabPublisher, "Publisher")


	def setSize(self, width, heigt):
		self.setGeometry(0, 0, width, height)


	def open(self):
		self.show()