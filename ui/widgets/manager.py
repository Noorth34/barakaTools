# coding:utf-8

from PySide2.QtWidgets import *
from modules.scene import Scene
from modules.directory import Directory
from functools import partial
import constants as const

class Manager(QWidget):

	def __init__(self):

		QWidget.__init__(self)

		self.dictAssets = {}
		self.dictAssets['character'] = {}
		self.dictAssets['prop'] = {}
		self.dictAssets['set'] = {}

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
		self.treeAsset.setHeaderLabels(['Pick what you want...'])
		self.itemAssets = QTreeWidgetItem(self.treeAsset, ['Assets'])

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

		self.itemCharacter = QTreeWidgetItem(self.itemAssets, ['character'])
		self.itemProp = QTreeWidgetItem(self.itemAssets, ['prop'])
		self.itemSet = QTreeWidgetItem(self.itemAssets, ['set'])

		listCateg = Directory.getChildren(const.PIPELINE_ROOT_PATH)

		# Get asset categories
		for categ in listCateg:

			listInCategProjects = Directory.getChildren( const.PIPELINE_ROOT_PATH + "/{}".format(categ) )

			# Get asset projects
			for proj in listInCategProjects:

				if categ == "character":
					itemProject = QTreeWidgetItem(self.itemCharacter, [proj])
				if categ == "prop":
					itemProject = QTreeWidgetItem(self.itemProp, [proj])
				if categ == "set":
					itemProject = QTreeWidgetItem(self.itemSet, [proj])

	def addItemCharacter(self, char):

		QTreeWidgetItem(self.itemCharacter, [char])

	def addItemProp(self, prop):

		QTreeWidgetItem(self.itemProp, [prop])

	def addItemSet(self, set):

		QTreeWidgetItem(self.itemSet, [set])

	def createCharacter(self):

		char = self.lineAssetCreation.text()
		Scene.createCharacter(char)
		self.lineAssetCreation.clear()
		self.addItemCharacter(char)

	def createProp(self):

		prop = self.lineAssetCreation.text()
		Scene.createProp(prop)
		self.lineAssetCreation.clear()
		self.addItemProp(prop)

	def createSet(self):

		set = self.lineAssetCreation.text()
		Scene.createSet(set)
		self.lineAssetCreation.clear()
		self.addItemSet(set)

	def contextMenuEvent(self, event):

		contextMenu = QMenu(self.treeAsset)

		newAction = contextMenu.addAction("New")
		openAction = contextMenu.addAction("Open")
		quitAction = contextMenu.addAction("Quit")

		action = contextMenu.exec_( self.mapToGlobal( event.pos() ) )