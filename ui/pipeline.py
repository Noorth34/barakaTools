# coing:utf-8

from PySide2 import QtCore
from PySide2.QtWidgets import *
from PySide2.QtGui import (QIcon, Qt)
from PySide2.QtCore import (QSize, QPropertyAnimation)
from ui.widgets.publisher import Publisher
from ui.widgets.manager import Manager
import ui.mayaWin as mayawin
import constants as const

class Pipeline(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self, parent=mayawin.getMayaMainWindow())

        self.widthManager = 425
        self.heightManager = 350

        self.widthPublisher = 225
        self.heightPublisher = 250

        self.setWindowTitle("Pipeline")
        self.setWindowIcon(QIcon(const.BARAKA_ICONS_PATH + "/coca.png"))
        self.setGeometry(600, 400, self.widthManager, self.heightManager)
        self.setMinimumWidth(self.widthPublisher)
        self.setMinimumHeight(self.widthPublisher)
        # self.setMaximumWidth(self.widthManager)
        # self.setMaximumHeight(self.widthManager)
        # self.setMaximumSize(self.widthManager*2, self.heightManager*2)

        self.initMenus()
        self.initTabWidget()
        self.initManager()
        self.initPublisher()

        self.setCentralWidget(self.tabWidget)
        self.setStyleSheet(open(const.BARAKA_STYLESHEETS_PATH + "/brkStyle.css").read())

    def initMenus(self):

        # UI Elements creation
        self.menuBar = self.menuBar()
        self.menuEdit = self.menuBar.addMenu("Edit")

        self.actionEditRootPath = QAction("Edit Root Path...")
        self.menuEdit.addAction(self.actionEditRootPath)

        self.actionEditRootPath.triggered.connect(self.openSetRootPathPopup)

    def initTabWidget(self):

        # Ui Element creation
        self.tabWidget = QTabWidget()

        # Connect SIGNAL to SLOT
        self.tabWidget.currentChanged.connect(self.setWidgetSize)

    def initManager(self):

        self.tabManager = Manager()
        self.tabWidget.addTab(self.tabManager, "Manager")

    def initPublisher(self):

    	self.tabPublisher = Publisher()
    	self.tabWidget.addTab(self.tabPublisher, "Publisher")

    def resizeWindow(self, width, height):
        
        self.animation = QPropertyAnimation(self, b"size")
        self.animation.setDuration(100)
        self.animation.setEndValue(QtCore.QSize(width, height))
        self.animation.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.animation.start()

    def setWidgetSize(self):

        currentIndex = int( self.tabWidget.currentIndex() )
        
        if currentIndex == 0:

            self.resizeWindow(self.widthManager, self.heightManager)

        if currentIndex == 1:

            self.resizeWindow(self.widthPublisher, self.heightPublisher)

    def openSetRootPathPopup(self):
        
        self.popup = PopupSetRootPath("Enter your project path...", "Set")

        # Connect SIGNAL to SLOT
        self.popup.btnSet.clicked.connect(self.setRootPath)
        self.popup.btnCancel.clicked.connect(self.popup.closePopup)

        self.popup.open()

    def setRootPath(self):
        from configparser import ConfigParser
        from maya import cmds
        from modules.path import Path

        const.PIPELINE_ROOT_PATH = Path.convertBackslashToSlash( self.popup.lineRootPath.text() )

        config = ConfigParser()
        config.read(const.BARAKA_CONFIG_PATH)
        config.set("PATH", "rootPath", const.PIPELINE_ROOT_PATH)
        with open(const.BARAKA_CONFIG_PATH, "wb") as cf:
            config.write(cf)
        
        const.PIPELINE_CHARACTERS = const.PIPELINE_ROOT_PATH + "/character"
        const.PIPELINE_PROPS = const.PIPELINE_ROOT_PATH + "/prop"
        const.PIPELINE_SETS = const.PIPELINE_ROOT_PATH + "/set"

        print(const.PIPELINE_ROOT_PATH)
        print(const.PIPELINE_CHARACTERS)
        print(const.PIPELINE_PROPS)
        print(const.PIPELINE_SETS)
        cmds.inViewMessage(amg='Root Path set to: \n <hl>' + const.PIPELINE_ROOT_PATH + '</hl>', pos='topCenter', fade=True)

        self.tabManager.populateTree()
        self.popup.closePopup()

    def open(self):

        self.show()

    def closeEvent(self, event):
        self.tabManager.lineAssetCreation.clear()
        event.accept()


class PopupSetRootPath(QDialog, Pipeline):

    def __init__(self, placeholder, button):
        QDialog.__init__(self, parent=mayawin.getMayaMainWindow())

        self.setWindowTitle("Pipeline - Set Root Path")
        self.setWindowIcon(QIcon(const.BARAKA_ICONS_PATH + "/coca.png"))
        self.setMinimumSize(300, 75)

        # UI elements creation and settings

        self.lineRootPath = QLineEdit(const.PIPELINE_ROOT_PATH)
        self.lineRootPath.setPlaceholderText(placeholder)

        self.btnSet = QPushButton(button)
        self.btnCancel = QPushButton("Cancel")

        # Layout Management

        self.layMain = QVBoxLayout()
        self.layButtons = QHBoxLayout()

        self.layMain.addWidget(self.lineRootPath)
        self.layButtons.addWidget(self.btnSet)
        self.layButtons.addWidget(self.btnCancel)

        self.layMain.layout().addLayout(self.layButtons)
        self.setLayout(self.layMain)

    def open(self):
        self.show()

    def closePopup(self):
        self.lineRootPath.clear()
        self.close()
        