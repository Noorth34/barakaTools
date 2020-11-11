# coding:utf-8

from PySide2.QtWidgets import QMainWindow
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance

def get_maya_main_window():
    omui.MQtUtil.mainWindow()
    ptr = omui.MQtUtil.mainWindow()
    main_win = wrapInstance(long(ptr), QMainWindow)
    return main_win