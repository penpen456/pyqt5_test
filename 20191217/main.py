import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from conunt_time import Ui_MainWindow


# 创建个性化窗口类
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 当修改时-分-秒，发送 值改变的信号，并刷新label_display
        # 从而达到label_display同步spinbox的效果
        self.spinBox_hour.valueChanged.connect(self.repaint)
        self.spinBox_minute.valueChanged.connect(self.repaint)
        self.spinBox_second.valueChanged.connect(self.repaint)

    # 槽方法（刷新label_display）
    def repaint(self):
        """
        label_display由3部分组成
        时:分:秒
        self.spinBox_hour.text() + ':' + self.spinBox_minute.text() + ':' + self.spinBox_second.text()
        """
        time_str = self.spinBox_hour.text() + ':' + self.spinBox_minute.text() + ':' + self.spinBox_second.text()
        self.label_display.setText(time_str)


if __name__ == "__main__":
    # 创建一个app，并传入外部参数
    app = QApplication(sys.argv)
    # 实例化窗口类
    mywindow = MyWindow()
    # 设置标题
    mywindow.setWindowTitle('计时器')
    mywindow.show()
    # 建立循环，并设置退出条件
    sys.exit(app.exec_())
