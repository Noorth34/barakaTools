# coding:utf-8

"""
"""
import sys
import launcher
import ui.autorigs as autorigs
import ui.pipeline as pipeline
import ui.widgets.manager as manager
import ui.widgets.publisher as publisher
import ui.widgets.utils as utils
import ui.maya_win as mayawin
import modules.path
import modules.directory
import modules.file
import modules.selection
import modules.scene
import modules.matrix_api
import modules.commit
import constants
from PySide2.QtWidgets import QApplication

def load_modules():
    reload(launcher)
    reload(constants)
    reload(autorigs)
    reload(pipeline)
    reload(manager)
    reload(publisher)
    reload(mayawin)
    reload(modules.path)
    reload(modules.directory)
    reload(modules.file)
    reload(modules.path)
    reload(modules.scene)
    reload(modules.matrix_api)
    reload(modules.commit)

if __name__ == "__main__":

    load_modules()

    global main_widget

    try:
        main_widget.close()
    except:
        pass

    try:
        app = QApplication([])
    except:
        app = QApplication.instance()

    main_widget = launcher.Launcher()
    main_widget.show(dockable=True, area="right")
    app.exec_()

