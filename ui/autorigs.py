# coding:utf-8

from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
import constants as const
import ui.maya_win as mayawin
from ui.widgets.utils import Utils


class Autorigs(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self, parent=mayawin.get_maya_main_window())

        self.width = 225
        self.height = 225

        self.setWindowTitle("Autorigs")
        self.setWindowIcon(QIcon(const.BARAKA_ICONS_PATH + "/burger.png"))
        self.setGeometry(800, 500, 0, 0)
        self.setFixedSize(self.width, self.height)

        self.init_tabs()
        self.init_limb_with_ribbon()
        self.init_utils()

        self.setCentralWidget(self.tab_widget)

    def init_tabs(self):

        self.tab_widget = QTabWidget()

        self.tab_limb = QWidget()
        self.tab_eyes = QWidget()
        self.tab_utils = QWidget()

        self.tab_widget.addTab(self.tab_limb, "Limb")
        self.tab_widget.addTab(self.tab_eyes, "Eyes")
        self.tab_widget.addTab(self.tab_utils, "Utils")

    def init_utils(self):

        self.utils = Utils()

        self.lay_utils = QVBoxLayout()
        self.tab_utils.setLayout(self.lay_utils)
        self.lay_utils.addWidget(self.utils)

    def init_limb_with_ribbon(self):

        # Create UI Elements

        self.widget_limb_ribbon = QWidget()
        self.lay_limb_ribbon = QVBoxLayout(self.widget_limb_ribbon)

        self.lay_limb = QVBoxLayout()
        self.tab_limb.setLayout(self.lay_limb)

        self.lay_driver_joints = QHBoxLayout()
        self.lay_bind_joints = QHBoxLayout()
        self.lay_rig_features = QGridLayout()

        self.list_rig_method = QComboBox()
        self.list_rig_method.addItem("Ribbon")
        self.list_rig_method.addItem("Spline")
        self.list_rig_method.currentTextChanged.connect(self.toggle_widget_limb_ribbon)

        self.btn_create_with_ribbon = QPushButton("Create with Ribbon")

        self.label_driver_joints = QLabel("Driver Joints")
        self.label_bind_joints = QLabel("Bind Joints")
        self.spin_driver_joints = QSpinBox()
        self.spin_bind_joints = QSpinBox()

        self.check_has_twist = QCheckBox("Twist")
        self.check_has_bend = QCheckBox("Bend")
        self.check_has_stretch = QCheckBox("Stretch")
        self.check_has_keep_volume = QCheckBox("Keep Volume")
        self.check_has_IK = QCheckBox("IK")
        self.check_has_FK = QCheckBox("FK")

        # Layout management

        self.lay_limb.addWidget(self.list_rig_method)
        self.lay_limb.addWidget(self.widget_limb_ribbon)

        self.lay_limb_ribbon.layout().addLayout(self.lay_driver_joints)
        self.lay_limb_ribbon.layout().addLayout(self.lay_bind_joints)
        self.lay_limb_ribbon.layout().addLayout(self.lay_rig_features)
        self.lay_limb_ribbon.addWidget(self.btn_create_with_ribbon)

        self.lay_driver_joints.addWidget(self.label_driver_joints)
        self.lay_driver_joints.addWidget(self.spin_driver_joints)

        self.lay_bind_joints.addWidget(self.label_bind_joints)
        self.lay_bind_joints.addWidget(self.spin_bind_joints)

        self.lay_rig_features.addWidget(self.check_has_stretch, 0, 1)
        self.lay_rig_features.addWidget(self.check_has_bend, 1, 1)
        self.lay_rig_features.addWidget(self.check_has_keep_volume, 2, 1)
        self.lay_rig_features.addWidget(self.check_has_twist, 0, 2)
        self.lay_rig_features.addWidget(self.check_has_FK, 1, 2)
        self.lay_rig_features.addWidget(self.check_has_IK, 2, 2)

    def toggle_widget_limb_ribbon(self):

        method = self.list_rig_method.currentText()

        if method == "Spline":
            self.widget_limb_ribbon.hide()
        else:
            self.widget_limb_ribbon.show()

    def open(self):

        self.show()
