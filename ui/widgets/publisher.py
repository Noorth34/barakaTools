# coding:utf-8

from PySide2.QtWidgets import *
from PySide2.QtGui import Qt
from modules.scene import Scene
from constants import *

class Publisher(QWidget):

    def __init__(self):
        
        QWidget.__init__(self)
        self.init()

    def init(self):

        # Layouts creation

        self.layMain = QVBoxLayout()
        self.setLayout(self.layMain)
        self.layEdit = QVBoxLayout()
        self.layPublish = QVBoxLayout()
        self.layStartEndFrame = QGridLayout()

        separator1 = QFrame()
        separator1.setFrameShape(QFrame.HLine)
        separator2 = QFrame()
        separator2.setFrameShape(QFrame.HLine)

        # UI Elements creation and settings

        self.btnEdit = QPushButton("Edit")
        self.btnPublish = QPushButton("Publish")

        self.checkWithAlembic = QCheckBox("With Alembic")
        self.checkWithAlembic.setCheckState(Qt.CheckState.Unchecked)

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

        # Connect SIGNAL to SLOT

        self.btnEdit.clicked.connect(Scene.edit)
        self.btnPublish.clicked.connect(Scene.publish)
        self.checkWithAlembic.clicked.connect(self.toggleAlembicStartEndFrame)

        # Layout Management

        self.layEdit.addWidget(self.lineCommit)
        self.layEdit.addWidget(self.btnEdit)

        self.layPublish.addWidget(self.checkWithAlembic)
        self.layPublish.addWidget(self.btnPublish)

        self.layStartEndFrame.addWidget(self.labelFrameStart, 0, 1)
        self.layStartEndFrame.addWidget(self.labelFrameEnd, 0, 2)
        self.layStartEndFrame.addWidget(self.spinFrameStart, 1, 1)
        self.layStartEndFrame.addWidget(self.spinFrameEnd, 1, 2)

        self.layMain.addWidget(separator1)
        self.layMain.layout().addLayout(self.layEdit)
        self.layMain.addWidget(separator2)
        self.layMain.layout().addLayout(self.layStartEndFrame)
        self.layMain.layout().addLayout(self.layPublish)

    def toggleAlembicStartEndFrame(self):

        isChecked = self.checkWithAlembic.isChecked()

        if isChecked == True:
            self.spinFrameStart.setEnabled(True)
            self.spinFrameEnd.setEnabled(True)
        else:
            self.spinFrameStart.setDisabled(True)
            self.spinFrameEnd.setDisabled(True)
