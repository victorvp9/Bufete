from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from model import commands_bufete
from model.serial_bufete import handler_sing
from view.athlete_manager import UiAthleteManager
from utils.util import util_sing
import _thread
import random

import csv

n_leds = 8

commands = commands_bufete.CommandsBufete()


class TrainingThread(QtCore.QThread):

    def __init__(self, training, hit_table):
        super(TrainingThread, self).__init__()

        self.training = training
        self.hit_table = hit_table
        self.intra_hit_time = 5

        self.semaphore = _thread.allocate_lock()

    def run(self):
        if handler_sing.is_already_connected():
            self.sleep(1)
            for hit in range(self.training.number_of_hits):
                hit_led_id = random.randrange(n_leds)
                print(hit_led_id)

                self.semaphore.acquire()
                response = commands.turn_on_leds(hit_led_id)
                print(response)
                self.semaphore.release()

                hit_time = util_sing.extract_hit_data(response)

                row_position = self.hit_table.rowCount()
                self.hit_table.insertRow(row_position)

                item = QtWidgets.QTableWidgetItem(str(hit_led_id+1))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.hit_table.setItem(row_position, 0, item)

                item = QtWidgets.QTableWidgetItem(str(hit_time))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.hit_table.setItem(row_position, 1, item)

                self.hit_table.verticalHeader().setVisible(False)

                self.sleep(self.intra_hit_time)

                while QtCore.QCoreApplication.processEvents():
                    pass
            util_sing.save_csv(self.training.name, self.hit_table)
        else:
            print('Bufete não conectado.')

    # def run(self):
    #     # Teste sem placa
    #     self.sleep(1)
    #     for hit in range(self.training.number_of_hits):
    #         hit_led_id = random.randrange(n_leds)
    #         print(hit_led_id)
    #
    #         row_position = self.hit_table.rowCount()
    #         self.hit_table.insertRow(row_position)
    #
    #         item = QtWidgets.QTableWidgetItem(str(hit_led_id+1))
    #         item.setTextAlignment(QtCore.Qt.AlignCenter)
    #         self.hit_table.setItem(row_position, 0, item)
    #
    #         item = QtWidgets.QTableWidgetItem(str(hit_led_id))
    #         item.setTextAlignment(QtCore.Qt.AlignCenter)
    #         self.hit_table.setItem(row_position, 1, item)
    #
    #         self.hit_table.verticalHeader().setVisible(False)
    #
    #         self.sleep(self.intra_hit_time)
    #
    #         while QtCore.QCoreApplication.processEvents():
    #             pass
    #     util_sing.save_csv(self.training.name, self.hit_table)