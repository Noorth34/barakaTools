# coing:utf-8

from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow, QDialog, QAction, QTabWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout
from PySide2.QtGui import QIcon, Qt
from PySide2.QtCore import QSize, QPropertyAnimation
from ui.widgets.publisher import Publisher
from ui.widgets.manager import Manager
from ui.mayaWin import get_maya_main_window
from constants import BARAKA_ICONS_PATH, BARAKA_STYLESHEETS_PATH, BARAKA_CONFIG_PATH
from constants import PIPELINE_ROOT_PATH, PIPELINE_SHOT_PATH, PIPELINE_ASSET_PATH
from constants import PIPELINE_CHARACTERS, PIPELINE_PROPS, PIPELINE_SETS


class Pipeline(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self, parent = get_maya_main_window())

        self.width_manager = 550
        self.height_manager = 490

        self.width_publisher = 225
        self.height_publisher = 280

        self.setWindowTitle("Pipeline")
        self.setWindowIcon(QIcon(BARAKA_ICONS_PATH + "/coca.png"))
        self.setGeometry(600, 400, self.width_manager, self.height_manager)
        self.setMinimumWidth(self.width_publisher)
        self.setMinimumHeight(self.width_publisher)

        self._init_menus()
        self._init_tab_widget()
        self._init_manager()
        self._init_publisher()

        self.setCentralWidget(self.tab_widget)
        self.setStyleSheet(open(BARAKA_STYLESHEETS_PATH + "/brkStyle.css").read())


    def _init_menus(self):
        # UI Elements creation
        self.menu_bar = self.menuBar()
        self.menu_edit = self.menu_bar.addMenu("Edit")

        self.action_edit_root_path = QAction("Edit Root Path...")
        self.menu_edit.addAction(self.action_edit_root_path)

        self.action_edit_root_path.triggered.connect(self.open_set_root_path_popup)


    def _init_tab_widget(self):
        # Ui Element creation
        self.tab_widget = QTabWidget()

        # Connect SIGNAL to SLOT
        self.tab_widget.currentChanged.connect(self.set_widget_size)


    def _init_manager(self):
        self.tab_manager = Manager()
        self.tab_widget.addTab(self.tab_manager, "Manager")


    def _init_publisher(self):
    	self.tab_publisher = Publisher()
    	self.tab_widget.addTab(self.tab_publisher, "Publisher")


    def resize_window(self, width, height):
        self.animation = QPropertyAnimation(self, b"size")
        self.animation.setDuration(100)
        self.animation.setEndValue(QtCore.QSize(width, height))
        self.animation.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.animation.start()


    def set_widget_size(self):
        current_index = int( self.tab_widget.currentIndex() )
        
        if current_index == 0:

            self.resize_window(self.width_manager, self.height_manager)

        if current_index == 1:

            self.resize_window(self.width_publisher, self.height_publisher)


    def open_set_root_path_popup(self):
        self.popup = PopupSetRootPath("Enter your project path...", "Set")
        self.popup.btn_set.clicked.connect(self.set_root_path)
        self.popup.btn_cancel.clicked.connect(self.popup.close_popup)
        self.popup.open()


    def set_root_path(self):
        from configparser import ConfigParser
        from maya.cmds import inViewMessage
        from modules.path import Path

        PIPELINE_ROOT_PATH = Path.convert_backslash_to_slash( self.popup.line_root_path.text() )

        # Set config file to new path
        config = ConfigParser()
        config.read(BARAKA_CONFIG_PATH)
        config.set("PATH", "root", PIPELINE_ROOT_PATH)
        with open(BARAKA_CONFIG_PATH, "wb") as cf:
            config.write(cf)
        
        # Update all pipeline paths
        PIPELINE_ASSET_PATH = PIPELINE_ROOT_PATH + "/04_asset"
        PIPELINE_CHARACTERS = PIPELINE_ASSET_PATH + "/character"
        PIPELINE_PROPS = PIPELINE_ASSET_PATH + "/prop"
        PIPELINE_SETS = PIPELINE_ASSET_PATH + "/set"
        PIPELINE_SHOT_PATH = PIPELINE_ROOT_PATH + "/05_shot"

        inViewMessage(amg='Root Path set to: \n <hl>' + PIPELINE_ASSET_PATH + '</hl>', pos='topCenter', fade=True)

        self.tab_manager.populate_tree()
        self.popup.close_popup()


    def open(self):

        self.show()


    def closeEvent(self, event):
        self.tab_manager.line_asset_creation.clear()
        event.accept()


class PopupSetRootPath(QDialog, Pipeline):

    def __init__(self, placeholder, button):
        QDialog.__init__(self, parent = get_maya_main_window())

        self.setWindowTitle("Pipeline - Set Root Path")
        self.setWindowIcon(QIcon(BARAKA_ICONS_PATH + "/coca.png"))
        self.setMinimumSize(300, 75)

        # UI elements creation and settings

        self.line_root_path = QLineEdit(PIPELINE_ROOT_PATH)
        self.line_root_path.setPlaceholderText(placeholder)

        self.btn_set = QPushButton(button)
        self.btn_cancel = QPushButton("Cancel")

        # Layout Management

        self.lay_main = QVBoxLayout()
        self.lay_buttons = QHBoxLayout()

        self.lay_main.addWidget(self.line_root_path)
        self.lay_buttons.addWidget(self.btn_set)
        self.lay_buttons.addWidget(self.btn_cancel)

        self.lay_main.layout().addLayout(self.lay_buttons)
        self.setLayout(self.lay_main)


    def open(self):
        self.show()


    def close_popup(self):
        self.line_root_path.clear()
        self.close()
        