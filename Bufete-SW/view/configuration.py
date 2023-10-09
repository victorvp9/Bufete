# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configuration.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time
from model.serial_bufete import handler_sing
from model.commands_bufete import CommandsBufete

class UiConfiguration(object):
    def setup_ui(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(183, 134)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-170, 80, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 47, 13))
        self.label.setObjectName("label")
        self.port_cbox = QtWidgets.QComboBox(Dialog)
        self.port_cbox.setGeometry(QtCore.QRect(70, 30, 81, 22))
        self.port_cbox.setObjectName("port_cbox")
        self.dialog = Dialog

        self.cmd = CommandsBufete()

        self.available_ports()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.ok_clicked)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def available_ports(self):
        self.port_cbox.clear()
        for i in handler_sing.list_available_ports():
            self.port_cbox.addItem(i)

    def ok_clicked(self):
        try:
            if not handler_sing.is_already_connected():
                handler_sing.disconnect()
                handler_sing.connect(self.port_cbox.currentText())
                res = self.cmd.connect()
                print(res)
                return self.dialog.accept()
            else:
                print('Já está conectado.')
        except Exception as e:
            print(e)

    # def ok_clicked(self):
    #     try:
    #         '''print(self.port_cbox.currentText())
    #         handler_sing.connect(self.port_cbox.currentText())
    #         if handler_sing.receive() == [b'x']:
    #             handler_sing.write('x')
    #             return self.dialog.accept()
    #         else:
    #             msg_box = QtWidgets.QMessageBox()
    #             msg_box.setWindowTitle("Erro")
    #             msg_box.setText("Por favor, verifique o dispositivo ou porta escolhida")
    #             msg_box.exec()'''
    #         print(self.port_cbox.currentText())
    #         count = 0
    #         handler_sing.connect(self.port_cbox.currentText())
    #         while handler_sing.receive() != [b'x']:
    #             time.sleep(1)
    #             count = count + 1
    #             if count == 4:
    #                 msg_box = QtWidgets.QMessageBox()
    #                 msg_box.setWindowTitle("Erro")
    #                 msg_box.setText("Por favor, verifique o dispositivo ou porta escolhida")
    #                 msg_box.exec()
    #                 return msg_box.reject()
    #         handler_sing.write([b'x'])
    #         return self.dialog.accept()
    #     except OSError as e:
    #         msg_box = QtWidgets.QMessageBox()
    #         msg_box.setWindowTitle("Erro")
    #         msg_box.setText("Não há comunicação com o Receptec nesta porta! Por favor, escolha outra porta.")
    #         msg_box.exec()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Configuração"))
        self.label.setText(_translate("Dialog", "Porta:"))
