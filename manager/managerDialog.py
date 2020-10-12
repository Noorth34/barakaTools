#coing:utf-8

from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon, Qt
from constants import *

class ManagerDialogInstance(QTabWidget):

	def __init__(self):

		QTabWidget.__init__(self)

		self.width = 225
		self.height = 200
		self.setWindowTitle("Manager")
		self.setWindowIcon(QIcon( BARAKA_ICONS_PATH + "/coca.png") )
		self.setGeometry(600, 400, self.width, self.height)
		self.setMinimumSize(225, 150)
		self.setMaximumSize(600, 500)

		self.initTabs()
		self.initPublisher()
		self.initAlembicGroup()


	def initPublisher(self):

		self.layMain = QVBoxLayout(self.tabPublisher)
		self.layPublisher = QGridLayout()

		self.textfield = QLineEdit()
		self.textfield.setPlaceholderText("Asset name...")
		self.layMain.addWidget(self.textfield)

		self.layMain.layout().addLayout(self.layPublisher)
		editButton = QPushButton("Edit")
		publishButton = QPushButton("Publish")
		self.alembicCheckBox = QCheckBox("Is Alembic")
		self.alembicCheckBox.setCheckState(Qt.CheckState.Unchecked)
		self.alembicCheckBox.clicked.connect(self.toggleAlembicGroup)

		self.layPublisher.addWidget(editButton, 0, 1)
		self.layPublisher.addWidget(publishButton, 0, 2)
		self.layPublisher.addWidget(self.alembicCheckBox, 1, 2)


	def initAlembicGroup(self):

		self.alembicGroupWidget = QWidget()
		self.alembicGroupWidget.setDisabled(True)
		self.layMain.addWidget(self.alembicGroupWidget)
		self.layAlembicGroup = QGridLayout(self.alembicGroupWidget)
		labelFrameStart = QLabel("Start")
		labelFrameEnd = QLabel("End")
		spinFrameStart = QSpinBox()
		spinFrameEnd = QSpinBox()
		self.layAlembicGroup.addWidget(labelFrameStart, 0, 1)
		self.layAlembicGroup.addWidget(labelFrameEnd, 1, 1)
		self.layAlembicGroup.addWidget(spinFrameStart, 0, 2)
		self.layAlembicGroup.addWidget(spinFrameEnd, 1, 2)


	def initTabs(self):
		
		self.tabManager = QWidget()
		self.tabPublisher = QWidget()

		self.addTab(self.tabManager, "Manager")
		self.addTab(self.tabPublisher, "Publisher")


	def toggleAlembicGroup(self):

		state = self.alembicCheckBox.isChecked()

		if state == True:
			self.alembicGroupWidget.setEnabled(True)
		else:
			self.alembicGroupWidget.setDisabled(True)


	def open(self):
		self.show()