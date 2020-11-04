# coing:utf-8

from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon, Qt
from constants import *
import modules.scene as scene
from ui.widgets.publisher import Publisher
from ui.widgets.manager import Manager


class Pipeline(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)

        self.widthManager = 425
        self.heightManager = 300

        self.widthPublisher = 225
        self.heightPublisher = 260

        self.setWindowTitle("Pipeline")
        self.setWindowIcon(QIcon(BARAKA_ICONS_PATH + "/coca.png"))
        self.setGeometry(600, 400, self.widthManager, self.heightManager)
        self.setMinimumSize(self.widthManager, self.heightManager)
        self.setMaximumSize(self.widthManager*2, self.heightManager*2)

        self.initMenus()
        self.initTabWidget()
        self.initManager()
        self.initPublisher()

        self.setCentralWidget(self.tabWidget)

    def initMenus(self):

        # UI Elements creation
        self.menuBar = self.menuBar()
        self.menuEdit = self.menuBar.addMenu("Edit")

        self.actionEditRootPath = QAction("Edit Root Path...")
        self.menuEdit.addAction(self.actionEditRootPath)

        self.actionEditRootPath.triggered.connect(self.setRootPath)

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

    def setWidgetSize(self):

        currentIndex = int( self.tabWidget.currentIndex() )

        if currentIndex == 0:
            self.setMinimumSize(self.widthManager, self.heightManager)
            self.resize(self.widthManager, self.heightManager)
        else:
            self.setFixedSize(self.widthPublisher, self.heightPublisher)
            self.resize(self.widthPublisher, self.heightPublisher)

    def setRootPath(self):
        
        self.popup = PopupSetRootPath("Enter your project path...", "Set")
        self.popup.open()

    def open(self):

        self.show()


class PopupSetRootPath(QDialog):

    def __init__(self, placeholder, button):
        QDialog.__init__(self)

        self.setWindowTitle("Pipeline - Set Root Path")
        self.setWindowIcon(QIcon(BARAKA_ICONS_PATH + "/coca.png"))
        self.setMinimumSize(300, 75)

        # UI elements creation and settings

        self.lineRootPath = QLineEdit()
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
