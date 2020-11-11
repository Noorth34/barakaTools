# coding:utf-8

from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon, QPixmap, Qt
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from ui.autorigs import Autorigs
from ui.pipeline import Pipeline
import constants as const
import ui.maya_win as mayawin


class Launcher(MayaQWidgetDockableMixin, QDialog):
    """
    """

    def __init__(self, *args):
        """
        """
        super(self.__class__, self).__init__(parent=mayawin.get_maya_main_window())

        self.autorig_window = Autorigs()
        self.pipeline_window = Pipeline()

        self.width = 200
        self.height = 300

        self.setWindowTitle("Brk Launcher")
        self.setWindowIcon(QIcon(const.BARAKA_ICONS_PATH + "/frites.png"))
        self.setGeometry(600, 400, 0, 0)
        self.setFixedSize(self.width, self.height)

        self.init_launcher()

    def init_launcher(self):

        image = QLabel()
        image.setPixmap(QPixmap(const.BARAKA_IMAGES_PATH + "/title.png"))
        image.setAlignment(Qt.AlignCenter)

        # Create UI Elements

        self.lay_main_buttons = QVBoxLayout(self)
        self.lay_main_buttons.addWidget(image)

        self.btn_autorig = QPushButton("Autorigs", self)
        self.btn_autorig.setIcon(QIcon(const.BARAKA_ICONS_PATH + "/burger.png"))
        self.btn_autorig.clicked.connect(self.autorig_window.open)
        self.btn_autorig.setToolTip("This is the autorig tool box")

        self.btn_pipeline = QPushButton("Manager", self)
        self.btn_pipeline.setIcon(QIcon(const.BARAKA_ICONS_PATH + "/coca.png"))
        self.btn_pipeline.clicked.connect(self.pipeline_window.open)

        self.btn_help = QPushButton("Help", self)
        self.btn_help.setIcon(QIcon(const.BARAKA_ICONS_PATH + "/help.png"))
        self.btn_help.clicked.connect(self.print_something)

        # Layout Management

        self.lay_main_buttons.addWidget(self.btn_autorig)
        self.lay_main_buttons.addWidget(self.btn_pipeline)
        self.lay_main_buttons.addWidget(self.btn_help)

    def print_something(self):

        print("Hey buddy")

    def dockCloseEventTriggered(self):
        self.deleteLater()
