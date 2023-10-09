# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from view.image_widget import ImgWidget1
from view.athlete_manager import UiAthleteManager
from view.training_manager import UiTrainingManager
from view.configuration import UiConfiguration
from view.led_tester import UiLedTester
from model.training_thread import TrainingThread
import db.dao_training as dao_training

from model.serial_bufete import handler_sing


class Ui_MainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 520)
        MainWindow.setFixedSize(MainWindow.size())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 221, 311))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.train_seq_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.train_seq_layout.setContentsMargins(0, 0, 0, 0)
        self.train_seq_layout.setObjectName("train_seq_layout")
        self.train_seq_list = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.train_seq_list.setObjectName("train_seq_list")
        self.train_seq_layout.addWidget(self.train_seq_list)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(240, 30, 205, 311))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.hit_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.hit_layout.setContentsMargins(0, 0, 0, 0)
        self.hit_layout.setObjectName("hit_layout")
        self.hit_table = QtWidgets.QTableWidget(self.horizontalLayoutWidget_2)
        self.hit_table.setObjectName("hit_table")
        self.hit_table.setColumnCount(2)
        self.hit_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.hit_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.hit_table.setHorizontalHeaderItem(1, item)
        self.hit_layout.addWidget(self.hit_table)
        self.train_seq_list_label = QtWidgets.QLabel(self.centralwidget)
        self.train_seq_list_label.setGeometry(QtCore.QRect(20, 10, 161, 16))
        self.train_seq_list_label.setObjectName("train_seq_list_label")
        self.hit_table_label = QtWidgets.QLabel(self.centralwidget)
        self.hit_table_label.setGeometry(QtCore.QRect(310, 10, 61, 16))
        self.hit_table_label.setObjectName("hit_table_label")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 380, 436, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.info_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.info_layout.setContentsMargins(0, 0, 0, 0)
        self.info_layout.setObjectName("info_layout")
        self.info_list = QtWidgets.QListWidget(self.horizontalLayoutWidget_3)
        self.info_list.setObjectName("info_list")
        item = QtWidgets.QListWidgetItem()
        self.info_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.info_list.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.info_list.addItem(item)
        self.info_layout.addWidget(self.info_list)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 360, 151, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar.addAction(self.menuFile.menuAction())

        # New code here \/
        self.hit_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        # Logo IEFES
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(460, 25, 181, 151))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.iefes_logo_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.iefes_logo_layout.setContentsMargins(0, 0, 0, 0)
        self.iefes_logo_layout.setObjectName("iefes_logo_layout")

        self.iefes_logo = ImgWidget1("./resources/icons/iefes-logo.png")
        self.iefes_logo_layout.addWidget(self.iefes_logo)
        self.iefes_logo.resize(179, 149)

        # Actions
        self.athlete_action = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/icons/athlete_manager.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.athlete_action.setIcon(icon)

        self.play_action = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_action.setIcon(icon)

        self.training_action = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/icons/training.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.training_action.setIcon(icon)

        self.conf_action = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/icons/conf-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.conf_action.setIcon(icon)

        self.led_test_action = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/icons/test_led.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.led_test_action.setIcon(icon)

        self.coletec_connected_action = QtWidgets.QAction(MainWindow)

        self.disconnected_icon = QtGui.QIcon()
        self.disconnected_icon.addPixmap(QtGui.QPixmap("./resources/icons/disconnected.png"), QtGui.QIcon.Normal,
                                         QtGui.QIcon.Off)

        self.connected_icon = QtGui.QIcon()
        self.connected_icon.addPixmap(QtGui.QPixmap("./resources/icons/connected.png"), QtGui.QIcon.Normal,
                                      QtGui.QIcon.Off)

        self.coletec_connected_action.setIcon(self.disconnected_icon)
        self.athlete_action.setDisabled(False)
        self.training_action.setDisabled(False)
        self.play_action.setDisabled(True)

        self.toolBar.addAction(self.athlete_action)
        self.toolBar.addAction(self.training_action)
        self.toolBar.addAction(self.led_test_action)
        self.toolBar.addAction(self.conf_action)
        self.toolBar.addAction(self.play_action)

        spacer = QtWidgets.QWidget()
        spacer.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.toolBar.addWidget(spacer)

        self.toolBar.addAction(self.coletec_connected_action)

        # Tooltips
        self.play_action.setToolTip('Iniciar treinamento.')
        self.training_action.setToolTip('Abrir gerenciador de treinamentos.')
        self.conf_action.setToolTip('Abrir gerenciador de configurações.')
        self.athlete_action.setToolTip('Abrir gerenciador de atletas.')
        self.led_test_action.setToolTip('Testar os LEDs disponíveis no BUFETE.')

        # Connects
        self.athlete_action.triggered.connect(self.open_athlete_manager)
        self.conf_action.triggered.connect(self.configuration)
        self.training_action.triggered.connect(self.open_training_manager)
        self.led_test_action.triggered.connect(self.led_test)
        self.train_seq_list.itemClicked.connect(self.on_click_training)
        self.play_action.triggered.connect(self.run_training)

        self.populate_training_list()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def led_test(self):
        self.dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint)
        self.ui_led_tester = UiLedTester()
        self.ui_led_tester.setup_ui(self.dialog)
        self.dialog.exec_()

    def configuration(self):
        self.dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint)
        self.ui_configuration = UiConfiguration()
        self.ui_configuration.setup_ui(self.dialog)
        self.dialog.exec_()
        if handler_sing.is_already_connected():
            self.coletec_connected_action.setIcon(self.connected_icon)

    def open_athlete_manager(self):
        self.dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint)
        self.ui_athlete_manager = UiAthleteManager()
        self.ui_athlete_manager.setup_ui(self.dialog)
        self.dialog.exec_()
        if not self.ui_athlete_manager.ATHLETE_GLOBAL:
            print("não ha escolha")
        else:
            self.play_action.setDisabled(False)

    def open_training_manager(self):
        self.dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint)
        self.ui_athlete_manager = UiTrainingManager()
        self.ui_athlete_manager.setup_ui(self.dialog)
        self.dialog.exec_()
        self.populate_training_list()
        # if not self.ui_athlete_manager.TRAINING_GLOBAL:
        #     print("não ha escolha")
        # else:
        #     self.play_action.setDisabled(False)
        #     item = self.info_list.item(0)
        #     item.setText("Nome                       : " + str(self.ui_athlete_manager.TRAINING_GLOBAL[0]))
        #     item = self.info_list.item(1)
        #     item.setText("Número de Golpes : " + str(self.ui_athlete_manager.TRAINING_GLOBAL[1]))

    def populate_training_list(self):
        self.train_seq_list.clear()
        self.training_list = dao_training.list_training()
        if self.training_list is not None:
            for training in self.training_list:
                item = QtWidgets.QListWidgetItem()
                item.setText(training.name)
                self.train_seq_list.addItem(item)

    def on_click_training(self, item):
        self.play_action.setDisabled(False)
        current_training = dao_training.recover_test_case(self.train_seq_list.indexFromItem(item).row())
        item = self.info_list.item(0)
        item.setText("Nome                       : " + str(current_training.name))
        item = self.info_list.item(1)
        item.setText("Número de Golpes : " + str(current_training.number_of_hits))

    def run_training(self):
        self.hit_table.setRowCount(0)
        current_training = dao_training.recover_test_case(self.train_seq_list.currentIndex().row())

        self.training_thread = TrainingThread(current_training, self.hit_table)
        self.training_thread.finished.connect(self.on_finish_training)
        self.training_thread.started.connect(self.on_start_training)
        self.training_thread.start()

    def on_finish_training(self):
        # Subir pop-up
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("INFO")
        msg_box.setText("Treinamento finalizado.")
        msg_box.exec()
        self.play_action.setDisabled(False)

    def on_start_training(self):
        self.play_action.setDisabled(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bufete v1"))
        item = self.hit_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Sensor ID"))
        item = self.hit_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tempo (ms)"))
        self.train_seq_list_label.setText(_translate("MainWindow", "Treinamentos disponíveis:"))
        self.hit_table_label.setText(_translate("MainWindow", "Resultados"))
        __sortingEnabled = self.info_list.isSortingEnabled()
        self.info_list.setSortingEnabled(False)
        item = self.info_list.item(0)
        item.setText(_translate("MainWindow", "Nome                       : "))
        item = self.info_list.item(1)
        item.setText(_translate("MainWindow", "Número de Golpes : "))
        # item = self.info_list.item(2)
        # item.setText(_translate("MainWindow", "Sequência                :"))
        self.info_list.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Informação do Treinamento:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


