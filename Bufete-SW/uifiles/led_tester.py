# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'led_tester.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
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

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.to_test_id_label.setText(_translate("Dialog", "LED ID a ser testado:"))


