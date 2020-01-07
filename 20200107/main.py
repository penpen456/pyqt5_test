import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QTextCursor
from qtUi import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton_read.clicked.connect(self.readText)
        self.pushButton_next.clicked.connect(self.findnextkey)
        self.pushButton_last.clicked.connect(self.findlastkey)

    def readText(self):
        with open('./text.txt', 'r', encoding='utf-8') as f:
            text = f.read()
        self.textEdit.setPlainText(text)
        self.findpos()

    def findpos(self):
        t = 0
        poslist = []
        key = '码云'
        string = self.textEdit.toPlainText()
        count = string.count(key)
        for i in range(count):
            pos = string.find(key, t)
            t = pos + 1
            poslist.append(pos)
        self.poslist = poslist  # 添加成员属性
        self.i = -1
        print(poslist)

    def findnextkey(self):
        if self.i < len(self.poslist)-1:
            self.i += 1
            cursor = self.textEdit.textCursor()
            cursor.setPosition(self.poslist[self.i])
            cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, 2)
            self.textEdit.setTextCursor(cursor)
            self.textEdit.setFocus()
        else:
            self.textEdit.setFocus()
            QMessageBox().information(self, 'error', '到顶了!', QMessageBox.Ok)

    def findlastkey(self):
        if self.i > 0:
            self.i -= 1
            cursor = self.textEdit.textCursor()
            cursor.setPosition(self.poslist[self.i])
            cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, 2)
            self.textEdit.setTextCursor(cursor)
            self.textEdit.setFocus()
        else:
            self.textEdit.setFocus()
            QMessageBox().information(self, 'error', '到顶了!', QMessageBox.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())
