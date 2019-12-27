import sys
import time
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow
from usetimesleep import Ui_MainWindow


class Mythread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        time.sleep(6)
        main.label.setText('123')


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.timetest)

    def timetest(self):
        # time.sleep(6)
        # self.label.setText('123')
        t1 = Mythread()
        t1.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())
