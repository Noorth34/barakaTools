# coing:utf-8

from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon, Qt
from constants import *
import modules.scene as scene
from ui.widgets.publisher import Publisher
from ui.widgets.manager import Manager


class Pipeline(QTabWidget):

    def __init__(self):

        QTabWidget.__init__(self)

        self.width = 225
        self.height = 220
        self.setWindowTitle("Pipeline")
        self.setWindowIcon(QIcon(BARAKA_ICONS_PATH + "/coca.png"))
        self.setGeometry(600, 400, self.width, self.height)
        self.setMinimumSize(self.width, self.height)
        self.setMaximumSize(self.width*2, self.height*2)

        self.initManager()
        self.initPublisher()

    def initManager(self):

        self.tabManager = Manager()
        self.addTab(self.tabManager, "Manager")

    def initPublisher(self):

    	self.tabPublisher = Publisher()
    	self.addTab(self.tabPublisher, "Publisher")

    def open(self):

        self.show()
