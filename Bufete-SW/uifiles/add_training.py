# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_training.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(460, 264)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 220, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.name_label = QtWidgets.QLabel(Dialog)
        self.name_label.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.name_label.setObjectName("name_label")
        self.name_ledit = QtWidgets.QLineEdit(Dialog)
        self.name_ledit.setGeometry(QtCore.QRect(180, 30, 221, 20))
        self.name_ledit.setObjectName("name_ledit")
        self.is_random_check_box = QtWidgets.QCheckBox(Dialog)
        self.is_random_check_box.setGeometry(QtCore.QRect(20, 110, 101, 17))
        self.is_random_check_box.setChecked(False)
        self.is_random_check_box.setObjectName("is_random_check_box")
        self.number_of_hits_ledit = QtWidgets.QLineEdit(Dialog)
        self.number_of_hits_ledit.setGeometry(QtCore.QRect(180, 70, 41, 20))
        self.number_of_hits_ledit.setObjectName("number_of_hits_ledit")
        self.number_of_hits_label = QtWidgets.QLabel(Dialog)
        self.number_of_hits_label.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.number_of_hits_label.setObjectName("number_of_hits_label")
        self.sequence_label = QtWidgets.QLabel(Dialog)
        self.sequence_label.setGeometry(QtCore.QRect(20, 150, 151, 16))
        self.sequence_label.setObjectName("sequence_label")
        self.to_add_led_id_ledit = QtWidgets.QLineEdit(Dialog)
        self.to_add_led_id_ledit.setEnabled(True)
        self.to_add_led_id_ledit.setGeometry(QtCore.QRect(180, 150, 41, 20))
        self.to_add_led_id_ledit.setObjectName("to_add_led_id_ledit")
        self.to_add_led_id_btn = QtWidgets.QPushButton(Dialog)
        self.to_add_led_id_btn.setEnabled(True)
        self.to_add_led_id_btn.setGeometry(QtCore.QRect(230, 150, 75, 23))
        self.to_add_led_id_btn.setObjectName("to_add_led_id_btn")
        self.chosen_sequence_label = QtWidgets.QLabel(Dialog)
        self.chosen_sequence_label.setGeometry(QtCore.QRect(20, 190, 51, 16))
        self.chosen_sequence_label.setObjectName("chosen_sequence_label")
        self.sequence_list_label = QtWidgets.QLabel(Dialog)
        self.sequence_list_label.setGeometry(QtCore.QRect(80, 190, 361, 16))
        self.sequence_list_label.setText("")
        self.sequence_list_label.setObjectName("sequence_list_label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.name_label.setText(_translate("Dialog", "Nome:"))
        self.is_random_check_box.setText(_translate("Dialog", "Ordem Aleatória"))
        self.number_of_hits_label.setText(_translate("Dialog", "Número de Golpes:"))
        self.sequence_label.setText(_translate("Dialog", "Adicionar à sequência (LED ID):"))
        self.to_add_led_id_btn.setText(_translate("Dialog", "Adicionar"))
        self.chosen_sequence_label.setText(_translate("Dialog", "Sequência:"))


