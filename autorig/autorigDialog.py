#coding:utf-8

from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from constants import *

class AutorigDialogInstance(QTabWidget):
	def __init__(self):
		super(AutorigDialogInstance, self).__init__()

		self.setWindowTitle("Autorig")
		self.setWindowIcon(QIcon( BARAKA_ICONS_PATH + "/burger.png") )
		self.setGeometry(800, 500, 225, 0)
		self.setMinimumSize(225, 200)
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

		limbVBox = QVBoxLayout()
		self.limbTab.setLayout(limbVBox)

		driverJointsHBox = QHBoxLayout()
		bindJointsHBox = QHBoxLayout()
		rigFeaturesGridBox = QGridLayout()

		limbRigMethod = QComboBox()
		limbRigMethod.addItem("Ribbon")
		limbRigMethod.addItem("Spline")

		createWithRibbonButton = QPushButton("Create with Ribbon")

		limbVBox.addWidget(limbRigMethod)
		limbVBox.layout().addLayout(driverJointsHBox)
		limbVBox.layout().addLayout(bindJointsHBox)
		limbVBox.layout().addLayout(rigFeaturesGridBox)
		limbVBox.addWidget(createWithRibbonButton)

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
		rigFeaturesGridBox.addWidget(hasStretchCheckBox)
		rigFeaturesGridBox.addWidget(hasBendCheckBox)
		rigFeaturesGridBox.addWidget(hasKeepVolumeCheckBox)
		rigFeaturesGridBox.addWidget(hasTwistCheckBox)


	def open(self):

		self.show()