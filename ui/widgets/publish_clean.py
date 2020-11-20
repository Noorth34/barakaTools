# coding:utf-8

from PySide2.QtWidgets import *
import constants as const

class PublishChecker(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		self.setWindowTitle("Publish Cleaner")
		self.setMinimumSize(500, 400)

		self.init()
		self.setStyleSheet(open(const.BARAKA_STYLESHEETS_PATH + "/brkStyle.css").read())


	def init(self):

		self.lay_main = QVBoxLayout()

		self.list_errors = QListWidget()
		self.btn_retry = QPushButton("Retry")


		self.setLayout(self.lay_main)

		self.lay_main.addWidget(self.list_errors)
		self.lay_main.addWidget(self.btn_retry)

		
		self.list_errors.setMinimumHeight(300)
		self.btn_retry.setMinimumHeight(25)


if __name__ == '__main__':

	app = QApplication.instance()
	widget = PublishChecker()

	widget.show()
	app.exec_()