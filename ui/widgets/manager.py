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
		self.layCreations = QVBoxLayout()
		self.layAssetCreation = QVBoxLayout()
		self.layShotCreation = QVBoxLayout()

		# UI Elements creation and settings

		self.treeAsset = QTreeWidget()
		self.treeAsset.setHeaderLabels(['Assets'])

			# Assets Group
		self.groupAssetCreation = QGroupBox("Assets Creation")

		self.lineAssetCreation = QLineEdit()
		self.lineAssetCreation.setPlaceholderText("Asset Name...")

		self.btnCreateCharacter = QPushButton("Character")
		self.btnCreateProp = QPushButton("Prop")
		self.btnCreateSet = QPushButton("Set")

			# Shots Group
		self.groupShotCreation = QGroupBox("Shots Creation")

		self.lineShotCreation = QLineEdit()
		self.lineShotCreation.setPlaceholderText("Shot name...")

		self.btnCreateShot = QPushButton("Shot")


		# Connect SIGNAL to SLOT

			# assets
		self.btnCreateCharacter.clicked.connect(self.createCharacter)
		self.btnCreateProp.clicked.connect(self.createProp)
		self.btnCreateSet.clicked.connect(self.createSet)

			# shots
		# self.btnCreateShot.clicked.connect(self.createShot) # TO ADD

		# Layout management

		self.setLayout(self.layMain)

		self.layMain.addLayout(self.layCreations)
		self.layMain.addLayout(self.layTree)

			# assets
		self.layCreations.addWidget(self.groupAssetCreation)

		self.groupAssetCreation.setLayout(self.layAssetCreation)

		self.layAssetCreation.addWidget(self.lineAssetCreation)
		self.layAssetCreation.addWidget(self.btnCreateCharacter)
		self.layAssetCreation.addWidget(self.btnCreateProp)
		self.layAssetCreation.addWidget(self.btnCreateSet)

			# shots
		self.layCreations.addWidget(self.groupShotCreation)

		self.groupShotCreation.setLayout(self.layShotCreation)

		self.layShotCreation.addWidget(self.lineShotCreation)
		self.layShotCreation.addWidget(self.btnCreateShot)

			# tree view
		self.layTree.addWidget(self.treeAsset)
		

	def populateTree(self):

		listCategAsset = Directory.getChildren(const.PIPELINE_ROOT_PATH)

		for categ in listCategAsset:
			categItem = QTreeWidgetItem(self.treeAsset, [categ])
			listItemsInCateg = Directory.getChildren( const.PIPELINE_ROOT_PATH + "/{}".format(categ) )

			for item in listItemsInCateg:
				itemItem = QTreeWidgetItem(categItem, [item])

	def updateTree(self):

		self.treeAsset.clear()
		self.populateTree()

	def createCharacter(self):
		Scene.createCharacter( self.lineAssetCreation.text() )
		self.lineAssetCreation.clear()
		self.updateTree()

	def createProp(self):
		Scene.createProp( self.lineAssetCreation.text() )
		self.lineAssetCreation.clear()
		self.updateTree()

	def createSet(self):
		Scene.createSet( self.lineAssetCreation.text() )
		self.lineAssetCreation.clear()
		self.updateTree()