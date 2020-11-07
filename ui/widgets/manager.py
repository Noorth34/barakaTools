# coding:utf-8

from PySide2.QtWidgets import *
from modules.scene import Scene
from modules.directory import Directory
from functools import partial
import constants as const

class Manager(QWidget):

	def __init__(self):

		QWidget.__init__(self)
		self.init()

		try:
			self.populateTree()
		except:
			pass

	def init(self):

		# Layouts creation

		self.layMain = QHBoxLayout()
		self.layTree = QVBoxLayout()
		self.layAssetCreation = QVBoxLayout()

		# UI Elements creation and settings

		self.treeAsset = QTreeWidget()
		self.treeAsset.setHeaderLabels(['Assets'])

		self.groupAssetCreation = QGroupBox("Create Asset")

		self.lineAssetCreation = QLineEdit()
		self.lineAssetCreation.setPlaceholderText("Asset Name...")

		self.btnCreateCharacter = QPushButton("Character")
		self.btnCreateProp = QPushButton("Prop")
		self.btnCreateSet = QPushButton("Set")

		# Connect SIGNAL to SLOT

		self.btnCreateCharacter.clicked.connect(self.createCharacter)
		self.btnCreateProp.clicked.connect(self.createProp)
		self.btnCreateSet.clicked.connect(self.createSet)

		# Layout management

		self.setLayout(self.layMain)

		self.layMain.addWidget(self.groupAssetCreation)
		self.layMain.addLayout(self.layTree)

		self.layTree.addWidget(self.treeAsset)

		self.layAssetCreation.addWidget(self.lineAssetCreation)
		self.layAssetCreation.addWidget(self.btnCreateCharacter)
		self.layAssetCreation.addWidget(self.btnCreateProp)
		self.layAssetCreation.addWidget(self.btnCreateSet)

		self.groupAssetCreation.setLayout(self.layAssetCreation)

	def populateTree(self):

		listCategAsset = Directory.getChildren(const.PIPELINE_ROOT_PATH)

		for categ in listCategAsset:
			categItem = QTreeWidgetItem(self.treeAsset, [categ])
			listItemsInCateg = Directory.getChildren( const.PIPELINE_ROOT_PATH + "/{}".format(categ) )

			for item in listItemsInCateg:
				itemItem = QTreeWidgetItem(categItem, [item])


	def createCharacter(self):
		Scene.createCharacter( self.lineAssetCreation.text() )

	def createProp(self):
		Scene.createProp( self.lineAssetCreation.text() )

	def createSet(self):
		Scene.createSet( self.lineAssetCreation.text() )