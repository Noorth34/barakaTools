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

        self.widthManager = 400
        self.heightManager = 220

        self.widthPublisher = 225
        self.heightPublisher = 220

        self.setWindowTitle("Pipeline")
        self.setWindowIcon(QIcon(BARAKA_ICONS_PATH + "/coca.png"))
        self.setGeometry(600, 400, self.widthManager, self.heightManager)
        self.setMinimumSize(self.widthManager, self.heightManager)
        self.setMaximumSize(self.widthManager*2, self.heightManager*2)

        self.blockSignals(True)
        self.currentChanged.connect(self.setWidgetSize)

        self.initManager()
        self.initPublisher()

        self.blockSignals(False)

    def initManager(self):

        self.tabManager = Manager()
        self.addTab(self.tabManager, "Manager")

    def initPublisher(self):

    	self.tabPublisher = Publisher()
    	self.addTab(self.tabPublisher, "Publisher")

    def setWidgetSize(self):

        currentIndex = int( self.currentIndex() )

        if currentIndex == 0:
            self.setMinimumSize(self.widthManager, self.heightManager)
            self.resize(self.widthManager, self.heightManager)
        else:
            self.setMinimumSize(self.widthPublisher, self.heightPublisher)
            self.resize(self.widthPublisher, self.heightPublisher)

    def open(self):

        self.show()
