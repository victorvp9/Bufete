# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_training.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from db.tables import Training
import db.dao_training as dao_training


class UiAddTraining(object):
    def setup_ui(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(361, 135)
        self.dialog = Dialog
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 100, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
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
        self.buttonBox.accepted.connect(self.ok_clicked)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def ok_clicked(self):
        new_training = Training(self.name_ledit.text(), int(self.number_of_hits_ledit.text()), [], True)
        dao_training.add_training(new_training)

        return self.dialog.accept()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Adicionar Treinamento"))
        self.name_label.setText(_translate("Dialog", "Nome:"))
        self.number_of_hits_label.setText(_translate("Dialog", "Número de Golpes:"))
