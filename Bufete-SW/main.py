import sys
from view.main_window import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("./resources/icons/iefes2.png"))
window = QMainWindow()
ui = Ui_MainWindow()
ui.setup_ui(window)

# window.showMaximized()
window.show()
sys.exit(app.exec_())
