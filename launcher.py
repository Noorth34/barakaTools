#coding:utf-8

from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon, QPixmap, Qt
from autorig.autorigDialog import AutorigDialogInstance
from pipeline.pipelineDialog import PipelineDialogInstance
from constants import *
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance


def getMayaMainWindow():
	omui.MQtUtil.mainWindow()    
	ptr = omui.MQtUtil.mainWindow()    
	widget = wrapInstance(long(ptr), QWidget)
	return widget


class LauncherInstance(QDialog):
	"""
	"""
	def __init__(self):
		"""
		"""
		QDialog.__init__(self)

		self.autorigDialog = AutorigDialogInstance()
		self.pipelineDialog = PipelineDialogInstance()

		self.width = 200
		self.height = 300

		self.setWindowTitle("Brk Launcher")
		self.setWindowIcon(QIcon( BARAKA_ICONS_PATH + "/frites.png") )
		self.setGeometry(600, 400, 0, 0)
		self.setFixedSize(self.width, self.height)

		self.initLauncher()
		


	def initLauncher(self):

		image = QLabel()
		image.setPixmap( QPixmap(BARAKA_IMAGES_PATH + "/title.png") )
		image.setAlignment(Qt.AlignCenter)

		self.layMainButtons = QVBoxLayout(self)
		self.layMainButtons.addWidget(image)

		self.btnAutorig = QPushButton("Autorigs", self)
		self.btnAutorig.setIcon( QIcon(BARAKA_ICONS_PATH + "/burger.png") )
		self.btnAutorig.clicked.connect(self.autorigDialog.open)
		self.btnAutorig.setToolTip("This is the autorig tool box")
		self.layMainButtons.addWidget(self.btnAutorig)

		self.btnPipeline = QPushButton("Manager", self)
		self.btnPipeline.setIcon( QIcon(BARAKA_ICONS_PATH + "/coca.png") )
		self.btnPipeline.clicked.connect(self.pipelineDialog.open)
		self.layMainButtons.addWidget(self.btnPipeline)

		self.btnHelp = QPushButton("Help", self)
		self.btnHelp.setIcon( QIcon(BARAKA_ICONS_PATH + "/help.png") )
		self.btnHelp.clicked.connect(self.printSomething)
		self.layMainButtons.addWidget(self.btnHelp)


	def printSomething(self):

		print("Hey buddy")

