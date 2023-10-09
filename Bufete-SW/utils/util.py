from PyQt5 import QtCore
from PyQt5.QtCore import QObject
import numpy as np
from datetime import datetime
import csv
from scipy import integrate
from math import sqrt, pow


GRAVITY = 9.80665
SENSIBILITY = 32/65535

cf = list()
acl = list()
vel = list()
pos = list()
a1 = 0
v1 = 0
s1 = 0
dt = 0.1
time = -0.02
media = 0

class Util(QObject):
    accel_data_to_graph = QtCore.pyqtSignal(list, list, list, list, list, list, name='accel_data_to_graph')

    def __init__(self) -> object:
        super(Util, self).__init__()

    def extract_accel_data(self, accel_data):
        global time, media
        self.v0 = 0
        self.dt = 0.1
        #accel_data.pop(0)
        '''
        accelX = list()
        accelY = list()
        accelZ = list()
        '''

        accelT = list()
        gyroX = list()
        gyroY = list()
        gyroZ = list()
        self.vel = list()
        timeT = list()


        velx0 = 0
        vely0 = 0
        velz0 = 0

        while accel_data.__len__() != 0:
            accelX_L = accel_data.pop(0)
            accelX_H = accel_data.pop(0)

            accelY_L = accel_data.pop(0)
            accelY_H = accel_data.pop(0)

            accelZ_L = accel_data.pop(0)
            accelZ_H = accel_data.pop(0)

            gyroX_L = accel_data.pop(0)
            gyroX_H = accel_data.pop(0)

            gyroY_L = accel_data.pop(0)
            gyroY_H = accel_data.pop(0)

            gyroZ_L = accel_data.pop(0)
            gyroZ_H = accel_data.pop(0)

            AD_L = accel_data.pop(0)
            AD_H = accel_data.pop(0)

            AD_byte = AD_H + AD_L
            ADlevel = (int.from_bytes(AD_byte, byteorder='big', signed=True))
            batteryRaw = 0.1887*ADlevel - 513.21
            # batteryLevel = 50

            accelX_byte = accelX_H + accelX_L
            accelX = (int.from_bytes(accelX_byte, byteorder='big', signed=True))
            accelX = accelX*SENSIBILITY*GRAVITY

            accelY_byte = accelY_H + accelY_L
            accelY = (int.from_bytes(accelY_byte, byteorder='big', signed=True))
            accelY = accelY * SENSIBILITY*GRAVITY

            accelZ_byte = accelZ_H + accelZ_L
            accelZ = (int.from_bytes(accelZ_byte, byteorder='big', signed=True))
            accelZ = accelZ * SENSIBILITY*GRAVITY

            #accelT.append(sqrt(pow(accelX, 2) + pow(accelY, 2) + pow(accelZ, 2)))
            time += 0.02
            timeT.append(round(time, 2))
            '''
            gyroX_byte = gyroX_H + gyroX_L
            gyroX.append(int.from_bytes(gyroX_byte, byteorder='big', signed=True))  # Ainda tem que ver como é

            gyroY_byte = gyroY_H + gyroY_L
            gyroY.append(int.from_bytes(gyroY_byte, byteorder='big', signed=True))  # Ainda tem que ver como é

            gyroZ_byte = gyroZ_H + gyroZ_L
            gyroZ.append(int.from_bytes(gyroZ_byte, byteorder='big', signed=True))  # Ainda tem que ver como é
            '''
        #return accelX, accelY, accelZ, gyroX, gyroY, gyroZ
        #return accelT, gyroX, gyroY, gyroZ, batteryLevel, timeT
        # return accelX, accelY, accelZ, batteryLevel, timeT
        return accelX, accelY, accelZ, batteryRaw, timeT

    AD_level_instant = QtCore.pyqtSignal(list, name='AD_Level_instant')


    def speed(self, a1, v0, dt):
        # valores de aceleracao instantanea

        # integral da aceleracao = velocidade instantanea
        # a = dv/dt >> dv = a dt >> vi - vi-1 = a dt >> vi = vi-1 + a dt
        v0 += a1 * dt
        self.vel.append(v0)
        return v0


    def position(self, vel):
        global pos, s1, v1, dt

        # valores de velocidade instantanea
        v1 = vel.pop(0)

        # integral da velocidade = espaco percorrido
        # v = ds/dt >> ds = v dt >> si - si-1 = v dt >> si = si-1 + v dt
        s1 = s1 + v1 * dt
        pos.append(s1)
        return pos

    def cycleF(self, vel, pos):
        v = vel.pop(0)
        s = pos.pop(0)
        f = v/s
        cf.append(f)
        return cf

    def speedIndex(self, vel):

        sampTime = 1.0 #need to know
        var = np.var(vel)
        stdDeviation = np.sqrt(var)
        vMed = sum(vel)/(len(vel)*sampTime)

        viv = stdDeviation/vMed
        return viv

    def extract_hit_data(self, response):
        # teste
        # conta para o tempo:  1 => 100 us valor => X
        if response[0] == -1:
            return 'ERRO: TIMEOUT'
        if len(response) == 2:
            return 'Errou'
        else:
            time_high = response[2]
            time_mid_high = response[3]
            time_mid_low = response[4]
            time_low = response[5]

            time_response_byte = time_high + time_mid_high + time_mid_low + time_low

            time_response = (int.from_bytes(time_response_byte, byteorder='big', signed=True))

            calculated_time = (100 * time_response)/1000

            return calculated_time

    def save_csv(self, training_name, table):
        timestamp = str(datetime.now()).split('.')[0].replace(':', '-')
        path = './Resultados/' + training_name + ' ' + timestamp + '.csv'
        if path:
            with open(path, 'w') as stream:
                print("saving", path)
                writer = csv.writer(stream, delimiter=';')
                for row in range(table.rowCount()):
                    rowdata = []
                    for column in range(table.columnCount()):
                        item = table.item(row, column)
                        if item is not None:
                            rowdata.append(item.text())
                        else:
                            rowdata.append('')
                    writer.writerow(rowdata)


