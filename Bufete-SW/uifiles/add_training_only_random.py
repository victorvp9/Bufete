# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_training_only_random.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(361, 135)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 100, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.name_label = QtWidgets.QLabel(Dialog)
        self.name_label.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.name_label.setObjectName("name_label")
        self.name_ledit = QtWidgets.QLineEdit(Dialog)
        self.name_ledit.setGeometry(QtCore.QRect(120, 30, 221, 20))
        self.name_ledit.setObjectName("name_ledit")
        self.number_of_hits_ledit = QtWidgets.QLineEdit(Dialog)
        self.number_of_hits_ledit.setGeometry(QtCore.QRect(120, 70, 41, 20))
        self.number_of_hits_ledit.setObjectName("number_of_hits_ledit")
        self.number_of_hits_label = QtWidgets.QLabel(Dialog)
        self.number_of_hits_label.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.number_of_hits_label.setObjectName("number_of_hits_label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Adicionar Treinamento"))
        self.name_label.setText(_translate("Dialog", "Nome:"))
        self.number_of_hits_label.setText(_translate("Dialog", "Número de Golpes:"))

