"""
周期性执行某个任务
QTimer计时器，每隔2s执行一次超时槽函数
开始计时：self.timer.start(间隔时间 毫秒)
结束计时：self.timer.stop()
"""


import sys
import time
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow


class Mywindow(QMainWindow):
    def __init__(self, parent=None):
        self.a = 9
        super().__init__(parent)
        self.timer = QTimer()
        self.timer.timeout.connect(self.text)

    def text(self):
        if self.a:
            print('\r' + str(time.time()), end='')
            self.a -= 1
        else:
            self.timer.stop()
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = Mywindow()
    mywindow.show()
    mywindow.timer.start(2000)
    sys.exit(app.exec_())
