# coding:utf-8

from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon, QPixmap, Qt
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from ui.autorigs import Autorigs
from ui.pipeline import Pipeline
import constants as const
import ui.mayaWin as mayawin


class Launcher(MayaQWidgetDockableMixin, QDialog):
    """
    """

    def __init__(self, *args):
        """
        """
        super(self.__class__, self).__init__(parent=mayawin.getMayaMainWindow())

        self.autorigDialog = Autorigs()
        self.pipelineDialog = Pipeline()

        self.width = 200
        self.height = 300

        self.setWindowTitle("Brk Launcher")
        self.setWindowIcon(QIcon(const.BARAKA_ICONS_PATH + "/frites.png"))
        self.setGeometry(600, 400, 0, 0)
        self.setFixedSize(self.width, self.height)

        self.initLauncher()

    def initLauncher(self):

        image = QLabel()
        image.setPixmap(QPixmap(const.BARAKA_IMAGES_PATH + "/title.png"))
        image.setAlignment(Qt.AlignCenter)

        # Create UI Elements

        self.layMainButtons = QVBoxLayout(self)
        self.layMainButtons.addWidget(image)

        self.btnAutorig = QPushButton("Autorigs", self)
        self.btnAutorig.setIcon(QIcon(const.BARAKA_ICONS_PATH + "/burger.png"))
        self.btnAutorig.clicked.connect(self.autorigDialog.open)
        self.btnAutorig.setToolTip("This is the autorig tool box")

        self.btnPipeline = QPushButton("Manager", self)
        self.btnPipeline.setIcon(QIcon(const.BARAKA_ICONS_PATH + "/coca.png"))
        self.btnPipeline.clicked.connect(self.pipelineDialog.open)

        self.btnHelp = QPushButton("Help", self)
        self.btnHelp.setIcon(QIcon(const.BARAKA_ICONS_PATH + "/help.png"))
        self.btnHelp.clicked.connect(self.printSomething)

        # Layout Management

        self.layMainButtons.addWidget(self.btnAutorig)
        self.layMainButtons.addWidget(self.btnPipeline)
        self.layMainButtons.addWidget(self.btnHelp)

    def printSomething(self):

        print("Hey buddy")

    def dockCloseEventTriggered(self):
        self.deleteLater()
