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

        self.lay_main = QVBoxLayout()
        self.setLayout(self.lay_main)
        self.lay_edit = QVBoxLayout()
        self.lay_publish = QVBoxLayout()
        self.lay_start_end_frame = QGridLayout()

        separator1 = QFrame()
        separator1.setFrameShape(QFrame.HLine)
        separator2 = QFrame()
        separator2.setFrameShape(QFrame.HLine)

        # UI Elements creation and settings

        self.btn_edit = QPushButton("Edit")
        self.btn_publish = QPushButton("Publish")

        self.group_with_alembic = QGroupBox("Publish With Alembic")
        self.group_with_alembic.setCheckable(True)
        self.group_with_alembic.setChecked(False)

        self.line_commit = QLineEdit()
        self.line_commit.setPlaceholderText("Write your commit here...")

        self.label_frame_start = QLabel("Start")
        self.label_frame_end = QLabel("End")
        self.label_frame_start.setAlignment(Qt.AlignCenter)
        self.label_frame_end.setAlignment(Qt.AlignCenter)

        self.spin_frame_start = QSpinBox()
        self.spin_frame_start.setValue(1)
        self.spin_frame_end = QSpinBox()
        self.spin_frame_end.setValue(1)

        # Connect SIGNAL to SLOT

        self.btn_edit.clicked.connect(Scene.edit)
        self.btn_publish.clicked.connect(self.publish_scene)

        # Layout Management

        self.lay_edit.addWidget(self.line_commit)
        self.lay_edit.addWidget(self.btn_edit)

        self.lay_publish.addWidget(self.group_with_alembic)
        self.lay_publish.addWidget(self.btn_publish)

        self.lay_start_end_frame.addWidget(self.label_frame_start, 0, 1)
        self.lay_start_end_frame.addWidget(self.label_frame_end, 0, 2)
        self.lay_start_end_frame.addWidget(self.spin_frame_start, 1, 1)
        self.lay_start_end_frame.addWidget(self.spin_frame_end, 1, 2)

        self.group_with_alembic.setLayout(self.lay_start_end_frame)
        self.lay_main.addWidget(separator1)
        self.lay_main.layout().addLayout(self.lay_edit)
        self.lay_main.addWidget(separator2)
        self.lay_main.layout().addLayout(self.lay_start_end_frame)
        self.lay_main.layout().addLayout(self.lay_publish)

        ##Set Properties

        self.line_commit.setMinimumHeight(20)
        self.btn_edit.setMinimumHeight(30)

        self.group_with_alembic.setMinimumHeight(80)

        self.btn_publish.setMinimumHeight(30)   

        self.lay_start_end_frame.setContentsMargins(9, 25, 9, 9)

    def publish_scene(self):

        Scene.publish()

        if self.group_with_alembic.isChecked() == True:
            print("Alembic exporting.......")
            scene = Scene.get_name()
            Scene.alembic_export(scene, start = self.spin_frame_start.value(), end = self.spin_frame_end.value())