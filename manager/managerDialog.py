#coding:utf-8

"""
"""

from PySide2 import QtCore, QtWidgets


class BarakaManagerUI():
	"""
	"""
	def __init__(self):
		"""
		"""
		super(monDialog, self).__init__(parent)
		data = ["square", "rectangle",
		"cube", "parallelepiped"]
		self.setWindowTitle("exemple de dialogue")
		#self.setFixedSize(300, 100)
		listWidget = QtWidgets.QListWidget(self)
		listWidget.addItems(data)
		

	def show(self):
		"""
		"""
		app = QtWidgets.QApplication.instance()
		d = monDialog()
		d.show()
		app.exec_()