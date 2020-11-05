# coding:utf-8

from PySide2.QtWidgets import QMainWindow
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance

def getMayaMainWindow():
    omui.MQtUtil.mainWindow()
    ptr = omui.MQtUtil.mainWindow()
    mainWin = wrapInstance(long(ptr), QMainWindow)
    return mainWin