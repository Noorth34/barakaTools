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


	def initPublisher(self):

		# UI Elements creation and settings

		self.layMain = QVBoxLayout(self.tabPublisher)
		self.layAssetInfo = QHBoxLayout()
		self.layEdit = QHBoxLayout()
		self.layPublish = QHBoxLayout()
		self.layStartEndFrame = QGridLayout()

		separator1 = QFrame()
		separator1.setFrameShape(QFrame.HLine)
		separator2 = QFrame()
		separator2.setFrameShape(QFrame.HLine)

		self.lineEditAssetName = QLineEdit()
		self.lineEditAssetName.setPlaceholderText("Asset name...")
		self.listAssetType = QComboBox()

		for type in ASSET_TYPES.keys():
			self.listAssetType.addItem(type)

		self.editButton = QPushButton("Edit")
		self.publishButton = QPushButton("Publish")

		self.alembicCheckBox = QCheckBox("Is Alembic")
		self.alembicCheckBox.setCheckState(Qt.CheckState.Unchecked)
		self.alembicCheckBox.clicked.connect(self.toggleAlembicGroup)

		self.lineCommit = QLineEdit()
		self.lineCommit.setPlaceholderText("Write your commit here...")

		labelFrameStart = QLabel("Start")
		labelFrameEnd = QLabel("End")
		labelFrameStart.setAlignment(Qt.AlignCenter)
		labelFrameEnd.setAlignment(Qt.AlignCenter)
		self.spinFrameStart = QSpinBox()
		self.spinFrameEnd = QSpinBox()
		self.spinFrameStart.setDisabled(True)
		self.spinFrameEnd.setDisabled(True)

		# Layout Management

		self.layAssetInfo.addWidget(self.lineEditAssetName)
		self.layAssetInfo.addWidget(self.listAssetType)
		self.layEdit.addWidget(self.lineCommit)
		self.layEdit.addWidget(self.editButton)
		self.layPublish.addWidget(self.publishButton)
		self.layPublish.addWidget(self.alembicCheckBox)
		self.layStartEndFrame.addWidget(labelFrameStart, 0, 1)
		self.layStartEndFrame.addWidget(labelFrameEnd, 0, 2)
		self.layStartEndFrame.addWidget(self.spinFrameStart, 1, 1)
		self.layStartEndFrame.addWidget(self.spinFrameEnd, 1, 2)

		self.layMain.layout().addLayout(self.layAssetInfo)
		self.layMain.addWidget(separator1)
		self.layMain.layout().addLayout(self.layEdit)
		self.layMain.addWidget(separator2)
		self.layMain.layout().addLayout(self.layPublish)
		self.layMain.layout().addLayout(self.layStartEndFrame)


	def initTabs(self):
		
		self.tabManager = QWidget()
		self.tabPublisher = QWidget()

		self.addTab(self.tabManager, "Manager")
		self.addTab(self.tabPublisher, "Publisher")


	def toggleAlembicGroup(self):

		state = self.alembicCheckBox.isChecked()

		if state == True:
			self.spinFrameStart.setEnabled(True)
			self.spinFrameEnd.setEnabled(True)
		else:
			self.spinFrameStart.setDisabled(True)
			self.spinFrameEnd.setDisabled(True)


	def open(self):

		self.show()