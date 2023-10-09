from PyQt5 import QtCore, QtGui, QtWidgets


class ImgWidget1(QtWidgets.QLabel):

    def __init__(self, imagePath, parent=None):
        super(ImgWidget1, self).__init__(parent)

        pic = QtGui.QPixmap(imagePath)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setPixmap(pic)
