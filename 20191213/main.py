import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from radio_button import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.text)

    def text(self):
        self.fruits = []
        if self.radioButton.isChecked():
            self.fruits.append(self.radioButton.text())
        if self.radioButton_2.isChecked():
            self.fruits.append(self.radioButton_2.text())
        if self.radioButton_3.isChecked():
            self.fruits.append(self.radioButton_3.text())
        if self.radioButton_4.isChecked():
            self.fruits.append(self.radioButton_4.text())
        print(self.fruits)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.setWindowTitle('radio_button测试')
    main.show()
    sys.exit(app.exec_())
