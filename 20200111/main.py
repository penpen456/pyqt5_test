from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from savefile import Ui_Form
import sys


class Mywindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.save)

    def save(self):
        # 只是返回一个文件路径，具体save操作还是要靠open实现
        s = QFileDialog.getSaveFileName(self, 'save file', 'C:\\', '文本文档(*.txt)')
        # s = QFileDialog.getOpenFileName(self, 'open file', 'C:\\', 'All Files (*)')
        with open(s[0], 'w') as f:
            f.write(self.textEdit.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Mywindow()
    main.show()
    sys.exit(app.exec_())
