# coding:utf-8

from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from modules.scene import Scene
from modules.directory import Directory
from modules.path import Path
from functools import partial
import constants as const

class Manager(QWidget):

	def __init__(self):

		QWidget.__init__(self)

		self.init()
		self.populate_tree()

	def init(self):

		# Layouts creation

		self.lay_main = QHBoxLayout()
		# self.layTree = QVBoxLayout()
		self.lay_creations = QVBoxLayout()
		self.lay_asset_creation = QVBoxLayout()
		self.lay_shot_creation = QVBoxLayout()

		# UI Elements creation and settings

		self.tree_asset = QTreeWidget()
		self.main_item_asset = QTreeWidgetItem(self.tree_asset, ['ASSET'])
		self.main_item_shot = QTreeWidgetItem(self.tree_asset, ['SHOT'])

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

		self.btn_create_seq = QPushButton("Sequence")
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
		self.lay_shot_creation.addWidget(self.btn_create_seq)
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
		self.btn_create_seq.setMaximumHeight(25)
		self.btn_create_shot.setMaximumHeight(25)

		self.tree_asset.setFocusPolicy(Qt.NoFocus)
		self.tree_asset.setMaximumSize(10000, 10000)
		self.tree_asset.setMinimumSize(100, 150)
		self.tree_asset.setAnimated(True)
		self.tree_asset.setHeaderHidden(True)

		self.main_item_asset.setFlags(Qt.ItemIsEnabled)
		self.main_item_shot.setFlags(Qt.ItemIsEnabled)

		self.lay_main.setSpacing(8)

		self.lay_creations.setSpacing(8)

		self.lay_asset_creation.setContentsMargins(9,25,9,9)
		self.lay_asset_creation.setSpacing(8)

		self.lay_shot_creation.setContentsMargins(9,25,9,9)
		self.lay_shot_creation.setSpacing(8)


	def populate_tree(self):

		# ASSET
		try:
			self.main_item_asset.removeChild(self.item_character)
			self.main_item_asset.removeChild(self.item_prop)
			self.main_item_asset.removeChild(self.item_set)
		except:
			pass

		self.item_character = QTreeWidgetItem(self.main_item_asset, ['character'])
		self.item_prop = QTreeWidgetItem(self.main_item_asset, ['prop'])
		self.item_set = QTreeWidgetItem(self.main_item_asset, ['set'])

		self.item_character.setFlags(Qt.ItemIsEnabled)
		self.item_prop.setFlags(Qt.ItemIsEnabled)
		self.item_set.setFlags(Qt.ItemIsEnabled)

		list_categ = Directory.get_children(const.PIPELINE_ASSET_PATH)

		# Get asset categories
		for categ in list_categ:
			if categ in const.FILE_TO_IGNORE_LIST:
				continue

			list_projects_in_categ = Directory.get_children( const.PIPELINE_ASSET_PATH + "/{}".format(categ) )

			# Get asset projects
			for proj in list_projects_in_categ:

				# Filter temp gelax folder
				if proj in const.FILE_TO_IGNORE_LIST:
					continue

				# For Characters
				if categ == "character":
					item_char = QTreeWidgetItem(self.item_character, [proj])

					# Check for items
					for folder in Directory.get_children(const.PIPELINE_ASSET_PATH + "/{}/{}/maya/scenes/edit/geo".format(categ, proj) ): 
						if folder == "items": 
							item_items = QTreeWidgetItem(item_char, ['items'])

							# List all item folders
							for i in Directory.get_children( const.PIPELINE_ASSET_PATH + "/{}/{}/maya/scenes/edit/geo/items".format(categ, proj) ):
								item_item_folder = QTreeWidgetItem(item_items, [i])

				# For Props
				if categ == "prop":
					item_prop = QTreeWidgetItem(self.item_prop, [proj])

					# Check for items
					for folder in Directory.get_children( const.PIPELINE_ASSET_PATH + "/{}/{}/maya/scenes/edit/geo".format(categ, proj) ): 
						if folder == "items": 
							item_items = QTreeWidgetItem(item_prop, ['items'])

							# List all item folders
							for i in Directory.get_children( const.PIPELINE_ASSET_PATH + "/{}/{}/maya/scenes/edit/geo/items".format(categ, proj) ):
								item_item_folder = QTreeWidgetItem(item_items, [i])

				# For Sets
				if categ == "set":
					item_set = QTreeWidgetItem(self.item_set, [proj])

					# Check for items folder
					for folder in Directory.get_children( const.PIPELINE_ASSET_PATH + "/{}/{}/maya/scenes/edit/geo".format(categ, proj) ): 
						if folder == "items": 
							item_items = QTreeWidgetItem(item_set, ['items'])

							# List all item folders
							for i in Directory.get_children( const.PIPELINE_ASSET_PATH + "/{}/{}/maya/scenes/edit/geo/items".format(categ, proj) ):
								item_item_folder = QTreeWidgetItem(item_items, [i])


		# SHOTS
		list_sequences = Directory.get_children( const.PIPELINE_SHOT_PATH )

		for seq in list_sequences:
			if seq in const.FILE_TO_IGNORE_LIST:
				continue

			item_seq = QTreeWidgetItem(self.main_item_shot, [seq])

			list_shots = Directory.get_children( const.PIPELINE_SHOT_PATH + "/{}".format(seq) )

			for shot in list_shots:
				item_shot = QTreeWidgetItem(item_seq, [shot])


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

		# ASSET
		context_menu_asset = QMenu(self)

		list_menus_asset = ['Edit', 'Publish']
		list_submenus_asset = ['Open last', 'Import last', 'Reference last']
		list_actions_asset = ['geo', 'rig', 'lookdev', 'dressing']

		for x in list_menus_asset:
			main_menu_asset = context_menu_asset.addMenu(x)

			for y in list_submenus_asset:
				action_menu_asset = main_menu_asset.addMenu(y)

				for z in list_actions_asset:
					action_asset = action_menu_asset.addAction(z)

					action_asset.triggered.connect( partial(self.do_context_menu_actions, x, y, z) )


		# SHOT
		context_menu_shot = QMenu(self)

		list_menus_shot = ['Open last', 'Import last', 'Reference last']
		list_actions_shot = ['Anim', 'Layout', 'Render']

		for menu in list_menus_shot:
			menu_shot = context_menu_shot.addMenu(menu)

			for action in list_actions_shot:
				action_shot = menu_shot.addAction(action)

		# Do
		if self.tree_asset.currentItem().parent().text(0) in ['character', 'prop', 'set']:
			action = context_menu_asset.exec_( self.mapToGlobal( event.pos() ) )

		if self.tree_asset.currentItem().parent().text(0) in ['SHOT']:
			action = context_menu_shot.exec_( self.mapToGlobal( event.pos() ) )

		if self.tree_asset.currentItem() is None:
			pass
			

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

			folder_item = const.PIPELINE_ASSET_PATH + "/{}/{}/maya/scenes/{}/{}/items/{}".format(
				text_categ,
				text_proj,
				action_type.lower(),
				scene_type.lower(),
				text_selected_item
				)

			last_item = Directory.get_children(folder_item)[-1]
			print("ITEM: " + folder_item + "/" + last_item)

			if 'Import' in action:
				Scene.import_scene(folder_item + "/" + last_item)

			if 'Open' in action:
				Scene.open_scene(folder_item + "/" + last_item)

			if 'Reference' in action:
				Scene.reference_scene(folder_item + "/" + last_item)

		else:
			categ = selected_item.parent()
			text_categ = categ.text(0)

			# Normal
			folder = const.PIPELINE_ASSET_PATH + "/{}/{}/maya/scenes/{}/{}".format(
				text_categ,
				text_selected_item,
				action_type.lower(),
				scene_type.lower()
				)

			files_and_folders = Directory.get_children(folder)

			last = None
			for x in files_and_folders:
				if x in const.FILE_TO_IGNORE_LIST:
					continue
				last = x

			print(folder + "/" + last)

			# Edit > Open last
			if 'Import' in action:
				Scene.import_scene(folder + "/" + last)

			if 'Open' in action:
				Scene.open_scene(folder + "/" + last)

			if 'Reference' in action:
				Scene.reference_scene(folder + "/" + last)