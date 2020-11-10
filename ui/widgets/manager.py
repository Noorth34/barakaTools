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
		# self.layTree = QVBoxLayout()
		self.layCreations = QVBoxLayout()
		self.layAssetCreation = QVBoxLayout()
		self.layShotCreation = QVBoxLayout()

		# UI Elements creation and settings

		self.treeAsset = QTreeWidget()
		self.itemAssets = QTreeWidgetItem(self.treeAsset, ['ASSETS'])

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

			# context menu


		# Layout management

		self.setLayout(self.layMain)

		self.layMain.addLayout(self.layCreations)

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
		self.layMain.addWidget(self.treeAsset)
		
		## Set Properties

		self.groupAssetCreation.setMinimumSize(110,158)
		self.groupAssetCreation.setMaximumSize(133,550)

		self.lineAssetCreation.setMaximumHeight(20)

		self.btnCreateCharacter.setMaximumHeight(25)
		self.btnCreateProp.setMaximumHeight(25)
		self.btnCreateSet.setMaximumHeight(25)

		self.groupShotCreation.setMinimumSize(110,110)
		self.groupShotCreation.setMaximumSize(133,550)

		self.lineShotCreation.setMaximumHeight(20)
		self.btnCreateShot.setMaximumHeight(25)

		self.treeAsset.setMaximumSize(1000, 1000)
		self.treeAsset.setMinimumSize(100, 150)
		self.treeAsset.setAnimated(True)
		self.treeAsset.setHeaderHidden(True)

		self.layMain.setSpacing(8)

		self.layCreations.setSpacing(8)

		self.layAssetCreation.setContentsMargins(9,25,9,9)
		self.layAssetCreation.setSpacing(8)

		self.layShotCreation.setContentsMargins(9,25,9,9)
		self.layShotCreation.setSpacing(8)

	def populateTree(self):

		try:
			self.itemAssets.removeChild(self.itemCharacter)
			self.itemAssets.removeChild(self.itemProp)
			self.itemAssets.removeChild(self.itemSet)
		except:
			pass

		self.itemCharacter = QTreeWidgetItem(self.itemAssets, ['character'])
		self.itemProp = QTreeWidgetItem(self.itemAssets, ['prop'])
		self.itemSet = QTreeWidgetItem(self.itemAssets, ['set'])

		listCateg = Directory.getChildren(const.PIPELINE_ROOT_PATH)

		# Get asset categories
		for categ in listCateg:
			if categ == "workspace.mel":
				continue

			listInCategProjects = Directory.getChildren( const.PIPELINE_ROOT_PATH + "/{}".format(categ) )

			# Get asset projects
			for proj in listInCategProjects:

				# Filter temp gelax folder
				if proj in const.FILE_TO_IGNORE_LIST:
					continue

				# For Characters
				if categ == "character":
					i_Char = QTreeWidgetItem(self.itemCharacter, [proj])

					# Check for items
					for file in Directory.getChildren( const.PIPELINE_ROOT_PATH + "/{}/{}/maya/scenes/edit/geo".format(categ, proj) ): 
						if file == "items": 
							i_Items = QTreeWidgetItem(i_Char, ['items'])

							# List all item folders
							for i in Directory.getChildren( const.PIPELINE_ROOT_PATH + "/{}/{}/maya/scenes/edit/geo/items".format(categ, proj) ):
								i_itemFol = QTreeWidgetItem(i_Items, [i])

				# For Props
				if categ == "prop":
					i_Prop = QTreeWidgetItem(self.itemProp, [proj])

					# Check for items
					for file in Directory.getChildren( const.PIPELINE_ROOT_PATH + "/{}/{}/maya/scenes/edit/geo".format(categ, proj) ): 
						if file == "items": 
							i_Items = QTreeWidgetItem(i_Prop, ['items'])

							# # List all item folders
							# for i in Directory.getChildren( const.PIPELINE_ROOT_PATH + "/{}/{}/maya/scenes/edit/geo/items".format(categ, proj) ):
							# 	i_itemFol = QTreeWidgetItem(i_Items, [i])

				# For Sets
				if categ == "set":
					i_Set = QTreeWidgetItem(self.itemSet, [proj])

					# Check for items folder
					for file in Directory.getChildren( const.PIPELINE_ROOT_PATH + "/{}/{}/maya/scenes/edit/geo".format(categ, proj) ): 
						if file == "items": 
							i_Items = QTreeWidgetItem(i_Set, ['items'])

							# List all item folders
							for i in Directory.getChildren( const.PIPELINE_ROOT_PATH + "/{}/{}/maya/scenes/edit/geo/items".format(categ, proj) ):
								i_itemFol = QTreeWidgetItem(i_Items, [i])


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

		contextMenu = QMenu(self)

		dictMenus = {

		"Edit" : {

				"Open last" : {

							"Geo" : "",
							"Rig" : "",
							"Lookdev" : "",
							"Dressing" : "",
							"LightRig" : ""

							},

				"Import last" : {

							"Geo" : "",
							"Rig" : "",
							"Lookdev" : "",
							"Dressing" : "",
							"LightRig" : ""

							},
				"Reference last" : {

							"Geo" : "",
							"Rig" : "",
							"Lookdev" : "",
							"Dressing" : "",
							"LightRig" : ""

							}
				},

		"Publish" : {

				"Open" : {

							"Geo" : "",
							"Rig" : "",
							"Lookdev" : "",
							"Dressing" : "",
							"LightRig" : ""

							},

				"Import" : {

							"Geo" : "",
							"Rig" : "",
							"Lookdev" : "",
							"Dressing" : "",
							"LightRig" : ""

							},
				"Reference" : {

							"Geo" : "",
							"Rig" : "",
							"Lookdev" : "",
							"Dressing" : "",
							"LightRig" : ""

							}
				}
		}

		listMenus = list( dictMenus.keys() )
		listMenus.sort()
		for x in listMenus:
			mainMenu = contextMenu.addMenu(x)

			listSubMenus = list( dictMenus[x].keys() )
			listSubMenus.sort()
			for y in listSubMenus:
				actionMenu = mainMenu.addMenu(y)

				listActions = list( dictMenus[x][y].keys() )
				listActions.sort()
				for z in listActions:
					action = actionMenu.addAction(z)

					action.triggered.connect( partial(self.doContextMenuActions, x, y, z) )

		action = contextMenu.exec_( self.mapToGlobal( event.pos() ) )


	def printZ(self, x, y, z):
		print("{}>{}>{}".format(x, y, z))

	def doContextMenuActions(self, actionType, action, sceneType):

		selectedItem = self.treeAsset.currentItem()
		asset = selectedItem.text(0)
		categItem = selectedItem.parent()
		textCateg = categItem.text(0)

		if [actionType, action] == ['Edit', 'Import last']:
			dirEdit = const.PIPELINE_ROOT_PATH + "/{}/{}/maya/scenes/edit/{}".format(textCateg, asset, sceneType.lower())
			last = Directory.getChildren(dirEdit)[-1]
			print(dirEdit + "/" + last)