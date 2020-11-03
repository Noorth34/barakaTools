# coding:utf-8

from PySide2.QtWidgets import *
from modules.scene import Scene

class Manager(QWidget):

	def __init__(self):

		QWidget.__init__(self)
		self.init()

	def init(self):

		# Layouts creation

		self.layMain = QHBoxLayout()
		self.layTree = QVBoxLayout()
		self.layAssetCreation = QVBoxLayout()

		# UI Elements creation and settings

		self.treeAsset = QTreeWidget()

		self.labelAssetCreation = QLabel("Create Asset")

		self.lineAssetCreation = QLineEdit()
		self.lineAssetCreation.setPlaceholderText("Asset Name...")

		self.btnCreateCharacter = QPushButton("Character")
		self.btnCreateProp = QPushButton("Prop")
		self.btnCreateSet = QPushButton("Set")

		# Connect SIGNAL to SLOT

		# self.btnCreateCharacter.clicked.connect(Scene.createCharacter)

		# Layout management

		self.setLayout(self.layMain)

		self.layMain.addLayout(self.layAssetCreation)
		self.layMain.addLayout(self.layTree)

		self.layTree.addWidget(self.treeAsset)

		self.layAssetCreation.addWidget(self.labelAssetCreation)
		self.layAssetCreation.addWidget(self.lineAssetCreation)
		self.layAssetCreation.addWidget(self.btnCreateCharacter)
		self.layAssetCreation.addWidget(self.btnCreateProp)
		self.layAssetCreation.addWidget(self.btnCreateSet)


