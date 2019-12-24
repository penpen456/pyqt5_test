import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from menu import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 返回一个QAction对象，可以传递给槽函数
        self.menu.triggered.connect(self.text)

    def text(self, q):
        # 判断具体点击的是哪个action对象
        if q.text() == '退出':
            self.close()
        elif q.text() == 'print':
            print('123')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())
