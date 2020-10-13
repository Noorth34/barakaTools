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
		
		self.initTabs()
		self.initLimbWithRibbon()



	def initTabs(self):


		self.tabLimb = QWidget()
		self.tabEyes = QWidget()
		self.tabUtils = QWidget()

		self.addTab(self.tabLimb, "Limb")
		self.addTab(self.tabEyes, "Eyes")
		self.addTab(self.tabUtils, "Utils")
		


	def initLimbWithRibbon(self):

		# Create UI Elements

		self.widgetLimbRibbon = QWidget()
		self.layLimbRibbon = QVBoxLayout(self.widgetLimbRibbon)

		self.layLimb = QVBoxLayout()
		self.tabLimb.setLayout(self.layLimb)

		self.layDriverJoints = QHBoxLayout()
		self.layBindJoints = QHBoxLayout()
		self.layRigFeatures = QGridLayout()

		self.listRigMethod = QComboBox()
		self.listRigMethod.addItem("Ribbon")
		self.listRigMethod.addItem("Spline")
		self.listRigMethod.currentTextChanged.connect(self.toggleWidgetLimbRibbon)

		self.btnCreateWithRibbon = QPushButton("Create with Ribbon")

		self.labelDriverJoints = QLabel("Driver Joints")
		self.labelBindJoints = QLabel("Bind Joints")
		self.spinDriverJoints = QSpinBox()
		self.spinBindJoints = QSpinBox()

		self.checkHasTwist = QCheckBox("Twist")
		self.checkHasBend = QCheckBox("Bend")
		self.checkHasStretch = QCheckBox("Stretch")
		self.checkHasKeepVolume = QCheckBox("Keep Volume")
		self.checkHasIK = QCheckBox("IK")
		self.checkHasFK = QCheckBox("FK")


		# Layout management

		self.layLimb.addWidget(self.listRigMethod)
		self.layLimb.addWidget(self.widgetLimbRibbon)

		self.layLimbRibbon.layout().addLayout(self.layDriverJoints)
		self.layLimbRibbon.layout().addLayout(self.layBindJoints)
		self.layLimbRibbon.layout().addLayout(self.layRigFeatures)
		self.layLimbRibbon.addWidget(self.btnCreateWithRibbon)
		
		self.layDriverJoints.addWidget(self.labelDriverJoints)
		self.layDriverJoints.addWidget(self.spinDriverJoints)

		self.layBindJoints.addWidget(self.labelBindJoints)
		self.layBindJoints.addWidget(self.spinBindJoints)

		self.layRigFeatures.addWidget(self.checkHasStretch, 0, 1 )
		self.layRigFeatures.addWidget(self.checkHasBend, 1, 1)
		self.layRigFeatures.addWidget(self.checkHasKeepVolume, 2, 1)
		self.layRigFeatures.addWidget(self.checkHasTwist, 0, 2)
		self.layRigFeatures.addWidget(self.checkHasFK, 1, 2)
		self.layRigFeatures.addWidget(self.checkHasIK, 2, 2)
		


	def toggleWidgetLimbRibbon(self):

		text = self.comboRigMethod.currentText() 
		
		if text == "Spline":
			self.widgetLimbRibbon.hide()
		else:
			self.widgetLimbRibbon.show()



	def open(self):

		self.show()