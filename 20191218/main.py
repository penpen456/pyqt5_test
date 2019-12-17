"""
QTimer计时器，每隔2s执行一次超时槽函数
"""


import sys
import time
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow


class Mywindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.timer = QTimer()
        self.timer.timeout.connect(self.text)

    def text(self):
        print('\r' + str(time.time()), end='')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = Mywindow()
    mywindow.show()
    mywindow.timer.start(2000)
    sys.exit(app.exec_())
