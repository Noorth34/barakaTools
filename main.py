# coding:utf-8

"""
"""
import sys
import launcher
import dialogs.autorigDialog as autorigDialog
import dialogs.pipelineDialog as pipelineDialog
import modules.path
import modules.directory
import modules.file
import modules.selection
import modules.scene
import constants
from PySide2.QtWidgets import QApplication


reload(launcher)
reload(constants)
reload(autorigDialog)
reload(pipelineDialog)
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

    mainWidget = launcher.LauncherInstance()
    mainWidget.show()
    mainApp.exec_()
