# coding:utf-8

"""
"""
import sys
import launcher
import dialogs.autorigDialog as autorigDialog
import dialogs.pipelineDialog as pipelineDialog
# import modules.path as Path
# import modules.file as File
# import modules.directory as Dir
# import modules.scene as Scene
import constants
from PySide2.QtWidgets import QApplication


reload(launcher)
reload(constants)
reload(autorigDialog)
reload(pipelineDialog)

# reload(Path)
# reload(File)
# reload(Dir)
# reload(Scene)


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
