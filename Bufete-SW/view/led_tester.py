# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'led_tester.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from view.image_widget import ImgWidget1
from model.commands_bufete import CommandsBufete
from model.serial_bufete import handler_sing


class UiLedTester(object):
    def setup_ui(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(231, 132)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-120, 80, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.to_test_id_label = QtWidgets.QLabel(Dialog)
        self.to_test_id_label.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.to_test_id_label.setObjectName("to_test_id_label")
        self.to_test_id_ledit = QtWidgets.QLineEdit(Dialog)
        self.to_test_id_ledit.setGeometry(QtCore.QRect(120, 40, 31, 20))
        self.to_test_id_ledit.setObjectName("to_test_id_ledit")

        # Led Status image
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(180, 30, 30, 30))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.iefes_logo_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.iefes_logo_layout.setContentsMargins(0, 0, 0, 0)
        self.iefes_logo_layout.setObjectName("iefes_logo_layout")

        self.iefes_logo = ImgWidget1("./resources/icons/test.png")
        self.iefes_logo_layout.addWidget(self.iefes_logo)
        self.iefes_logo.resize(30, 30)

        self.cmd = CommandsBufete()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.test_led)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def test_led(self):
        if handler_sing.is_already_connected():
            led_id = int(self.to_test_id_ledit.text())-1
            res = self.cmd.test_led(led_id)
            print(res)
        else:
            print('Conecte o dispositivo.')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.to_test_id_label.setText(_translate("Dialog", "LED ID a ser testado:"))


