import sys
from PySide2 import QtCore, QtWidgets

class monDialog(QtWidgets.QDialog):
	def __init__(self, parent = None):
		super(monDialog, self).__init__(parent)
		data = ["square", "rectangle",
		"cube", "parallelepiped"]
		self.setWindowTitle("exemple de dialogue")
		#self.setFixedSize(300, 100)
		listWidget = QtWidgets.QListWidget(self)
		listWidget.addItems(data)


			
app = QtWidgets.QApplication.instance()
d = monDialog()
d.show()
app.exec_()