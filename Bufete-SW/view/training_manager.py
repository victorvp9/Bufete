# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'training_manager.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from view.add_training import UiAddTraining
from view.edit_training import UiEditTraining
import db.dao_training as dao_training
# from view.edit_training import UiEditTraining
#import view.main_window as main_window
#from view.main_window import Ui_MainWindow as main_window

class UiTrainingManager(object):
    def setup_ui(self, Dialog):
        self.TRAINING_GLOBAL = list()
        self.TRAINING_GLOBAL_NAME = ""
        Dialog.setObjectName("Dialog")
        Dialog.resize(462, 478)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 430, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 231, 401))
        self.listWidget.setObjectName("listWidget")
        self.add_btn = QtWidgets.QPushButton(Dialog)
        self.add_btn.setGeometry(QtCore.QRect(320, 70, 75, 23))
        self.add_btn.setObjectName("add_btn")
        self.delete_btn = QtWidgets.QPushButton(Dialog)
        self.delete_btn.setGeometry(QtCore.QRect(320, 110, 75, 23))
        self.delete_btn.setObjectName("delete_btn")
        self.edit_btn = QtWidgets.QPushButton(Dialog)
        self.edit_btn.setGeometry(QtCore.QRect(320, 150, 75, 23))
        self.edit_btn.setObjectName("edit_btn")
        # self.cpf_info_label = QtWidgets.QLabel(Dialog)
        # self.cpf_info_label.setGeometry(QtCore.QRect(260, 230, 31, 16))
        # self.cpf_info_label.setObjectName("cpf_info_label")
        # self.sex_info_label = QtWidgets.QLabel(Dialog)
        # self.sex_info_label.setGeometry(QtCore.QRect(260, 260, 31, 16))
        # self.sex_info_label.setObjectName("sex_info_label")
        # self.weigt_info_label = QtWidgets.QLabel(Dialog)
        # self.weigt_info_label.setGeometry(QtCore.QRect(260, 290, 31, 16))
        # self.weigt_info_label.setObjectName("weigt_info_label")
        # self.height_info_label = QtWidgets.QLabel(Dialog)
        # self.height_info_label.setGeometry(QtCore.QRect(260, 320, 41, 16))
        # self.height_info_label.setObjectName("height_info_label")
        # self.pick_btn = QtWidgets.QPushButton(Dialog)
        # self.pick_btn.setGeometry(QtCore.QRect(320, 30, 75, 23))
        # self.pick_btn.setObjectName("pick_btn")
        # self.weigt_info_label_2 = QtWidgets.QLabel(Dialog)
        # self.weigt_info_label_2.setGeometry(QtCore.QRect(300, 290, 191, 16))
        # self.weigt_info_label_2.setText("")
        # self.weigt_info_label_2.setObjectName("weigt_info_label_2")
        # self.sex_info_label_2 = QtWidgets.QLabel(Dialog)
        # self.sex_info_label_2.setGeometry(QtCore.QRect(300, 260, 191, 16))
        # self.sex_info_label_2.setText("")
        # self.sex_info_label_2.setObjectName("sex_info_label_2")
        # self.cpf_info_label_2 = QtWidgets.QLabel(Dialog)
        # self.cpf_info_label_2.setGeometry(QtCore.QRect(300, 230, 191, 16))
        # self.cpf_info_label_2.setText("")
        # self.cpf_info_label_2.setObjectName("cpf_info_label_2")
        # self.height_info_label_2 = QtWidgets.QLabel(Dialog)
        # self.height_info_label_2.setGeometry(QtCore.QRect(300, 320, 191, 16))
        # self.height_info_label_2.setText("")
        # self.height_info_label_2.setObjectName("height_info_label_2")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/icons/add-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_btn.setIcon(icon)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/icons/edit-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_btn.setIcon(icon)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/icons/delete-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_btn.setIcon(icon)
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("./resources/icons/pick-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.pick_btn.setIcon(icon)

        self.add_btn.clicked.connect(self.add_new_training)
        self.delete_btn.clicked.connect(self.delete_training)
        # self.listWidget.itemSelectionChanged.connect(self.fill_the_fields)
        # self.pick_btn.clicked.connect(self.pick_training)
        self.edit_btn.clicked.connect(self.edit_training)

        self.populate_training_list()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # def pick_training(self):
    #     self.msg = QMessageBox()
    #     # It verifies if an item is selected before trying to delete
    #     if self.listWidget.currentItem() is not None:
    #         index = self.listWidget.currentRow()
    #         training = dao_training.recover_test_case(index)
    #         self.TRAINING_GLOBAL_NAME = training.name
    #         self.TRAINING_GLOBAL.append(training.name)
    #         self.TRAINING_GLOBAL.append(training.number_of_hits)
    #         self.TRAINING_GLOBAL.append(training.sequence)
    #         self.TRAINING_GLOBAL.append(training.is_random)
    #         print(training)
    #     else:
    #         # Else show message to select a item to delete
    #         button_reply = QMessageBox.information(self.msg, "Escolher treinamento",
    #                                                "Selecione algum treinamento.",
    #                                                QMessageBox.Ok, QMessageBox.Ok)

    def add_new_training(self):
        self.dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint)
        self.ui_add_training = UiAddTraining()
        self.ui_add_training.setup_ui(self.dialog)
        self.dialog.exec_()
        self.populate_training_list()

    def edit_training(self):
        self.msg = QMessageBox()
        # It verifies if an item is selected before trying to delete
        if self.listWidget.currentItem() is not None:
            index = self.listWidget.currentRow()
            training = dao_training.recover_test_case(index)
            self.dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint)
            self.ui_edit_training = UiEditTraining()
            self.ui_edit_training.setup_ui(self.dialog, index)
            self.dialog.exec_()
            self.populate_training_list()
        else:
            # Else show message to select a item to delete
            button_reply = QMessageBox.information(self.msg, "Escolher treinamento",
                                                   "Selecione algum treinamento.",
                                                   QMessageBox.Ok, QMessageBox.Ok)
        '''
        self.dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint)
        self.ui_edit_training = UiEditTraining()
        self.ui_edit_training.setup_ui(self.dialog)
        self.dialog.exec_()
        self.populate_training_list()
        '''
    def delete_training(self):
        self.msg = QMessageBox()
        # It verifies if an item is selected before trying to delete
        if self.listWidget.currentItem() is not None:
            # Show confirmation message if user really wants to delete a selected item
            button_reply = QMessageBox.critical(self.msg, "Apagar treinamento",
                                                "Tem certeza?",
                                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if button_reply == QMessageBox.Yes:
                # If user is sure of this, recover id from list and
                # search id in the database and so delete the test suite
                index = self.listWidget.currentRow()
                if dao_training.recover_test_case(index).name == self.TRAINING_GLOBAL_NAME:
                    self.TRAINING_GLOBAL.clear()
                dao_training.delete_training_by_id(index)
                self.populate_training_list()

            else:
                print('No clicked.')
        else:
            # Else show message to select a item to delete
            button_reply = QMessageBox.information(self.msg, "Apagar treinamento",
                                                   "Selecione antes de querer apagar.",
                                                   QMessageBox.Ok, QMessageBox.Ok)

    # def fill_the_fields(self):
    #     try:
    #         index = self.listWidget.currentRow()
    #         if index is not None:
    #             training = dao_training.recover_test_case(index)
    #             if training is not None:
    #                 self.cpf_info_label_2.setText(str(training.cpf))
    #                 self.sex_info_label_2.setText(training.sex)
    #                 self.height_info_label_2.setText(str(training.height))
    #                 self.weigt_info_label_2.setText(str(training.weight))
    #     except Exception as e:
    #         print(str(e))

    def populate_training_list(self):
        self.listWidget.clear()

        training_list = dao_training.list_training()
        count = 0
        if training_list is None:
            pass
        else:
            for training in training_list:
                name_sport = str(training.name)
                self.listWidget.insertItem(count, name_sport)
                count += 1

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Gerenciar treinamento"))
        # self.cpf_info_label.setText(_translate("Dialog", "CPF:"))
        # self.sex_info_label.setText(_translate("Dialog", "Sexo:"))
        # self.weigt_info_label.setText(_translate("Dialog", "Peso:"))
        # self.height_info_label.setText(_translate("Dialog", "Altura:"))
        #self.pick_btn.setText(_translate("Dialog", "Escolher"))

