import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
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
        self.pushButton_start.clicked.connect(self.start)

    # 槽方法（刷新label_display）
    def repaint(self):
        """
        label_display由3部分组成
        时:分:秒
        self.spinBox_hour.text() + ':' + self.spinBox_minute.text() + ':' + self.spinBox_second.text()
        """
        time_str = self.spinBox_hour.text() + ':' + self.spinBox_minute.text() + ':' + self.spinBox_second.text()
        self.label_display.setText(time_str)

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


# 创建倒计时显示窗口
class Display(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # 倒计时函数
    def countdown(self):
        pass


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
