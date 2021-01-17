# coding:utf-8

from PySide2.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton
from PySide2.QtGui import QIcon, QPixmap, Qt
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from ui.mayaWin import get_maya_main_window
from ui.autorigs import Autorigs
from ui.pipeline import Pipeline
from constants import BARAKA_ICONS_PATH, BARAKA_IMAGES_PATH


class Launcher(MayaQWidgetDockableMixin, QDialog):
    """
    """

    def __init__(self, *args):
        """
        """
        super(self.__class__, self).__init__(parent = get_maya_main_window())

        self.autorig_window = Autorigs()
        self.pipeline_window = Pipeline()

        self.width = 200
        self.height = 300

        self.setWindowTitle("Brk Launcher")
        self.setWindowIcon(QIcon(BARAKA_ICONS_PATH + "/frites.png"))
        self.setGeometry(600, 400, 0, 0)
        self.setFixedSize(self.width, self.height)

        self.init_launcher()


    def init_launcher(self):

    	# Fetch for project image
        image = QLabel()
        image.setPixmap(QPixmap(BARAKA_IMAGES_PATH + "/title.png"))
        image.setAlignment(Qt.AlignCenter)


        # Create UI Elements
        self.lay_main_buttons = QVBoxLayout(self)
        self.lay_main_buttons.addWidget(image)

        self.btn_autorig = QPushButton("Autorigs", self)
        self.btn_autorig.setIcon(QIcon(BARAKA_ICONS_PATH + "/burger.png"))
        self.btn_autorig.clicked.connect(self.autorig_window.open)
        self.btn_autorig.setToolTip("This is the autorig tool box")

        self.btn_pipeline = QPushButton("Manager", self)
        self.btn_pipeline.setIcon(QIcon(BARAKA_ICONS_PATH + "/coca.png"))
        self.btn_pipeline.clicked.connect(self.pipeline_window.open)


        # Layout Management
        self.lay_main_buttons.addWidget(self.btn_autorig)
        self.lay_main_buttons.addWidget(self.btn_pipeline)


    def dockCloseEventTriggered(self):
        self.deleteLater()
