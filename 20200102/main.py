import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from readonly import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.text)
        self.pushButton_2.clicked.connect(self.clear)
        self.pushButton_3.clicked.connect(self.add)

    def text(self):
        self.textEdit.setText('只读的')

    def clear(self):
        self.textEdit.setText('')

    def add(self):
        self.textEdit.append('-----')
        self.textEdit.append('新添加的')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())
