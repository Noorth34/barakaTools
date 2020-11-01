# coding:utf-8

from PySide2.QtWidgets import *
from PySide2.QtGui import Qt
from constants import *

class Publisher(QWidget):

    def __init__(self):
        
        QWidget.__init__(self)
        self.init()

    def init(self):

        # UI Elements creation and settings

        self.layMain = QVBoxLayout()
        self.setLayout(self.layMain)
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

        self.btnEdit = QPushButton("Edit")
        self.btnPublish = QPushButton("Publish")

        self.checkIsAlembic = QCheckBox("Is Alembic")
        self.checkIsAlembic.setCheckState(Qt.CheckState.Unchecked)
        self.checkIsAlembic.clicked.connect(self.toggleAlembicStartEndFrame)

        self.lineCommit = QLineEdit()
        self.lineCommit.setPlaceholderText("Write your commit here...")

        self.labelFrameStart = QLabel("Start")
        self.labelFrameEnd = QLabel("End")
        self.labelFrameStart.setAlignment(Qt.AlignCenter)
        self.labelFrameEnd.setAlignment(Qt.AlignCenter)

        self.spinFrameStart = QSpinBox()
        self.spinFrameEnd = QSpinBox()
        self.spinFrameStart.setDisabled(True)
        self.spinFrameEnd.setDisabled(True)

        # Layout Management

        self.layAssetInfo.addWidget(self.lineEditAssetName)
        self.layAssetInfo.addWidget(self.listAssetType)
        self.layEdit.addWidget(self.lineCommit)
        self.layEdit.addWidget(self.btnEdit)
        self.layPublish.addWidget(self.btnPublish)
        self.layPublish.addWidget(self.checkIsAlembic)
        self.layStartEndFrame.addWidget(self.labelFrameStart, 0, 1)
        self.layStartEndFrame.addWidget(self.labelFrameEnd, 0, 2)
        self.layStartEndFrame.addWidget(self.spinFrameStart, 1, 1)
        self.layStartEndFrame.addWidget(self.spinFrameEnd, 1, 2)

        self.layMain.layout().addLayout(self.layAssetInfo)
        self.layMain.addWidget(separator1)
        self.layMain.layout().addLayout(self.layEdit)
        self.layMain.addWidget(separator2)
        self.layMain.layout().addLayout(self.layPublish)
        self.layMain.layout().addLayout(self.layStartEndFrame)

    def toggleAlembicStartEndFrame(self):

        isChecked = self.checkIsAlembic.isChecked()

        if isChecked == True:
            self.spinFrameStart.setEnabled(True)
            self.spinFrameEnd.setEnabled(True)
        else:
            self.spinFrameStart.setDisabled(True)
            self.spinFrameEnd.setDisabled(True)
