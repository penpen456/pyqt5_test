"""
1.功能：
 （1）菜单栏exit退出程序（信号与槽）
 （2）键盘事件：esc退出程序
 （3）字符出现次数统计
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from findStrUI import Ui_MainWindow


# 主窗口类
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 菜单栏动作连接
        self.menu.triggered.connect(self.menu_action)
        # 点击查找按钮触发find方法
        self.pushButton_find.clicked.connect(self.find)

    def menu_action(self, action):
        # 点击exit按钮退出程序
        if action.text() == 'exit':
            self.close()

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