util_sing = Util()

'''
accelX_byte = accelX_H + accelX_L
            accelX = (int.from_bytes(accelX_byte, byteorder='big', signed=True))
            accelX = accelX*SENSIBILITY*GRAVITY
            #accelX.append((int.from_bytes(accelX_byte, byteorder='big', signed=True)/2**14)*GRAVITY)
            #print('X =', accelX)
            accelY_byte = accelY_H + accelY_L
            accelY = (int.from_bytes(accelY_byte, byteorder='big', signed=True))
            accelY = accelY * SENSIBILITY*GRAVITY
            #accelY.append((int.from_bytes(accelY_byte, byteorder='big', signed=True)/2**14)*GRAVITY)
            #print('y =', accelY)
            accelZ_byte = accelZ_H + accelZ_L
            accelZ = (int.from_bytes(accelZ_byte, byteorder='big', signed=True))
            accelZ = accelZ * SENSIBILITY*GRAVITY


            at = sqrt(pow(accelX, 2) + pow(accelY, 2) + pow(accelZ, 2))
            av = (sqrt(pow(accelX, 2) + pow(accelY, 2) + pow(accelZ, 2)) - GRAVITY)
            if av < 0:
                av = av*(-1)
            accelT.append(at)
            self.v0 = self.speed(av, self.v0, 0.02)
            time += 0.02
            timeT.append(time)


            gyroX_byte = gyroX_H + gyroX_L
            gyroX.append(int.from_bytes(gyroX_byte, byteorder='big', signed=True))  # Ainda tem que ver como é

            gyroY_byte = gyroY_H + gyroY_L
            gyroY.append(int.from_bytes(gyroY_byte, byteorder='big', signed=True))  # Ainda tem que ver como é

            gyroZ_byte = gyroZ_H + gyroZ_L
            gyroZ.append(int.from_bytes(gyroZ_byte, byteorder='big', signed=True))  # Ainda tem que ver como é

'''