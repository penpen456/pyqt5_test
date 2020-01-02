"""
1.功能：
 （1）菜单栏exit退出程序（信号与槽）-
 （2）键盘事件：esc退出程序-
 （3）字符出现次数统计-
 （4）实现菜单栏open打开文件对话框选择文件并显示在input里面-
2.优化：
  （1）只有input和keyword2个输入框都有文本时，才能点击查找按钮-
  （2）用单独的线程去打开文件并读取,然后将结果通过信号发送给显示文本的槽函数，防止IO导致程序假死-
  （3）当文件行数过多时，无法显示在input框，添加下一页按钮
  （4）未选择文件时报错 FileNotFoundError: [Errno 2] No such file or directory: ''-
"""

import sys
# import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import Qt, QThread, pyqtSignal
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
        # 点击查找按钮触发find方法
        self.pushButton_find.clicked.connect(self.find)
        # 设置查找按钮初始为false，当input和keyword文本改变时判断是否启用按钮
        self.pushButton_find.setEnabled(False)
        self.textEdit_input.textChanged.connect(self.enable_find_button)
        self.plainTextEdit_keyword.textChanged.connect(self.enable_find_button)
        # 创建一个读取文件子线程
        self.readthread = Readthread()
        # io线程执行完成后发送信号连接绘制函数
        self.readthread.signal.connect(self.to_text_input)

    # 菜单栏action槽函数
    def menu_action(self, action):
        # 点击exit按钮退出程序
        if action.text() == 'exit':
            self.close()
        # 点击open打开文件对话框，选择文件
        elif action.text() == 'open':
            file_path = QFileDialog.getOpenFileName(self, 'open file', 'C:\\', 'All Files (*)')[0]
            # 只有选择了文件,才去启动读取线程
            if file_path:
                # 给子线程添加一个属性,相当于向子线程中传递值
                self.readthread.file_path = file_path
                self.readthread.start()

    def keyPressEvent(self, event):
        # 当按下esc键时退出程序
        if event.key() == Qt.Key_Escape:
            self.close()

    # 查找按钮的槽函数
    def find(self):
        # 字符串
        string = self.textEdit_input.toPlainText()
        # 要查找的关键词
        keyword = self.plainTextEdit_keyword.toPlainText()
        # 出现的次数
        count = string.count(keyword)
        # 输出到label_display
        self.label_display.setText('"{0}"出现的次数为: {1}次'.format(keyword, count))

    # 判断是否启用查找按钮的槽函数
    def enable_find_button(self):
        if self.textEdit_input.toPlainText() and self.plainTextEdit_keyword.toPlainText():
            self.pushButton_find.setEnabled(True)
        else:
            self.pushButton_find.setEnabled(False)

    # 写入文件文本到input输入框的槽函数
    def to_text_input(self, string):
        self.textEdit_input.setText(string)


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
