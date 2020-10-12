#coding:utf-8

from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from constants import *

class AutorigDialogInstance(QTabWidget):

	def __init__(self):

		QTabWidget.__init__(self)

		self.width = 225
		self.height = 225

		self.setWindowTitle("Autorigs")
		self.setWindowIcon(QIcon( BARAKA_ICONS_PATH + "/burger.png") )
		self.setGeometry(800, 500, 0, 0)
		self.setFixedSize(self.width, self.height)
		

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

		self.limbRigMethod = QComboBox()
		self.limbRigMethod.addItem("Ribbon")
		self.limbRigMethod.addItem("Spline")
		self.limbRigMethod.currentTextChanged.connect(self.toggleLimbRibbonWidget)

		createWithRibbonButton = QPushButton("Create with Ribbon")

		self.limbRibbonVBox.layout().addLayout(driverJointsHBox)
		self.limbRibbonVBox.layout().addLayout(bindJointsHBox)
		self.limbRibbonVBox.layout().addLayout(rigFeaturesGridBox)
		self.limbRibbonVBox.addWidget(createWithRibbonButton)
		
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

		limbVBox.addWidget(self.limbRigMethod)
		limbVBox.addWidget(self.limbRibbonWidget)
		


	def toggleLimbRibbonWidget(self):

		text = self.limbRigMethod.currentText() 
		
		if text == "Spline":
			self.limbRibbonWidget.hide()
		else:
			self.limbRibbonWidget.show()



	def open(self):

		self.show()