"""
1.计时器核心内容：
（1）设置窗口：利用self.spinBox.valueChanged来发送信号，实时同步显示与设置的值
（2）display窗口：
     （1）利用qtimer实现周期性执行递减函数（每隔1s执行一次）
     （2）递减槽函数算法实现（主要用于显示）
2.调整优化：
（1）设置界面时分秒都为0时，无法按start启动
    （1）默认设置start按钮为false，因为默认时分秒都为0
    （2）当3个spinBox的值发生改变时，调用检查判断
（2）计时界面，设置一个返回按钮，返回设置界面
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QTimer
from conunt_time import Ui_MainWindow
from display import Ui_Form


# 创建个性化窗口类(设置窗口)
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 当修改时-分-秒，发送 值改变的信号，并刷新label_display
        # 从而达到label_display同步spinbox的效果
        self.spinBox_hour.valueChanged.connect(self.repaint)
        self.spinBox_minute.valueChanged.connect(self.repaint)
        self.spinBox_second.valueChanged.connect(self.repaint)
        # 开始按钮（点击发送信号连接开始槽）
        # 默认start按钮为false
        self.pushButton_start.setEnabled(False)
        self.pushButton_start.clicked.connect(self.start)

    # 槽方法（刷新label_display）,并且判断是否启用start按钮
    def repaint(self):
        """
        label_display由3部分组成
        时:分:秒
        self.spinBox_hour.text() + ':' + self.spinBox_minute.text() + ':' + self.spinBox_second.text()
        """
        time_str = self.spinBox_hour.text() + ':' + self.spinBox_minute.text() + ':' + self.spinBox_second.text()
        self.label_display.setText(time_str)
        # 当时分秒都为0时，关闭start按钮
        if int(self.spinBox_hour.text()) or int(self.spinBox_minute.text()) or int(self.spinBox_second.text()):
            self.pushButton_start.setEnabled(True)
        else:
            self.pushButton_start.setEnabled(False)

    # 槽方法（开始倒计时）
    def start(self):
        """
        (1)设置display窗口初始时间(时分秒3个标签)
        (2)关闭设置窗口
        (3)显示display窗口
        """
        display.label_hour.setText(self.spinBox_hour.text())
        display.label_minute.setText(self.spinBox_minute.text())
        display.label_second.setText(self.spinBox_second.text())
        self.close()
        display.show()
        # 开始计时
        display.timer.start(1000)


# 创建倒计时显示窗口
class Display(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 创建一个计时器
        self.timer = QTimer()
        self.timer.timeout.connect(self.countdown)
        # 返回按钮连接槽函数
        self.pushButton_back.clicked.connect(self.comeback)

    # 倒计时显示函数
    # 最关键的算法
    def countdown(self):
        """
        if 秒>0:
            秒-1
        else:
            if 分>0:
                分-1
                秒变成59
            else:
                if 时>0:
                    时-1
                    分变59，秒变59
                else:
                    timer.stop()
        """
        int_second, int_minute, int_hour = \
            int(self.label_second.text()), int(self.label_minute.text()), int(self.label_hour.text())
        if int_second:
            self.label_second.setText(str(int_second - 1))
        else:
            if int_minute:
                self.label_minute.setText(str(int_minute - 1))
                self.label_second.setText('59')
            else:
                if int_hour:
                    self.label_hour.setText(str(int_hour - 1))
                    self.label_minute.setText('59')
                    self.label_second.setText('59')
                else:
                    self.timer.stop()

    # 返回按钮槽函数
    def comeback(self):
        # 计时中途返回，需要先停止计时
        if int(self.label_hour.text()) or int(self.label_minute.text()) or int(self.label_second.text()):
            self.timer.stop()
        self.close()
        mywindow.show()


if __name__ == "__main__":
    # 创建一个app，并传入外部参数
    app = QApplication(sys.argv)
    # 实例化窗口类(设置窗口)
    mywindow = MyWindow()
    # 设置标题
    mywindow.setWindowTitle('计时器')
    mywindow.show()
    # 实例化display窗口
    display = Display()
    # 设置标题
    display.setWindowTitle('计时器')
    # 建立循环，并设置退出条件
    sys.exit(app.exec_())
