from PyQt5.QtWidgets import QWidget, QApplication
from textCursor import Ui_Form
import sys


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.test)

    def test(self):
        
        return None
        # 在文本末尾追加内容(文本类型自动识别)
        self.textEdit.append('123')
        self.textEdit.append('<h1>123</h1>')
        # 在光标处插入文本（需要手点确定光标位置）(不会覆盖之前的)
        self.textEdit.insertPlainText('123')
        self.textEdit.insertHtml('<h1>123</h1>')
        # 插入纯文本
        self.textEdit.setPlainText('<h1>123</h1>')
        # 插入HTML
        self.textEdit.setHtml('<h1>123</h1>')
        # 自动识别文本类型
        self.textEdit.setText('<h1>123</h1>')
        self.textEdit.setText('123')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())
