# coing:utf-8

from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon, Qt
from PySide2.QtCore import QDir
from constants import *
import modules.scene as scene
import modules.directory as Dir
import os


class PipelineDialogInstance(QTabWidget):

    def __init__(self):

        QTabWidget.__init__(self)

        self.width = 225
        self.height = 200
        self.setWindowTitle("Pipeline")
        self.setWindowIcon(QIcon(BARAKA_ICONS_PATH + "/coca.png"))
        self.setGeometry(600, 400, self.width, self.height)
        self.setMinimumSize(self.width, self.height)
        self.setMaximumSize(self.width * 2, self.height * 2)

        self.initTabs()
        self.initPublisher()

        self.items = AssetPaths()
        self.initManager()

    def initTabs(self):

        self.tabManager = QWidget()
        self.tabPublisher = QWidget()

        self.addTab(self.tabManager, "Manager")
        self.addTab(self.tabPublisher, "Publisher")

    def initPublisher(self):

        # UI Elements creation and settings

        self.layMain = QVBoxLayout(self.tabPublisher)
        self.layAssetInfo = QHBoxLayout()
        self.layEdit = QHBoxLayout()
        self.layPublish = QHBoxLayout()
        self.layStartEndFrame = QGridLayout()

        separator1 = QFrame()
        separator1.setFrameShape(QFrame.HLine)
        separator2 = QFrame()
        separator2.setFrameShape(QFrame.HLine)

        self.lineEditAssetName = QLineEdit()
        self.lineEditAssetName.setPlaceholderText("Asset name...")
        self.listAssetType = QComboBox()

        for type in ASSET_TYPES.keys():
            self.listAssetType.addItem(type)

        self.btnEdit = QPushButton("Edit")
        self.btnEdit.clicked.connect(self.edit)
        self.btnPublish = QPushButton("Publish")

        self.checkIsAlembic = QCheckBox("Is Alembic")
        self.checkIsAlembic.setCheckState(Qt.CheckState.Unchecked)
        self.checkIsAlembic.clicked.connect(self.toggleAlembicStartEndFrame)

        self.lineCommit = QLineEdit()
        self.lineCommit.setPlaceholderText("Write your commit here...")

        self.labelFrameStart = QLabel("Start")
        self.labelFrameEnd = QLabel("End")
        self.labelFrameStart.setAlignment(Qt.AlignCenter)
        self.labelFrameEnd.setAlignment(Qt.AlignCenter)

        self.spinFrameStart = QSpinBox()
        self.spinFrameEnd = QSpinBox()
        self.spinFrameStart.setDisabled(True)
        self.spinFrameEnd.setDisabled(True)

        # Layout Management

        self.layAssetInfo.addWidget(self.lineEditAssetName)
        self.layAssetInfo.addWidget(self.listAssetType)
        self.layEdit.addWidget(self.lineCommit)
        self.layEdit.addWidget(self.btnEdit)
        self.layPublish.addWidget(self.btnPublish)
        self.layPublish.addWidget(self.checkIsAlembic)
        self.layStartEndFrame.addWidget(self.labelFrameStart, 0, 1)
        self.layStartEndFrame.addWidget(self.labelFrameEnd, 0, 2)
        self.layStartEndFrame.addWidget(self.spinFrameStart, 1, 1)
        self.layStartEndFrame.addWidget(self.spinFrameEnd, 1, 2)

        self.layMain.layout().addLayout(self.layAssetInfo)
        self.layMain.addWidget(separator1)
        self.layMain.layout().addLayout(self.layEdit)
        self.layMain.addWidget(separator2)
        self.layMain.layout().addLayout(self.layPublish)
        self.layMain.layout().addLayout(self.layStartEndFrame)

    def initManager(self):

        self.layList = QHBoxLayout(self.tabManager)
        self.listWidget = QListWidget()
        self.listWidget.itemDoubleClicked.connect(self.itemDoubleClickedEvent)

        for i in os.listdir(PIPELINE_ROOT_PATH):
            QListWidgetItem(i, self.listWidget)

        self.layList.addWidget(self.listWidget)

    def itemDoubleClickedEvent(self, item):
        self.selectedItem = item.text()

    # def dive(self):

    #     self.listWidget.clear()

    #     selectedItem = self.itemDoubleClickedEvent()
    #     self.items.click(selectedItem)

    #     for i in self.items.dictPath.keys():
    #         QListWidgetItem(i, self.listWidget)

    def toggleAlembicStartEndFrame(self):

        isChecked = self.checkIsAlembic.isChecked()

        if isChecked == True:
            self.spinFrameStart.setEnabled(True)
            self.spinFrameEnd.setEnabled(True)
        else:
            self.spinFrameStart.setDisabled(True)
            self.spinFrameEnd.setDisabled(True)

    def edit(self):

        scene.save("mayaAscii")

    def open(self):

        self.show()


class AssetPaths():
    
    def __init__(self):
        
        self.dictPath = {"rootPath":"{}".format(PIPELINE_ROOT_PATH)}
        self.curPath = self.dictPath['rootPath']
        self.getItemsPath(self.curPath)

    def getItemsPath(self, path):
        for i in os.listdir( path ):
            self.dictPath[i] = path + "/" + i

    def click(self, item):
        self.curPath = self.dictPath.get(item)
        self.dictPath.clear()
        self.getItemsPath(self.curPath)
    
    def goBack(self):
        if self.curPath == PIPELINE_ROOT_PATH:
            pass
        else:
            self.curPath = "/".join(self.curPath.split("/")[0:-1])
            self.dictPath.clear()
            self.getItemsPath(self.curPath)