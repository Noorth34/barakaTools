# coding:utf-8

from PySide2.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout
from PySide2.QtGui import QIcon
from ui.mayaWin import get_maya_main_window
from ui.widgets.utils import Utils
from constants import BARAKA_ICONS_PATH


class Autorigs(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self, parent = get_maya_main_window())

        self.width = 225
        self.height = 225

        self.setWindowTitle("Autorigs")
        self.setWindowIcon(QIcon(BARAKA_ICONS_PATH + "/burger.png"))
        self.setGeometry(1800, 250, 0, 0)
        self.setFixedSize(self.width, self.height)

        self._init_tabs()
        self._init_utils()

        self.setCentralWidget(self.tab_widget)


    def _init_tabs(self):

        self.tab_widget = QTabWidget()
        self.tab_utils = QWidget()
        self.tab_widget.addTab(self.tab_utils, "Utils")


    def _init_utils(self):

        self.utils = Utils()

        self.lay_utils = QVBoxLayout()
        self.tab_utils.setLayout(self.lay_utils)
        self.lay_utils.addWidget(self.utils)


    def open(self):

        self.show()
