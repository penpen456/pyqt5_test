from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QTextCursor, QTextListFormat, QFont, QTextTableFormat, QColor
from textCursor import Ui_Form
import sys


class MyWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.test)

    def test(self):
        # 选中文本字符
        cursor = self.textEdit.textCursor()  # 每次点击必须获取新的textCursor
        # 打印当前光标的位置
        print(cursor.position())
        cursor.setPosition(3, QTextCursor.KeepAnchor)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.setFocus()
        print(cursor.selectedText())  # 打印选中的文本
        return None
        qc = QColor(255, 0, 0)
        self.textEdit.setTextBackgroundColor(qc)
        self.textEdit.setFocus()
        
        cursor = self.textEdit.textCursor()
        # 移动光标
        cursor.movePosition(QTextCursor.Left, n=1)
        # 移动完成之后，在编辑器上显示出来
        self.textEdit.setTextCursor(cursor)
        # 获取光标的焦点(未设置可以移动，但无法显示光标)
        self.textEdit.setFocus()
        
        cursor.insertText('hello')
        # 选中文本
        cursor.select(QTextCursor.WordUnderCursor)
        print(cursor.selectionStart(), cursor.selectionEnd())
        print(cursor.selectedText())
        # 插入一个表格(行,列)
        ttf = QTextTableFormat()
        ttf.setCellSpacing(10.0)
        ttf.setCellPadding(10.0)
        cursor.insertTable(2, 3, ttf)
        # 插入一个列表
        tlf = QTextListFormat()
        tlf.setStyle(QTextListFormat.ListDisc)
        cursor.insertList(tlf)
        cursor.insertList(QTextListFormat.ListDisc)
        # 利用文本光标插入纯文本或者HTML
        cursor.insertText('<h1>123</h1>')
        cursor.insertHtml('<h1>123</h1>')
        cursor.insertImage('./start.jpg')  # 暂时无法显示
        # 设置字体
        qfont = QFont()
        qfont.setFamily('微软雅黑')
        self.textEdit.setCurrentFont(qfont)  # 从当前光标处开始为微软雅黑
        # 设置文档标题
        self.textEdit.setDocumentTitle('第一次')
        self.textEdit.setFontFamily('微软雅黑')
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
