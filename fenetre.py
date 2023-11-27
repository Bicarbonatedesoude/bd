from PyQt5.QtWidgets import QApplication
from MaSuperFenetre import MainWindow, Ui_MainWindow

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()