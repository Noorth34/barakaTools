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

		self.limbRibbonWidget = QWidget()
		limbVBox.addWidget(limbRibbonWidget)

		driverJointsHBox = QHBoxLayout()
		bindJointsHBox = QHBoxLayout()
		rigFeaturesGridBox = QGridLayout()

		limbRigMethod = QComboBox()
		limbRigMethod.addItem("Ribbon")
		limbRigMethod.addItem("Spline")

		createWithRibbonButton = QPushButton("Create with Ribbon")

		limbVBox.addWidget(limbRigMethod)
		limbVBox.addWidget(createWithRibbonButton)

		self.limbRibbonWidget.layout().addLayout(driverJointsHBox)
		self.limbRibbonWidget.layout().addLayout(bindJointsHBox)
		self.limbRibbonWidget.layout().addLayout(rigFeaturesGridBox)
		

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
		rigFeaturesGridBox.addWidget(hasStretchCheckBox)
		rigFeaturesGridBox.addWidget(hasBendCheckBox)
		rigFeaturesGridBox.addWidget(hasKeepVolumeCheckBox)
		rigFeaturesGridBox.addWidget(hasTwistCheckBox)
		rigFeaturesGridBox.addWidget(hasIKCheckBox)
		rigFeaturesGridBox.addWidget(hasFKCheckBox)


	def open(self):

		self.show()