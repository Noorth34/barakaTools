#coing:utf-8

from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon, Qt
from constants import *

class PipelineDialogInstance(QTabWidget):

	def __init__(self):

		QTabWidget.__init__(self)

		self.width = 225
		self.height = 200
		self.setWindowTitle("Pipeline")
		self.setWindowIcon(QIcon( BARAKA_ICONS_PATH + "/coca.png") )
		self.setGeometry(600, 400, self.width, self.height)
		self.setMinimumSize(self.width, self.height)
		self.setMaximumSize(self.width*2, self.height*2)
		self.initTabs()
		self.initPublisher()
		self.initAlembicGroup()


	def initPublisher(self):

		self.layMain = QVBoxLayout(self.tabPublisher)
		self.layAssetNameGroup = QHBoxLayout()
		self.layPublisher = QGridLayout()

		self.textField = QLineEdit()
		self.textField.setPlaceholderText("Asset name...")
		self.assetTypeList = QComboBox()

		for type in ASSET_TYPES.keys():
			self.assetTypeList.addItem(type)

		self.layAssetNameGroup.addWidget(self.textField)
		self.layAssetNameGroup.addWidget(self.assetTypeList)

		editButton = QPushButton("Edit")
		publishButton = QPushButton("Publish")
		self.alembicCheckBox = QCheckBox("Is Alembic")
		self.alembicCheckBox.setCheckState(Qt.CheckState.Unchecked)
		self.alembicCheckBox.clicked.connect(self.toggleAlembicGroup)

		commitLine = QLineEdit()
		commitLine.setPlaceholderText("Write your commit here...")

		self.layPublisher.addWidget(commitLine, 0, 1)
		self.layPublisher.addWidget(editButton, 0, 2)
		self.layPublisher.addWidget(publishButton, 1, 1)
		self.layPublisher.addWidget(self.alembicCheckBox, 1, 2)
		self.layMain.layout().addLayout(self.layAssetNameGroup)
		self.layMain.layout().addLayout(self.layPublisher)

		

	def initAlembicGroup(self):

		self.alembicGroupWidget = QWidget()
		self.alembicGroupWidget.setDisabled(True)
		self.layMain.addWidget(self.alembicGroupWidget)
		self.layAlembicGroup = QGridLayout(self.alembicGroupWidget)
		labelFrameStart = QLabel("Start")
		labelFrameEnd = QLabel("End")
		labelFrameStart.setAlignment(Qt.AlignRight)
		labelFrameEnd.setAlignment(Qt.AlignRight)
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