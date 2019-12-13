import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from combox import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        list1 = ['python', 'c++', 'java']
        super().__init__(parent)
        self.setupUi(self)
        self.comboBox.addItems(list1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.setWindowTitle('combox测试')
    main.show()
    sys.exit(app.exec_())
