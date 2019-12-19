"""
pyqt5 如何实现当spinBox的值为0时，关闭按钮
（1）spinBox默认值为0，并且button默认为false
（2）当spinBox的值发生改变时，发送信号，调用判断槽函数，判断是否为0，不为0启用按钮
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from enable_button import Ui_MainWindow
# from PyQt5.QtCore import QEvent


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.setEnabled(False)
        self.spinBox.valueChanged.connect(self.check)

    def check(self):
        if int(self.spinBox.text()):
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())
