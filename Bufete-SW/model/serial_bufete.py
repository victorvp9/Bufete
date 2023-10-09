import serial
import serial.tools.list_ports
import time

# Defines
CRC_MASK = 0xA001
CRC_2_INT = 0x00FF
CRC_ENABLE = False
FLAG_JUMP = 0
FLAG_SHDLC = b"\x7E"
ESCAPE_SHDLC_7D = b"\x7D"
ESCAPE_SHDLC_5E = b"\x5E"
ESCAPE_SHDLC_5D = b"\x5D"
SOURCE_SHDLC = b"\x00"
DESTINATION_SHDLC = b"\x00"
HEADER_LENGTH = 3
# TIMEOUT_SERIAL = 40
TIMEOUT_SERIAL = 10
BAUDRATE = 115200


class SerialBufete:
    def __init__(self) -> object:
        self.ser = serial.Serial()
        self.ser.baudrate = BAUDRATE
        self.ser.timeout = TIMEOUT_SERIAL
        self.ser.parity = serial.PARITY_NONE
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.bytesize = serial.EIGHTBITS

    def list_available_ports(self):
        portsInfo = serial.tools.list_ports.comports()
        ports = list()
        for portInfo in portsInfo:
            ports.append(portInfo.device)
        print(ports)
        return ports

    '''def wifi_connect(self):
        time.sleep(20)
        colrec_connection = self.receive()
        if colrec_connection == [b'C', b'O', b'N', b'N', b'E', b'C', b'T']:
            return colrec_connection
        else:
            return 'ERRO: coletec não conectado!'''''

    def wifi_connect(self):
        colrec_connection = 0
        count = 0
        while colrec_connection != [b'C', b'O', b'N', b'N', b'E', b'C', b'T']:

            colrec_connection = self.receive()

            time.sleep(1)
            count = count + 1
            if count == 5:
                return 'ERRO: coletec não conectado!'
        return colrec_connection

    def connect(self, port):
        self.ser.port = port
        self.ser.open()
        self.ser.isOpen()
        print(self.ser.is_open)

    def disconnect(self):
        self.ser.close()

    def is_already_connected(self):
        return self.ser.is_open

    def write(self, package):
        enconded_package = self.encodeSHDLC(package)
        package = b''.join(enconded_package)
        print(package)
        try:
            self.ser.write(package)
        except Exception as e:
            print(str(e))
        # enconded_package = "~" + package + "~"
            # self.ser.write(d.encode('utf-8') for d in enconded_package)

    def receive(self):
        # Response:
        count = 0
        code = list()
        response = list()
        while count < 2:
            try:
                read_byte = self.ser.read()
            except Exception as e:
                print(str(e))
                return e
            if read_byte != b'':
                if read_byte == FLAG_SHDLC:
                    count += 1
                response.append(read_byte)
            else:
                break
        if count == 2:
            #print("RESraw: ", response)
            decoded_response = self.decodeSHDLC(response)
            #print("RES: ", decoded_response)
            return decoded_response
        else:
            print("Corrupted package or No response!")
            code.append(-1)
            return code

    def encodeSHDLC(self, command):
        encondedSHDLC = list()
        encondedSHDLC.append(FLAG_SHDLC)

        for i in command:
            if i == FLAG_SHDLC:
                encondedSHDLC.append(ESCAPE_SHDLC_7D)
                encondedSHDLC.append(ESCAPE_SHDLC_5E)
            elif i == ESCAPE_SHDLC_7D:
                encondedSHDLC.append(ESCAPE_SHDLC_7D)
                encondedSHDLC.append(ESCAPE_SHDLC_5D)
            else:
                encondedSHDLC.append(i)

        encondedSHDLC.append(FLAG_SHDLC)
        return encondedSHDLC

    def decodeSHDLC(self, response):
        decodedSHDLC = list()
        response.pop(0)
        response.pop(response.__len__() - 1)
        FLAG_JUMP = 0
        for i in range(0, response.__len__()):
            if response[i] == ESCAPE_SHDLC_7D and response[i + 1] == ESCAPE_SHDLC_5E:
                decodedSHDLC.append(FLAG_SHDLC)
                FLAG_JUMP = 1

            elif response[i] == ESCAPE_SHDLC_7D and response[i + 1] == ESCAPE_SHDLC_5D:
                decodedSHDLC.append(ESCAPE_SHDLC_7D)
                FLAG_JUMP = 1

            elif (response[i] == ESCAPE_SHDLC_5E or response[i] == ESCAPE_SHDLC_5D) and FLAG_JUMP == 1:
                FLAG_JUMP = 0
                pass
            else:
                decodedSHDLC.append(response[i])

        return decodedSHDLC

handler_sing = SerialBufete()
