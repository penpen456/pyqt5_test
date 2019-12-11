"""
为什么要新建一个main.py来显示，而不是直接在first.py里面显示
因为如果修改了布局，重新生成ui文件，就会覆盖原来的代码，那么逻辑代码也不见了
而如果新建一个main.py，那么只需修改ui文件，而无需修改逻辑代码
"""


import sys
from first import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


# 创建自己的窗口类
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 调用父类的方法
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
