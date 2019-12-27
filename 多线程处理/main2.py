import sys
import time
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal
from usetimesleep import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.t = MyThread()
        self.pushButton.clicked.connect(self.start)
        self.t.signal.connect(self.printt)

    def start(self):
        self.t.start()

    def printt(self, a):
        self.textEdit.setText(a)


class MyThread(QThread):
    signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()

    def run(self):
        time.sleep(6)
        self.signal.emit('123')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())
