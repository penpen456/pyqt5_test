import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPalette, QTextCursor, QImage, QTextImageFormat
from PyQt5.QtCore import Qt
from changecolor import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # self.image = QImage('.\\电脑.jpg')
        self.textEdit.setPlaceholderText('默认')
        self.pushButton.clicked.connect(self.change_color)

    def change_color(self):
        # 最大边界(光标最大值) anchor() == position()
        # t = self.cursor.anchor()
        # t = self.cursor.position()
        # 光标是否在一行的最开始或结尾
        # t = self.cursor.atBlockEnd()
        # t = self.cursor.atBlockStart()
        # 光标是否在文档的最开始或结尾
        # t = self.cursor.atEnd()
        # t = self.cursor.atStart()
        # 插入文本的开始与结束（一起使用）
        # t = self.cursor.beginEditBlock()
        # 插入文本
        # self.cursor.insertText('hello')
        # self.cursor.insertText('hello')
        # self.cursor.endEditBlock()
        # 返回一个QTextBlock对象
        # t = self.cursor.block()
        # 暂时理解成行，返回多少行,从0开始（文本实际内容的行数，不是textEdit显示的行数）
        # t = self.cursor.blockNumber()
        # t = self.cursor.clearSelection()
        # t = self.cursor.columnNumber()
        # t = self.cursor.deleteChar()
        # t = self.cursor.hasSelection()
        # t = self.cursor.insertImage(self.image)
        # t = self.cursor.isNull()
        # t = self.cursor.movePosition(QTextCursor.Up, QTextCursor.KeepAnchor)
        # self.cursor.movePosition(QTextCursor.Down, n=2)
        # self.cursor.select(QTextCursor.LineUnderCursor)
        # t = self.cursor.selectedText()
        # t = self.cursor.setPosition(3)
        self.cursor = self.textEdit.textCursor()
        # self.cursor.insertText('test')
        img = QTextImageFormat()
        img.setName('电脑.jpg')
        img.setWidth(700)
        img.setHeight(700)
        self.cursor.insertImage(img)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec_())
