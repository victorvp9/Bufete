# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_athlete.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from db.tables import Athlete
import db.dao_athlete as dao_athlete
import re

class UiAddAthlete(object):
    def setup_ui(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(469, 264)
        self.dialog = Dialog
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 220, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.name_label = QtWidgets.QLabel(Dialog)
        self.name_label.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.name_label.setObjectName("name_label")
        self.cpf_label = QtWidgets.QLabel(Dialog)
        self.cpf_label.setGeometry(QtCore.QRect(20, 60, 101, 16))
        self.cpf_label.setObjectName("cpf_label")
        self.sex_label = QtWidgets.QLabel(Dialog)
        self.sex_label.setGeometry(QtCore.QRect(20, 90, 101, 16))
        self.sex_label.setObjectName("sex_label")
        self.borndt_label = QtWidgets.QLabel(Dialog)
        self.borndt_label.setGeometry(QtCore.QRect(20, 120, 111, 16))
        self.borndt_label.setObjectName("borndt_label")
        self.age_label = QtWidgets.QLabel(Dialog)
        self.age_label.setGeometry(QtCore.QRect(290, 120, 41, 16))
        self.age_label.setObjectName("age_label")
        self.weight_label = QtWidgets.QLabel(Dialog)
        self.weight_label.setGeometry(QtCore.QRect(20, 150, 111, 16))
        self.weight_label.setObjectName("weight_label")
        self.height_label = QtWidgets.QLabel(Dialog)
        self.height_label.setGeometry(QtCore.QRect(290, 150, 41, 16))
        self.height_label.setObjectName("height_label")
        self.name_ledit = QtWidgets.QLineEdit(Dialog)
        self.name_ledit.setGeometry(QtCore.QRect(130, 30, 221, 20))
        self.name_ledit.setObjectName("name_ledit")
        self.cpf_ledit = QtWidgets.QLineEdit(Dialog)
        self.cpf_ledit.setGeometry(QtCore.QRect(130, 60, 121, 20))
        self.cpf_ledit.setObjectName("cpf_ledit")
        #self.cpf_regex = QtCore.QRegExp("^([ddddddddddd])$")
        #self.cpf_valid = QtGui.QRegExpValidator(self.cpf_regex)
        #self.cpf_ledit.setValidator(self.cpf_valid)

        self.borndt_ledit = QtWidgets.QLineEdit(Dialog)
        self.borndt_ledit.setGeometry(QtCore.QRect(130, 120, 91, 20))
        self.borndt_ledit.setObjectName("borndt_ledit")
        # self.borndt_ledit.setText("DD/MM/AAAA")
        #self.borndt_regex = QtCore.QRegExp("")

        self.age_ledit = QtWidgets.QLineEdit(Dialog)
        self.age_ledit.setGeometry(QtCore.QRect(330, 120, 91, 20))
        self.age_ledit.setObjectName("age_ledit")

        self.weight_ledit = QtWidgets.QLineEdit(Dialog)
        self.weight_ledit.setGeometry(QtCore.QRect(130, 150, 91, 20))
        self.weight_ledit.setObjectName("weight_ledit")
        self.weight_regex = QtCore.QRegExp("^([3-9][0-9]|[12][0-9][0-9])$")
        self.weight_valid = QtGui.QRegExpValidator(self.weight_regex)
        self.weight_ledit.setValidator(self.weight_valid)

        self.height_ledit = QtWidgets.QLineEdit(Dialog)
        self.height_ledit.setGeometry(QtCore.QRect(330, 150, 91, 20))
        self.height_ledit.setObjectName("height_ledit")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(130, 90, 31, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        # self.borndt_calendar_btn = QtWidgets.QPushButton(Dialog)
        # self.borndt_calendar_btn.setGeometry(QtCore.QRect(230, 120, 31, 23))
        # self.borndt_calendar_btn.setText("")
        # self.borndt_calendar_btn.setObjectName("borndt_calendar_btn")
        self.sport_label = QtWidgets.QLabel(Dialog)
        self.sport_label.setGeometry(QtCore.QRect(20, 180, 111, 16))
        self.sport_label.setObjectName("sport_label")
        self.sport_cbox = QtWidgets.QComboBox(Dialog)
        self.sport_cbox.setGeometry(QtCore.QRect(130, 180, 91, 22))
        self.sport_cbox.setObjectName("sport_cbox")
        self.sport_cbox.addItem("")
        self.sport_cbox.addItem("")
        self.sport_cbox.addItem("")

        self.date_rx = QtCore.QRegExp("^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$")
        self.date_validator = QtGui.QRegExpValidator(self.date_rx)

        self.borndt_ledit.setValidator(self.date_validator)


        self.retranslateUi(Dialog)
        #self.weight_ledit.textChanged.connect(self.check_state)
        self.buttonBox.accepted.connect(self.ok_clicked)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def check_state(self):
        send = self.sender()
        valid = send.validator()
        state = valid.validate(send.text(), 0)[0]
        if state == QtGui.QValidator.Acceptable:
            color = '#c4df9b'  # green
        elif state == QtGui.QValidator.Intermediate:
            color = '#fff79a'  # yellow
        else:
            color = '#f6989d'  # red
        send.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def ok_clicked(self):



        new_athlete = Athlete(self.name_ledit.text(), self.cpf_ledit.text(), self.comboBox.currentText(),
                              self.borndt_ledit.text(), int(self.age_ledit.text()), float(self.height_ledit.text()),
                              float(self.weight_ledit.text()), self.sport_cbox.currentText())
        dao_athlete.add_athlete(new_athlete)
        return self.dialog.accept()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Novo Atleta"))
        self.name_label.setText(_translate("Dialog", "Nome Completo:"))
        self.cpf_label.setText(_translate("Dialog", "CPF:"))
        self.sex_label.setText(_translate("Dialog", "Sexo:"))
        self.borndt_label.setText(_translate("Dialog", "Data de Nascimento:"))
        self.age_label.setText(_translate("Dialog", "Idade: "))
        self.weight_label.setText(_translate("Dialog", "Peso:"))
        self.height_label.setText(_translate("Dialog", "Altura:"))
        self.comboBox.setItemText(0, _translate("Dialog", "M"))
        self.comboBox.setItemText(1, _translate("Dialog", "F"))
        self.sport_label.setText(_translate("Dialog", "Esporte:"))
        self.sport_cbox.setItemText(0, _translate("Dialog", "Karatê"))
        self.sport_cbox.setItemText(1, _translate("Dialog", "Taekwondo"))
        self.sport_cbox.setItemText(2, _translate("Dialog", "Muay Thai"))



