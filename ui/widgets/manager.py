# coding:utf-8

from PySide2.QtWidgets import *
from modules.scene import Scene
from modules.directory import Directory
from functools import partial
import constants as const

class Manager(QWidget):

	def __init__(self):

		QWidget.__init__(self)

		self.dict_assets = {}
		self.dict_assets['character'] = {}
		self.dict_assets['prop'] = {}
		self.dict_assets['set'] = {}

		self.init()

		try:
			self.populate_tree()
		except:
			pass

	def init(self):

		# Layouts creation

		self.lay_main = QHBoxLayout()
		# self.layTree = QVBoxLayout()
		self.lay_creations = QVBoxLayout()
		self.lay_asset_creation = QVBoxLayout()
		self.lay_shot_creation = QVBoxLayout()

		# UI Elements creation and settings

		self.tree_asset = QTreeWidget()
		self.item_assets = QTreeWidgetItem(self.tree_asset, ['ASSETS'])

			# Assets Group
		self.group_asset_creation = QGroupBox("Assets Creation")

		self.line_asset_creation = QLineEdit()
		self.line_asset_creation.setPlaceholderText("Asset Name...")

		self.btn_create_character = QPushButton("Character")
		self.btn_create_prop = QPushButton("Prop")
		self.btn_create_set = QPushButton("Set")

			# Shots Group
		self.group_shot_creation = QGroupBox("Shots Creation")

		self.line_shot_creation = QLineEdit()
		self.line_shot_creation.setPlaceholderText("Shot name...")

		self.btn_create_shot = QPushButton("Shot")

		# Connect SIGNAL to SLOT

			# assets
		self.btn_create_character.clicked.connect(self.create_character)
		self.btn_create_prop.clicked.connect(self.create_prop)
		self.btn_create_set.clicked.connect(self.create_set)

			# shots
		# self.btnCreateShot.clicked.connect(self.createShot) # TO ADD

			# context menu


		# Layout management

		self.setLayout(self.lay_main)

		self.lay_main.addLayout(self.lay_creations)

			# assets
		self.lay_creations.addWidget(self.group_asset_creation)

		self.group_asset_creation.setLayout(self.lay_asset_creation)

		self.lay_asset_creation.addWidget(self.line_asset_creation)
		self.lay_asset_creation.addWidget(self.btn_create_character)
		self.lay_asset_creation.addWidget(self.btn_create_prop)
		self.lay_asset_creation.addWidget(self.btn_create_set)

			# shots
		self.lay_creations.addWidget(self.group_shot_creation)

		self.group_shot_creation.setLayout(self.lay_shot_creation)

		self.lay_shot_creation.addWidget(self.line_shot_creation)
		self.lay_shot_creation.addWidget(self.btn_create_shot)

			# tree view
		self.lay_main.addWidget(self.tree_asset)
		
		## Set Properties

		self.group_asset_creation.setMinimumSize(110,158)
		self.group_asset_creation.setMaximumSize(133,550)

		self.line_asset_creation.setMaximumHeight(20)

		self.btn_create_character.setMaximumHeight(25)
		self.btn_create_prop.setMaximumHeight(25)
		self.btn_create_set.setMaximumHeight(25)

		self.group_shot_creation.setMinimumSize(110,110)
		self.group_shot_creation.setMaximumSize(133,550)

		self.line_shot_creation.setMaximumHeight(20)
		self.btn_create_shot.setMaximumHeight(25)

		self.tree_asset.setMaximumSize(10000, 10000)
		self.tree_asset.setMinimumSize(100, 150)
		self.tree_asset.setAnimated(True)
		self.tree_asset.setHeaderHidden(True)

		self.lay_main.setSpacing(8)

		self.lay_creations.setSpacing(8)

		self.lay_asset_creation.setContentsMargins(9,25,9,9)
		self.lay_asset_creation.setSpacing(8)

		self.lay_shot_creation.setContentsMargins(9,25,9,9)
		self.lay_shot_creation.setSpacing(8)

	def populate_tree(self):

		try:
			self.item_assets.removeChild(self.item_character)
			self.item_assets.removeChild(self.item_prop)
			self.item_assets.removeChild(self.item_set)
		except:
			pass

		self.item_character = QTreeWidgetItem(self.item_assets, ['character'])
		self.item_prop = QTreeWidgetItem(self.item_assets, ['prop'])
		self.item_set = QTreeWidgetItem(self.item_assets, ['set'])

		list_categ = Directory.get_children(const.PIPELINE_ROOT_PATH)

		# Get asset categories
		for categ in list_categ:
			if categ in const.FILE_TO_IGNORE_LIST:
				continue

			list_projects_in_categ = Directory.get_children( const.PIPELINE_ROOT_PATH + "/{}".format(categ) )

			# Get asset projects
			for proj in list_projects_in_categ:

				# Filter temp gelax folder
				if proj in const.FILE_TO_IGNORE_LIST:
					continue

				# For Characters
				if categ == "character":
					item_char = QTreeWidgetItem(self.item_character, [proj])

					# Check for items
					for folder in Directory.get_children( const.PIPELINE_ROOT_PATH + "/{}/{}/maya/scenes/edit/geo".format(categ, proj) ): 
						if folder == "items": 
							item_items = QTreeWidgetItem(item_char, ['items'])

							# List all item folders
							for i in Directory.get_children( const.PIPELINE_ROOT_PATH + "/{}/{}/maya/scenes/edit/geo/items".format(categ, proj) ):
								item_item_folder = QTreeWidgetItem(item_items, [i])

				# For Props
				if categ == "prop":
					item_prop = QTreeWidgetItem(self.item_prop, [proj])

					# Check for items
					for folder in Directory.get_children( const.PIPELINE_ROOT_PATH + "/{}/{}/maya/scenes/edit/geo".format(categ, proj) ): 
						if folder == "items": 
							item_items = QTreeWidgetItem(item_prop, ['items'])

							# List all item folders
							for i in Directory.get_children( const.PIPELINE_ROOT_PATH + "/{}/{}/maya/scenes/edit/geo/items".format(categ, proj) ):
								item_item_folder = QTreeWidgetItem(item_items, [i])

				# For Sets
				if categ == "set":
					item_set = QTreeWidgetItem(self.item_set, [proj])

					# Check for items folder
					for folder in Directory.get_children( const.PIPELINE_ROOT_PATH + "/{}/{}/maya/scenes/edit/geo".format(categ, proj) ): 
						if folder == "items": 
							item_items = QTreeWidgetItem(item_set, ['items'])

							# List all item folders
							for i in Directory.get_children( const.PIPELINE_ROOT_PATH + "/{}/{}/maya/scenes/edit/geo/items".format(categ, proj) ):
								item_item_folder = QTreeWidgetItem(item_items, [i])


	def add_item_character(self, char):

		QTreeWidgetItem(self.item_character, [char])

	def add_ttem_prop(self, prop):

		QTreeWidgetItem(self.item_prop, [prop])

	def add_item_set(self, set):

		QTreeWidgetItem(self.item_set, [set])

	def create_character(self):

		char = self.line_asset_creation.text()
		Scene.create_character(char)
		self.line_asset_creation.clear()
		self.add_item_character(char)

	def create_prop(self):

		prop = self.line_asset_creation.text()
		Scene.create_prop(prop)
		self.line_asset_creation.clear()
		self.add_item_prop(prop)

	def create_set(self):

		set = self.line_asset_creation.text()
		Scene.create_set(set)
		self.line_asset_creation.clear()
		self.add_item_set(set)

	def contextMenuEvent(self, event):

		context_menu = QMenu(self)

		dict_menus = {

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

		list_menus = list( dict_menus.keys() )
		list_menus.sort()
		for x in list_menus:
			main_menu = context_menu.addMenu(x)

			list_submenus = list( dict_menus[x].keys() )
			list_submenus.sort()
			for y in list_submenus:
				action_menu = main_menu.addMenu(y)

				list_actions = list( dict_menus[x][y].keys() )
				list_actions.sort()
				for z in list_actions:
					action = action_menu.addAction(z)

					action.triggered.connect( partial(self.do_context_menu_actions, x, y, z) )

		action = context_menu.exec_( self.mapToGlobal( event.pos() ) )


	def printZ(self, x, y, z):
		print("{}>{}>{}".format(x, y, z))

	def do_context_menu_actions(self, action_type, action, scene_type):

		selected_item = self.tree_asset.currentItem()
		text_selected_item = selected_item.text(0)

		if selected_item.parent().text(0) == "items":
			
			# Asset Proj root
			proj = selected_item.parent().parent()
			text_proj = proj.text(0)

			# Categ asset
			categ = proj.parent()
			text_categ = categ.text(0)

			# if selected_item is an item 
			dir_edit_item = const.PIPELINE_ROOT_PATH + "/{}/{}/maya/scenes/edit/{}/items/{}".format(text_categ, text_proj, scene_type.lower(), text_selected_item)
			last_item = Directory.get_children(dir_edit_item)[-1]
			print("ITEM: " + dir_edit_item + "/" + last_item)

			if [action_type, action] == ['Edit', 'Import last']:
				Scene.import_scene(dir_edit_item + "/" + last_item)

			if [action_type, action] == ['Edit', 'Open last']:
				Scene.open_scene(dir_edit_item + "/" + last_item)

			if [action_type, action] == ['Edit', 'Reference last']:
				Scene.reference_scene(dir_edit_item + "/" + last_item)

				


		else:
			categ = selected_item.parent()
			text_categ = categ.text(0)

			# Normal
			dir_edit = const.PIPELINE_ROOT_PATH + "/{}/{}/maya/scenes/edit/{}".format(text_categ, text_selected_item, scene_type.lower())
			last = Directory.get_children(dir_edit)[-1]
			print(dir_edit + "/" + last)

			# Edit > Open last
			if [action_type, action] == ['Edit', 'Import last']:
				Scene.import_scene(dir_edit + "/" + last)

			if [action_type, action] == ['Edit', 'Open last']:
				Scene.open_scene(dir_edit + "/" + last)

			if [action_type, action] == ['Edit', 'Reference last']:
				Scene.reference_scene(dir_edit + "/" + last)