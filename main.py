# coding:utf-8

"""
"""
import launcher
import ui.autorigs as autorigs
import ui.pipeline as pipeline
import ui.widgets.manager as manager
import ui.widgets.publisher as publisher
import ui.widgets.utils as utils
import ui.mayaWin as mayaWin
import modules.path as path
import modules.directory as directory
import modules.file as file
import modules.selection as selection
import modules.scene as scene
import modules.matrix_api as matrix_api
import modules.commit as commit
import constants
from PySide2.QtWidgets import QApplication

def load_modules():
    reload(launcher)
    reload(constants)
    reload(autorigs)
    reload(pipeline)
    reload(manager)
    reload(publisher)
    reload(mayaWin)
    reload(path)
    reload(directory)
    reload(file)
    reload(path)
    reload(scene)
    reload(matrix_api)
    reload(commit)


def start():
    load_modules()

    global main_widget

    try:
        main_widget.close()                 # if widget already exists, then close and delete it
    except:
        pass

    try:                                    # if QApplication singleton already exists,
        app = QApplication([])              # then create one instance of it                      
    except:
        app = QApplication.instance()

    main_widget = launcher.Launcher()
    main_widget.show(dockable=True, area="right")
    app.exec_()


