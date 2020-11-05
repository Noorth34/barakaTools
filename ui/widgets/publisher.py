# coding:utf-8

from PySide2.QtWidgets import *
from PySide2.QtGui import Qt
from modules.scene import Scene
import constants as const

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

        self.groupWithAlembic = QGroupBox("Publish With Alembic")
        self.groupWithAlembic.setCheckable(True)
        self.groupWithAlembic.setChecked(False)

        self.lineCommit = QLineEdit()
        self.lineCommit.setPlaceholderText("Write your commit here...")

        self.labelFrameStart = QLabel("Start")
        self.labelFrameEnd = QLabel("End")
        self.labelFrameStart.setAlignment(Qt.AlignCenter)
        self.labelFrameEnd.setAlignment(Qt.AlignCenter)

        self.spinFrameStart = QSpinBox()
        self.spinFrameEnd = QSpinBox()

        # Connect SIGNAL to SLOT

        self.btnEdit.clicked.connect(Scene.edit)
        self.btnPublish.clicked.connect(Scene.publish)

        # Layout Management

        self.layEdit.addWidget(self.lineCommit)
        self.layEdit.addWidget(self.btnEdit)

        self.layPublish.addWidget(self.groupWithAlembic)
        self.layPublish.addWidget(self.btnPublish)

        self.layStartEndFrame.addWidget(self.labelFrameStart, 0, 1)
        self.layStartEndFrame.addWidget(self.labelFrameEnd, 0, 2)
        self.layStartEndFrame.addWidget(self.spinFrameStart, 1, 1)
        self.layStartEndFrame.addWidget(self.spinFrameEnd, 1, 2)

        self.groupWithAlembic.setLayout(self.layStartEndFrame)
        self.layMain.addWidget(separator1)
        self.layMain.layout().addLayout(self.layEdit)
        self.layMain.addWidget(separator2)
        self.layMain.layout().addLayout(self.layStartEndFrame)
        self.layMain.layout().addLayout(self.layPublish)
