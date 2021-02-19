# coding:utf-8

from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from modules.scene import Scene
from modules.directory import Directory
from modules.path import Path
from functools import partial
import constants as const
import sys

class Manager(QWidget):

	def __init__(self):

		QWidget.__init__(self)

		self.init()

		try:
			self.populate_tree()
		except:
			pass

		self.selected_item_parent = lambda: self.tree_asset.currentItem().parent().text(0)

	def init(self):

		# Layouts creation

		self.lay = QVBoxLayout()
		self.lay_main = QHBoxLayout()
		# self.layTree = QVBoxLayout()
		self.lay_creations = QVBoxLayout()
		self.lay_asset_creation = QVBoxLayout()
		self.lay_shot_creation = QVBoxLayout()

		# UI Elements creation and settings

		self.tree_asset = QTreeWidget()

			# Assets Group
		self.group_asset_creation = QGroupBox("Assets Creation")

		self.line_asset_creation = QLineEdit()
		self.line_asset_creation.setPlaceholderText("Asset Name...")

		self.btn_create_character = QPushButton("Character")
		self.btn_create_prop = QPushButton("Prop")
		self.btn_create_set = QPushButton("Set")
		self.separator_set = QFrame()
		self.separator_set.setObjectName("separator_set")
		self.separator_set.setFrameShape(QFrame.HLine)
		self.btn_create_set_item = QPushButton("Item")
		self.btn_create_set_module = QPushButton("Module")
		self.btn_create_set_dressing = QPushButton("Dressing")

			# Shots Group
		self.group_shot_creation = QGroupBox("Shots Creation")

		self.line_shot_creation = QLineEdit()
		self.line_shot_creation.setPlaceholderText("Shot name...")

		self.btn_create_seq = QPushButton("Sequence")
		self.btn_create_shot = QPushButton("Shot")

			# status bar
		self.status_bar = QStatusBar()
		self.status_bar.showMessage("# [ INIT ] : Hi sweeties ! 😀")

		# Connect SIGNAL to SLOT

			# assets
		self.btn_create_character.clicked.connect(self.create_character)
		self.btn_create_prop.clicked.connect(self.create_prop)
		self.btn_create_set.clicked.connect(self.create_set)
		self.btn_create_set_item.clicked.connect(self.create_set_item)
		self.btn_create_set_module.clicked.connect(self.create_set_module)
		self.btn_create_set_dressing.clicked.connect(self.create_set_dressing)

			# shots
		self.btn_create_seq.clicked.connect(self.create_sequence)
		self.btn_create_shot.clicked.connect(self.create_shot)

		# Layout management

		self.setLayout(self.lay)

		self.lay.addLayout(self.lay_main)
		self.lay.addWidget(self.status_bar)

		self.lay_main.addLayout(self.lay_creations)

			# assets
		self.lay_creations.addWidget(self.group_asset_creation)

		self.group_asset_creation.setLayout(self.lay_asset_creation)

		self.lay_asset_creation.addWidget(self.line_asset_creation)
		self.lay_asset_creation.addWidget(self.btn_create_character)
		self.lay_asset_creation.addWidget(self.btn_create_prop)
		self.lay_asset_creation.addWidget(self.btn_create_set)
		self.lay_asset_creation.addWidget(self.separator_set)
		self.lay_asset_creation.addWidget(self.btn_create_set_item)
		self.lay_asset_creation.addWidget(self.btn_create_set_module)
		self.lay_asset_creation.addWidget(self.btn_create_set_dressing)

			# shots
		self.lay_creations.addWidget(self.group_shot_creation)

		self.group_shot_creation.setLayout(self.lay_shot_creation)

		self.lay_shot_creation.addWidget(self.line_shot_creation)
		self.lay_shot_creation.addWidget(self.btn_create_seq)
		self.lay_shot_creation.addWidget(self.btn_create_shot)

			# tree view
		self.lay_main.addWidget(self.tree_asset)
		
		## Set Properties

		self.group_asset_creation.setMinimumSize(133,260)
		self.group_asset_creation.setMaximumSize(133,575)

		self.line_asset_creation.setMaximumHeight(20)

		self.btn_create_character.setMaximumHeight(25)
		self.btn_create_prop.setMaximumHeight(25)
		self.btn_create_set.setMaximumHeight(25)
		self.btn_create_set_item.setMaximumHeight(25)
		self.btn_create_set_module.setMaximumHeight(25)
		self.btn_create_set_dressing.setMaximumHeight(25)

		self.group_shot_creation.setMinimumSize(133,120)
		self.group_shot_creation.setMaximumSize(133,550)

		self.line_shot_creation.setMaximumHeight(20)
		self.btn_create_seq.setMaximumHeight(25)
		self.btn_create_shot.setMaximumHeight(25)

		self.tree_asset.setFocusPolicy(Qt.NoFocus)
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

		# ASSET
		self.tree_asset.clear()

		self.main_item_asset = QTreeWidgetItem(self.tree_asset, ['ASSET'])
		self.main_item_asset.setFlags(Qt.ItemIsEnabled)

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


				# For Props
				if categ == "prop":
					item_prop = QTreeWidgetItem(self.item_prop, [proj])


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

					# Check for modules folder
					for folder in Directory.get_children( const.PIPELINE_ASSET_PATH + "/{}/{}/maya/scenes/edit/lookdev".format(categ, proj) ):
						if folder == "modules": 
							item_module = QTreeWidgetItem(item_set, ['modules'])

							# List all module folders
							for i in Directory.get_children( const.PIPELINE_ASSET_PATH + "/{}/{}/maya/scenes/edit/lookdev/modules".format(categ, proj) ):
								item_module_folder = QTreeWidgetItem(item_module, [i])


					# Check for dressing folder
					for folder in Directory.get_children( const.PIPELINE_ASSET_PATH + "/{}/{}/maya/scenes/edit".format(categ, proj) ):
						if folder == "dressing": 
							item_dressing = QTreeWidgetItem(item_set, ['dressing'])

							# List all dressing folders
							for i in Directory.get_children( const.PIPELINE_ASSET_PATH + "/{}/{}/maya/scenes/edit/dressing".format(categ, proj) ):
								item_dressing_folder = QTreeWidgetItem(item_dressing, [i])
		

		# SHOTS
		self.main_item_shot = QTreeWidgetItem(self.tree_asset, ['SHOT'])
		self.main_item_shot.setFlags(Qt.ItemIsEnabled)

		list_sequences = Directory.get_children( const.PIPELINE_SHOT_PATH )

		for seq in list_sequences:
			if not seq.startswith("seq"):
				continue
			else:
				item_seq = QTreeWidgetItem(self.main_item_shot, [seq])

				list_shots = Directory.get_children( const.PIPELINE_SHOT_PATH + "/{}".format(seq) )

				for shot in list_shots:
					if not shot.startswith("shot"):
						continue
					item_shot = QTreeWidgetItem(item_seq, [shot])


	def contextMenuEvent(self, event):

		# ASSET
		context_menu_asset = QMenu(self)

		list_menus_asset = ['Edit', 'Publish']
		list_submenus_asset = ['Open last', 'Import last', 'Reference last']
		list_actions_asset = ['geo', 'rig', 'lookdev']

		for x in list_menus_asset:
			main_menu_asset = context_menu_asset.addMenu(x)

			for y in list_submenus_asset:
				action_menu_asset = main_menu_asset.addMenu(y)

				for z in list_actions_asset:
					action_asset = action_menu_asset.addAction(z)

					action_asset.triggered.connect( partial(self.do_context_asset_actions, x, y, z) )


		context_menu_items = QMenu(self)

		list_menus_items = ['Edit', 'Publish']
		list_submenus_items = ['Open last', 'Import last', 'Reference last']
		list_actions_items = ['geo', 'lookdev']

		for x in list_menus_items:
			main_menu_items = context_menu_items.addMenu(x)

			for y in list_submenus_items:
				action_menu_items = main_menu_items.addMenu(y)

				for z in list_actions_items:
					action_items = action_menu_items.addAction(z)

					action_items.triggered.connect( partial(self.do_context_asset_actions, x, y, z) )


		context_menu_modules = QMenu(self)

		list_menus_modules = ['Edit', 'Publish']
		list_submenus_modules = ['Open last', 'Import last', 'Reference last']
		list_actions_modules = ['lookdev']

		for x in list_menus_modules:
			main_menu_modules = context_menu_modules.addMenu(x)

			for y in list_submenus_modules:
				action_menu_modules = main_menu_modules.addMenu(y)

				for z in list_actions_modules:
					action_modules = action_menu_modules.addAction(z)				

					action_modules.triggered.connect( partial(self.do_context_asset_actions, x, y, z) )


		context_menu_dressing = QMenu(self)

		list_menus_dressing = ['Edit', 'Publish']
		list_submenus_dressing = ['Open last', 'Import last', 'Reference last']
		list_actions_dressing = ['dressing']

		for x in list_menus_dressing:
			main_menu_dressing = context_menu_dressing.addMenu(x)

			for y in list_submenus_dressing:
				action_menu_dressing = main_menu_dressing.addMenu(y)

				for z in list_actions_dressing:
					action_dressing = action_menu_dressing.addAction(z)				

					action_dressing.triggered.connect( partial(self.do_context_asset_actions, x, y, z) )


		# SHOT
		context_menu_shot = QMenu(self)

		list_menus_shot = ['Open last', 'Import last', 'Reference last']
		list_actions_shot = ['anim', 'layout', 'render']

		for menu in list_menus_shot:
			menu_shot = context_menu_shot.addMenu(menu)

			for action in list_actions_shot:
				action_shot = menu_shot.addAction(action)

				action_shot.triggered.connect( partial(self.do_context_shot_actions, menu, action) )


		# master
		context_menu_seq = QMenu(self)

		list_menus_seq = ['Open last', 'Import last', 'Reference last']
		list_actions_seq = ['roughLayout', 'technicalLayout', 'finalLayout']

		for menu in list_menus_seq:
			menu_seq = context_menu_seq.addMenu(menu)

			for action in list_actions_seq:
				action_seq = menu_seq.addAction(action)

				action_seq.triggered.connect( partial(self.do_context_seq_actions, menu, action) )


		# Do
		selected_item_parent = lambda: self.tree_asset.currentItem().parent().text(0)

		try: 
			selected_item_parent()
		except:
			return

		if selected_item_parent() in ['character', 'prop', 'set']:
			action = context_menu_asset.exec_( self.mapToGlobal( event.pos() ) )

		if selected_item_parent() == "items":
			action = context_menu_items.exec_( self.mapToGlobal( event.pos() ) )

		if selected_item_parent() == "modules":
			action = context_menu_modules.exec_( self.mapToGlobal( event.pos() ) )

		if selected_item_parent() == "dressing":
			action = context_menu_dressing.exec_( self.mapToGlobal( event.pos() ) )

		if self.tree_asset.currentItem().text(0).startswith("shot"):
			action = context_menu_shot.exec_( self.mapToGlobal( event.pos() ) )

		if self.tree_asset.currentItem().text(0).startswith("seq"):
			action = context_menu_seq.exec_( self.mapToGlobal( event.pos() ) )


	def do_context_asset_actions(self, action_type, action, scene_type):

		selected_item = self.tree_asset.currentItem()
		text_selected_item = selected_item.text(0)
		parent_selected_item = selected_item.parent().text(0)

		if parent_selected_item in ["items", "modules"]:
			
			# Asset Proj root
			proj = selected_item.parent().parent()
			text_proj = proj.text(0)

			# Categ asset
			categ = proj.parent()
			text_categ = categ.text(0)

			if action_type == "Edit":

				folder = const.PIPELINE_ASSET_PATH + "/{}/{}/maya/scenes/{}/{}/{}/{}".format(
					text_categ,
					text_proj,
					action_type.lower(),
					scene_type.lower(),
					parent_selected_item,
					text_selected_item
					)

			if action_type == "Publish":

				folder = const.PIPELINE_ASSET_PATH + "/{}/{}/maya/scenes/{}/{}/{}".format(
					text_categ,
					text_proj,
					action_type.lower(),
					scene_type.lower(),
					parent_selected_item
					)

			files_list = Directory.get_children(folder)

			for file in files_list:
				if text_selected_item in file and file.endswith(".ma"):
					last = file

			if last:
				print("ITEM: " + folder + "/" + last)

				if 'Import' in action:
					Scene.import_scene(folder + "/" + last)
					self.status_bar.showMessage("# [ EVENT ] : '{}' imported.".format(last))

				if 'Open' in action:
					Scene.open_scene(folder + "/" + last)
					self.status_bar.showMessage("# [ EVENT ] : '{}' opened.".format(last))

				if 'Reference' in action:
					Scene.reference_scene(folder + "/" + last)
					self.status_bar.showMessage("# [ EVENT ] : '{}' referenced.".format(last))


		if parent_selected_item == "dressing":
			
			# Asset Proj root
			proj = selected_item.parent().parent() # proj
			text_proj = proj.text(0) # proj

			# Categ asset
			categ = proj.parent() # set
			text_categ = categ.text(0) #set

			# folder = const.PIPELINE_ASSET_PATH + "/{}/{}/maya/scenes/{}/{}/{}".format(
			# 	text_categ,
			# 	text_proj,
			# 	action_type.lower(),
			# 	scene_type.lower(),
			# 	text_selected_item
			# 	)
			if action_type == "Edit":

				folder = const.PIPELINE_ASSET_PATH + "/{}/{}/maya/scenes/{}/{}/{}".format(
					text_categ,
					text_proj,
					action_type.lower(),
					scene_type.lower(),
					text_selected_item
					)

			if action_type == "Publish":

				folder = const.PIPELINE_ASSET_PATH + "/{}/{}/maya/scenes/{}/{}".format(
					text_categ,
					text_proj,
					action_type.lower(),
					scene_type.lower()
					)

			files_list = Directory.get_children(folder)

			for file in files_list:
				if text_selected_item in file and file.endswith(".ma"):
					last = file

			if last:
				print("ITEM: " + folder + "/" + last)

				if 'Import' in action:
					Scene.import_scene(folder + "/" + last)
					self.status_bar.showMessage("# [ EVENT ] : '{}' imported.".format(last))

				if 'Open' in action:
					Scene.open_scene(folder + "/" + last)
					self.status_bar.showMessage("# [ EVENT ] : '{}' opened.".format(last))

				if 'Reference' in action:
					Scene.reference_scene(folder + "/" + last)
					self.status_bar.showMessage("# [ EVENT ] : '{}' referenced.".format(last))


		if parent_selected_item not in ["items", "modules", "dressing"]:
			
			categ = selected_item.parent()
			text_categ = categ.text(0)

			# Normal
			folder = const.PIPELINE_ASSET_PATH + "/{}/{}/maya/scenes/{}/{}".format(
				text_categ,
				text_selected_item,
				action_type.lower(),
				scene_type.lower()
				)

			files_list = Directory.get_children(folder)

			for file in files_list:
				if text_selected_item in file and file.endswith(".ma"):
					last = file

			print(folder + "/" + last)

			# Edit > Open last
			if 'Import' in action:
				Scene.import_scene(folder + "/" + last)
				self.status_bar.showMessage("# [ EVENT ] : '{}' imported.".format(last))

			if 'Open' in action:
				Scene.open_scene(folder + "/" + last)
				self.status_bar.showMessage("# [ EVENT ] : '{}' opened.".format(last))

			if 'Reference' in action:
				Scene.reference_scene(folder + "/" + last)
				self.status_bar.showMessage("# [ EVENT ] : '{}' referenced.".format(last))


	def do_context_seq_actions(self, action, scene_type):

		seq_item = self.tree_asset.currentItem()

		seq = seq_item.text(0)

		if seq_item.parent().text(0) == "SHOT":

			folder = const.PIPELINE_SHOT_PATH + "/{}/master/maya/scenes/{}".format(seq, scene_type)

			files_list = Directory.get_children(folder)

			for file in files_list:
				if seq in file and file.endswith(".ma"):
					last = file

			if 'Import' in action:
				Scene.import_scene(folder + "/" + last)
				self.status_bar.showMessage("# [ EVENT ] : '{}' imported.".format(last))

			if 'Open' in action:
				Scene.open_scene(folder + "/" + last)
				self.status_bar.showMessage("# [ EVENT ] : '{}' opened.".format(last))

			if 'Reference' in action:
				Scene.reference_scene(folder + "/" + last)
				self.status_bar.showMessage("# [ EVENT ] : '{}' referenced.".format(last))


	def do_context_shot_actions(self, action, scene_type):

		shot_item = self.tree_asset.currentItem()
		sequence_item = shot_item.parent()

		shot = shot_item.text(0)
		sequence = sequence_item.text(0)

		if sequence_item.parent().text(0) == "SHOT":

			folder = const.PIPELINE_SHOT_PATH + "/{}/{}/maya/scenes/{}".format(sequence, shot, scene_type)

			files_list = Directory.get_children(folder)

			for file in files_list:
				if shot in file and file.endswith(".ma"):
					last = file

			if 'Import' in action:
				Scene.import_scene(folder + "/" + last)
				self.status_bar.showMessage("# [ EVENT ] : '{}' imported.".format(last))

			if 'Open' in action:
				Scene.open_scene(folder + "/" + last)
				self.status_bar.showMessage("# [ EVENT ] : '{}' opened.".format(last))

			if 'Reference' in action:
				Scene.reference_scene(folder + "/" + last)
				self.status_bar.showMessage("# [ EVENT ] : '{}' referenced.".format(last))


	def add_item_character(self, char):

		if char == "":
			self.status_bar.showMessage("# [ ERROR ] : Any name in line edit. Must put a name in 'asset' line edit.")
			return

		QTreeWidgetItem(self.item_character, [char])


	def add_item_prop(self, prop):

		if prop == "":
			self.status_bar.showMessage("# [ ERROR ] : Any name in line edit. Must put a name in 'asset' line edit.")
			return

		QTreeWidgetItem(self.item_prop, [prop])


	def add_item_set(self, set):

		if set == "":
			self.status_bar.showMessage("# [ ERROR ] : Any name in line edit. Must put a name in 'asset' line edit.")
			return

		QTreeWidgetItem(self.item_set, [set])
		self.populate_tree()


	def add_item_set_item(self, set_item):

		if set_item == "":
			self.status_bar.showMessage("# [ ERROR ] : Any name in line edit. Must put a name in 'asset' line edit.")
			return

		try:
			QTreeWidgetItem(self.tree_asset.currentItem(), [set_item])
		except:
			self.status_bar.showMessage("# [ ERROR ] : Any set selected. Must select the parent's item set before create item.")


	def add_item_set_module(self, set_module):

		if set_module == "":
			self.status_bar.showMessage("# [ ERROR ] : Any name in line edit. Must put a name in 'asset' line edit.")
			return

		try:
			QTreeWidgetItem(self.tree_asset.currentItem(), [set_module])
		except:
			self.status_bar.showMessage("# [ ERROR ] : Any set selected. Must select the parent's item set before create item.")


	def add_item_set_dressing(self, set_dressing):

		if set_dressing == "":
			self.status_bar.showMessage("# [ ERROR ] : Any name in line edit. Must put a name in 'asset' line edit.")
			return

		try:
			QTreeWidgetItem(self.tree_asset.currentItem(), [set_dressing])
		except:
			self.status_bar.showMessage("# [ ERROR ] : Any set selected. Must select the parent's item set before create item.")


	def add_item_seq(self, seq):

		if seq == "":
			self.status_bar.showMessage("# [ ERROR ] : Any name in line edit. Must put a name in 'shot' line edit.")
			return

		QTreeWidgetItem(self.main_item_shot, [seq])


	def add_item_shot(self, shot):
		
		if shot == "":
			self.status_bar.showMessage("# [ ERROR ] : Any name in line edit. Must put a name in 'shot' line edit.")
			return

		QTreeWidgetItem(self.tree_asset.currentItem(), [shot])


	def create_character(self):

		char = self.line_asset_creation.text()

		if char:
			self.add_item_character(char)
			self.line_asset_creation.clear()

			Scene.create_character(char)
			self.status_bar.showMessage("# [ EVENT ] : character '{}' created.".format(char))

		else:
			self.status_bar.showMessage("# [ ERROR ] : Any name in line edit. Must put a name in 'asset' line edit.")


	def create_prop(self):

		prop = self.line_asset_creation.text()

		if prop:
			self.add_item_prop(prop)
			self.line_asset_creation.clear()
			Scene.create_prop(prop)
			self.status_bar.showMessage("# [ EVENT ] : prop '{}' created.".format(prop))

		else:
			self.status_bar.showMessage("# [ ERROR ] : Any name in line edit. Must put a name in 'asset' line edit.")
		

	def create_set(self):

		set = self.line_asset_creation.text()

		if set:
			self.add_item_set(set)
			self.line_asset_creation.clear()
			Scene.create_set(set)
			self.status_bar.showMessage("# [ EVENT ] : set '{}' created.".format(set))

		else:
			self.status_bar.showMessage("# [ ERROR ] : Any name in line edit. Must put a name in 'asset' line edit.")


	def create_set_item(self):

		if self.tree_asset.currentItem() is not None:
			if self.tree_asset.currentItem().text(0) == "items":
				set = self.tree_asset.currentItem().parent().text(0)
				set_item = self.line_asset_creation.text()

				if set_item:
					self.add_item_set_item(set_item)
					self.line_asset_creation.clear()
					Scene.create_item(set_item, set)
					self.status_bar.showMessage("# [ EVENT ] : item '{}' created in set '{}'.".format(set_item, set))

				else:
					self.status_bar.showMessage("# [ ERROR ] : Any name in line edit. Must put a name in 'asset' line edit.")

			else:
				self.status_bar.showMessage("# [ ERROR ] : Select 'items' folder under the desired set in order to create an item.")

		else:
			self.status_bar.showMessage("# [ ERROR ] : Select 'items' folder under the desired set in order to create an item.")


	def create_set_module(self):

		if self.tree_asset.currentItem() is not None:
			if self.tree_asset.currentItem().text(0) == "modules":
				set = self.tree_asset.currentItem().parent().text(0)
				set_module = self.line_asset_creation.text()

				if set_module:

					self.add_item_set_module(set_module)
					self.line_asset_creation.clear()
					Scene.create_module(set_module, set)
					self.status_bar.showMessage("# [ EVENT ] : item '{}' created in set '{}'.".format(set_module, set))

				else:
					self.status_bar.showMessage("# [ ERROR ] : Any name in line edit. Must put a name in 'asset' line edit.")

			else:
				self.status_bar.showMessage("# [ ERROR ] : Select 'modules' folder under the desired set in order to create a module.")

		else:
			self.status_bar.showMessage("# [ ERROR ] : Select 'modules' folder under the desired set in order to create a module.")


	def create_set_dressing(self):

		if self.tree_asset.currentItem() is not None:
			if self.tree_asset.currentItem().text(0) == "dressing":
				set = self.tree_asset.currentItem().parent().text(0)
				set_dressing = self.line_asset_creation.text()

				if set_dressing:

					self.add_item_set_module(set_dressing)
					self.line_asset_creation.clear()
					Scene.create_dressing(set_dressing, set)
					self.status_bar.showMessage("# [ EVENT ] : item '{}' created in set '{}'.".format(set_dressing, set))

				else:
					self.status_bar.showMessage("# [ ERROR ] : Any name in line edit. Must put a name in 'asset' line edit.")

			else:
				self.status_bar.showMessage("# [ ERROR ] : Select 'dressing' folder under the desired set in order to create a dressing.")

		else:
			self.status_bar.showMessage("# [ ERROR ] : Select 'dressing' folder under the desired set in order to create a dressing.")


	def create_sequence(self):

		seq_name = self.line_shot_creation.text()

		if seq_name:
			self.add_item_seq(seq_name)		
			self.line_shot_creation.clear()
			Scene.create_sequence(seq_name)

		else:
			self.status_bar.showMessage("# [ ERROR ] : Any name in line edit. Must put a name in 'shot' line edit.")


	def create_shot(self):

		shot_name = self.line_shot_creation.text()

		if shot_name:
			self.add_item_shot(shot_name)
			self.line_shot_creation.clear()
			Scene.create_shot(shot_name, self.tree_asset.currentItem().text(0))

		else:
			self.status_bar.showMessage("# [ ERROR ] : Any name in line edit. Must put a name in 'shot' line edit.")