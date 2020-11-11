# coding:utf-8

"""
"""
import sys
import launcher
import ui.autorigs as autorigs
import ui.pipeline as pipeline
import ui.widgets.manager as manager
import ui.widgets.publisher as publisher
import ui.maya_win as mayawin
import modules.path
import modules.directory
import modules.file
import modules.selection
import modules.scene
import constants
from PySide2.QtWidgets import QApplication

def loadModules():
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

if __name__ == "__main__":

    loadModules()

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

