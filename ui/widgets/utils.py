# coding:utf-8

from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
import modules.matrix_api as mtx

class Utils(QWidget):

	def __init__(self):
		QWidget.__init__(self)

		self.lay_main = QVBoxLayout()
		self.setLayout(self.lay_main)
		self.lay_mtx_constraint = QVBoxLayout()

		self.group_mtx_constraint = QGroupBox("Matrix Constraint")
		self.group_mtx_constraint.setLayout(self.lay_mtx_constraint)

		self.btn_mtx_constraint = QPushButton("Matrix Constraint")

		self.radio_parent = QRadioButton("Parent")
		self.radio_point = QRadioButton("Point")
		self.radio_orient = QRadioButton("Orient")
		self.radio_scale = QRadioButton("Scale")

		self.check_offset = QCheckBox("Maintain Offset")


		# self.btn_mtx_constraint.clicked.connect()

		self.lay_main.addWidget(self.group_mtx_constraint)

		self.lay_mtx_constraint.addWidget(self.radio_parent)
		self.lay_mtx_constraint.addWidget(self.radio_point)
		self.lay_mtx_constraint.addWidget(self.radio_orient)
		self.lay_mtx_constraint.addWidget(self.radio_scale)
		self.lay_mtx_constraint.addWidget(self.check_offset)
		self.lay_mtx_constraint.addWidget(self.btn_mtx_constraint)

	# method for matrix constraint





