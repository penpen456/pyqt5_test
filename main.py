from PyQt5.QtWidgets import QMainWindow, QApplication
from first_gui import Ui_Form
import sys
import os


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        # 记录字符串
        self.dis_str = ''
        super().__init__(parent)
        self.setupUi(self)
        # 链接信号与槽函数
        self.close_btn.clicked.connect(self.close)
        self.get_btn.clicked.connect(self.print_text)

    def print_text(self):
        if self.lineEdit.text():
            ping_str = 'ping {} -n 1'.format(self.lineEdit.text())
            with os.popen(ping_str) as f:
                self.dis_str = self.dis_str + f.read() + '..........\n'
                self.textEdit.setPlainText(self.dis_str)
        else:
            self.dis_str += 'ip地址不能为空！\n.......\n'
            self.textEdit.setPlainText(self.dis_str)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
