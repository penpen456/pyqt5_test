"""
1.功能：
 （1）菜单栏exit退出程序（信号与槽）-
 （2）键盘事件：esc退出程序-
 （3）字符出现次数统计-
 （4）实现菜单栏open打开文件对话框选择文件并显示在input里面-
 （5）添加按钮清空textEdit_display-
 （6）查找结果定位功能-20200111
2.优化：
  （1）只有input和keyword2个输入框都有文本时，才能点击查找按钮-
  （2）用单独的线程去打开文件并读取,然后将结果通过信号发送给显示文本的槽函数，防止IO导致程序假死-
  （3）当文件行数过多时，无法显示在input框，添加下一页按钮
  （4）未选择文件时报错 FileNotFoundError: [Errno 2] No such file or directory: ''-
  （5）将label_display改成textEdit,设置只读,方便复制-
  （6）查找结果保留之前的结果（append）-
  （7）enter键实现查找
  （8）界面优化-20200111
  （9）添加调整文件编码消息提示框
  （10）优化统计和定位槽函数,只有在input和keyword改变时才执行find-20200111
"""

import sys
# import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QTextCursor
from findStrUI import Ui_MainWindow


# 读取文件并通过信号将结果传输到GUI的线程
class Readthread(QThread):
    signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        # time.sleep(5)
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                # 将读取的字符串传递给主窗口
                self.signal.emit(f.read())
        except UnicodeDecodeError:
            print('调整文件编码为UTF-8')


# 主窗口类
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 菜单栏动作连接
        self.menu.triggered.connect(self.menu_action)
        # 点击统计按钮触发display_result方法
        self.pushButton_find.clicked.connect(self.display_result)
        # 设置查找按钮初始为false，当input和keyword文本改变时判断是否启用按钮
        self.pushButton_find.setEnabled(False)
        self.textEdit_input.textChanged.connect(self.enable_find_button)
        self.plainTextEdit_keyword.textChanged.connect(self.enable_find_button)
        # 创建一个读取文件子线程
        self.readthread = Readthread()
        # io线程执行完成后发送信号连接绘制函数
        self.readthread.signal.connect(self.to_text_input)
        # 添加清空textEdit_display的按钮
        self.pushButton_clear.clicked.connect(self.clear_display)
        # 下一个按钮连接槽函数(上一个按钮)
        self.pushButton_next.setEnabled(False)
        self.pushButton_next.clicked.connect(self.keyword_next)
        self.pushButton_last.setEnabled(False)
        self.pushButton_last.clicked.connect(self.keyword_last)
        # 一些初始化变量
        self.keyword = ''
        self.string = ''

    # 菜单栏action槽函数
    def menu_action(self, action):
        # 点击exit按钮退出程序
        if action.text() == 'exit':
            self.close()
        # 点击open打开文件对话框，选择文件
        elif action.text() == 'open':
            file_path = QFileDialog.getOpenFileName(self, 'open file', 'C:\\', 'All Files (*)')[0]
            # 只有选择了文件,才去启动读取线程（文件未选择,file_path为空）
            if file_path:
                # 给子线程添加一个属性,相当于向子线程中传递值
                self.readthread.file_path = file_path
                self.readthread.start()

    def keyPressEvent(self, event):
        # 当按下esc键时退出程序
        if event.key() == Qt.Key_Escape:
            self.close()

    # 查找按钮的槽函数(核心)
    def find(self):
        t = 0
        self.pos_list = []
        self.i = -1
        # 字符串
        self.string = self.textEdit_input.toPlainText()
        # 要查找的关键词
        self.keyword = self.plainTextEdit_keyword.toPlainText()
        # 出现的次数
        self.count = self.string.count(self.keyword)
        # 出现的位置
        for i in range(self.count):
            pos = self.string.find(self.keyword, t)
            t = pos + 1
            self.pos_list.append(pos)

    # 统计槽函数
    def display_result(self):
        # 当文本和关键词发生改变时，才去执行查找代码，防止重复执行降低效率
        if self.string != self.textEdit_input.toPlainText() or self.keyword != self.plainTextEdit_keyword.toPlainText():
            self.find()
        # 输出到textEdit_display(利用append不覆盖之前的结果)
        self.textEdit_display.append('"{0}"出现的次数为: {1}次'.format(self.keyword, self.count))
        self.textEdit_display.append('-'*60)
        self.textEdit_display.append('-'*60)

    # 下一个槽函数
    def keyword_next(self):
        if self.string != self.textEdit_input.toPlainText() or self.keyword != self.plainTextEdit_keyword.toPlainText():
            self.find()
        if self.i < len(self.pos_list)-1:
            self.i += 1
            cursor = self.textEdit_input.textCursor()
            cursor.setPosition(self.pos_list[self.i])
            cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, len(self.keyword))
            self.textEdit_input.setTextCursor(cursor)
            self.textEdit_input.setFocus()
        else:
            self.textEdit_input.setFocus()
            QMessageBox().information(self, 'error', '到顶了!', QMessageBox.Ok)

    # 上一个槽函数
    def keyword_last(self):
        if self.string != self.textEdit_input.toPlainText() or self.keyword != self.plainTextEdit_keyword.toPlainText():
            self.find()
        if self.i > 0:
            self.i -= 1
            cursor = self.textEdit_input.textCursor()
            cursor.setPosition(self.pos_list[self.i])
            cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, len(self.keyword))
            self.textEdit_input.setTextCursor(cursor)
            self.textEdit_input.setFocus()
        else:
            self.textEdit_input.setFocus()
            QMessageBox().information(self, 'error', '到顶了!', QMessageBox.Ok)

    # 判断是否启用统计按钮的槽函数
    def enable_find_button(self):
        if self.textEdit_input.toPlainText() and self.plainTextEdit_keyword.toPlainText():
            self.pushButton_find.setEnabled(True)
            self.pushButton_next.setEnabled(True)
            self.pushButton_last.setEnabled(True)
        else:
            self.pushButton_find.setEnabled(False)
            self.pushButton_next.setEnabled(False)
            self.pushButton_last.setEnabled(False)

    # 写入文件文本到input输入框的槽函数
    def to_text_input(self, string):
        self.textEdit_input.setText(string)

    # 清空textEdit_display的槽函数
    def clear_display(self):
        self.textEdit_display.setText('')


if __name__ == "__main__":
    # 创建一个app
    app = QApplication(sys.argv)
    # 创建主窗口
    mainwindow = MyWindow()
    # 设置标题
    mainwindow.setWindowTitle('单词查找器')
    mainwindow.show()
    # 建立循环
    sys.exit(app.exec_())
