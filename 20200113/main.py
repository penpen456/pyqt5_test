from PyQt5.QtWidgets import QApplication, QWidget
from progressBar import Ui_Form
from PyQt5.QtCore import QTimer
import sys


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.func)
        self.pushButton.clicked.connect(self.start)
        # 进度条步长
        self.sep = 10

    def func(self):
        num = int(self.label.text())
        if num:
            num -= 1
            self.label.setText(str(num))
            # 每过1秒，进度条的value值+10,这样一共加10次，刚好100%
            self.progressBar.setValue(self.progressBar.value() + 10)
        else:
            self.timer.stop()

    def start(self):
        self.timer.start(1000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())
