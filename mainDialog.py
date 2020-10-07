#coding:utf-8

from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from constants import *
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance


def getMayaMainWindow():
	omui.MQtUtil.mainWindow()    
	ptr = omui.MQtUtil.mainWindow()    
	widget = wrapInstance(long(ptr), QWidget)
	return widget


class MainDialogInstance(QDialog):
	"""
	"""
	def __init__(self):
		"""
		"""
		super(MainDialogInstance, self).__init__()

		self.autorigDialog = AutorigDialogInstance()
		self.managerDialog = ManagerDialogInstance()

		self.width = 180
		self.height = 300

		self.setWindowTitle("BrkTools")
		self.setWindowIcon(QIcon( BARAKA_ICONS_PATH + "/frites.png") )
		self.setGeometry(600, 400, 0, 0)
		self.setFixedSize(self.width, self.height)


		self.initUI()
		


	def initUI(self):

		image = QLabel()
		image.setObjectName("label")
		image.setStyleSheet(open(BARAKA_STYLESHEETS_PATH + "/mainStyleSheet.css").read())

		mainButtonsVBox = QVBoxLayout(self)
		mainButtonsVBox.addWidget(image)

		autorigButton = QPushButton("Autorig", self)
		autorigButton.setIcon( QIcon(BARAKA_ICONS_PATH + "/burger.png") )
		autorigButton.clicked.connect(self.autorigDialog.open)
		autorigButton.setToolTip("This is the autorig tool box")
		mainButtonsVBox.addWidget(autorigButton)

		managerButton = QPushButton("Manager", self)
		managerButton.setIcon( QIcon(BARAKA_ICONS_PATH + "/coca.png") )
		managerButton.clicked.connect(self.managerDialog.open)
		mainButtonsVBox.addWidget(managerButton)

		helpButton = QPushButton("Help", self)
		helpButton.setIcon( QIcon(BARAKA_ICONS_PATH + "/help.png") )
		helpButton.clicked.connect(self.printSomething)
		mainButtonsVBox.addWidget(helpButton)


	def printSomething(self):

		print("Hey buddy")


class AutorigDialogInstance(QTabWidget):

	def __init__(self):

		super(AutorigDialogInstance, self).__init__()

		self.setWindowTitle("Autorig")
		self.setWindowIcon(QIcon( BARAKA_ICONS_PATH + "/burger.png") )
		self.setGeometry(800, 500, 225, 0)
		self.setMinimumSize(225, 225)
		self.setMaximumSize(600, 500)

		self.initUI()
		self.createLimbWithRibbonUI()



	def initUI(self):


		self.limbTab = QWidget()
		self.eyesTab = QWidget()
		self.utilsTab = QWidget()

		self.addTab(self.limbTab, "Limb")
		self.addTab(self.eyesTab, "Eyes")
		self.addTab(self.utilsTab, "Utils")
		


	def createLimbWithRibbonUI(self):

		self.limbRibbonWidget = QWidget()
		self.limbRibbonVBox = QVBoxLayout(self.limbRibbonWidget)

		limbVBox = QVBoxLayout()
		self.limbTab.setLayout(limbVBox)

		driverJointsHBox = QHBoxLayout()
		bindJointsHBox = QHBoxLayout()
		rigFeaturesGridBox = QGridLayout()

		limbRigMethod = QComboBox()
		limbRigMethod.addItem("Ribbon")
		limbRigMethod.addItem("Spline")

		createWithRibbonButton = QPushButton("Create with Ribbon")

		self.limbRibbonVBox.layout().addLayout(driverJointsHBox)
		self.limbRibbonVBox.layout().addLayout(bindJointsHBox)
		self.limbRibbonVBox.layout().addLayout(rigFeaturesGridBox)
		
		driverJointsLabel = QLabel("Driver Joints")
		driverJointsSpinBox = QSpinBox()
		driverJointsHBox.addWidget(driverJointsLabel)
		driverJointsHBox.addWidget(driverJointsSpinBox)

		bindJointsLabel = QLabel("Bind Joints")
		bindJointsSpinBox = QSpinBox()
		bindJointsHBox.addWidget(bindJointsLabel)
		bindJointsHBox.addWidget(bindJointsSpinBox)

		hasTwistCheckBox = QCheckBox("Twist")
		hasBendCheckBox = QCheckBox("Bend")
		hasStretchCheckBox = QCheckBox("Stretch")
		hasKeepVolumeCheckBox = QCheckBox("Keep Volume")
		hasIKCheckBox = QCheckBox("IK")
		hasFKCheckBox = QCheckBox("FK")
		rigFeaturesGridBox.addWidget(hasStretchCheckBox, 0, 1 )
		rigFeaturesGridBox.addWidget(hasBendCheckBox, 1, 1)
		rigFeaturesGridBox.addWidget(hasKeepVolumeCheckBox, 2, 1)
		rigFeaturesGridBox.addWidget(hasTwistCheckBox, 0, 2)
		rigFeaturesGridBox.addWidget(hasIKCheckBox, 1, 2)
		rigFeaturesGridBox.addWidget(hasFKCheckBox, 2, 2)

		limbVBox.addWidget(limbRigMethod)
		limbVBox.addWidget(self.limbRibbonWidget)
		limbVBox.addWidget(createWithRibbonButton)


	def open(self):

		self.show()


class ManagerDialogInstance(QWidget):

	def __init__(self):

		super(ManagerDialogInstance, self).__init__()
		self.setWindowTitle("Manager")
		self.setWindowIcon(QIcon( BARAKA_ICONS_PATH + "/coca.png") )
		self.setGeometry(600, 400, 225, 0)
		self.setMinimumSize(225, 200)
		self.setMaximumSize(600, 500)


	def initManagerDialog(self):
		pass

	def open(self):
		self.show()
