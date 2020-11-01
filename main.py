# coding:utf-8

"""
"""
import sys
import launcher
import ui.autorigs as autorigs
import ui.pipeline as pipeline
import ui.widgets.manager as manager
import ui.widgets.publisher as publisher
import modules.path
import modules.directory
import modules.file
import modules.selection
import modules.scene
import constants
from PySide2.QtWidgets import QApplication


reload(launcher)
reload(constants)
reload(autorigs)
reload(pipeline)
reload(manager)
reload(publisher)
reload(modules.path)
reload(modules.directory)
reload(modules.file)
reload(modules.path)
reload(modules.scene)


if __name__ == "__main__":

    global mainWidget

    try:
        mainWidget.close()
    except:
        pass

    try:
        mainApp = QApplication(sys.argv)
    except:
        mainApp = QApplication.instance()

    mainWidget = launcher.Launcher()
    mainWidget.show()
    mainApp.exec_()
